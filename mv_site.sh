#!/bin/bash
cp ./report/main.html ./docs/index.html
rm -rf ./docs/figure
cp -R ./report/figure ./docs
rm -rf ./docs/main_files
cp -R ./report/main_files ./docs