def iniUI(self):#

        self.tableView = QtWidgets.QTableWidget(self)
        self.tableView.setHidden(True)

        self.label_sample = QtWidgets.QLabel(self)
        self.label_sample.setText('sample name:')
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
        self.tableView.setHidden(True)


def unhide2(self):#unhide all labels from 1 to 12
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
        self.tableView.setHidden(True)


"""
def unhide(self):#show all labels from 1 to 24  
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
        self.tableView.setHidden(True)
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
        self.tableView.setHidden(True)
"""


def unhide(self, first_label_nr, last_label_nr, BOOLEAN):
       
        label_name_list = ["label" + str(item) for item in list(range(first_label_nr, (int(last_label_nr) + 1), 1))]
        for label_name in label_name_list:
            current_label = int(label_name_list[label_name])
            [self.current_label.setHidden(BOOLEAN)]
        self.tableView.setHidden(True)


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
        self.tableView.setHidden(True)


def sample_96(self):
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
        

def open_sheet(self):
        #file_1 = global variable with suffix from uploaded file
        #self.tableWidget.setItem(0,0, QtWidgets.QTableWidgetItem("barcode")
        column = 0
        if file_1 == 'csv':
            self.tableView.setRowCount(0)
            self.tableView.setColumnCount(2)
            my_file = pd.read_csv(upload_sample_path, sep=',',header=None)
            my_file_rows = len(my_file)
            my_file_columns = len(my_file.columns)
            self.tableView.setRowCount(my_file_rows)
            self.tableView.setColumnCount(my_file_columns)
            for rows in range(0, my_file_rows):
                barcode = my_file.loc[rows, 0]
                sample_id = my_file.loc[rows, 1]
                self.tableView.setItem(rows,column, QtWidgets.QTableWidgetItem(barcode))
                column = column + 1
                self.tableView.setItem(rows,column, QtWidgets.QTableWidgetItem(sample_id))
                column = 0
            

                


        column = 0
        if file_1 == 'xlsx':
            self.tableView.setRowCount(0)
            self.tableView.setColumnCount(2)
            my_file = pd.read_excel(upload_sample_path, header=None)
            my_file_rows = len(my_file)
            my_file_columns = len(my_file.columns)
            self.tableView.setRowCount(my_file_rows)
            self.tableView.setColumnCount(my_file_columns)
            for rows in range(0, my_file_rows):
                barcode = my_file.loc[rows, 0]
                sample_id = my_file.loc[rows, 1]
                self.tableView.setItem(rows,column, QtWidgets.QTableWidgetItem(str(barcode)))
                column = column + 1
                self.tableView.setItem(rows,column, QtWidgets.QTableWidgetItem(sample_id))
                column = 0
        self.tableView.move(15,100)
        self.tableView.setMaximumWidth(240)
        self.tableView.setMinimumWidth(240)
        self.tableView.setMaximumHeight(250)
        self.tableView.setMinimumHeight(250)
        self.tableView.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableView.setHidden(False)
        self.tableView.show                


def displayInfo(self):#shows window2
        self.show( )