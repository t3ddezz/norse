from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog,  QFileDialog, QFrame, QMessageBox
from PyQt5.QtGui import QPalette, QColor, QIcon, QPixmap
from PyQt5.QtCore import Qt, QFileInfo
from  upload_data import password_hide_unhide
def iniUI(self):
        # 'self' is the first parameter of the methods of a class that refers to the instance of the same

        #self.window2 = Window2()   #for initiating window2
    


        self.logo_label = QtWidgets.QLabel(self)
        self.logo_label.setText('norse')
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
        self.checkbox_hide_unhide.stateChanged.connect(password_hide_unhide(self))
        self.checkbox_hide_unhide.move(370, 405)

        self.label_sonderzeichen = QtWidgets.QLabel(self)
        self.label_sonderzeichen.setText(':')
        self.label_sonderzeichen.adjustSize()
        self.label_sonderzeichen.move(250, 406)
        
        self.kitinfos_label = QtWidgets.QLabel(self)
        self.kitinfos_label.move(10, 50)
        self.kitinfos_label.setText('Ligation kit:')

        self.sequencing_edit = QtWidgets.QLineEdit(self)
        self.sequencing_edit.setPlaceholderText('e.g SQK-LSK109')
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

    
        self.label1 = QtWidgets.QLabel(self)# labels for lineedits for the samples
        self.label1.setText('1')
        self.label1.move(245, 20)
        self.lineedit1 = QtWidgets.QLineEdit(self)
        self.lineedit1.move(260,20)
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

        

        self.textedit_csv = QtWidgets.QTextEdit(self)#little edit field to add additional info
        self.textedit_csv.setPlaceholderText('barcode,sample_id             1,sample_1                           2,sample_2                          3,sample_3                          5,sample_5')
        self.textedit_csv.setGeometry(400, 238, 225, 150)
        self.textedit_csv.setHidden(True)
        self.textedit_csv_label = QtWidgets.QLabel(self)
        self.textedit_csv_label.setText("csv example:")
        self.textedit_csv_label.move(400, 215)
        self.textedit_csv_label.setHidden(True)
        self.textedit_csv_label.setFont(QtGui.QFont("arial", 15))
        



        # check if there is a user info.txt if not no abortion
        try:
            
            user_pre_info = open('user_info.txt','r')
            
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