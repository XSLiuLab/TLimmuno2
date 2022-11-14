# TLimmuno2: predicting HLA class II antigen immunogenicity through integrated deep learning

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![version](https://img.shields.io/badge/version-dev-green.svg)](https://shields.io/)

## Overview

This repository provides the analysis reports, code, data and python packages for readers who are interest in this project and make it easier to reproduce the whole analysis procedure.

Read online analysis report at https://xsliulab.github.io/TLimmuno2/.

## Contents

* [Python](./Python) The python code of TLimmuno2 package.
* [data](./data) The data used and produced by analysis report.
* [docs](./docs) Website pages and figures used for showing analysis reports.
* [report](./report) Rmarkdown files of analysis report and related html web page files.
* [figure](./figure) The figure produced by all Rmarkdown files.

## Usage

Dependency
```
pandas
numpy
tensorflow
pyarrow
```
You can download the entire repository and repeat our work, but the repository is a little big.
If you just want to use TLimmuno2 model, you can just pull ```Python``` file by using below command:
```
mkdir TLimmuno2
cd TLimmuno2
git init
git remote add -f origin https://github.com/XSLiuLab/TLimmuno2.git
git config core.sparsecheckout true
echo "Python" >> .git/info/sparse-checkout
git pull origin main
```
There are two ways to use TLimmuno2: ```line``` mode and ```file``` mode:

For ```line``` model, you can get singe epitope result on terminal, here are the sample:
```
python Python/TLimmuno2.py --mode line --epitope GLLFRRLTSREVLLL --hla DRB1_0803
```

For ```file``` model, you can input a file like ```example.csv``` and get the ```result.csv``` in output filer:
```
python Python/TLimmuno2.py --mode file --intdir ./Python/data/example.csv --outdir .
```

A full help prompt is as below:
```
usage: TLimmuno2.py [-h] [--mode MODE] [--epitope EPITOPE] [--hla HLA] [--intdir INTDIR] [--outdir OUTDIR] [--gpu GPU]

TLimmuno2 command line

optional arguments:
  -h, --help         show this help message and exit
  --mode MODE        line mode or file mode
  --epitope EPITOPE  if line mode, specifying your epitope
  --hla HLA          if line mode, specifying your HLA allele
  --intdir INTDIR    if file mode, specifying the path to your input file
  --outdir OUTDIR    if file mode, specifying the path to your output folder
  --gpu GPU          if you device don't have GPU, please set it to False

```


## Citation

waitting to add paper

## Acknowledgement

We thank ShanghaiTech University High Performance Computing Public Service Platform for computing services.This work was supported by Shanghai Science and Technology Commission (21ZR1442400), the National Natural Science Foundation of China (31771373), and startup funding from ShanghaiTech University.

## License

***

**Cancer Biology Group @ShanghaiTech**

**Research group led by Xue-Song Liu in ShanghaiTech University**


