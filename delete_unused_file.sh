#!/usr/bin/bash

find . -name "*.pyc" -exec ls -lv {} \;
find . -name "*.pyc" -exec rm -rfv {} \;





#To revert some files from git
#git checkout -- c/threads/bogotobogodotcom/Makefile
#git checkout -- data_structure_n_algorithm/Searching/hashtable/www6_uniovi_es/Makefile

exit 0
