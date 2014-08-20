#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#=====================================================================
PROGRAM = "diff-u"
VERSION = "0.1"
# --
# Ce programme permet de comparer deux fichiers textes sans tenir 
# compte de l'ordre des lignes et génère un fichier CSV contenant
# le DIFF. 
# --
# Author :  Julien Pecqueur (JPEC)
# Email :   jpec@julienpecqueur.net
# Site :    http://julienpecqueur.net
# 
# License :
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#=====================================================================

#=====================================================================
# Modules
#=====================================================================

from sys import argv
from os.path import isfile


#=====================================================================
# Functions
#=====================================================================

def compareFiles(fRef, fNew, fRes):
    
    """Compare 2 files"""
    
    # Open files
    log("Opening files...")
    fileRef, fileNew, fileRes = openFiles(fRef, fNew, fRes)
    # Load reference file in memory
    dRef = fileRef.readlines()
    cRef = len(dRef)
    log("Ref file contains {} line(s).".format(cRef))
    # Load new file in memory
    dNew = fileNew.readlines()
    cNew = len(dNew)
    log("New file contains {} line(s).".format(cNew))
    # Compare lines of new file
    log("Comparing files...")
    cErr, cCur, cCurErr = 0, 0, 0
    dErr = []
    displayLog(cRef, cCur, cErr)
    for lNew in dNew:
        cCur += 1
        displayLog(cRef, cCur, cErr)
        if lNew in dRef: 
            dRef.remove(lNew)
        else:
            cCurErr += 1
            cErr += 1
            dErr.append(lNew)
        if cCurErr >= 1000:
            log("Append 1000 new lines in diff file...")
            appendLines('new', dErr, fileRes)
            dErr = []
            cCurErr = 0
    displayLog(cRef, cNew, cErr)
    # Append remaining lines of new file
    log("Append remaining new lines in diff file...")
    appendLines('new', dErr, fileRes)
    # Append remaining lines of reference file
    log("Append remaining ref lines in diff file...")
    cRem = appendLines('ref', dRef, fileRes)
    # Close files
    log("Closing files...")
    closeFiles(fileRef, fileNew, fileRes)
    # Results
    displayResults(fRef, fNew, fRes, cRef, cNew, cErr, cRem)


def openFiles(fRef, fNew, fRes):

    """Open files"""

    log("Ref file '{}'".format(fRef))
    fileRef = open(fRef, "r")
    log("Res file '{}'".format(fRes))
    fileRes = open(fRes, "w")
    fileRes.write("*** start ***\n")
    log("New file '{}'".format(fNew))
    fileNew = open(fNew, "r")
    return(fileRef, fileNew, fileRes)


def closeFiles(fRef, fNew, fRes):

    """Close files"""

    fRef.close()
    fNew.close()
    fRes.write("*** end ***\n")
    fRes.close()


def appendLines(type, dRes, fRes):
    
    """Append lines in file"""

    for line in dRes:
        if type == "new":
            fRes.write("+;"+line)
        elif type == "ref":
            fRes.write("-;"+line)
        else:
            fRes.write("?;"+line)
    return(len(dRes))


def displayResults(fRef, fNew, fRes, cRef, cNew, cErr, cRem):

    """Display results"""

    print("*** RESULTS ***")
    print("Ref file '{}'".format(fRef))
    print("New file '{}'".format(fNew))
    print("Res file '{}'".format(fRes))
    print("Nbr lines in ref file      : {}".format(cRef))
    print("Nbr lines in new file      : {}".format(cNew))
    print("Nbr lines only in new file : {}".format(cErr))
    print("Nbr lines only in ref file : {}".format(cRem))


def displayLog(cRef, count, cErr):

    """Display log during execution (every n %)"""

    nPercent = cRef // 10
    if nPercent > 0 and count % nPercent == 0:
        actual = int (count / cRef * 100)
        msg = "Comparing line {0} / {1} : {2} % >>> {3} differences"
        log(msg.format(count, cRef, actual, cErr))


def usage(prog):

    """Display usage"""

    print("Usage: {} <ref file> <new file> <res file>".format(prog))


def version(prog, vers):

    """Display version"""

    print("{} v{}".format(prog, vers))


def log(msg):

    """Display log message"""

    print("[LOG] {}".format(msg))


def error(msg):

    """Display error message"""

    print("[ERR] {}".format(msg))


#=====================================================================
# Begin of program
#====================================================================

if len(argv) == 4:
    # Compare files
    fRef, fNew, fRes = argv[1], argv[2], argv[3]
    if isfile(fRef) and isfile(fNew):
        compareFiles(fRef, fNew, fRes)
    else:
        error("One of the files isn't correct.")
elif len(argv) == 2 and argv[1] == "-v":
    # Display version
    version(argv[0], VERSION)
else:
    # Display usage
    usage(argv[0])


#=====================================================================
# End of program
#=====================================================================

