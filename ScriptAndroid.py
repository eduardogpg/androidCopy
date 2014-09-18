#!/usr/bin/env python. 
# -*- coding: utf-8 -*-
import os
from os import listdir
import sys
import shutil


__author__ ="Eduardo Ismael García Pérez"
__Colaborador__ ="Christian Eduardo Galdamez Blanco"

"""
	Descripción 

"""
class barredora():
	def __init__(self, path, pathToCopy):
		self.countFile = 0

		self.makeFolder(pathToCopy)
		self.fileList = self.listFile(path,pathToCopy )

		self.autidar()

	def autidar(self):
		if self.countFile == len(self.fileList):
			print "Todos los archivos movidos"
		else:
			print "Es posible que no todos los archivos se hayan movido"

	def makeFolder(self, pathToCopy):
		try:
			os.mkdir( pathToCopy )
		except:
			pass

	def listFile(self,directoryPath,pathToCopy):
	    myListFile = []
	    currentFolder = pathToCopy
	    for currentFile in listdir(directoryPath):
	        newDir = os.path.join(directoryPath, currentFile)
	        
	        if os.path.isdir(newDir):
	            currentFolder  = pathToCopy +"/"+currentFile
	            os.mkdir( currentFolder )
	            myListFile.extend(self.listFile( newDir, currentFolder )) 
	            currentFolder = pathToCopy

	        else:
	            myListFile.append(currentFile)
	            self.copyFile(newDir,   os.path.join(currentFolder, currentFile) )

	    return myListFile

	def copyFile(self, fileToCopy, pathToCopy):
		try:
			shutil.copyfile(fileToCopy, pathToCopy)
			self.countFile +=1
		except:
			print "Problems with the file " + str(fileToCopy)

if __name__ == "__main__":
	if len(sys.argv) >=2 :
		nuevaBarredora = barredora( sys.argv[1] , sys.argv[2] )
	else:	
		nuevaBarredora = barredora( ".", "copiaSeguridad" )