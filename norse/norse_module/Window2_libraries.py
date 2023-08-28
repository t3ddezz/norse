import sys
import sys ; sys.setrecursionlimit(sys.getrecursionlimit() * 5)
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog,  QFileDialog, QFrame, QMessageBox
from PyQt5.QtGui import QPalette, QColor, QIcon, QPixmap
from PyQt5.QtCore import Qt, QFileInfo
import pandas as pd
#from libraries.MainWindow_libraries import file_1, upload_sample_path

class Window2(QMainWindow):#class for window2 (pop up window)
    
    def __init__(self):
        super(Window2,self).__init__()
        self.setWindowTitle("check your data")
        self.setGeometry(400, 400, 330, 385)

        self.label_name_list = ["label" + str(item) for item in list(range(1, (24 + 1), 1))]
        self.input_name_list = ["input" + str(item) for item in list(range(1, (24 + 1), 1))]
        self.iniUI()
        
        
    def iniUI(self):
        globs, locs = globals(), locals()
        [exec(f"self.{label_name} = QtWidgets.QLabel(self)",globs, locs) for label_name in self.label_name_list]
        [exec(f"self.{input_name} = QtWidgets.QLabel(self)",globs, locs) for input_name in self.input_name_list]
        self.tableView = QtWidgets.QTableWidget(self)
        self.tableView.setHidden(True)

        x_y_values_for_label = []
        label_move_y_value = 70
        for i in range(1,25,1):
            if i < 10:
                x_value = 10
            elif 9 < i <= 12:
                x_value = 6
            elif i == 13:
                x_value = 180
                label_move_y_value = 70
            label_move_y_value += 20
            x_y_values_for_label.append([x_value,label_move_y_value])

        [exec(f"self.{self.label_name_list[index]}.move(*{x_y_values_for_label[index]})",globs, locs) for index in range(len(self.label_name_list))]
        [exec(f"self.{self.label_name_list[index]}.setText(str({index}+ 1))",globs, locs) for index in range(len(self.label_name_list))]

        x_y_values_for_input = []
        input_move_y_value = 70
        for i in range(1,25,1):
            if i <= 12:
                x_value = 20
            elif i == 13:
                x_value = 200
                input_move_y_value = 70
            input_move_y_value += 20
            x_y_values_for_input.append([x_value,input_move_y_value])
        
        [exec(f"self.{self.input_name_list[index]}.move(*{x_y_values_for_input[index]})",globs, locs) for index in range(len(self.input_name_list))]
        
        self.label_sample = QtWidgets.QLabel(self)
        self.label_sample.setText('sample name:')
        self.label_sample.move(20, 70)
        
        self.kitlabel = QtWidgets.QLabel(self)
        self.kitlabel.move(20, 10)
        self.kitlabel.setText('kit:')
        self.input_kit = QtWidgets.QLabel(self)
        self.input_kit.move(115, 10)

        self.barlabel = QtWidgets.QLabel(self)
        self.barlabel.move(20, 30)
        self.barlabel.setText('barcoding kit:')
        self.input_barcode = QtWidgets.QLabel(self)
        self.input_barcode.move(115, 30)
        
        self.barcodinglabel = QtWidgets.QLabel(self)
        self.barcodinglabel.move(20, 50)
        self.barcodinglabel.setText('flowcell:')
        self.input_flowcell = QtWidgets.QLabel(self)
        self.input_flowcell.move(115, 50)

        self.button = QtWidgets.QPushButton(self)
        self.button.setText('ok!')
        self.button.move(230, 355)
        self.button.clicked.connect(self.close)#close window2


    def hide_and_show(self,first_label_index, last_label_index, BOOLEAN):   #hide or show labels
        globs, locs = globals(), locals()
        #list comprehension build string (exec) using label_name an then execute the command
        [exec(f'self.{label_name}.setHidden({BOOLEAN})', globs,locs) for label_name in self.label_name_list[(first_label_index - 1):last_label_index]]
        self.tableView.setHidden(True)


    def open_sheet(self):
        #file_1 = global variable with suffix from uploaded file
        #self.tableWidget.setItem(0,0, QtWidgets.QTableWidgetItem("barcode")
        column = 0
        if self.file_1 == 'csv':
            self.tableView.setRowCount(0)
            self.tableView.setColumnCount(2)
            my_file = pd.read_csv(self.upload_sample_path, sep=',',header=None)
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
        if self.file_1 == 'xlsx':
            self.tableView.setRowCount(0)
            self.tableView.setColumnCount(2)
            my_file = pd.read_excel(self.upload_sample_path, header=None)
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


    def displayInfo(self):  #shows window2
        self.show( )