def choose_dir(self):#pyqt5 build in directory select
        save_path = QFileDialog().getExistingDirectory(self, 'Select an  directory')

        self.lineedit_path_dir.setText(save_path)


def upload(self, state):#function to upload files and create run_info.txt
        print("upload startet")
        save_path = self.lineedit_path_dir.text()
        
        name_of_file = 'run_info' 
        

        completeName = os.path.join(save_path, name_of_file + ".txt")    

        date = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')
           
        #demo == run_info.txt
        demo = open(completeName, "w")

        kit = self.sequencing_edit.text()
        barcodekit = self.barcode_edit.text()
        flowcell = self.flowcell_edit.text()

        demo.write('##toolname version '+ version)
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
        
        
        ## build for run_info.txt
        if label_yes_no == 'no':
            lineedit01 = self.lineedit1.text()
            demo.write('NB01    ')
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
                    demo.write('    ')
                    demo.write(liste[i])
                    demo.write('\n')
                    a = a + 1       
        if label_yes_no == "96":
            #print(file_1)
            if file_1 == "csv":
                sample_csv = pd.read_csv(upload_sample_path, sep=',',header=None)
                #print(sample_csv)
            if file_1 == "xlsx":
                sample_excel = pd.read_excel(upload_sample_path, header=None)
                #print(sample_excel)


            #reading csv files
            if file_1  == "csv":
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
                            demo.write('    ')
                            demo.write(str(sample_csv.iloc[zeilen, 1]))#sample id
                            demo.write('\n')
                        else:
                            demo.write('NB')
                            demo.write(str(sample_csv.iloc[zeilen, 0]))#barcode number
                            demo.write('    ')
                            demo.write(str(sample_csv.iloc[zeilen, 1]))#sample id
                            demo.write('\n')
                

            #reading excel files (xlsx)
            if file_1 == "xlsx":
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
                            demo.write('    ')
                            demo.write(str(sample_excel.iloc[zeilen, 1]))#sample id
                            demo.write('\n')
                        else:
                            demo.write('NB')
                            demo.write(str(sample_excel.iloc[zeilen, 0]))#barcode number
                            demo.write('    ')
                            demo.write(str(sample_excel.iloc[zeilen, 1]))#sample id
                            demo.write('\n')

               

        

    
                    
        
        additional_info = self.textedit.toPlainText()
        
        demo.write('\n')
        demo.write('##additional info')
        demo.write('\n')
        demo.write(additional_info)

        demo.close()

        date = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')
        folder_name = os.path.basename(os.path.normpath(save_path))
        neuer_ordner_name = date + '_' + folder_name


        #check if rsync is avaible if yes then command (which rsync oder rsync -v)
        #os.system(f'rsync --rsync-path="/bin/rsync" -acr --remove-source-files "{save_path}" "~/Desktop/test_server/{neuer_ordner_name}"')
        #else scp

        path_on_server = self.lineedit_path.text()
        username = self.lineedit_username.text()
        ip = self.lineedit_ip_adress.text()
        password = self.password.text()
        

        port = 22
        cmd = 'which rsync'

        #connect to server, if fail error printed. But connection is tested in func test_upload
        try:
            
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(ip ,port ,username ,password, timeout=10)
            stdin,stdout,stderr = ssh.exec_command(cmd) 
            time.sleep(5)
            outlines = stdout.readlines()
            resp = ''.join(outlines)
            rsync_var = resp
            rsync_var = rsync_var.strip()

            if rsync_var =='rsync not found':
                os.system('scp -r ' + save_path + username + "@" +
                    ip + ":" + path_on_server + "/" + neuer_ordner_name)
                os.system(f"scp -r {save_path} {username}@{ip}:{path_on_server}/{neuer_ordner_name}")

            else:
                #os.system('rsync --rsync-path=' + rsync_var + "-acrv --remove-source-files " + 
                 #   save_path + " " + username + "@" + ip + ":" + path_on_server + "/" + neuer_ordner_name) {neuer_ordner_name}
                
                os.system(f"rsync --rsync-path={rsync_var} -acrv --remove-source-files {save_path} {username}@{ip}:{path_on_server}/{neuer_ordner_name}")
                print(" ")
                print("file upload complete")
                print(" ")
                
        except paramiko.AuthenticationException:
            print('connection error')
        except socket.timeout:
            print('connection error')
    

def test_upload(self):#test connection to server and add info to user_info.txt


    
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


def password_hide_unhide(self,state):#fucntion to hide password
        if state == QtCore.Qt.Checked:
            self.password.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.password.setEchoMode(QtWidgets.QLineEdit.Password)
    
