#!/usr/bin/env python
# -*- coding:utf-8 -*-
#需要 eyed3 python-magic ffmpge pydub
import eyed3
import os
import sys
import magic
from shutil import copyfile
from pydub.utils import mediainfo


def getMp3FilesPath(mPath):
	files = []
	if not os.path.exists(mPath):
		return files
	for parent,dirnames,filenames in os.walk(mPath):
		for filename in filenames:
			files.append(os.path.join(parent,filename))
	return files

def parseFilesInfo():
	reload(sys)
	sys.setdefaultencoding('utf8')

	usage = "usage: justringMaster SearchPath DstPath"
	if(len(sys.argv)<3):
		print(usage)
		exit()

	searchPath = sys.argv[1]
	destPath = sys.argv[2]

	if not os.path.exists(searchPath):
		print("searchPath 不存在")
		exit()

	files = getMp3FilesPath(searchPath)
	count = 0;
	tMagic = magic.Magic("mime=true")
	for fItem in files:
		print("************处理开始******************")
		print("待解析文件名:"+fItem)
		ftype = tMagic.from_file(fItem)
		fname,fext = os.path.splitext(fItem)
		if ftype == "audio/mpeg":
			ed3 = eyed3.load(fItem)
			name,ext = os.path.splitext(fItem)
			dstFileName = ed3.tag.title+ext
			dstParentName = destPath+"/"+ed3.tag.album
			dstFileAbsPath = dstParentName+"/"+dstFileName
			dstRealParentName = os.path.dirname(dstFileAbsPath)
			print("  解析文件名:"+dstFileName)
			print("    目标路径:"+dstRealParentName)
			if not (os.path.exists(dstRealParentName) and os.path.isdir(dstRealParentName)):
				os.makedirs(dstRealParentName)
			copyfile(fItem,dstFileAbsPath)
			count = count+1
			print("    复制文件:"+fItem+"-->"+dstFileAbsPath)
		elif fext==".mp3" and mediainfo(fItem).get('TAG',None)!=None:
			name,ext = os.path.splitext(fItem)
			fdata = mediainfo(fItem).get('TAG',None)		
			dstFileName = fdata['title']+ext
			dstParentName = destPath+"/"+fdata['album']
			dstFileAbsPath = dstParentName+"/"+dstFileName
			dstRealParentName = os.path.dirname(dstFileAbsPath)
			print("  解析文件名:"+dstFileName)
			print("    目标路径:"+dstRealParentName)
			if not (os.path.exists(dstRealParentName) and os.path.isdir(dstRealParentName)):
				os.makedirs(dstRealParentName)
			copyfile(fItem,dstFileAbsPath)
			count = count+1
			print("    复制文件:"+fItem+"-->"+dstFileAbsPath)
		else:
			dstUnsortedPath = destPath+"/unknown"
			dstUnKnowFileName = os.path.basename(fItem)
			dstUnKnowFilePath = dstUnsortedPath + "/" + dstUnKnowFileName
			if not os.path.exists(dstUnsortedPath) :
				os.makedirs(dstUnsortedPath)
			copyfile(fItem,dstUnKnowFilePath)
			count = count+1
			print("    复制文件:"+fItem+"-->"+dstUnKnowFileName)
			print("该文件不属于静雅思听音频文件，程序无法解析")
		print("***********已完成:"+str(count)+"*******************")
	print("done")


if __name__ == "__main__":
    parseFilesInfo()
    sys.exit()


		
