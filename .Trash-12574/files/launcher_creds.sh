#!/bin/bash
ssh-keyscan github.com  >> ~/.ssh/known_hosts
DATE_WITH_TIME=`date "+%Y%m%d-%H%M%S"`
echo "TIME STAMP" $DATE_WITH_TIME
pwd
echo $DATE_WITH_TIME >> launcher_repo.txt
git add .
git commit -m "test launcher user"
git push
