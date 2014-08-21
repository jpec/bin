#!/bin/bash

cd ~/
cat .bash_history > .history
diff .history_backup .history
cat .bash_history > .history_backup
