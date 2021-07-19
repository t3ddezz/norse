def sequencing_changed(self):

        url="https://raw.githubusercontent.com/t3ddezz/data/main/sequencing_data.txt"
        re=requests.get(url).content
        sequencing=pd.read_csv(io.StringIO(re.decode('utf-8')),sep='\t',index_col=False,header=None)

        kit_input = self.sequencing_edit.text()
        lange = len(sequencing)
        zahler = 0
        kit = 0

        for i in range(lange):
            if  kit_input == sequencing.loc[zahler,0]:
                kit = 1
                break
    
            else: 
                zahler = zahler + 1
        if kit == 0:
            msg = QMessageBox()
            msg.setWindowTitle("sequencing input")
            msg.setText("Something is wrong with your input!")
            x = msg.exec_()  # this will show our messagebox
            msg.setIcon(QMessageBox.Critical)
            self.sequencing_edit.clear()


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

        for i in range(lange):
            if  flow_input == flowcell.loc[zahler,0]:
                kit = 1
                break
    
            else: 
                zahler = zahler + 1
        if kit == 0:
            msg = QMessageBox()
            msg.setWindowTitle("flowcell input")
            msg.setText("Something is wrong with your input!")
            x = msg.exec_()  # this will show our messagebox
            msg.setIcon(QMessageBox.Critical)
            self.flowcell_edit.clear()