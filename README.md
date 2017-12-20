# JustingAudioInfoExtract

该脚本用来提取由静雅思听网站下载的音频文件信息。因为付费后下载好的音频是以数字命名的mp3存储在介质中,不能方便的知道该音频的内容。用该脚本可以提取出这些音频文件的相关信息，并以该信息对文件进行重命名。

## 使用说明

### 1. 安装python2.7

### 2. 安装pip

查看是否有安装pip,因为官方文档的说明是
>pip is already installed if you are using Python 2 >=2.7.9 or Python 3 >=3.4 downloaded from python.org or if you are working in a Virtual Environment created by virtualenv or pyvenv. Just make sure to upgrade pip.

如果没有安装pip,则进行安装

	curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

如果是windows系统则下载<https://bootstrap.pypa.io/get-pip.py>,并执行`python get-pip.py`

### 3. 安装依赖的模块
	pip install eyeD3
	pip install pydub

### 4. 运行脚本
	python justingMaster.py 待转换文件目录 目标目录

## 作者

**夜月昆仑**
- <https://github.com/yeyuekunlun>
- <https://yeyuekunlun.github.io>



