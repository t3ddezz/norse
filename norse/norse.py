#!/usr/bin/env python
import sys
import sys ; sys.setrecursionlimit(sys.getrecursionlimit() * 5)
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog,  QFileDialog, QFrame, QMessageBox
from PyQt5.QtGui import QPalette, QColor, QIcon, QPixmap
from PyQt5.QtCore import Qt
import pandas as pd
import io
import requests
import os.path
from datetime import datetime
import paramiko
import socket
import time
import os

class Validator(QtGui.QValidator):
    def validate(self, string, pos):
        return QtGui.QValidator.Acceptable, string.upper(), pos
class Window2(QMainWindow):#class for window2 (pop up window)
    def __init__(self):
        super(Window2,self).__init__()
        self.setWindowTitle("check your data")
        self.setGeometry(400, 400, 330, 385)
        self.iniUI()


    def iniUI(self):#
        
        #self.window1 = MyWindow()
       
        

        self.tablewidget = QtWidgets.QTableWidget

        self.label_sample = QtWidgets.QLabel(self)
        self.label_sample.setText('sampel name:')
        self.label_sample.move(20, 70)
        
        
        self.kitlabel = QtWidgets.QLabel(self)
        self.kitlabel.move(20, 10)
        self.kitlabel.setText('kit:')

        self.barlabel = QtWidgets.QLabel(self)
        self.barlabel.move(20, 30)
        self.barlabel.setText('barcoding kit:')
        
        self.barcodinglabel = QtWidgets.QLabel(self)
        self.barcodinglabel.move(20, 50)
        self.barcodinglabel.setText('flowcell:')
        
        self.input0 = QtWidgets.QLabel(self)#kit
        self.input0.move(115, 10)

        self.input00 = QtWidgets.QLabel(self)#barcode
        self.input00.move(115, 30)

        self.input000 = QtWidgets.QLabel(self)#flowcell
        self.input000.move(115, 50)
        
        self.input1 = QtWidgets.QLabel(self)#samples 1-24
        self.input1.move(20, 90)
        self.label1 = QtWidgets.QLabel(self)
        self.label1.setText('1')
        self.label1.move(10, 90)
        
        self.input2 = QtWidgets.QLabel(self)
        self.input2.move(20,110)
        self.label2 = QtWidgets.QLabel(self)
        self.label2.setText('2')
        self.label2.move(10, 110)
        
        self.input3 = QtWidgets.QLabel(self)
        self.input3.move(20,130)
        self.label3 = QtWidgets.QLabel(self)
        self.label3.setText('3')
        self.label3.move(10, 130)
    
        self.input4 = QtWidgets.QLabel(self)
        self.input4.move(20,150)
        self.label4 = QtWidgets.QLabel(self)
        self.label4.setText('4')
        self.label4.move(10, 150)
        
        self.input5 = QtWidgets.QLabel(self)
        self.input5.move(20,170)
        self.label5 = QtWidgets.QLabel(self)
        self.label5.setText('5')
        self.label5.move(10, 170)
        
        self.input6 = QtWidgets.QLabel(self)
        self.input6.move(20,190)
        self.label6 = QtWidgets.QLabel(self)
        self.label6.setText('6')
        self.label6.move(10, 190)
        
        self.input7 = QtWidgets.QLabel(self)
        self.input7.move(20,210)
        self.label7 = QtWidgets.QLabel(self)
        self.label7.setText('7')
        self.label7.move(10, 210)
        
        self.input8 = QtWidgets.QLabel(self)
        self.input8.move(20,230)
        self.label8 = QtWidgets.QLabel(self)
        self.label8.setText('8')
        self.label8.move(10, 230)
        
        self.input9 = QtWidgets.QLabel(self)
        self.input9.move(20,250)
        self.label9 = QtWidgets.QLabel(self)
        self.label9.setText('9')
        self.label9.move(10, 250)
        
        self.input10 = QtWidgets.QLabel(self)
        self.input10.move(20,270)
        self.label10 = QtWidgets.QLabel(self)
        self.label10.setText('10')
        self.label10.move(6, 270)
        
        self.input11 = QtWidgets.QLabel(self)
        self.input11.move(20,290)
        self.label11 = QtWidgets.QLabel(self)
        self.label11.setText('11')
        self.label11.move(6, 290)
        
        self.input12 = QtWidgets.QLabel(self)
        self.input12.move(20,310)
        self.label12 = QtWidgets.QLabel(self)
        self.label12.setText('12')
        self.label12.move(6, 310)
        
        self.input13 = QtWidgets.QLabel(self)
        self.input13.move(200,90)
        self.label13 = QtWidgets.QLabel(self)
        self.label13.setText('13')
        self.label13.move(184, 90)
       
        self.input14 = QtWidgets.QLabel(self)
        self.input14.move(200,110)
        self.label14 = QtWidgets.QLabel(self)
        self.label14.setText('14')
        self.label14.move(184, 110)
        
        self.input15 = QtWidgets.QLabel(self)
        self.input15.move(200,130)
        self.label15 = QtWidgets.QLabel(self)
        self.label15.setText('16')
        self.label15.move(184, 130)
        
        self.input16 = QtWidgets.QLabel(self)
        self.input16.move(200,150)
        self.label16 = QtWidgets.QLabel(self)
        self.label16.setText('16')
        self.label16.move(184, 150)
        
        self.input17 = QtWidgets.QLabel(self)
        self.input17.move(200,170)
        self.label17 = QtWidgets.QLabel(self)
        self.label17.setText('17')
        self.label17.move(184, 170)
        
        self.input18 = QtWidgets.QLabel(self)
        self.input18.move(200,190)
        self.label18 = QtWidgets.QLabel(self)
        self.label18.setText('18')
        self.label18.move(184, 190)
        
        self.input19 = QtWidgets.QLabel(self)
        self.input19.move(200,210)
        self.label19 = QtWidgets.QLabel(self)
        self.label19.setText('19')
        self.label19.move(184, 210)
        
        self.input20 = QtWidgets.QLabel(self)
        self.input20.move(200,230)
        self.label20 = QtWidgets.QLabel(self)
        self.label20.setText('20')
        self.label20.move(184, 230)
        
        self.input21 = QtWidgets.QLabel(self)
        self.input21.move(200,250)
        self.label21 = QtWidgets.QLabel(self)
        self.label21.setText('21')
        self.label21.move(184, 250)
        
        self.input22 = QtWidgets.QLabel(self)
        self.input22.move(200,270)
        self.label22 = QtWidgets.QLabel(self)
        self.label22.setText('22')
        self.label22.move(184, 270)
        
        self.input23 = QtWidgets.QLabel(self)
        self.input23.move(200,290)
        self.label23 = QtWidgets.QLabel(self)
        self.label23.setText('23')
        self.label23.move(184, 290)
        
        self.input24 = QtWidgets.QLabel(self)
        self.input24.move(200,310)
        self.label24 = QtWidgets.QLabel(self)
        self.label24.setText('24')
        self.label24.move(184, 310)

        self.button = QtWidgets.QPushButton(self)
        self.button.setText('ok!')
        self.button.move(230, 355) 
        #self.button.clicked.connect(self.upload_activated)
        self.button.clicked.connect(self.close)#close window2


    def hide2(self):#hide all labels from 2 to 12 
        self.label2.setHidden(True)
        self.label3.setHidden(True)
        self.label4.setHidden(True)
        self.label5.setHidden(True)
        self.label6.setHidden(True)
        self.label7.setHidden(True)
        self.label8.setHidden(True)
        self.label9.setHidden(True)
        self.label10.setHidden(True)
        self.label11.setHidden(True)
        self.label12.setHidden(True)  


    def unhide2(self):#unhide all labels from 2 to 12
        self.label2.setHidden(False)
        self.label3.setHidden(False)
        self.label4.setHidden(False)
        self.label5.setHidden(False)
        self.label6.setHidden(False)
        self.label7.setHidden(False)
        self.label8.setHidden(False)
        self.label9.setHidden(False)
        self.label10.setHidden(False)
        self.label11.setHidden(False)
        self.label12.setHidden(False)


    def unhide(self):#show all labels from 13 to 24
         self.label13.setHidden(False)
         self.label14.setHidden(False)
         self.label15.setHidden(False)
         self.label16.setHidden(False)
         self.label17.setHidden(False)
         self.label18.setHidden(False)
         self.label19.setHidden(False)
         self.label20.setHidden(False)
         self.label21.setHidden(False)
         self.label22.setHidden(False)
         self.label23.setHidden(False)
         self.label24.setHidden(False)


    def hide(self):#hide all labels from 13 to 24
        self.label13.setHidden(True)
        self.label14.setHidden(True)
        self.label15.setHidden(True)
        self.label16.setHidden(True)
        self.label17.setHidden(True)
        self.label18.setHidden(True)
        self.label19.setHidden(True)
        self.label20.setHidden(True)
        self.label21.setHidden(True)
        self.label22.setHidden(True)
        self.label23.setHidden(True)
        self.label24.setHidden(True)

 
    def displayInfo(self):#shows window2
        self.show( )


    #def upload_activated(self):
     #   self.window1.button_upload.setEnabled(True)
