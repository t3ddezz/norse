#!/usr/bin/env python3
import sys
import sys ; sys.setrecursionlimit(sys.getrecursionlimit() * 5)
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog,  QFileDialog, QFrame, QMessageBox
from PyQt5.QtGui import QPalette, QColor, QIcon, QPixmap
from PyQt5.QtCore import Qt, QFileInfo
import pandas as pd
import io
import requests
import os.path
from datetime import datetime
import paramiko
import socket
import time
import os
import argparse
from .norse_module.MainWindow_libraries import MyWindow, version

program = "norse"

def main(sysargs = sys.argv[1:]):   #main function to run script and see version
    
    parser = argparse.ArgumentParser(prog = program,
    description='norse, nanopore sequencing data transfer',
    usage='''norse [options]''')

    parser.add_argument("-v","--version", action='version', version=f"norse = {version}")
    parser.add_argument("-r","--run",action='store_true', help=f"run {program}")
        
    if len(sysargs)<1:  #if nothing typed show all arguments which avaible
        parser.print_help()
        sys.exit(-1)
    else:
        args = parser.parse_args(sysargs)
    args = parser.parse_args()
    
    if args.run:
        window()    #function to show GUI


def window():   # func to show GUI and exit correctly
    app = QApplication(sys.argv)
    
    # dark mode pallette
    app.setStyle('Fusion')
    dark_palette = QtGui.QPalette()

    dark_palette.setColor(QtGui.QPalette.Window, QtGui.QColor(53, 53, 53))
    dark_palette.setColor(QtGui.QPalette.WindowText, QtCore.Qt.white)
    dark_palette.setColor(QtGui.QPalette.Base, QtGui.QColor(25, 25, 25))
    dark_palette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(53, 53, 53))
    dark_palette.setColor(QtGui.QPalette.ToolTipBase, QtCore.Qt.white)
    dark_palette.setColor(QtGui.QPalette.ToolTipText, QtCore.Qt.white)
    dark_palette.setColor(QtGui.QPalette.Text, QtCore.Qt.white)
    dark_palette.setColor(QtGui.QPalette.Button, QtGui.QColor(53, 53, 53))
    dark_palette.setColor(QtGui.QPalette.ButtonText, QtCore.Qt.white)
    dark_palette.setColor(QtGui.QPalette.BrightText, QtCore.Qt.red)
    dark_palette.setColor(QtGui.QPalette.Link, QtGui.QColor(42, 130, 218))
    dark_palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(42, 130, 218))
    dark_palette.setColor(QtGui.QPalette.HighlightedText, QtCore.Qt.black)

    app.setPalette(dark_palette)

    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':  #to clarify this has to be mainscript and not a imported module
    main()
    #window()