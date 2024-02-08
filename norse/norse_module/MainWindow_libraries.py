#functions defining main Window GUI and In-/Outputs

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

version = "0.5.0"

class MyWindow(QMainWindow):    #create a window through the initUI() method, and call it in the initialization method init()
    
    def __init__(self): #'self' is the first parameter of a class' methods that refers to the actual instance of the class
        super(MyWindow, self).__init__()
        
        #define window geometry and title
        self.setGeometry(200, 200, 800, 600)
        self.setWindowTitle('norse')
        
        #create two lists of 24 strings each, called "label1"/"lineedit1" to "label24"/"lineedit24" -> a label is a text element shown in the GUI
        self.label_name_list_main = ["label" + str(item) for item in list(range(1, 25, 1))]
        self.input_name_list_main = ["lineedit" + str(item) for item in list(range(1, 25, 1))]
        
        self.upload_sample_path = "0"
        self.iniUI()    #function call


    def iniUI(self):

        self.window2 = Window2()    #initiate window2
        home = str(Path.home())
        self.norse_user_info_path = home + "/norse_user_info.txt"
        globs, locs = globals(), locals()
        [exec(f"self.{label_name} = QtWidgets.QLabel(self)",globs, locs) for label_name in self.label_name_list_main]
        [exec(f"self.{input_name} = QtWidgets.QLineEdit(self)",globs, locs) for input_name in self.input_name_list_main]
        
        x_y_coords_for_label = []   #set up empty list
        x_y_coords_for_input = []
        Y_COORD = 20 #initial label y-coord
        for i in range(1,25,1): #loop over 24 numbers to adjust x and y coords to set up two columns with 12 label and input fields each
            if i == 1:
                LABEL_X_COORD = 245
                INPUT_X_COORD = 260
            elif i < 13:
                Y_COORD += 30
            elif i == 13:
                LABEL_X_COORD = 533
                INPUT_X_COORD = 550
                Y_COORD = 20
            elif i > 13:
                Y_COORD += 30
            x_y_coords_for_label.append([LABEL_X_COORD,Y_COORD])
            x_y_coords_for_input.append([INPUT_X_COORD,Y_COORD])

        #create label and input fields with names and coords
        [exec(f"self.{self.label_name_list_main[index]}.move(*{x_y_coords_for_label[index]})",globs, locs) for index in range(len(self.label_name_list_main))]
        [exec(f"self.{self.input_name_list_main[index]}.move(*{x_y_coords_for_input[index]})",globs, locs) for index in range(len(self.input_name_list_main))]
        
        #set mock-text for each label and input field
        [exec(f"self.{self.label_name_list_main[index]}.setText(str({index}+ 1))",globs, locs) for index in range(len(self.label_name_list_main))]
        [exec(f'self.{input_name}.resize(240,30)', globs,locs) for input_name in self.input_name_list_main[(1-1):24]]

        #hide all label and input fields on initialization
        [exec(f'self.{label_name}.setHidden(True)', globs,locs) for label_name in self.label_name_list_main[(1-1):24]]
        [exec(f'self.{input_name}.setHidden(True)', globs,locs) for input_name in self.input_name_list_main[(1-1):24]]

        #show first label and input field upon initialization
        self.label1.setHidden(False)   
        self.lineedit1.setHidden(False)

        #set up field for dir input
        self.lineedit_dir_name = QtWidgets.QLineEdit(self)  #create instance of wanted class in the QtWidgets-package 
        self.lineedit_dir_name.setPlaceholderText('your directory name(optional)')  #set mock text
        self.lineedit_dir_name.move(5, 10)  #move field to specified position
        self.lineedit_dir_name.setFixedWidth(210)   #declare fixed width of field

        #set up frames in window
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

        #set up field for password input
        self.password = QtWidgets.QLineEdit(self)
        self.password.move(260, 400)
        self.password.setPlaceholderText('password')
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)

        #set up button to hide/show text in password field above
        self.checkbox_hide_unhide = QtWidgets.QCheckBox('show',self)
        self.checkbox_hide_unhide.adjustSize()
        self.checkbox_hide_unhide.stateChanged.connect(self.password_hide_unhide)
        self.checkbox_hide_unhide.move(370, 405)

        #set up label ":"
        self.label_special_character = QtWidgets.QLabel(self)
        self.label_special_character.setText(':')
        self.label_special_character.adjustSize()
        self.label_special_character.move(250, 406)
        
        #set up label and input field for sequencing kit (with option table and self-validation)
        self.label_sequencing_kit = QtWidgets.QLabel(self)
        self.label_sequencing_kit.move(10, 50)
        self.label_sequencing_kit.setText('Ligation kit:')

        with open('/norse/data/sequencing_kit_data.txt') as file:   #open file containing all possible sequencing kits
            sequencing_kit_list = [line.rstrip() for line in file]  #read all lines into list removing whitespaces
        self.input_sequencing_kit = QtWidgets.QComboBox(self)    #initialize necessary class instance
        self.input_sequencing_kit.setEditable(True)  #allow inputs to the field
        self.input_sequencing_kit.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.input_sequencing_kit.addItems(sequencing_kit_list)  #add list of seq-kits as options for the field
        self.input_sequencing_kit.setMinimumWidth(190)
        self.input_sequencing_kit.move(10, 75)
        self.validator = Validator(self)
        self.input_sequencing_kit.setValidator(self.validator)
        self.input_sequencing_kit.lineEdit().editingFinished.connect(self.sequencing_kit_changed)    #validate field input upon writing is finished -> checks if input matches a seq-kit from the list

        #label and input field for barcode-kit (analog to seq-kit input above)
        self.label_barcode_kit = QtWidgets.QLabel(self)
        self.label_barcode_kit.move(10, 102)
        self.label_barcode_kit.setText('Barcode kit (optional):')
        self.label_barcode_kit.adjustSize()

        self.input_barcode_kit = QtWidgets.QLineEdit(self)
        self.input_barcode_kit.setPlaceholderText('e.g EXP-PBC096')
        self.input_barcode_kit.adjustSize()
        self.input_barcode_kit.move(10, 120)
        self.input_barcode_kit.setValidator(self.validator)
        self.input_barcode_kit.editingFinished.connect(self.barcode_kit_changed)
        
        #label and input field for flowcell-type (analog to seq-kit input above)
        self.label_flowcell_kit = QtWidgets.QLabel(self)
        self.label_flowcell_kit.move(10, 140)
        self.label_flowcell_kit.setText('Flowcell:')

        with open('/norse/data/flowcell_data.txt') as file:
            flowcell_type_list = [line.rstrip() for line in file]
        self.input_flowcell_kit = QtWidgets.QComboBox(self)
        self.input_flowcell_kit.setEditable(True)
        self.input_flowcell_kit.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.input_flowcell_kit.addItems(flowcell_type_list)
        self.input_flowcell_kit.setMinimumWidth(190)
        self.input_flowcell_kit.move(10, 165)
        self.input_flowcell_kit.setValidator(self.validator)
        self.input_flowcell_kit.lineEdit().editingFinished.connect(self.flowcell_changed)

        #set up Barcode "yes" and "no" buttons - grouped, only one can be selected
        self.label_barcodes_question = QtWidgets.QLabel(self)
        self.label_barcodes_question.setText('Barcodes?')
        self.label_barcodes_question.move(10, 200)

        self.radiobutton_barcodes_no = QtWidgets.QRadioButton(self)  #set up round button for "no"
        self.radiobutton_barcodes_no.toggled.connect(self.radioclicked_no)  #toggle function "radioclicked_no" when button is selected
        self.radiobutton_barcodes_no.move(10, 225)
        self.label_radiobutton_no = QtWidgets.QLabel(self)
        self.label_radiobutton_no.setText('no')
        self.label_radiobutton_no.move(30, 225)

        self.radiobutton_barcodes_yes = QtWidgets.QRadioButton(self)
        self.radiobutton_barcodes_yes.toggled.connect(self.radioclicked_yes)
        self.radiobutton_barcodes_yes.move(10, 245)
        self.label_radiobutton_yes = QtWidgets.QLabel(self)
        self.label_radiobutton_yes.setText('yes (12)')
        self.label_radiobutton_yes.move(30, 245)

        #set up label for test_upload and hide it
        self.label_test_upload_variable = QtWidgets.QLabel(self)
        self.label_test_upload_variable.setHidden(True)

        #set up button to select input for 24 samples 
        self.radiobutton_24_samples = QtWidgets.QRadioButton(self)
        self.radiobutton_24_samples.toggled.connect(self.radiobutton_24)
        self.radiobutton_24_samples.move(10, 265)
        self.samples_24_label = QtWidgets.QLabel(self)
        self.samples_24_label.setText('yes (24)')
        self.samples_24_label.move(30, 265)

        ##set up button to select input of an individual sample sheet (csv/tsv/xlsx)
        self.radiobutton_sample_sheet = QtWidgets.QRadioButton(self)
        self.radiobutton_sample_sheet.toggled.connect(self.radiobutton_96)
        self.radiobutton_sample_sheet.move(10, 285)
        self.sample_sheet_label = QtWidgets.QLabel(self)
        self.sample_sheet_label.setText('yes (sample sheet)')
        self.sample_sheet_label.move(30, 290)
        self.sample_sheet_label.resize(150, 20)

        #group buttons so only one of them is active at a time
        self.radiobutton_group = QtWidgets.QButtonGroup(self)
        self.radiobutton_group.addButton(self.radiobutton_barcodes_yes)
        self.radiobutton_group.addButton(self.radiobutton_barcodes_no)
        self.radiobutton_group.addButton(self.radiobutton_24_samples)
        self.radiobutton_group.addButton(self.radiobutton_sample_sheet)

        #set up upload button for user barcode-file
        self.pushbutton_download_template = QtWidgets.QPushButton(self)
        self.pushbutton_download_template.setText('upload data')
        self.pushbutton_download_template.setDisabled(True)
        self.pushbutton_download_template.move(290, 140)
        self.pushbutton_download_template.clicked.connect(self.sample_upload)
        #show tooltip with help message while mouse hovers on button
        self.pushbutton_download_template.setToolTip('Click info to activate. Upload your 96-samples')
        self.setStyleSheet("""QToolTip { 
                           background-color: black; 
                           color: white; 
                           border: black solid 1px
                           }""")

        self.pushbutton_download_template.setHidden(True)

        #set up button to upload info??? -> button is only active when using 96-sample sheet input
        self.upload_info = QtWidgets.QPushButton(self)
        self.upload_info.setText('info')
        self.upload_info.setDisabled(True)
        self.upload_info.move(290,100)
        self.upload_info.setHidden(True)
        self.upload_info.clicked.connect(self.info)

        #set up input fields for user, ip-adresse and pathes on server and to upload dir
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

        self.lineedit_server_path = QtWidgets.QLineEdit(self)
        self.lineedit_server_path.move(10, 440)
        self.lineedit_server_path.setPlaceholderText('/path/on/server')
        self.lineedit_server_path.resize(290, 30)

        self.lineedit_upload_dir_path = QtWidgets.QLineEdit(self)
        self.lineedit_upload_dir_path.move(10, 500)
        self.lineedit_upload_dir_path.setPlaceholderText('/path/to/dir')
        self.lineedit_upload_dir_path.resize(290, 30)

        #set up push button to test server connection
        self.button_test_connection = QtWidgets.QPushButton(self)
        self.button_test_connection.move(320, 440)
        self.button_test_connection.setText('test connection')
        self.button_test_connection.clicked.connect(self.test_upload)

        #set up input field for additional info
        self.input_additional_info = QtWidgets.QTextEdit(self)
        self.input_additional_info.setPlaceholderText('Additional information,  this info will be uploaded to the server with run_info.txt')
        self.input_additional_info.setGeometry(430, 400, 365, 195)

        #set up label for barcdes yes/no button???
        self.label_barcode_yes_no = QtWidgets.QLabel(self)
        self.label_barcode_yes_no.setHidden(True)

        #set up push button to check data
        self.button_checkdata = QtWidgets.QPushButton(self)
        self.button_checkdata.setText('check data')
        self.button_checkdata.move(40, 350)
        self.button_checkdata.setWhatsThis('check your data')   #
        self.button_checkdata.clicked.connect(self.passinInformation)   #upon clicking call function to open another window

        #set up push button to choose upload dir
        self.button_upload_dir = QtWidgets.QPushButton(self)
        self.button_upload_dir.setText('choose dir')
        self.button_upload_dir.move(320, 500)
        self.button_upload_dir.clicked.connect(self.choose_upload_dir)

        #set up push button to upload data to server (with tooltip)
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

        #set up hidden, empty label ??? 
        self.label_upload = QtWidgets.QLabel(self)
        self.label_upload.setText('')
        self.label_upload.setHidden(True)

        """self.label_image = QtWidgets.QLabel(self)
        self.label_image.move(300, 140)
        self.label
        self.image = QtGui.QPixmap('image.png')
        self.label_image.setPixmap(self.image)"""

        #set up hidden table
        self.tableWidget = QtWidgets.QTableWidget(self)
        self.tableWidget.move(400, 23)
        self.tableWidget.setHidden(True)
        self.tableWidget.setRowCount(6) #row count
        self.tableWidget.setColumnCount(2)  #column count

        #insert values in table [row, column, value]
        self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem("barcode"))
        self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem("sample_id"))
        self.tableWidget.setItem(1, 0, QtWidgets.QTableWidgetItem("1"))
        self.tableWidget.setItem(1, 1, QtWidgets.QTableWidgetItem("sample_1"))
        self.tableWidget.setItem(2, 0, QtWidgets.QTableWidgetItem("2"))
        self.tableWidget.setItem(2, 1, QtWidgets.QTableWidgetItem("sample_2"))
        self.tableWidget.setItem(3, 0, QtWidgets.QTableWidgetItem("3"))
        self.tableWidget.setItem(3, 1, QtWidgets.QTableWidgetItem("sample_3"))
        self.tableWidget.setItem(4, 0, QtWidgets.QTableWidgetItem("4"))
        self.tableWidget.setItem(4, 1, QtWidgets.QTableWidgetItem("sample_4"))
        self.tableWidget.setItem(5, 0, QtWidgets.QTableWidgetItem("6"))
        self.tableWidget.setItem(5, 1, QtWidgets.QTableWidgetItem("sample_6"))
        self.tableWidget.setItem(6, 0, QtWidgets.QTableWidgetItem("7"))
        self.tableWidget.setItem(6, 1, QtWidgets.QTableWidgetItem("sample_7"))

        #define table outlines and trigger on edit
        self.tableWidget.setMaximumWidth(215)
        self.tableWidget.setMinimumWidth(215)
        self.tableWidget.setMaximumHeight(200)
        self.tableWidget.setMinimumHeight(200)
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

        #table cant be changed
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        #set up labels for table
        self.tableWidget_label = QtWidgets.QLabel(self)
        self.tableWidget_label.setText("xlsx example:")
        self.tableWidget_label.move(400,0)
        self.tableWidget_label.setHidden(True)
        self.tableWidget_label.setFont(QtGui.QFont("arial", 15))
        self.tableWidget_label.adjustSize()

        #set up input field and label for csv example
        self.textedit_csv = QtWidgets.QTextEdit(self)   #little edit field to add additional info
        self.textedit_csv.setPlaceholderText('barcode,sample_id             1,sample_1                           2,sample_2                          3,sample_3                          5,sample_5')
        self.textedit_csv.setGeometry(400, 238, 225, 150)
        self.textedit_csv.setHidden(True)
        self.textedit_csv_label = QtWidgets.QLabel(self)
        self.textedit_csv_label.setText("csv example:")
        self.textedit_csv_label.move(400, 215)
        self.textedit_csv_label.setHidden(True)
        self.textedit_csv_label.setFont(QtGui.QFont("arial", 15))
        self.textedit_csv_label.adjustSize()

        #set up checkbox to exclud fast5/pod5 files from upload
        self.exclude_fast5_files = QtWidgets.QCheckBox('exclude fast5/pod5 files', self)
        self.exclude_fast5_files.move(150, 565)
        self.exclude_fast5_files.adjustSize()

        # check if there is a user_info.txt if not no abortion -> file is created in function "test_upload"
        try:    #test if command can be executed else exceptions according to errors
            user_pre_info_file = open(self.norse_user_info_path, 'r')    #open file in read-mode
            user_pre_info_list = user_pre_info_file.read().splitlines()  #read file splitting into list by lines
            
            #put username, ip-adresse and server-path into according fields in the GUI
            self.lineedit_username.setText(user_pre_info_list[0])
            self.lineedit_server_path.setText(user_pre_info_list[2])
            self.lineedit_ip_adress.setText(user_pre_info_list[1])
        
            user_pre_info_file.close()  #close file
            self.label_test_upload_variable.setText('true')

        #capture exceptions
        except IndexError:
            print('index error')
        except FileNotFoundError:
            print('file not found')


    def choose_upload_dir(self):   #def directory select function for upload dir (pyqt5 build-in function)
        upload_dir_path = QFileDialog().getExistingDirectory(self, 'Select an  directory')  #set up dialg field
        self.lineedit_upload_dir_path.setText(upload_dir_path)  #put upload dir path into according field after selection


    def upload(self, state):    #def function to upload files and create run_info.txt
        #def variables using inputs from the according GUI fields
        additional_info = self.input_additional_info.toPlainText()
        barcodekit = self.input_barcode_kit.text()
        barcode_button_value = self.label_upload.text()
        date = datetime.today().strftime('%Y-%m-%d-%H%M%S')
        exclude_fast5_files_status = self.exclude_fast5_files.isChecked()
        flowcell = self.input_flowcell_kit.currentText()
        ip = self.lineedit_ip_adress.text()
        password = self.password.text()
        path_on_server = self.lineedit_server_path.text()
        seq_kit = self.input_sequencing_kit.currentText()
        upload_dir_path = self.lineedit_upload_dir_path.text()
        username = self.lineedit_username.text()

        #set up message window to capture empty variables from above
        user_message_box = QMessageBox()
        user_message_box.setWindowTitle("user info")
        if username == "":
            user_message_box.setText("username is empty")
            x = user_message_box.exec_()
            return 13
        if ip == "":
            user_message_box.setText("ip-address is empty")
            x = user_message_box.exec_()
            return 14
        if password == "":
            user_message_box.setText("password is empty")
            x = user_message_box.exec_()
            return 15
        if path_on_server == "":
            user_message_box.setText("\"/path/on/server\" (directory on server) is empty")
            x = user_message_box.exec_()
            return 16
        if upload_dir_path == "":
            user_message_box.setText("\"/path/to/dir\" (upload directory) is empty")
            x = user_message_box.exec_()
            return 17

        #use individual dir name if user input exists
        if self.lineedit_dir_name.text():
            upload_dir_name = self.lineedit_dir_name.text()
            new_upload_dir_name = date + '_' + upload_dir_name
            print("if")
            print(new_upload_dir_name)
        else:
            upload_dir_name = os.path.basename(os.path.normpath(upload_dir_path))
            new_upload_dir_name = date + '_' + upload_dir_name
            print("else")
            print(new_upload_dir_name)

        #create run_info.txt
        run_info_file_path = os.path.join(upload_dir_path, "run_info.txt")    
        run_info_file = open(run_info_file_path, "w")

        #write general information to run_info.txt
        run_info_file.write(f'Automatically generated by norse (version: {version})\n')
        run_info_file.write(f'##Kit:\t{seq_kit}\n')
        run_info_file.write(f'##Barcodekit:\t{barcodekit}\n')
        run_info_file.write(f'##Flowcell:\t{flowcell}\n')
        run_info_file.write(f'##Run name:\t{new_upload_dir_name}\n')
        
        #write barcode-sampleIDs to run_info.txt
        run_info_file.write("Barcode\tSample-name\n")
        
        #no barcodes -> single sample
        if barcode_button_value == 'no':
            lineedit01 = self.lineedit1.text()
            run_info_file.write(f'Sample\t{lineedit01}')

        #barcodes 1-12 (active if "yes" or "24" selected)
        elif barcode_button_value in ['yes', '24']:
            #def variables getting sampleID from according barcode field in GUI
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
            
            #add all 12 variables to list
            barcode_sample_list = [lineedit01,lineedit02,lineedit03,lineedit04,lineedit05,lineedit06,lineedit07,lineedit08,
            lineedit09,lineedit10,lineedit11,lineedit12]

            #barcodes 13-24 (active if "24" selected)
            if barcode_button_value == '24':
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

                #extend list by additional sampleIDs for barcodes 13-24
                barcode_sample_list.extend([lineedit13,lineedit14,lineedit15,lineedit16,lineedit17,lineedit18,lineedit19,lineedit20,
                lineedit21,lineedit22,lineedit23,lineedit24])
            
            #write barcodes + sampleIDs to run_info.txt
            for index in range(len(barcode_sample_list)):
                if index < 9:
                    run_info_file.write(f'barcode0{str(index + 1)}\t{barcode_sample_list[index]}\n')
                else:
                    run_info_file.write(f'barcode{str(index + 1)}\t{barcode_sample_list[index]}\n')

        #up to 96 barcodes via user input-file
        elif barcode_button_value == "96":
            #check file type and read into panda dataframe
            if self.file_1 == "csv":
                barcode_sample_df = pd.read_csv(self.upload_sample_path, sep = ',', header=None)
            elif self.file_1 == "tsv":
                barcode_sample_df = pd.read_csv(self.upload_sample_path, sep = "\t", header=None)
            elif self.file_1 == "xlsx":
                barcode_sample_df = pd.read_excel(self.upload_sample_path, header=None)
            #could need here else confdition with exit if file-format is not matching one of the above???

            #read dataframe
            ROW = 0
            BARCODE_FILE_DF_LENGTH = len(barcode_sample_df)
            while True:
                if barcode_sample_df.iloc[ROW, 0] == "barcode":   #detect header
                    ROW = ROW + 1   #set begin to row after header
                    for ROWS in range(ROW, BARCODE_FILE_DF_LENGTH):  #loop over all rows following the header
                        if ROWS < 10:
                            run_info_file.write(f'barcode0{str(barcode_sample_df.iloc[ROWS, 0])}\t{str(barcode_sample_df.iloc[ROWS, 1])}\n')
                        else:
                            run_info_file.write(f'barcode{str(barcode_sample_df.iloc[ROWS, 0])}\t{str(barcode_sample_df.iloc[ROWS, 1])}\n')
                    break   #end while loop
                else:
                    ROW = ROW + 1   #increase ROW variable -> go to next row 
                    if ROW == BARCODE_FILE_DF_LENGTH:    #check if actual row is last row in file
                        ROW = 0
                        break   #add here a sys.exit to tell user he has to rename column???

        #write additional info to run_info.txt
        run_info_file.write(f'\n##Additional info\n{additional_info}\n')

        #close run_info.txt
        run_info_file.close()

        #check if rsync is avaible if yes then command (which rsync oder rsync -v)
        #os.system(f'rsync --rsync-path="/bin/rsync" -acr --remove-source-files "{upload_dir_path}" "~/Desktop/test_server/{new_upload_dir_name}"')
        #else scp

        port = 22
        cmd = 'which rsync'
        cmd2 = 'echo $?'

        #connect and upload to server -> if failure occurs error is printed. Connection is tested separately in func "test_upload"
        try:
            #set up messsage window (pop-up)
            message_box = QMessageBox()
            message_box.setWindowTitle("upload started")
            message_box.setText("Upload started, close this window")
            x = message_box.exec()
            msg = QMessageBox()
            msg.setWindowTitle("upload")

            ###deactivated rsync check for now due to server-sided permission issues related to this 
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
            exit_code = "1" #hardcoded this to always use the rsync option for the moment
            
            if exit_code == "0":
                if exclude_fast5_files_status == False:
                    EXCLUDE_FAST5 = ''
                else:
                    EXCLUDE_FAST5 = '--exclude "*.fast5" --exclude "*.pod5"'
                
                #os.system('scp -r ' + upload_dir_path + username + "@" +
                    #   ip + ":" + path_on_server + "/" + new_upload_dir_name)
                scp_exit_code = os.system(f'scp -r {upload_dir_path} {username}@{ip}:"{path_on_server}"/"{new_upload_dir_name}"')
                if scp_exit_code != 0:
                    msg.setText("upload failed")
                    x = msg.exec_()
                else:
                    msg.setText("upload complete")
                    x = msg.exec_()

            #rsync upload
            else:
                #def variable to insert flag depending on fast5 exclusion yes/no
                if exclude_fast5_files_status == False:
                    EXCLUDE_FAST5 = ''
                else:
                    EXCLUDE_FAST5 = '--exclude "*.fast5" --exclude "*.pod5"'
                
                rsync_exit_code = os.system(f'sshpass -p {password} rsync {EXCLUDE_FAST5} -acrv --remove-source-files "{upload_dir_path}" {username}@{ip}:"{path_on_server}"/"{new_upload_dir_name}"')
                
                #check exit code and display pop-up message according to result
                if rsync_exit_code != 0:
                    msg.setText("upload failed")
                    x = msg.exec_()
                else:
                    msg.setText("upload complete")
                    x = msg.exec_()                      
                    #sys.exit(0)

        #capture according errors
        except paramiko.AuthenticationException:
            print('connection error')
        except socket.timeout:
            print('connection error')
        

    def sequencing_kit_changed(self):   #def function to check input for seq-kit field in GUI
        #open file with all available seq-kit options and read line-wise into list
        with open('/norse/data/sequencing_kit_data.txt') as file:
            sequencing_kit_list = [line.rstrip() for line in file]

        #def variables
        sequencing_kit_input = self.input_sequencing_kit.currentText()
        kit = 0

        #check if field is not empty (str length > 0)
        if len(sequencing_kit_input) > 0:
            #compare input to seq-kit list entries and break if match
            for element in sequencing_kit_list:
                if element == sequencing_kit_input:
                    kit = 1
                    break

            #if input does not match seq-kit list entries inform user via pop-up message and reset input-field to first seq-kit list entry
            if kit == 0:
                msg = QMessageBox()
                msg.setWindowTitle("Sequencing-Kit input")
                msg.setText(f"Something is wrong with your input!\nResetting Box-value.")
                x = msg.exec_()  # this will show our messagebox
                msg.setIcon(QMessageBox.Critical)
                self.input_sequencing_kit.setEditText(f"{sequencing_kit_list[0]}")

    def barcode_kit_changed(self):  #def function to check input for barcode-kit field in GUI -> could add barcode-kit restriction analog to seq-kit/flowcell
        pass


    def flowcell_changed(self): #def function to check input for flowcell field in GUI (analog to "sequencing_kit_changed" function)
        with open('/norse/data/flowcell_data.txt') as file:
            flowcell_type_list = [line.rstrip() for line in file]

        flowcell_input = self.flowcell_edit.currentText()
        kit = 0

        if len(flowcell_input) > 0:
            for element in flowcell_type_list:
                if element == flowcell_input:
                    kit = 1
                    break
            
            if kit == 0:
                msg = QMessageBox()
                msg.setWindowTitle("Flowcell input")
                msg.setText(f"Something is wrong with your input!\nResetting Box-value.")
                x = msg.exec_()  # this will show our messagebox
                msg.setIcon(QMessageBox.Critical)
                self.flowcell_edit.setEditText(f"{flowcell_type_list[0]}")


    def test_upload(self):  #def function to test connection to server and add info to user_info.txt
        username = self.lineedit_username.text()
        ip = self.lineedit_ip_adress.text()
        password = self.password.text()
        path = self.lineedit_server_path.text()

        user_info = open(self.norse_user_info_path, "w+")   #open new file with write acess

        user_info.truncate(0)
        
        user_info.write(f'{username}\n{ip}\n{path}')
        user_info.close()

        try:
            port = 22

            cmd  = 'ls'
            cmd3 = 'ls -d ' + path 

            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(ip ,port ,username ,password, timeout=10)
            # stdin,stdout,stderr = ssh.exec_command(cmd)
            # time.sleep(5)
            # outlines = stdout.readlines()
            # resp = ''.join(outlines)

            stdin,stdout,stderr = ssh.exec_command(cmd3)
            time.sleep(5)
            outlines = stdout.readlines()
            resp3 = ''.join(outlines)

            #print(path in resp3)#string doesnt have to match exactly at moment
            if path in resp3:
                msg = QMessageBox()
                msg.setWindowTitle("test upload")
                msg.setText("Connected succesfully!")
                msg.setIcon(QMessageBox.Information)
                x = msg.exec_()  # this will show our messagebox
            else:
                msg1 = QMessageBox()
                msg1.setWindowTitle("test upload")
                msg1.setText(f"Path doesnt exist: Error {stderr}")
                msg1.setIcon(QMessageBox.Critical)
                x1 = msg1.exec_()  # this will show our messagebox
    
        except paramiko.AuthenticationException:
            msg2 = QMessageBox()
            msg2.setWindowTitle("test upload")
            msg2.setText("Wrong username or password")
            msg2.setIcon(QMessageBox.Information)
            x = msg2.exec_()  # this will show our messagebox
        except socket.error:
            msg3 = QMessageBox()
            msg3.setWindowTitle("test upload")
            msg3.setText('Wrong ip')
            msg3.setIcon(QMessageBox.Information)
            x = msg3.exec_()  # this will show our messagebox


    def radioclicked_no(self):  #button: no barcodes
        self.window2.hide_and_show(2,24,True)
        self.label_upload.setText('no')
        self.label_barcode_yes_no.setText('no')
        globs, locs = globals(), locals()
        [exec(f'self.{label_name}.setHidden(True)', globs,locs) for label_name in self.label_name_list_main[(0):24]]
        [exec(f'self.{input_name}.setHidden(True)', globs,locs) for input_name in self.input_name_list_main[(0):24]]

        self.label1.setHidden(False)
        self.lineedit1.setHidden(False)

        self.pushbutton_download_template.setHidden(True)
        self.pushbutton_download_template.setDisabled(True)
        self.upload_info.setHidden(True)
        self.upload_info.setDisabled(True)
        self.tableWidget.setHidden(True)
        self.textedit_csv.setHidden(True)
        self.textedit_csv_label.setHidden(True)
        self.tableWidget_label.setHidden(True)
   

    def radioclicked_yes(self): #button: 1-12 samples with barcodes

        self.window2.hide_and_show(1,12,False)
        self.window2.hide_and_show(13,24,True)
        self.label_upload.setText('yes')
        self.label_barcode_yes_no.setText('yes')
        
        globs, locs = globals(), locals()
        [exec(f'self.{label_name}.setHidden(False)', globs,locs) for label_name in self.label_name_list_main[(0):12]]
        [exec(f'self.{input_name}.setHidden(False)', globs,locs) for input_name in self.input_name_list_main[(0):12]]
        
        [exec(f'self.{label_name}.setHidden(True)', globs,locs) for label_name in self.label_name_list_main[(12):24]]
        [exec(f'self.{input_name}.setHidden(True)', globs,locs) for input_name in self.input_name_list_main[(12):24]]

        self.pushbutton_download_template.setHidden(True)
        self.pushbutton_download_template.setDisabled(True)
        self.upload_info.setHidden(True)
        self.upload_info.setDisabled(True)
        self.tableWidget.setHidden(True)
        self.textedit_csv_label.setHidden(True)
        self.textedit_csv.setHidden(True)
        self.tableWidget_label.setHidden(True)
    

    def radiobutton_24(self):   #button: 1-24 samples with barcodes
        self.label_upload.setText('24')

        globs, locs = globals(), locals()
        [exec(f'self.{label_name}.setHidden(False)', globs,locs) for label_name in self.label_name_list_main[(0):24]]
        [exec(f'self.{input_name}.setHidden(False)', globs,locs) for input_name in self.input_name_list_main[(0):24]]

        self.window2.hide_and_show(1,24,False)

        self.pushbutton_download_template.setHidden(True)
        self.pushbutton_download_template.setDisabled(True)
        self.upload_info.setHidden(True)
        self.upload_info.setDisabled(True)
        self.tableWidget.setHidden(True)
        self.textedit_csv.setHidden(True)
        self.textedit_csv_label.setHidden(True)
        self.tableWidget_label.setHidden(True)


    def radiobutton_96(self):   #button: up to 96 samples with barcodes

            self.label_upload.setText('96')
            self.pushbutton_download_template.setHidden(False)
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
    

    def passinInformation(self):    #all infos from mainwindow for window 2 to display there
        self.button_upload.setEnabled(True)
        self.window2.input_flowcell.setText(self.flowcell_edit.text())
        self.window2.input_kit.setText(self.input_sequencing_kit.text())
        self.window2.input_barcode.setText(self.input_barcode_kit.text())
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
     

    def password_hide_unhide(self,state):   #button to show/hide password
        if state == QtCore.Qt.Checked:
            self.password.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.password.setEchoMode(QtWidgets.QLineEdit.Password)
    

    def sample_upload(self):    #
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
        

    def info(self): #
        msg = QMessageBox()
        msg.setWindowTitle("data input")
        msg.setText("If you wanna use 96 samples, please create a csv (.csv) or excel (.xlsx) file as shown on the rigth side. Remember to write the headers (barcode, sampleid) not in caps.")
        x = msg.exec_()
        self.pushbutton_download_template.setDisabled(False)