class MyWindow(QMainWindow):#create a window through the initUI() method, and call it in the initialization method init()
    rsync_var = 0
    trasnfer_path_var = 0
    def __init__(self):
        super(MyWindow, self).__init__()
        
        #self.secondwindow = Window2()
        self.setGeometry(200, 200, 800, 600)
        self.setWindowTitle('norse')
        self.iniUI()#function call
        #self.layoutUI()

    def iniUI(self):
        # 'self' is the first parameter of the methods of a class that refers to the instance of the same

        self.window2 = Window2()#for initiating window2
    
        self.rsync_var_label = QtWidgets.QLabel(self)
        self.rsync_var_label.setHidden(True)

        self.logo_label = QtWidgets.QLabel(self)
        self.logo_label.setText('norse')
        #pixmap = QPixmap('auge.png')
        #self.logo_label.setPixmap(pixmap)
        self.logo_label.move(10, 10)

        self.upper_frame = QtWidgets.QFrame(self)
        self.upper_frame.setFixedWidth(210)
        self.upper_frame.setFixedHeight(145)
        self.upper_frame.move(5, 50)
        self.upper_frame.setFrameShape(QFrame.StyledPanel)
        self.upper_frame.setFrameShadow(QFrame.Raised)

        self.mid_frame = QtWidgets.QFrame(self)
        self.mid_frame.setFixedWidth(210)
        self.mid_frame.setFixedHeight(130)
        self.mid_frame.move(5, 200)
        self.mid_frame.setFrameShape(QFrame.StyledPanel)
        self.mid_frame.setFrameShadow(QFrame.Raised)

        self.password = QtWidgets.QLineEdit(self)
        self.password.move(260, 400)
        self.password.setPlaceholderText('password')
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)

        self.checkbox_hide_unhide = QtWidgets.QCheckBox('show',self)
        self.checkbox_hide_unhide.adjustSize()
        self.checkbox_hide_unhide.stateChanged.connect(self.checkbox)
        self.checkbox_hide_unhide.move(370, 405)

        self.label_sonderzeichen = QtWidgets.QLabel(self)
        self.label_sonderzeichen.setText(':')
        self.label_sonderzeichen.adjustSize()
        self.label_sonderzeichen.move(250, 406)
        

        



        barcode_liste = ['EXP-PBC096','EXP-PBC001','EXP-NBD114','EXP-NBD104','EXP-NBD196']
        
        
        self.kitinfos_label = QtWidgets.QLabel(self)
        self.kitinfos_label.move(10, 50)
        self.kitinfos_label.setText('Ligation kit:')

        self.sequencing_edit = QtWidgets.QLineEdit(self)
        self.sequencing_edit.setPlaceholderText('e.g SQK-PCB109')
        self.sequencing_edit.setMaxLength(13)
        self.sequencing_edit.adjustSize()
        self.sequencing_edit.move(10, 75)
        self.validator = Validator(self)
        self.sequencing_edit.setValidator(self.validator)
        #self.sequencing_edit.textChanged[str].connect(self.sequencing_changed)
        self.sequencing_edit.editingFinished.connect(self.sequencing_changed)

        self.barcode_label = QtWidgets.QLabel(self)
        self.barcode_label.move(10, 102)
        self.barcode_label.setText('Barcode kit (optional):')
        self.barcode_label.adjustSize()

        
        self.barcode_edit = QtWidgets.QLineEdit(self)
        self.barcode_edit.setPlaceholderText('e.g EXP-PBC096')
        self.barcode_edit.adjustSize()
        self.barcode_edit.move(10, 120)
        self.validator = Validator(self)
        self.barcode_edit.setValidator(self.validator)
        #self.barcode_edit.textChanged[str].connect(self.barcode_changed)
        self.barcode_edit.editingFinished.connect(self.barcode_changed)
        
        self.flowcell_label = QtWidgets.QLabel(self)
        self.flowcell_label.move(10, 140)
        self.flowcell_label.setText('Flowcell:')

        self.flowcell_edit = QtWidgets.QLineEdit(self)
        self.flowcell_edit.setPlaceholderText('e.g FLO-MIN106')
        self.flowcell_edit.adjustSize()
        self.flowcell_edit.move(10, 165)
        self.validator = Validator(self)
        self.flowcell_edit.setValidator(self.validator)
        self.flowcell_edit.editingFinished.connect(self.flowcell_changed)

        self.barcodes_label = QtWidgets.QLabel(self)
        self.barcodes_label.setText('Barcodes?')
        self.barcodes_label.move(10, 200)

        
        self.radiobutton_no = QtWidgets.QRadioButton(self)# round button (grouped with radiobutton_yes)- only one can be selected
        self.radiobutton_no.toggled.connect(self.radioclicked_no)
        self.radiobutton_no.move(10, 225)
        self.label_radiobutton_no = QtWidgets.QLabel(self)
        self.label_radiobutton_no.setText('no')
        self.label_radiobutton_no.move(30, 225)

        self.radiobutton_yes = QtWidgets.QRadioButton(self)
        self.radiobutton_yes.toggled.connect(self.radioclicked_yes)
        self.radiobutton_yes.move(10, 245)
        self.label_radiobutton_yes = QtWidgets.QLabel(self)
        self.label_radiobutton_yes.setText('yes (12)')
        self.label_radiobutton_yes.move(30, 245)

        self.test_upload_variable = QtWidgets.QLabel(self)
        self.test_upload_variable.setHidden(True)

        self.radiobutton_24_samples = QtWidgets.QRadioButton(self)
        self.radiobutton_24_samples.toggled.connect(self.clickbox)
        self.radiobutton_24_samples.move(10, 265)
        self.samples_24_label = QtWidgets.QLabel(self)
        self.samples_24_label.setText('yes (24)')
        self.samples_24_label.move(30, 265)

        self.radiobutton_sample_sheet = QtWidgets.QRadioButton(self)
        self.radiobutton_sample_sheet.toggled.connect(self.clickbox2)
        self.radiobutton_sample_sheet.move(10, 285)
        self.sample_sheet_label = QtWidgets.QLabel(self)
        self.sample_sheet_label.setText('yes (sample sheet)')
        self.sample_sheet_label.move(30, 290)
        self.sample_sheet_label.resize(150, 20)


        self.radiobutton_group = QtWidgets.QButtonGroup(self)
        self.radiobutton_group.addButton(self.radiobutton_yes)
        self.radiobutton_group.addButton(self.radiobutton_no)
        self.radiobutton_group.addButton(self.radiobutton_24_samples)
        self.radiobutton_group.addButton(self.radiobutton_sample_sheet)
        
        self.download_template = QtWidgets.QPushButton(self)
        self.download_template.setText('download template')
        self.download_template.setDisabled(True)
        self.download_template.move(290, 100)
        self.download_template.adjustSize()
        self.download_template.setToolTip('Here you can download a template for 96 samples')
        self.setStyleSheet("""QToolTip { 
                           background-color: black; 
                           color: white; 
                           border: black solid 1px
                           }""")
        self.download_template.setHidden(True)

        self.upload_data = QtWidgets.QPushButton(self)
        self.upload_data.setText('upload data')
        self.upload_data.setDisabled(True)
        self.upload_data.move(290,140)
        #self.upload_data.adjustSize()
        self.upload_data.setHidden(True)


        

        self.lineedit_username = QtWidgets.QLineEdit(self)
        self.lineedit_username.move(10, 400)
        self.lineedit_username.setPlaceholderText('username')
        #self.label_username.adjustSize()
        
        #self.lineedit_username.setEchoMode(QtWidgets.QLineEdit.Password)#if password is needed

        self.lineedit_ip_adress = QtWidgets.QLineEdit(self)
        self.lineedit_ip_adress.move(125, 400)
        self.lineedit_ip_adress.setPlaceholderText('ip-adress')
        self.lineedit_ip_adress.resize(120, 30)

        self.label_at = QtWidgets.QLabel(self)
        self.label_at.move(112, 407)
        self.label_at.setText('@')
        self.label_at.adjustSize()

        self.lineedit_path = QtWidgets.QLineEdit(self)
        self.lineedit_path.move(10, 440)
        self.lineedit_path.setPlaceholderText('/path/on/server')
        self.lineedit_path.resize(290, 30)

        self.lineedit_path_dir = QtWidgets.QLineEdit(self)
        self.lineedit_path_dir.move(10, 500)
        self.lineedit_path_dir.setPlaceholderText('/path/to/dir')
        self.lineedit_path_dir.resize(290, 30)



        self.button_test = QtWidgets.QPushButton(self)
        self.button_test.move(320, 440)
        self.button_test.setText('test connection')
        self.button_test.clicked.connect(self.test_upload)


        self.textedit = QtWidgets.QTextEdit(self)#little edit field to add additional info
        self.textedit.setPlaceholderText('Additional information,  this info will be uploaded to the server with run_info.txt')
        self.textedit.setGeometry(430, 400, 365, 195)

        Flowcell_liste = ['FLO-MIN106']


        
        self.label_barcode_yes_no = QtWidgets.QLabel(self)
        self.label_barcode_yes_no.setHidden(True)

    
        self.label1 = QtWidgets.QLabel(self)# labels for lineedits for the samples
        self.label1.setText('1')
        self.label1.move(245, 20)
        self.lineedit1 = QtWidgets.QLineEdit(self)
        self.lineedit1.move(260,20)
        #self.lineedit1.setFixedWidth(120)
        self.lineedit1.resize(240, 30)


        self.label2 = QtWidgets.QLabel(self)
        self.label2.setText('2')
        self.label2.move(245, 50)
        self.label2.setHidden(True)
        self.lineedit2 = QtWidgets.QLineEdit(self)
        self.lineedit2.move(260,50)
        self.lineedit2.setHidden(True)
        self.lineedit2.resize(240, 30)

        

        self.label3 = QtWidgets.QLabel(self) 
        self.label3.setText('3')
        self.label3.move(245, 80)
        self.label3.setHidden(True)
        self.lineedit3 = QtWidgets.QLineEdit(self)
        self.lineedit3.move(260,80)
        self.lineedit3.setHidden(True)
        self.lineedit3.resize(240, 30)


        self.label4 = QtWidgets.QLabel(self)
        self.label4.setText('4')
        self.label4.move(245, 110)
        self.label4.setHidden(True)
        self.lineedit4 = QtWidgets.QLineEdit(self)
        self.lineedit4.move(260,110)
        self.lineedit4.setHidden(True)
        self.lineedit4.resize(240, 30)


        self.label5 = QtWidgets.QLabel(self)
        self.label5.setText('5')
        self.label5.move(245, 140)
        self.label5.setHidden(True)
        self.lineedit5 = QtWidgets.QLineEdit(self)
        self.lineedit5.move(260,140)
        self.lineedit5.setHidden(True)
        self.lineedit5.resize(240, 30)


        self.label6 = QtWidgets.QLabel(self)
        self.label6.setText('6')
        self.label6.move(245, 170)
        self.label6.setHidden(True)
        self.lineedit6 = QtWidgets.QLineEdit(self)
        self.lineedit6.move(260,170)
        self.lineedit6.setHidden(True)
        self.lineedit6.resize(240, 30)


        self.label7 = QtWidgets.QLabel(self)
        self.label7.setText('7')
        self.label7.move(245, 200)
        self.label7.setHidden(True)
        self.lineedit7 = QtWidgets.QLineEdit(self)
        self.lineedit7.move(260,200)
        self.lineedit7.setHidden(True)
        self.lineedit7.resize(240, 30)

        self.label8 = QtWidgets.QLabel(self)
        self.label8.setText('8')
        self.label8.move(245, 230)
        self.label8.setHidden(True)
        self.lineedit8 = QtWidgets.QLineEdit(self)
        self.lineedit8.move(260,230)
        self.lineedit8.setHidden(True)
        self.lineedit8.resize(240, 30)

        self.label9 = QtWidgets.QLabel(self)
        self.label9.setText('9')
        self.label9.move(245, 260)
        self.label9.setHidden(True)
        self.lineedit9 = QtWidgets.QLineEdit(self)
        self.lineedit9.move(260,260)
        self.lineedit9.setHidden(True)
        self.lineedit9.resize(240, 30)

        self.label10 = QtWidgets.QLabel(self)
        self.label10.setText('10')
        self.label10.move(245, 290)
        self.label10.setHidden(True)
        self.lineedit10 = QtWidgets.QLineEdit(self)
        self.lineedit10.move(260,290)
        self.lineedit10.setHidden(True)
        self.lineedit10.resize(240, 30)

        self.label11 = QtWidgets.QLabel(self)
        self.label11.setText('11')
        self.label11.move(245, 320)
        self.label11.setHidden(True)
        self.lineedit11 = QtWidgets.QLineEdit(self)
        self.lineedit11.move(260,320)
        self.lineedit11.setHidden(True)
        self.lineedit11.resize(240, 30)

        self.label12 = QtWidgets.QLabel(self)
        self.label12.setText('12')
        self.label12.move(245, 350)
        self.label12.setHidden(True)
        self.lineedit12 = QtWidgets.QLineEdit(self)
        self.lineedit12.move(260, 350)
        self.lineedit12.setHidden(True)
        self.lineedit12.resize(240, 30)

        self.label13 = QtWidgets.QLabel(self)
        self.label13.setText('13')
        self.label13.move(533, 20)
        self.label13.setHidden(True)
        self.lineedit13 = QtWidgets.QLineEdit(self)
        self.lineedit13.move(550, 20)
        self.lineedit13.setHidden(True)
        self.lineedit13.resize(240, 30)

        self.label14 = QtWidgets.QLabel(self)
        self.label14.setText('14')
        self.label14.move(533, 50)
        self.label14.setHidden(True)
        self.lineedit14 = QtWidgets.QLineEdit(self)
        self.lineedit14.move(550,50)
        self.lineedit14.setHidden(True)
        self.lineedit14.resize(240, 30)

        self.label15 = QtWidgets.QLabel(self)
        self.label15.setText('15')
        self.label15.move(533, 80)
        self.label15.setHidden(True)
        self.lineedit15 = QtWidgets.QLineEdit(self)
        self.lineedit15.move(550, 80)
        self.lineedit15.setHidden(True)
        self.lineedit15.resize(240, 30)
        
        self.label16 = QtWidgets.QLabel(self)
        self.label16.setText('16')
        self.label16.move(533, 110)
        self.label16.setHidden(True)
        self.lineedit16 = QtWidgets.QLineEdit(self)
        self.lineedit16.move(550, 110)
        self.lineedit16.setHidden(True)
        self.lineedit16.resize(240, 30)
        
        self.label17 = QtWidgets.QLabel(self)
        self.label17.setText('17')
        self.label17.move(533, 140)
        self.label17.setHidden(True)
        self.lineedit17 = QtWidgets.QLineEdit(self)
        self.lineedit17.move(550, 140)
        self.lineedit17.setHidden(True)
        self.lineedit17.resize(240, 30)
        
        self.label18 = QtWidgets.QLabel(self)
        self.label18.setText('18')
        self.label18.move(533, 170)
        self.label18.setHidden(True)
        self.lineedit18 = QtWidgets.QLineEdit(self)
        self.lineedit18.move(550, 170)
        self.lineedit18.setHidden(True)
        self.lineedit18.resize(240, 30)
        
        self.label19 = QtWidgets.QLabel(self)
        self.label19.setText('19')
        self.label19.move(533, 200)
        self.label19.setHidden(True)
        self.lineedit19 = QtWidgets.QLineEdit(self)
        self.lineedit19.move(550, 200)
        self.lineedit19.setHidden(True)
        self.lineedit19.resize(240, 30)
        
        self.label20 = QtWidgets.QLabel(self)
        self.label20.setText('20')
        self.label20.move(533, 230)
        self.label20.setHidden(True)
        self.lineedit20 = QtWidgets.QLineEdit(self)
        self.lineedit20.move(550, 230)
        self.lineedit20.setHidden(True)
        self.lineedit20.resize(240, 30)
        
        self.label21 = QtWidgets.QLabel(self)
        self.label21.setText('21')
        self.label21.move(533, 260)
        self.label21.setHidden(True)
        self.lineedit21 = QtWidgets.QLineEdit(self)
        self.lineedit21.move(550, 260)
        self.lineedit21.setHidden(True)
        self.lineedit21.resize(240, 30)
        
        self.label22 = QtWidgets.QLabel(self)
        self.label22.setText('22')
        self.label22.move(533, 290)
        self.label22.setHidden(True)
        self.lineedit22 = QtWidgets.QLineEdit(self)
        self.lineedit22.move(550, 290)
        self.lineedit22.setHidden(True)
        self.lineedit22.resize(240, 30)
        
        self.label23 = QtWidgets.QLabel(self)
        self.label23.setText('23')
        self.label23.move(533, 320)
        self.label23.setHidden(True)
        self.lineedit23 = QtWidgets.QLineEdit(self)
        self.lineedit23.move(550, 320)
        self.lineedit23.setHidden(True)
        self.lineedit23.resize(240, 30)
        
        self.label24 = QtWidgets.QLabel(self)
        self.label24.setText('24')
        self.label24.move(533, 350)
        self.label24.setHidden(True)
        self.lineedit24 = QtWidgets.QLineEdit(self)
        self.lineedit24.move(550, 350)
        self.lineedit24.setHidden(True)
        self.lineedit24.resize(240, 30)

        

        self.button_checkdata = QtWidgets.QPushButton(self)#button to insepct data
        self.button_checkdata.setText('check data')
        self.button_checkdata.move(40, 350)
        self.button_checkdata.setWhatsThis('check your data')
        self.button_checkdata.clicked.connect(self.passinInformation)#function to open another window

        
        self.button_dir = QtWidgets.QPushButton(self)
        self.button_dir.setText('choose dir')
        self.button_dir.move(320, 500)
        self.button_dir.clicked.connect(self.choose_dir)


        self.button_upload = QtWidgets.QPushButton(self)
        self.button_upload.setText('Upload')
        self.button_upload.move(40, 560)
        self.button_upload.setToolTip('check data first, to enable upload')
        self.setStyleSheet("""QToolTip { 
                           background-color: black; 
                           color: white; 
                           border: black solid 1px
                           }""")
        self.button_upload.clicked.connect(self.upload)
        
    
        
        kitliste = ['Select Kit','SQK-PCB109','SQK-RNA002','SQK-PCS109','SQK-DCS109','SQK-CS9109','SQK-LSK109','SQK-LSK109-XL','SQK-16S024','SQK-LSK110',
        'SQK-LRK001','SQK-RBK004','SQK-PBK004','SQK-RAB204','SQK-RPB004','SQK-PSK004','SQK-RAD004'] 
        self.labelupload = QtWidgets.QLabel(self)
        self.labelupload.setText('')
        self.labelupload.setHidden(True)

        try:
            
            user_pre_info = open('/Users/T3ddezz/Desktop/Venv/GUI/user_info.txt','r')
            
            data_list = user_pre_info.read().splitlines()
            
            self.lineedit_username.setText(data_list[0])
            self.lineedit_path.setText(data_list[2])
            self.lineedit_ip_adress.setText(data_list[1])
        
            user_pre_info.close()
            self.test_upload_variable.setText('true')
        except IndexError:
            print('index error')

    def choose_dir(self):
        save_path = QFileDialog().getExistingDirectory(self, 'Select an  directory')

        self.lineedit_path_dir.setText(save_path)


    def upload(self, state):#function to upload files and create run_info.txt
        print("upload startet")
        save_path = self.lineedit_path_dir.text()
        
        name_of_file = 'run_info' 

        completeName = os.path.join(save_path, name_of_file + ".txt")    

        date = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')
           

        demo = open(completeName, "w")

        kit = self.sequencing_edit.text()
        barcodekit = self.barcode_edit.text()
        flowcell = self.flowcell_edit.text()

        demo.write('##toolname version 0')
        demo.write('\n')

        demo.write('##Kit:    ')
        demo.write(kit)
        demo.write('\n')

        demo.write('##Barcodekit:    ')
        demo.write(barcodekit)
        demo.write('\n')

        demo.write('##Flowcell:    ')
        demo.write(flowcell)
        demo.write('\n')
        
        
        
        label_yes_no = self.labelupload.text()
        
        if label_yes_no == 'no':
            lineedit01 = self.lineedit1.text()
            demo.write('NB01    ')
            demo.write(lineedit01)
            
        
        
        if label_yes_no == 'yes':
            checkbox_24 = self.checkbox.checkState()
            
            if checkbox_24 == 2:
                lineedit13 = self.lineedit13.text()
                lineedit14 = self.lineedit14.text()
                lineedit15 = self.lineedit15.text()
                lineedit16 = self.lineedit16.text()
                lineedit17 = self.lineedit17.text()
                lineedit18 = self.lineedit18.text()
                lineedit19 = self.lineedit19.text()
                lineedit20 = self.lineedit20.text()
                lineedit21 = self.lineedit21.text()
                lineedit22 = self.lineedit22.text()
                lineedit23 = self.lineedit23.text()
                lineedit24 = self.lineedit24.text()

                liste = [lineedit13,lineedit14,lineedit15,lineedit16,lineedit17,lineedit18,lineedit19,lineedit20,
                lineedit21,lineedit22,lineedit23,lineedit24]

                a = 13
                for i in range(0,12):
                    demo.write('NB0')
                    demo.write(str(a))
                    demo.write('    ')
                    demo.write(liste[i])
                    demo.write('\n')
                    a = a + 1       
            if checkbox_24 == 0 :
                
                lineedit01 = self.lineedit1.text()
                lineedit02 = self.lineedit2.text()
                lineedit03 = self.lineedit3.text()
                lineedit04 = self.lineedit4.text()
                lineedit05 = self.lineedit5.text()
                lineedit06 = self.lineedit6.text()
                lineedit07 = self.lineedit7.text()
                lineedit08 = self.lineedit8.text()
                lineedit09 = self.lineedit9.text()
                lineedit10 = self.lineedit10.text()
                lineedit11 = self.lineedit11.text()
                lineedit12 = self.lineedit12.text()
                liste = [lineedit01,lineedit02,lineedit03,lineedit04,lineedit05,lineedit06,lineedit07,lineedit08,
                lineedit09,lineedit10,lineedit11,lineedit12]
                a = 1
                for i in range(0,12):
                    if a<10:
                        demo.write('NB0')
                        demo.write(str(a))
                        demo.write('    ')
                        demo.write(liste[i])
                        demo.write('\n')
                        a = a + 1
                    else:
                        demo.write('NB')
                        demo.write(str(a))
                        demo.write('    ')
                        demo.write(liste[i])
                        demo.write('\n')
                        a = a + 1
            
            
                    
        
        additional_info = self.textedit.toPlainText()
        
        
        demo.write('##additional info')
        demo.write('\n')
        #demo.write('##')
        demo.write(additional_info)


        #/n zeilenumbruch
        demo.close()

        date = datetime.today().strftime('%Y-%m-%d')
        folder_name = os.path.basename(os.path.normpath(save_path))
        neuer_ordner_name = date + '_' + folder_name


        #check if rsync is avaible if yes then command (which rsync oder rsync -v)
        #os.system(f'rsync --rsync-path="/bin/rsync" -acr --remove-source-files "{save_path}" "~/Desktop/test_server/{neuer_ordner_name}"')
        #else scp

        path_on_server = self.lineedit_path.text()
        username = self.lineedit_username.text()
        ip = self.lineedit_ip_adress.text()
        password = self.password.text()
        rsync_var = self.rsync_var_label.text()
        rsync_var = rsync_var.strip()

        port = 22

        cmd = 'which rsync'
        try:
            
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(ip ,port ,username ,password, timeout=10)
            stdin,stdout,stderr = ssh.exec_command(cmd) 
            #print (stdout.channel.recv_exit_status())
            time.sleep(5)
            outlines = stdout.readlines()
            resp = ''.join(outlines)
            print(resp)
            rsync_var = resp
            rsync_var = rsync_var.strip()

            if rsync_var == 'rsync not found':
                os.system('scp -r ' + save_path + username + "@" +
                    ip + ":" + path_on_server + "/" + neuer_ordner_name)

            else:
                os.system('rsync --rsync-path=' + rsync_var + "-acrv --remove-source-files " + 
                    save_path + username + "@" + ip + ":" + path_on_server + "/" + neuer_ordner_name)
            except
                pass
        
    def sequencing_changed(self):

        url="https://raw.githubusercontent.com/t3ddezz/data/main/sequencing_data.txt"
        re=requests.get(url).content
        sequencing=pd.read_csv(io.StringIO(re.decode('utf-8')),sep='\t',index_col=False,header=None)

        kit_input = self.sequencing_edit.text()
        länge = len(sequencing)
        zähler = 0
        kit = 0

        for i in range(länge):
            if  kit_input == sequencing.loc[zähler,0]:
                kit = 1
                break
    
            else: 
                zähler = zähler + 1
        if kit == 0:
            msg = QMessageBox()
            msg.setWindowTitle("sequencing input")
            msg.setText("Something is wrong with your input!")
            x = msg.exec_()  # this will show our messagebox
            msg.setIcon(QMessageBox.Critical)
            self.sequencing_edit.clear()
            
    def barcode_changed(self):
        pass

    def flowcell_changed(self):
        url="https://raw.githubusercontent.com/t3ddezz/data/main/flowcell_data.txt"
        re=requests.get(url).content
        flowcell=pd.read_csv(io.StringIO(re.decode('utf-8')),sep='\t',index_col=False,header=None)

        flow_input = self.flowcell_edit.text()
        länge = len(flowcell)
        zähler = 0
        kit = 0

        for i in range(länge):
            if  flow_input == flowcell.loc[zähler,0]:
                kit = 1
                break
    
            else: 
                zähler = zähler + 1
        if kit == 0:
            msg = QMessageBox()
            msg.setWindowTitle("flowcell input")
            msg.setText("Something is wrong with your input!")
            x = msg.exec_()  # this will show our messagebox
            msg.setIcon(QMessageBox.Critical)
            self.flowcell_edit.clear()
        
    def test_upload(self):
        #dialog = QFileDialog()
        #save_path = dialog.getExistingDirectory(self, 'Select an  directory')
        
        
        #completeInfo = os.path.join('/Users/T3ddezz/Desktop/test_server',  'user_info.txt')
    
        username = self.lineedit_username.text()
        
        ip = self.lineedit_ip_adress.text()
        
        path = self.lineedit_path.text()
        
        password = self.password.text()

        

        user_info = open('user_info.txt', "w+")

        user_info.truncate(0)
        
        user_info.write(username)
        user_info.write('\n')
        user_info.write(ip)
        user_info.write('\n')
        user_info.write(path)

        user_info.close()

        try:
            #ip = '141.35.69.19'
            port = 22

            cmd  = 'ls'
            cmd2 = 'which rsync'
            cmd3 = 'ls -d ' + path 

            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(ip ,port ,username ,password, timeout=10)
            stdin,stdout,stderr = ssh.exec_command(cmd)
            #print (stdout.channel.recv_exit_status())
            time.sleep(5)
            outlines = stdout.readlines()
            resp = ''.join(outlines)
            #print(resp)

            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(ip ,port ,username ,password, timeout=10)
            stdin,stdout,stderr = ssh.exec_command(cmd2)
            #print (stdout.channel.recv_exit_status())
            time.sleep(5)
            outlines = stdout.readlines()
            resp2 = ''.join(outlines)
            #print(resp2)

            self.rsync_var_label.setText(resp2)
            rsync_var = resp2

            stdin,stdout,stderr = ssh.exec_command(cmd3)
            #print (stdout.channel.recv_exit_status())
            time.sleep(5)
            outlines = stdout.readlines()
            resp3 = ''.join(outlines)
            #print(resp3)
        


            print(path in resp3)#string doesnt have to match exactly at moment
            if path in resp3:
                msg = QMessageBox()
                msg.setWindowTitle("test upload")
                msg.setText("Connected succesfully!")
                x = msg.exec_()  # this will show our messagebox
                msg.setIcon(QMessageBox.Information)
            else:
                msg1 = QMessageBox()
                msg1.setWindowTitle("test upload")
                msg1.setText("Path doesnt exist")
                x1 = msg1.exec_()  # this will show our messagebox
                msg1.setIcon(QMessageBox.Critical)
                

    
        except paramiko.AuthenticationException:
            msg2 = QMessageBox()
            msg2.setWindowTitle("test upload")
            msg2.setText("Wrong username or password")
            x = msg2.exec_()  # this will show our messagebox
            msg2.setIcon(QMessageBox.Information)
        except socket.error:
            msg3 = QMessageBox()
            msg3.setWindowTitle("test upload")
            msg3.setText('Wrong ip')
            x = msg3.exec_()  # this will show our messagebox
            msg3.setIcon(QMessageBox.Information)
            

    def radioclicked_no(self):# 
        self.window2.hide()
        self.window2.hide2()
        self.labelupload.setText('no')
        self.label_barcode_yes_no.setText('no')
        self.label1.setHidden(False)
        self.label2.setHidden(True)
        self.label3.setHidden(True)
        self.label4.setHidden(True)
        self.label5.setHidden(True)
        self.label6.setHidden(True)
        self.label7.setHidden(True)
        self.label8.setHidden(True)
        self.label9.setHidden(True)
        self.label10.setHidden(True)
        self.label11.setHidden(True)
        self.label12.setHidden(True)
        self.lineedit1.setHidden(False)
        self.lineedit2.setHidden(True)
        self.lineedit3.setHidden(True)
        self.lineedit4.setHidden(True)
        self.lineedit5.setHidden(True)
        self.lineedit6.setHidden(True)
        self.lineedit7.setHidden(True)
        self.lineedit8.setHidden(True)
        self.lineedit9.setHidden(True)
        self.lineedit10.setHidden(True)
        self.lineedit11.setHidden(True)
        self.lineedit12.setHidden(True)
        self.label13.setHidden(True)
        self.lineedit13.setHidden(True)
        self.label14.setHidden(True)
        self.lineedit14.setHidden(True)
        self.label15.setHidden(True)
        self.lineedit15.setHidden(True)
        self.label16.setHidden(True)
        self.lineedit16.setHidden(True)
        self.label17.setHidden(True)
        self.lineedit17.setHidden(True)
        self.label18.setHidden(True)
        self.lineedit18.setHidden(True)
        self.label19.setHidden(True)
        self.lineedit19.setHidden(True)
        self.label20.setHidden(True)
        self.lineedit20.setHidden(True)
        self.label21.setHidden(True)
        self.lineedit21.setHidden(True)
        self.label22.setHidden(True)
        self.lineedit22.setHidden(True)
        self.label23.setHidden(True)
        self.lineedit23.setHidden(True)
        self.label24.setHidden(True)
        self.lineedit24.setHidden(True)
        self.download_template.setHidden(True)
        self.upload_data.setHidden(True)
   
    def radioclicked_yes(self):

        self.window2.hide()
        self.window2.unhide2()
        self.labelupload.setText('yes')
        self.label_barcode_yes_no.setText('yes')
        #self.checkbox.setHidden(False)
        #self.textedit.setDisabled(True)
        #self.textedit.setHidden(True)
        self.label1.setHidden(False)
        self.label2.setHidden(False)
        self.label3.setHidden(False)
        self.label4.setHidden(False)
        self.label5.setHidden(False)
        self.label6.setHidden(False)
        self.label7.setHidden(False)
        self.label8.setHidden(False)
        self.label9.setHidden(False)
        self.label10.setHidden(False)
        self.label11.setHidden(False)
        self.label12.setHidden(False)
        self.lineedit1.setHidden(False)
        self.lineedit2.setHidden(False)
        self.lineedit3.setHidden(False)
        self.lineedit4.setHidden(False)
        self.lineedit5.setHidden(False)
        self.lineedit6.setHidden(False)
        self.lineedit7.setHidden(False)
        self.lineedit8.setHidden(False)
        self.lineedit9.setHidden(False)
        self.lineedit10.setHidden(False)
        self.lineedit11.setHidden(False)
        self.lineedit12.setHidden(False)
        self.label13.setHidden(True)
        self.lineedit13.setHidden(True)
        self.label14.setHidden(True)
        self.lineedit14.setHidden(True)
        self.label15.setHidden(True)
        self.lineedit15.setHidden(True)
        self.label16.setHidden(True)
        self.lineedit16.setHidden(True)
        self.label17.setHidden(True)
        self.lineedit17.setHidden(True)
        self.label18.setHidden(True)
        self.lineedit18.setHidden(True)
        self.label19.setHidden(True)
        self.lineedit19.setHidden(True)
        self.label20.setHidden(True)
        self.lineedit20.setHidden(True)
        self.label21.setHidden(True)
        self.lineedit21.setHidden(True)
        self.label22.setHidden(True)
        self.lineedit22.setHidden(True)
        self.label23.setHidden(True)
        self.lineedit23.setHidden(True)
        self.label24.setHidden(True)
        self.lineedit24.setHidden(True)
        self.download_template.setHidden(True)
        self.upload_data.setHidden(True)

    
    def clickbox(self):
        self.label13.setHidden(False)
        self.lineedit13.setHidden(False)
        self.label14.setHidden(False)
        self.lineedit14.setHidden(False)
        self.label15.setHidden(False)
        self.lineedit15.setHidden(False)
        self.label16.setHidden(False)
        self.lineedit16.setHidden(False)
        self.label17.setHidden(False)
        self.lineedit17.setHidden(False)
        self.label18.setHidden(False)
        self.lineedit18.setHidden(False)
        self.label19.setHidden(False)
        self.lineedit19.setHidden(False)
        self.label20.setHidden(False)
        self.lineedit20.setHidden(False)
        self.label21.setHidden(False)
        self.lineedit21.setHidden(False)
        self.label22.setHidden(False)
        self.lineedit22.setHidden(False)
        self.label23.setHidden(False)
        self.lineedit23.setHidden(False)
        self.label24.setHidden(False)
        self.lineedit24.setHidden(False)
        self.window2.unhide()

        self.download_template.setHidden(True)
        self.upload_data.setHidden(True)
        self.label1.setHidden(False)
        self.label2.setHidden(False)
        self.label3.setHidden(False)
        self.label4.setHidden(False)
        self.label5.setHidden(False)
        self.label6.setHidden(False)
        self.label7.setHidden(False)
        self.label8.setHidden(False)
        self.label9.setHidden(False)
        self.label10.setHidden(False)
        self.label11.setHidden(False)
        self.label12.setHidden(False)
        self.lineedit1.setHidden(False)
        self.lineedit2.setHidden(False)
        self.lineedit3.setHidden(False)
        self.lineedit4.setHidden(False)
        self.lineedit5.setHidden(False)
        self.lineedit6.setHidden(False)
        self.lineedit7.setHidden(False)
        self.lineedit8.setHidden(False)
        self.lineedit9.setHidden(False)
        self.lineedit10.setHidden(False)
        self.lineedit11.setHidden(False)
        self.lineedit12.setHidden(False)
        '''
        self.label13.setHidden(True)
        self.lineedit13.setHidden(True)
        self.label14.setHidden(True)
        self.lineedit14.setHidden(True)
        self.label15.setHidden(True)
        self.lineedit15.setHidden(True)
        self.label16.setHidden(True)
        self.lineedit16.setHidden(True)
        self.label17.setHidden(True)
        self.lineedit17.setHidden(True)
        self.label18.setHidden(True)
        self.lineedit18.setHidden(True)
        self.label19.setHidden(True)
        self.lineedit19.setHidden(True)
        self.label20.setHidden(True)
        self.lineedit20.setHidden(True)
        self.label21.setHidden(True)
        self.lineedit21.setHidden(True)
        self.label22.setHidden(True)
        self.lineedit22.setHidden(True)
        self.label23.setHidden(True)
        self.lineedit23.setHidden(True)
        self.label24.setHidden(True)
        self.lineedit24.setHidden(True)
        self.window2.hide()'''
    
    def clickbox2(self):
        
            self.download_template.setHidden(False)
            self.upload_data.setHidden(False)
            self.label1.setHidden(True)
            self.label2.setHidden(True)
            self.label3.setHidden(True)
            self.label4.setHidden(True)
            self.label5.setHidden(True)
            self.label6.setHidden(True)
            self.label7.setHidden(True)
            self.label8.setHidden(True)
            self.label9.setHidden(True)
            self.label10.setHidden(True)
            self.label11.setHidden(True)
            self.label12.setHidden(True)
            self.lineedit1.setHidden(True)
            self.lineedit2.setHidden(True)
            self.lineedit3.setHidden(True)
            self.lineedit4.setHidden(True)
            self.lineedit5.setHidden(True)
            self.lineedit6.setHidden(True)
            self.lineedit7.setHidden(True)
            self.lineedit8.setHidden(True)
            self.lineedit9.setHidden(True)
            self.lineedit10.setHidden(True)
            self.lineedit11.setHidden(True)
            self.lineedit12.setHidden(True)
            self.label13.setHidden(True)
            self.lineedit13.setHidden(True)
            self.label14.setHidden(True)
            self.lineedit14.setHidden(True)
            self.label15.setHidden(True)
            self.lineedit15.setHidden(True)
            self.label16.setHidden(True)
            self.lineedit16.setHidden(True)
            self.label17.setHidden(True)
            self.lineedit17.setHidden(True)
            self.label18.setHidden(True)
            self.lineedit18.setHidden(True)
            self.label19.setHidden(True)
            self.lineedit19.setHidden(True)
            self.label20.setHidden(True)
            self.lineedit20.setHidden(True)
            self.label21.setHidden(True)
            self.lineedit21.setHidden(True)
            self.label22.setHidden(True)
            self.lineedit22.setHidden(True)
            self.label23.setHidden(True)
            self.lineedit23.setHidden(True)
            self.label24.setHidden(True)
            self.lineedit24.setHidden(True)
            self.window2.hide()
            '''
            self.download_template.setHidden(True)
            self.upload_data.setHidden(True)
            self.label1.setHidden(False)
            self.label2.setHidden(False)
            self.label3.setHidden(False)
            self.label4.setHidden(False)
            self.label5.setHidden(False)
            self.label6.setHidden(False)
            self.label7.setHidden(False)
            self.label8.setHidden(False)
            self.label9.setHidden(False)
            self.label10.setHidden(False)
            self.label11.setHidden(False)
            self.label12.setHidden(False)
            self.lineedit1.setHidden(False)
            self.lineedit2.setHidden(False)
            self.lineedit3.setHidden(False)
            self.lineedit4.setHidden(False)
            self.lineedit5.setHidden(False)
            self.lineedit6.setHidden(False)
            self.lineedit7.setHidden(False)
            self.lineedit8.setHidden(False)
            self.lineedit9.setHidden(False)
            self.lineedit10.setHidden(False)
            self.lineedit11.setHidden(False)
            self.lineedit12.setHidden(False)'''
    
    def passinInformation(self):
        self.button_upload.setEnabled(True)
        self.window2.input000.setText(self.flowcell_edit.text())
        self.window2.input0.setText(self.sequencing_edit.text())
        self.window2.input00.setText(self.barcode_edit.text())
        self.window2.input1.setText(self.lineedit1.text())
        self.window2.input3.setText(self.lineedit3.text())
        self.window2.input2.setText(self.lineedit2.text())
        self.window2.input4.setText(self.lineedit4.text())
        self.window2.input5.setText(self.lineedit5.text())
        self.window2.input6.setText(self.lineedit6.text())
        self.window2.input7.setText(self.lineedit7.text())
        self.window2.input8.setText(self.lineedit8.text())
        self.window2.input9.setText(self.lineedit9.text())
        self.window2.input10.setText(self.lineedit10.text())
        self.window2.input11.setText(self.lineedit11.text())
        self.window2.input12.setText(self.lineedit12.text())
        self.window2.input13.setText(self.lineedit13.text())
        self.window2.input14.setText(self.lineedit14.text())
        self.window2.input15.setText(self.lineedit15.text())
        self.window2.input16.setText(self.lineedit16.text())
        self.window2.input17.setText(self.lineedit17.text())
        self.window2.input18.setText(self.lineedit18.text())
        self.window2.input19.setText(self.lineedit19.text())
        self.window2.input20.setText(self.lineedit20.text())
        self.window2.input21.setText(self.lineedit21.text())
        self.window2.input22.setText(self.lineedit22.text())
        self.window2.input23.setText(self.lineedit23.text())
        self.window2.input24.setText(self.lineedit24.text())


        self.window2.displayInfo()
     

    def checkbox(self,state):
        if state == QtCore.Qt.Checked:
            self.password.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.password.setEchoMode(QtWidgets.QLineEdit.Password)
    




def window():
    app = QApplication(sys.argv)
    
    
    
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
window()    
