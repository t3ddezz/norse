#header with description 

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
from .Window2_libraries import *
from .validator_libraries import *
from pathlib import Path

#from __init__ import version

#print(version)
version = "0.3.2"

class MyWindow(QMainWindow):#create a window through the initUI() method, and call it in the initialization method init()
    
    def __init__(self):
        super(MyWindow, self).__init__()
        
        #self.secondwindow = Window2()
        self.setGeometry(200, 200, 800, 600)
        self.setWindowTitle('norse')
        self.label_name_list_main = ["label" + str(item) for item in list(range(1, (24 + 1), 1))]
        self.input_name_list_main = ["lineedit" + str(item) for item in list(range(1, (24 + 1), 1))]
        self.upload_sample_path = "0"
        self.iniUI()#function call

    def iniUI(self):
        # 'self' is the first parameter of the methods of a class that refers to the instance of the same

        self.window2 = Window2()#for initiating window2
        home = str(Path.home())
        self.norse_user_info_path = home + "/norse_user_info.txt"
        globs, locs = globals(), locals()
        [exec(f"self.{label_name} = QtWidgets.QLabel(self)",globs, locs) for label_name in self.label_name_list_main]
        [exec(f"self.{input_name} = QtWidgets.QLineEdit(self)",globs, locs) for input_name in self.input_name_list_main]
        
        x_y_values_for_label = []
        label_move_y_value = 20
        for i in range(1,25,1):
            if i == 1:
                x_value = 245
            elif i < 13:
                label_move_y_value += 30
            elif i == 13:
                x_value = 533
                label_move_y_value = 20
            elif i > 13:
                label_move_y_value += 30
            x_y_values_for_label.append([x_value,label_move_y_value])

        [exec(f"self.{self.label_name_list_main[index]}.move(*{x_y_values_for_label[index]})",globs, locs) for index in range(len(self.label_name_list_main))]
        [exec(f"self.{self.label_name_list_main[index]}.setText(str({index}+ 1))",globs, locs) for index in range(len(self.label_name_list_main))]
        [exec(f'self.{label_name}.setHidden(True)', globs,locs) for label_name in self.label_name_list_main[(1-1):24]]
        self.label1.setHidden(False)

        x_y_values_for_input = []
        input_move_y_value = 20
        for i in range(1,25,1):
            if i == 1:
                x_value = 260
            elif i < 13:
                input_move_y_value += 30
            elif i == 13:
                x_value = 550
                input_move_y_value = 20
            elif i > 13:
                input_move_y_value += 30
            x_y_values_for_input.append([x_value,input_move_y_value])

        [exec(f"self.{self.input_name_list_main[index]}.move(*{x_y_values_for_input[index]})",globs, locs) for index in range(len(self.input_name_list_main))]
        [exec(f'self.{input_name}.resize(240,30)', globs,locs) for input_name in self.input_name_list_main[(1-1):24]]
        [exec(f'self.{input_name}.setHidden(True)', globs,locs) for input_name in self.input_name_list_main[(1-1):24]]
        self.lineedit1.setHidden(False)


        self.lineedit_dir_name = QtWidgets.QLineEdit(self)
        self.lineedit_dir_name.setPlaceholderText('your directory name(optional)')
        self.lineedit_dir_name.move(5, 10)
        self.lineedit_dir_name.setFixedWidth(210)

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
        self.checkbox_hide_unhide.stateChanged.connect(self.password_hide_unhide)
        self.checkbox_hide_unhide.move(370, 405)

        self.label_sonderzeichen = QtWidgets.QLabel(self)
        self.label_sonderzeichen.setText(':')
        self.label_sonderzeichen.adjustSize()
        self.label_sonderzeichen.move(250, 406)
        
        self.kitinfos_label = QtWidgets.QLabel(self)
        self.kitinfos_label.move(10, 50)
        self.kitinfos_label.setText('Ligation kit:')

        self.sequencing_kit_edit = QtWidgets.QComboBox(self)
        self.sequencing_kit_edit.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.sequencing_kit_edit.addItems(["SQK-LSK114", "SQK-LSK109", "RBK-004", "RBK-110.96"])
        #self.sequencing_kit_edit.setPlaceholderText('e.g SQK-LSK109')
        #self.sequencing_kit_edit.setMaxLength(13)
        self.sequencing_kit_edit.adjustSize()
        self.sequencing_kit_edit.move(10, 75)
        self.validator = Validator(self)
        self.sequencing_kit_edit.setValidator(self.validator)
        #self.sequencing_edit.textChanged[str].connect(self.sequencing_changed)
        self.sequencing_kit_edit.editingFinished.connect(self.text_changed) #.connect(self.sequencing_changed)currentTextChanged

        self.barcode_label = QtWidgets.QLabel(self)
        self.barcode_label.move(10, 102)
        self.barcode_label.setText('Barcode kit (optional):')
        self.barcode_label.adjustSize()

        
        self.barcode_edit = QtWidgets.QLineEdit(self)
        self.barcode_edit.setPlaceholderText('e.g EXP-PBC096')
        self.barcode_edit.adjustSize()
        self.barcode_edit.move(10, 120)
        self.barcode_edit.setValidator(self.validator)
        self.barcode_edit.editingFinished.connect(self.barcode_changed)
        
        self.flowcell_label = QtWidgets.QLabel(self)
        self.flowcell_label.move(10, 140)
        self.flowcell_label.setText('Flowcell:')

        self.flowcell_edit = QtWidgets.QLineEdit(self)
        self.flowcell_edit.setPlaceholderText('e.g FLO-MIN106')
        self.flowcell_edit.adjustSize()
        self.flowcell_edit.move(10, 165)
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
        self.radiobutton_24_samples.toggled.connect(self.radiobutton_24)
        self.radiobutton_24_samples.move(10, 265)
        self.samples_24_label = QtWidgets.QLabel(self)
        self.samples_24_label.setText('yes (24)')
        self.samples_24_label.move(30, 265)

        self.radiobutton_sample_sheet = QtWidgets.QRadioButton(self)
        self.radiobutton_sample_sheet.toggled.connect(self.radiobutton_96)
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
        self.download_template.setText('upload data')
        self.download_template.setDisabled(True)
        self.download_template.move(290, 140)
        self.download_template.clicked.connect(self.sample_upload)
        #tooltip is a help message, while mouse on button
        self.download_template.setToolTip('Click info to activate. Upload your 96-samples')
        self.setStyleSheet("""QToolTip { 
                           background-color: black; 
                           color: white; 
                           border: black solid 1px
                           }""")


        self.download_template.setHidden(True)

        self.upload_info = QtWidgets.QPushButton(self)
        self.upload_info.setText('info')
        self.upload_info.setDisabled(True)
        self.upload_info.move(290,100)
        self.upload_info.setHidden(True)
        self.upload_info.clicked.connect(self.info)

        self.lineedit_username = QtWidgets.QLineEdit(self)
        self.lineedit_username.move(10, 400)
        self.lineedit_username.setPlaceholderText('username')

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


        
        self.label_barcode_yes_no = QtWidgets.QLabel(self)
        self.label_barcode_yes_no.setHidden(True)

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
        self.button_upload.setToolTip('check data before upload')
        self.setStyleSheet("""QToolTip { 
                           background-color: black; 
                           color: white; 
                           border: black solid 1px
                           }""")
        self.button_upload.clicked.connect(self.upload)
        
        self.labelupload = QtWidgets.QLabel(self)#
        self.labelupload.setText('')
        self.labelupload.setHidden(True)


        """self.label_image = QtWidgets.QLabel(self)
        self.label_image.move(300, 140)
        self.label
        self.image = QtGui.QPixmap('image.png')
        self.label_image.setPixmap(self.image)"""

        self.tableWidget = QtWidgets.QTableWidget(self)
        self.tableWidget.move(400, 23)
        self.tableWidget.setHidden(True)
  
        #Row count
        self.tableWidget.setRowCount(6) 
  
        #Column count
        self.tableWidget.setColumnCount(2)  
  
        self.tableWidget.setItem(0,0, QtWidgets.QTableWidgetItem("barcode"))
        self.tableWidget.setItem(0,1, QtWidgets.QTableWidgetItem("sample_id"))
        self.tableWidget.setItem(1,0, QtWidgets.QTableWidgetItem("1"))
        self.tableWidget.setItem(1,1, QtWidgets.QTableWidgetItem("sample_1"))
        self.tableWidget.setItem(2,0, QtWidgets.QTableWidgetItem("2"))
        self.tableWidget.setItem(2,1, QtWidgets.QTableWidgetItem("sample_2"))
        self.tableWidget.setItem(3,0, QtWidgets.QTableWidgetItem("3"))
        self.tableWidget.setItem(3,1, QtWidgets.QTableWidgetItem("sample_3"))
        self.tableWidget.setItem(4,0, QtWidgets.QTableWidgetItem("4"))
        self.tableWidget.setItem(4,1, QtWidgets.QTableWidgetItem("sample_4"))
        self.tableWidget.setItem(5,0, QtWidgets.QTableWidgetItem("6"))
        self.tableWidget.setItem(5,1, QtWidgets.QTableWidgetItem("sample_6"))
        self.tableWidget.setItem(6,0, QtWidgets.QTableWidgetItem("7"))
        self.tableWidget.setItem(6,1, QtWidgets.QTableWidgetItem("sample_7"))

        self.tableWidget.setMaximumWidth(215)
        self.tableWidget.setMinimumWidth(215)
        self.tableWidget.setMaximumHeight(200)
        self.tableWidget.setMinimumHeight(200)
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

        #table cant be changed
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        #self.tableWidget.resizeColumnsToContents()
        #self.tableWidget.setFixedWidth(self.tableWidget.columnWidth(0) + self.tableWidget.columnWidth(1))
        #self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableWidget_label = QtWidgets.QLabel(self)
        self.tableWidget_label.setText("xlsx example:")
        self.tableWidget_label.move(400,0)
        self.tableWidget_label.setHidden(True)
        self.tableWidget_label.setFont(QtGui.QFont("arial", 15))
        self.tableWidget_label.adjustSize()

        

        self.textedit_csv = QtWidgets.QTextEdit(self)#little edit field to add additional info
        self.textedit_csv.setPlaceholderText('barcode,sample_id             1,sample_1                           2,sample_2                          3,sample_3                          5,sample_5')
        self.textedit_csv.setGeometry(400, 238, 225, 150)
        self.textedit_csv.setHidden(True)
        self.textedit_csv_label = QtWidgets.QLabel(self)
        self.textedit_csv_label.setText("csv example:")
        self.textedit_csv_label.move(400, 215)
        self.textedit_csv_label.setHidden(True)
        self.textedit_csv_label.setFont(QtGui.QFont("arial", 15))
        self.textedit_csv_label.adjustSize()

        self.exclude_fast5_files = QtWidgets.QCheckBox('exclude fast5 files', self)
        self.exclude_fast5_files.move(150, 565)
        self.exclude_fast5_files.adjustSize()

        



        # check if there is a user info.txt if not no abortion
        try:
            
            user_pre_info = open(self.norse_user_info_path,'r')
            
            data_list = user_pre_info.read().splitlines()
            
            self.lineedit_username.setText(data_list[0])
            self.lineedit_path.setText(data_list[2])
            self.lineedit_ip_adress.setText(data_list[1])
        
            user_pre_info.close()
            self.test_upload_variable.setText('true')
        except IndexError:
            print('index error')
        except FileNotFoundError:
            print('file not found')


    def choose_dir(self):#pyqt5 build in directory select
        save_path = QFileDialog().getExistingDirectory(self, 'Select an  directory')

        self.lineedit_path_dir.setText(save_path)


    def upload(self, state):#function to upload files and create run_info.txt
        
        path_on_server = self.lineedit_path.text()
        username = self.lineedit_username.text()
        ip = self.lineedit_ip_adress.text()
        password = self.password.text()

        user_message_box = QMessageBox()
        user_message_box.setWindowTitle("user info")
        
        if username == "":
            user_message_box.setText("username is empty")
            x = user_message_box.exec_()
            return 13
        if ip == "":
            user_message_box.setText("ip is empty")
            x = user_message_box.exec_()
            return 14
        if path_on_server == "":
            user_message_box.setText("path is empty")
            x = user_message_box.exec_()
            return 15
        
        
        exclude_fast5_files_status = self.exclude_fast5_files.isChecked()
        
        save_path = self.lineedit_path_dir.text()
        
        name_of_file = 'run_info' 
        

        completeName = os.path.join(save_path, name_of_file + ".txt")    

        date = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')
           
        #demo == run_info.txt
        demo = open(completeName, "w")

        kit = self.sequencing_kit_edit.text()
        barcodekit = self.barcode_edit.text()
        flowcell = self.flowcell_edit.text()

        demo.write('Automatically generated by norse (version:' + version + ')')
        demo.write('\n')

        demo.write('##Kit:\t')
        demo.write(kit) 
        demo.write('\n')

        demo.write('##Barcodekit:\t')
        demo.write(barcodekit)
        demo.write('\n')

        demo.write('##Flowcell:\t')
        demo.write(flowcell)
        demo.write('\n\n')


        label_yes_no = self.labelupload.text()
        
        
        ## build for run_info.txt
        demo.write("Barcode\tSample-name\n")
        if label_yes_no == 'no':
            lineedit01 = self.lineedit1.text()
            
            demo.write('NB01\t')
            demo.write(lineedit01)
            
        
        
        if label_yes_no == 'yes':
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
                    demo.write('\t')
                    demo.write(liste[i])
                    demo.write('\n')
                    a = a + 1
                else:
                    demo.write('NB')
                    demo.write(str(a))
                    demo.write('\t')
                    demo.write(liste[i])
                    demo.write('\n')
                    a = a + 1
            

            
        if label_yes_no == '24':
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
                    demo.write('\t')
                    demo.write(liste[i])
                    demo.write('\n')
                    a = a + 1       
        if label_yes_no == "96":
            #print(file_1)
            if self.file_1 == "csv":
                sample_csv = pd.read_csv(self.upload_sample_path, sep=',',header=None)
                #print(sample_csv)
            if self.file_1 == "xlsx":
                sample_excel = pd.read_excel(self.upload_sample_path, header=None)
                #print(sample_excel)


            #reading csv files
            if self.file_1  == "csv":
                zeile = 0
                gesamt_zeilen = len(sample_csv)
                while True:
                    if sample_csv.iloc[zeile, 0] == "barcode":
                        #print(zeile)
                        break
                    else:
                        zeile = zeile + 1
                        if zeile == gesamt_zeilen:
                            zeile = 0
                            break

                if sample_csv.iloc[zeile, 0] == "barcode":
                    zeile = zeile + 1
                    for zeilen in range(zeile, gesamt_zeilen):
                        if zeilen < 10:
                            demo.write('NB0')
                            demo.write(str(sample_csv.iloc[zeilen, 0]))#barcode number
                            demo.write('\t')
                            demo.write(str(sample_csv.iloc[zeilen, 1]))#sample id
                            demo.write('\n')
                        else:
                            demo.write('NB')
                            demo.write(str(sample_csv.iloc[zeilen, 0]))#barcode number
                            demo.write('\t')
                            demo.write(str(sample_csv.iloc[zeilen, 1]))#sample id
                            demo.write('\n')
                

            #reading excel files (xlsx)
            if self.file_1 == "xlsx":
                zeile = 0
                gesamt_zeilen = len(sample_excel)
                while True:
                    if sample_excel.iloc[zeile, 0] == "barcode":
                        #print(zeile)
                        break
                    else:
                        zeile = zeile + 1 
                        if zeile == gesamt_zeilen:
                            zeile = 0
                            break

                if sample_excel.iloc[zeile, 0] == "barcode":
                    zeile = zeile + 1
                    for zeilen in range(zeile, gesamt_zeilen):
                        if zeilen < 10:
                            demo.write('NB0')
                            demo.write(str(sample_excel.iloc[zeilen, 0]))#barcode number
                            demo.write('\t')
                            demo.write(str(sample_excel.iloc[zeilen, 1]))#sample id
                            demo.write('\n')
                        else:
                            demo.write('NB')
                            demo.write(str(sample_excel.iloc[zeilen, 0]))#barcode number
                            demo.write('\t‚')
                            demo.write(str(sample_excel.iloc[zeilen, 1]))#sample id
                            demo.write('\n')

               

        

    
                    
        
        additional_info = self.textedit.toPlainText()
        
        demo.write('\n')
        demo.write('##Additional info')
        demo.write('\n')
        demo.write(additional_info)
        demo.write('\n')

        demo.close()

        date = datetime.today().strftime('%Y-%m-%d-%H%M%S')
        if self.lineedit_dir_name.text():
            folder_name = self.lineedit_dir_name.text()
            neuer_ordner_name = date + '_' + folder_name
            print("if")
            print(neuer_ordner_name)
        else:
            folder_name = os.path.basename(os.path.normpath(save_path))
            neuer_ordner_name = date + '_' + folder_name
            print("else")
            print(neuer_ordner_name)


        #check if rsync is avaible if yes then command (which rsync oder rsync -v)
        #os.system(f'rsync --rsync-path="/bin/rsync" -acr --remove-source-files "{save_path}" "~/Desktop/test_server/{neuer_ordner_name}"')
        #else scp

        path_on_server = self.lineedit_path.text()
        username = self.lineedit_username.text()
        ip = self.lineedit_ip_adress.text()
        password = self.password.text()
        

        port = 22
        cmd = 'which rsync'
        cmd2 = 'echo $?'

        #connect to server, if fail error printed. But connection is tested in func test_upload
        try:
            
            message_box = QMessageBox()
            message_box.setWindowTitle("upload startet")
            message_box.setText("Upload startet, close this window")
            x = message_box.exec()
            msg = QMessageBox()
            msg.setWindowTitle("upload")

            # ssh = paramiko.SSHClient()
            # ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            # ssh.connect(ip ,port ,username ,password, timeout=10)
            # stdin,stdout,stderr = ssh.exec_command(cmd) 
            # time.sleep(5)
            # outlines = stdout.readlines()
            # resp = ''.join(outlines)
            # rsync_var = resp
            # rsync_var = rsync_var.strip()

            # ssh2 = paramiko.SSHClient()
            # ssh2.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            # ssh2.connect(ip ,port ,username ,password, timeout=10)
            # stdin,stdout,stderr = ssh2.exec_command("which rsync \n echo $?") 
            # time.sleep(5)
            # outlines2 = stdout.readlines()
            # exit_code = outlines2[1]
            # exit_code = exit_code.strip()
            exit_code = "0"
            
            if exit_code != "0":
                if exclude_fast5_files_status == False:
                    #os.system('scp -r ' + save_path + username + "@" +
                     #   ip + ":" + path_on_server + "/" + neuer_ordner_name)
                    scp_exit_code = os.system(f'scp -r {save_path} {username}@{ip}:"{path_on_server}"/"{neuer_ordner_name}"')
                    if scp_exit_code != 0:
                        msg.setText("upload failed")
                        x = msg.exec_()
                    else:
                        msg.setText("upload complete")
                        x = msg.exec_()
                elif exclude_fast5_files_status == True:
                    scp_exit_code = os.system(f'scp -r {save_path} {username}@{ip}:"{path_on_server}"/"{neuer_ordner_name}"')
                    if scp_exit_code != 0:
                        msg.setText("upload failed")
                        x = msg.exec_()
                    else:
                        msg.setText("upload complete")
                        x = msg.exec_()
                
            else:
                if exclude_fast5_files_status == False:
                    rsync_exit_code = os.system(f'rsync -acrv --remove-source-files "{save_path}" {username}@{ip}:"{path_on_server}"/"{neuer_ordner_name}"')
                    if rsync_exit_code != 0:
                        msg.setText("upload failed")
                        x = msg.exec_()
                    else:
                        msg.setText("upload complete")
                        x = msg.exec_()  

                    
                    #sys.exit(0)
                elif exclude_fast5_files_status == True:
                    rsync_exit_code = os.system(f'rsync  --exclude "*.fast5" --exclude "*.pod5" -acrv --remove-source-files "{save_path}" {username}@{ip}:"{path_on_server}"/"{neuer_ordner_name}"')
                    if rsync_exit_code != 0:
                        msg.setText("upload failed")
                        x = msg.exec_()
                    else:
                        msg.setText("upload complete")
                        x = msg.exec_()
                
               
            
        except paramiko.AuthenticationException:
            print('connection error')
        except socket.timeout:
            print('connection error')
        

    def sequencing_changed(self):

        url="https://raw.githubusercontent.com/t3ddezz/data/main/sequencing_data.txt"
        re=requests.get(url).content
        sequencing=pd.read_csv(io.StringIO(re.decode('utf-8')),sep='\t',index_col=False,header=None)

        kit_input = self.sequencing_kit_edit.text()
        lange = len(sequencing)
        zahler = 0
        kit = 0

        if len(kit_input) > 0:
            for i in range(lange):
                if  kit_input == sequencing.loc[zahler,0]:
                    kit = 1
                    break
        
                else: 
                    zahler = zahler + 1
            if kit == 0:
                msg = QMessageBox()
                msg.setWindowTitle("Sequencing-Kit input")
                msg.setText("Something is wrong with your input!")
                x = msg.exec_()  # this will show our messagebox
                msg.setIcon(QMessageBox.Critical)
                self.sequencing_kit_edit.clear()


    def barcode_changed(self):#if barcode list, could add barcode restriction
        pass


    def flowcell_changed(self):#flowcell check after flowcell input 
        url="https://raw.githubusercontent.com/t3ddezz/data/main/flowcell_data.txt"
        re=requests.get(url).content
        flowcell=pd.read_csv(io.StringIO(re.decode('utf-8')),sep='\t',index_col=False,header=None)

        flow_input = self.flowcell_edit.text()
        lange = len(flowcell)
        zahler = 0
        kit = 0

        if len(flow_input) > 0:
            for i in range(lange):
                if  flow_input == flowcell.loc[zahler,0]:
                    kit = 1
                    break
        
                else: 
                    zahler = zahler + 1
            if kit == 0:
                msg = QMessageBox()
                msg.setWindowTitle("Flowcell input")
                msg.setText("Something is wrong with your input!")
                x = msg.exec_()  # this will show our messagebox
                msg.setIcon(QMessageBox.Critical)
                self.flowcell_edit.clear()
        

    def test_upload(self):#test connection to server and add info to user_info.txt

    
        username = self.lineedit_username.text()
        
        ip = self.lineedit_ip_adress.text()
        
        path = self.lineedit_path.text()
        
        password = self.password.text()

         

        user_info = open(self.norse_user_info_path, "w+")

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
            cmd3 = 'ls -d ' + path 

            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(ip ,port ,username ,password, timeout=10)
            stdin,stdout,stderr = ssh.exec_command(cmd)
            time.sleep(5)
            outlines = stdout.readlines()
            resp = ''.join(outlines)




            stdin,stdout,stderr = ssh.exec_command(cmd3)
            time.sleep(5)
            outlines = stdout.readlines()
            resp3 = ''.join(outlines)
        


            #print(path in resp3)#string doesnt have to match exactly at moment
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


    def radioclicked_no(self):# button no barcodes
        self.window2.hide_and_show(2,24,True)
        self.labelupload.setText('no')
        self.label_barcode_yes_no.setText('no')
        globs, locs = globals(), locals()
        [exec(f'self.{label_name}.setHidden(True)', globs,locs) for label_name in self.label_name_list_main[(0):24]]
        [exec(f'self.{input_name}.setHidden(True)', globs,locs) for input_name in self.input_name_list_main[(0):24]]

        self.label1.setHidden(False)
        self.lineedit1.setHidden(False)

        self.download_template.setHidden(True)
        self.download_template.setDisabled(True)
        self.upload_info.setHidden(True)
        self.upload_info.setDisabled(True)
        self.tableWidget.setHidden(True)
        self.textedit_csv.setHidden(True)
        self.textedit_csv_label.setHidden(True)
        self.tableWidget_label.setHidden(True)
   

    def radioclicked_yes(self):# button for 1-12 samples

        self.window2.hide_and_show(1,12,False)
        self.window2.hide_and_show(13,24,True)
        self.labelupload.setText('yes')
        self.label_barcode_yes_no.setText('yes')
        
        globs, locs = globals(), locals()
        [exec(f'self.{label_name}.setHidden(False)', globs,locs) for label_name in self.label_name_list_main[(0):12]]
        [exec(f'self.{input_name}.setHidden(False)', globs,locs) for input_name in self.input_name_list_main[(0):12]]
        
        [exec(f'self.{label_name}.setHidden(True)', globs,locs) for label_name in self.label_name_list_main[(12):24]]
        [exec(f'self.{input_name}.setHidden(True)', globs,locs) for input_name in self.input_name_list_main[(12):24]]

        self.download_template.setHidden(True)
        self.download_template.setDisabled(True)
        self.upload_info.setHidden(True)
        self.upload_info.setDisabled(True)
        self.tableWidget.setHidden(True)
        self.textedit_csv_label.setHidden(True)
        self.textedit_csv.setHidden(True)
        self.tableWidget_label.setHidden(True)
    

    def radiobutton_24(self): #button for samples 1-24
        self.labelupload.setText('24')

        globs, locs = globals(), locals()
        [exec(f'self.{label_name}.setHidden(False)', globs,locs) for label_name in self.label_name_list_main[(0):24]]
        [exec(f'self.{input_name}.setHidden(False)', globs,locs) for input_name in self.input_name_list_main[(0):24]]

        self.window2.hide_and_show(1,24,False)

        self.download_template.setHidden(True)
        self.download_template.setDisabled(True)
        self.upload_info.setHidden(True)
        self.upload_info.setDisabled(True)
        self.tableWidget.setHidden(True)
        self.textedit_csv.setHidden(True)
        self.textedit_csv_label.setHidden(True)
        self.tableWidget_label.setHidden(True)


    def radiobutton_96(self):#button for 94-samples

            self.labelupload.setText('96')
            self.download_template.setHidden(False)
            self.upload_info.setHidden(False)
            self.upload_info.setDisabled(False)
            self.tableWidget.setHidden(False)
            self.textedit_csv.setHidden(False)
            self.textedit_csv_label.setHidden(False)
            self.tableWidget_label.setHidden(False)
            self.window2.hide_and_show(1,24,True)

            globs, locs = globals(), locals()
            [exec(f'self.{label_name}.setHidden(True)', globs,locs) for label_name in self.label_name_list_main[(0):24]]
            [exec(f'self.{input_name}.setHidden(True)', globs,locs) for input_name in self.input_name_list_main[(0):24]]
            
            self.window2.hide()
    

    def passinInformation(self):#all infos from mainwindow for window 2 to display there
        self.button_upload.setEnabled(True)
        self.window2.input_flowcell.setText(self.flowcell_edit.text())
        self.window2.input_kit.setText(self.sequencing_kit_edit.text())
        self.window2.input_barcode.setText(self.barcode_edit.text())
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
     

    def password_hide_unhide(self,state):#fucntion to hide password
        if state == QtCore.Qt.Checked:
            self.password.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.password.setEchoMode(QtWidgets.QLineEdit.Password)
    

    def sample_upload(self):
        #download template, so its unique to read 
        try:
            
            self.upload_sample_path, _ = QFileDialog.getOpenFileName(self, 'Select sample sheet',"~", "data files(*.csv *.xlsx)")
            self.window2.upload_sample_path = self.upload_sample_path
            filename =  QFileInfo(self.upload_sample_path).fileName()

            self.file_1 = filename.split(".",1)[1]
            self.window2.file_1 = self.file_1
            self.window2.open_sheet()
            
        except IndexError:
            print('no file selected')
        

    def info(self):
        msg = QMessageBox()
        msg.setWindowTitle("data input")
        msg.setText("If you wanna use 96 samples, please create a csv(.csv) or excel(.xlsx) file with like shown on the rigth side. Remember to write the headers (barcode, sampleid) not in caps.")
        x = msg.exec_()
        self.download_template.setDisabled(False)
