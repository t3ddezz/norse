def sample_upload(self):
        #download template, so its unique to read 
        try:
            global upload_sample_path
            upload_sample_path, _ = QFileDialog.getOpenFileName(self, 'Select sample sheet',"~", "data files(*.csv *.xlsx)")
            filename =  QFileInfo(upload_sample_path).fileName()
            global file_1
            file_1 = filename.split(".",1)[1]
            self.window2.open_sheet()
            
        except IndexError:
            print('no file selected')


def info(self):
        msg = QMessageBox()
        msg.setWindowTitle("data input")
        msg.setText("If you wanna use 96 samples, please create a csv(.csv) or excel(.xlsx) file with like shown on the rigth side. Remember to write the headers (barcode, sampleid) not in caps.")
        x = msg.exec_()
        self.download_template.setDisabled(False)