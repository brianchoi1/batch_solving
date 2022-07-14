from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QMessageBox, QTableWidgetItem, QCheckBox, QPushButton, QFileDialog, QApplication, QTextEdit, QDialog, QLabel, QLineEdit, QGridLayout, QHeaderView, QProgressBar
import os, sys, paramiko, time, subprocess, threading


class Ui_MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ssh = paramiko.SSHClient()
        self.login_key = 0 
        self.ip = 'hpc.lge.com'
        self.default_fld = 'hpc_run_default'
        self.scr_fld = 'scratch'
        self.postfix_data = ''
        self.setupUi(MainWindow)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("HPC Run")
        MainWindow.setFixedSize(1117, 903)
        # MainWindow.resize(1117, 903)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(9, 603, 1101, 291))
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")

        self.txtedt = QtWidgets.QTextEdit(self.groupBox)
        self.txtedt.setObjectName("listView")
        self.horizontalLayout_5.addWidget(self.txtedt)

        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(9, 9, 1081, 206))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(10, 10, 100, 27))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setContentsMargins(1, 0, 1, 1)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.pushButton_2 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("New_Icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_3.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./Open_Icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_4.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./Save_Icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)

        self.groupBox1 = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox1.setGeometry(QtCore.QRect(10, 92, 1071, 55))
        self.groupBox1.setObjectName("groupBox1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox1)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)

        self.pushButton = QtWidgets.QPushButton(self.groupBox1)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)

        self.label_5 = QtWidgets.QLabel(self.groupBox1)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)

        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox1)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem('Moldflow')
        self.horizontalLayout_3.addWidget(self.comboBox_2)

        self.label_6 = QtWidgets.QLabel(self.groupBox1)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)

        self.comboBox_3 = QtWidgets.QComboBox(self.groupBox1)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem('8')
        self.comboBox_3.addItem('4')
        self.comboBox_3.addItem('16')
        self.comboBox_3.addItem('32')
        self.comboBox_3.addItem('64')
        self.horizontalLayout_3.addWidget(self.comboBox_3)

        self.label_7 = QtWidgets.QLabel(self.groupBox1)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)

        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox1)
        self.lineEdit_3.setObjectName("lineEdit_3")
        # self.lineEdit_3.setText('')
        self.horizontalLayout_3.addWidget(self.lineEdit_3)

        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox1)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_3.addWidget(self.pushButton_6)

        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setGeometry(QtCore.QRect(10, 43, 571, 43))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.frame_5)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)

        self.lineEdit = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.label_2 = QtWidgets.QLabel(self.frame_5)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.horizontalLayout_2.addWidget(self.lineEdit_2)

        self.label_3 = QtWidgets.QLabel(self.frame_5)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)

        self.comboBox = QtWidgets.QComboBox(self.frame_5)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem('평택')
        self.comboBox.addItem('창원')
        self.horizontalLayout_2.addWidget(self.comboBox)

        self.pushButton_5 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 153, 1071, 43))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_4.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_4.addWidget(self.pushButton_8)
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_4.addWidget(self.pushButton_9)
        self.pushButton_10 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_4.addWidget(self.pushButton_10)
        self.pushButton_11 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_11.setObjectName("pushButton_11")
        self.horizontalLayout_4.addWidget(self.pushButton_11)
        self.pushButton_12 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_12.setObjectName("pushButton_12")
        self.horizontalLayout_4.addWidget(self.pushButton_12)
        self.pushButton_13 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_13.setObjectName("pushButton_13")
        self.horizontalLayout_4.addWidget(self.pushButton_13)

        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(9, 226, 1101, 371))
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout.setObjectName("verticalLayout")

        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_4)
        self.tableWidget.setRowCount(15)
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setObjectName("tableWidget")
        table_column=['' , 'ID' , '                      Filename                      ', 'NCPU', '                                Run Command                                ', '', 'Status', 'Scratch', '']
        self.tableWidget.setHorizontalHeaderLabels(table_column)  

        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(5, QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(6, QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(7, QHeaderView.ResizeToContents)
        self.verticalLayout.addWidget(self.tableWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.tableWidget.setColumnWidth(0, 10)
        self.tableWidget.setColumnWidth(8, 1)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton_2.clicked.connect(self.__init__)
        self.pushButton_3.clicked.connect(self.pjt_open_Clicked)
        self.pushButton.clicked.connect(self.inp_open_Clicked)
        self.pushButton_5.clicked.connect(self.login_act)
        self.pushButton_6.clicked.connect(self.postfix)
        self.pushButton_7.clicked.connect(self.upload_func)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox1.setTitle(_translate("MainWindow", "Input files setup"))
        self.label_4.setText(_translate("MainWindow", "Input Files"))
        self.pushButton.setText(_translate("MainWindow", "Open"))
        self.label_5.setText(_translate("MainWindow", "Solver"))
        self.label_6.setText(_translate("MainWindow", "NCPU"))
        self.label_7.setText(_translate("MainWindow", "POSTFIX"))
        self.pushButton_6.setText(_translate("MainWindow", "APPLY"))
        self.label.setText(_translate("MainWindow", "HPC ID"))
        self.label_2.setText(_translate("MainWindow", "PW"))
        self.label_3.setText(_translate("MainWindow", "Server"))
        self.pushButton_5.setText(_translate("MainWindow", "Login"))
        self.pushButton_7.setText(_translate("MainWindow", "UP/Solving"))
        self.pushButton_8.setText(_translate("MainWindow", "Bkill"))
        self.pushButton_9.setText(_translate("MainWindow", "Bjobs all"))
        self.pushButton_10.setText(_translate("MainWindow", "Refresh"))
        self.pushButton_11.setText(_translate("MainWindow", "Download"))
        self.pushButton_12.setText(_translate("MainWindow", "Folder Open"))
        self.pushButton_13.setText(_translate("MainWindow", "Remove"))

    def postfix(self):
        self.postfix_data = self.lineEdit_3.text()

    def login_act(self):
        self.id = self.lineEdit.text()
        self.pw = self.lineEdit_2.text()
        self.login_key = self.login_check()
        if self.login_key == 1:
            self.success_event()
            self.close()
            self.check_string()
        else:
            self.fail_event()

    def check_string(self):
        with open('user_list_AC.txt') as temp_f:
            datafile = temp_f.readlines()
        for line in datafile:
            if self.id in line:
                self.hpc_path_default = '/nas/users/AC'
            else:
                self.hpc_path_default = '/nas/users/HA'

    def success_event(self): 
        QMessageBox.about(self,'ID available','Login comfirmed')

    def fail_event(self): 
        QMessageBox.about(self,'ID or PW wrong','Login failed')

    def login_check(self):
        if str(self.comboBox.currentText()) == '평택':
            self.ip = 'hpc.lge.com'
        else:
            self.ip = 'cwhpc.lge.com'
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
        try:
            self.ssh.connect(self.ip, 22, self.id, self.pw)
            login_key = 1
            self.ssh.close()
            return login_key
        except:
            login_key = 0
            self.ssh.close()
            return login_key

    def pjt_open_Clicked(self):
        try:
            fname = QFileDialog.getOpenFileNames(self, filter='*.sdy')
            fname = fname[0]                                    # QFileDialog >> Tuple로 받아들여서 >> List로 변환
            self.fname_list0 = []
            self.fname_list = []
            self.c_dir = []
            self.c_dir.append(os.path.dirname(fname[0]))
            self.c_fld = []
            self.c_fld.append(str(self.c_dir[0]).split('/')[-1])
            for fname_item in fname:                            # 다중파일 선택 시 차례대로 파일이름추출
                self.fname_list.append(os.path.basename(fname_item))
            charac1 = '('
            charac2 = ')'
            charac = '()'
            ii = 0
            for fname_item in self.fname_list:
                if charac1 in fname_item or charac2 in fname_item:
                    oldpath = self.c_dir[0] + '/' + fname_item
                    for x in range(len(charac)):                        
                        fname_item = fname_item.replace(charac[x], "")
                    newpath = self.c_dir[0] + '/' + fname_item
                    os.rename(oldpath, newpath)
                    self.fname_list[ii] = fname_item
                self.txtedt.append(fname_item + '   is selected')
                ii += 1
            self.fselect = 1
            self.txtedt.verticalScrollBar().setValue(20000)
            return self.c_dir, self.c_fld, self.fname_list, self.fselect
        except:
            self.fselect = 0
            self.fname_list = []
            self.c_dir = []
            self.c_fld = []
            return self.c_dir, self.c_fld, self.fname_list, self.fselect

    def inp_open_Clicked(self):
        try:
            fname = QFileDialog.getOpenFileNames(self, filter='*.sdy')
            fname = fname[0]                                    # QFileDialog >> Tuple로 받아들여서 >> List로 변환
            self.fname_list = []
            self.c_dir = []
            self.c_dir.append(os.path.dirname(fname[0]))
            self.c_fld = []
            self.c_fld.append(str(self.c_dir[0]).split('/')[-1])
            self.group_table_list = []
            for fname_item in fname:                            # 다중파일 선택 시 차례대로 파일이름추출
                self.fname_list.append(os.path.basename(fname_item))
            charac1 = '('
            charac2 = ')'
            charac = '()'
            ii = 0
            for fname_item in self.fname_list:
                if charac1 in fname_item or charac2 in fname_item:
                    oldpath = self.c_dir[0] + '/' + fname_item
                    for x in range(len(charac)):                        
                        fname_item = fname_item.replace(charac[x], "")
                    newpath = self.c_dir[0] + '/' + fname_item
                    os.rename(oldpath, newpath)
                    self.fname_list[ii] = fname_item
                ii += 1
            for index, (path1, path2) in enumerate(zip(self.fname_list, fname)):
                id = index + 1
                globals()["table_list_{}".format(id)] = {"id" : id, "filename" : path1, "filepath" : path2, "ncpu" : 8, "postfix" : '', "run_cmd" : 'lsdyna ncpu=8 i=' + path1, "include_file" : '', "include_file_path" : '', "solve_key" : 0, "running_key" : 0, "error_key" : 0, "bkill_key" : 0, "status" : '', "status_progress" : 0, "scratch" : 1}
                self.group_table_list.append("table_list_{}".format(id))
            self.file_distributor()
            return self.c_dir, self.c_fld, self.fname_list
        except:
            self.fname_list = []
            self.c_dir = []
            self.c_fld = []
            return self.c_dir, self.c_fld, self.fname_list

    def file_distributor(self):
        if len(self.fname_list) > 15:
            self.tableWidget.setRowCount(len(self.fname_list))
        for table_list in self.group_table_list:
            table_list = globals()[table_list]
            item = QTableWidgetItem(str(table_list['id']))
            item.setTextAlignment(Qt.AlignVCenter | Qt.AlignCenter)
            self.tableWidget.setItem(table_list['id']-1, 1, item)
            self.tableWidget.setItem(table_list['id']-1, 2, QTableWidgetItem(str(table_list['filename'])))
            self.tableWidget.setItem(table_list['id']-1, 3, QTableWidgetItem(str(table_list['ncpu'])))
            self.tableWidget.setItem(table_list['id']-1, 4, QTableWidgetItem(str(table_list['run_cmd'])))

            progressbar = self.progress_bar(table_list)
            chkbox = self.chkbox(table_list)
            scratch_ckkbox = self.scratch_chkbox(table_list)
            pshbtn = self.pshbtn(table_list)
            include_btn = self.include_btn(table_list)

    def progress_bar(self, table_list):
        pbar = QProgressBar(self.tableWidget)
        pbar.setValue(table_list['status_progress'])    
        pbar.setAlignment(Qt.AlignCenter)
        self.tableWidget.setCellWidget(table_list['id']-1, 6, pbar)

    def chkbox(self, table_list):
        ckbox = QCheckBox(self.tableWidget)
        ckbox.setCheckState(Qt.Checked)
        self.tableWidget.setCellWidget(table_list['id']-1, 0, ckbox)

    def scratch_chkbox(self, table_list):
        ckbox = QCheckBox(self.tableWidget)
        ckbox.setCheckState(Qt.Checked)
        self.tableWidget.setCellWidget(table_list['id']-1, 7, ckbox)
    
    def pshbtn(self, table_list):
        btn1 = QPushButton("X", self.tableWidget)
        self.tableWidget.setCellWidget(table_list['id']-1, 8, btn1)
        btn1.clicked.connect(self.remove_row)

    def remove_row(self):
        button = self.sender()
        item = self.tableWidget.indexAt(button.pos())   
        dd = item.row()  
        self.tableWidget.removeRow(dd)

    def include_btn(self, table_list):
        btn1 = QPushButton("include", self.tableWidget)
        self.tableWidget.setCellWidget(table_list['id']-1, 5, btn1)
        btn1.clicked.connect(self.include_Clicked)

    def upload_func(self):
        if self.login_key == 1:
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
            self.ssh.connect(self.ip, 22, self.id, self.pw)
            for table_list in self.group_table_list:
                table_list = globals()[table_list]
                input_fld = str(table_list['filename']).split('.')[0]
                if table_list['scratch'] == 1:
                    self.ssh.exec_command('mkdir -p ' + self.hpc_path_default + '/' + self.id + '/' + self.scr_fld + '/' + self.default_fld + '/' + input_fld)
                else:
                    self.ssh.exec_command('mkdir -p ' + self.hpc_path_default + '/' + self.id + '/' + self.default_fld + '/' + input_fld)
                filepath_str = str(table_list['filepath'])
                d = filepath_str.split('/')
                d.pop()
                filepath = '\\'.join(d)
                if table_list['scratch'] == 1:
                    t = open('upload_cmd', 'w', encoding='utf-8')
                    t.write('cd scratch/' + self.default_fld + '/' + input_fld + '\nlcd ' + filepath + '\nput ' + str(table_list['filepath']) + '\n')
                    t.close()
                    th = threading.Thread(target=self.run)
                    th.start()
                    time.sleep(5)
                    thr = threading.Thread(target=self.upload_check, args=(('cd scratch/' + self.default_fld + '/' + input_fld), str(table_list['filepath']), str(table_list['filename']), str(table_list['ncpu'])))
                    thr.start()
                else:
                    t = open('upload_cmd', 'w', encoding='utf-8')
                    t.write('cd ' + self.default_fld + '/' + input_fld + '\nlcd ' + filepath + '\nput ' + str(table_list['filepath']) + '\n')
                    t.close()
                    th = threading.Thread(target=self.run)
                    th.start()
                    time.sleep(5)
                    thr = threading.Thread(target=self.upload_check, args=(('cd ' + self.default_fld + '/' + input_fld), str(table_list['filepath']), str(table_list['filename']), str(table_list['ncpu'])))
                    thr.start()
                # self.run()
                # self.ssh.close()
 
        else:
            print('dd')

        print('ff')

    def run(self):
            cmd = "psftp.exe"
            p = subprocess.Popen([cmd, self.ip, '-l', self.id, '-pw', self.pw, '-b', 'upload_cmd'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True) 
            print('dd')

    def upload_check(self, hpc_path, filepath, fname, ncpu):
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
        self.ssh.connect(self.ip, 22, self.id, self.pw)
        i = 1
        while i > 0:
            stdin, stdout, stderr = self.ssh.exec_command(hpc_path + ';ls -l')
            dd = stdout.readlines()
            # self.ssh.close()
            try:
                for i, rr in enumerate(dd):
                    if fname in rr:
                        # print(i)
                        item = int(rr.split()[4])

                file_size = os.path.getsize(r"{}".format(filepath)) 
                # print('File Size:', file_size, 'bytes')
                ratio = item / file_size
                print("%.2f%%" % (ratio * 100))
                if ratio == 1:
                    i -= 1
                    stdin, stdout, stderr = self.ssh.exec_command(' cd ' + hpc_path + '; . /etc/profile;. ~/.bash_profile;. ~/.bashrc; lsdyna i=' + fname + ' ncpu=' + ncpu + ' ' + self.postfix_data)
                time.sleep(10)
            except:
                time.sleep(10)
                continue

    def include_Clicked(self):
        try:
            fname = QFileDialog.getOpenFileNames(self, filter='*.sdy')
            fname = fname[0]                                    # QFileDialog >> Tuple로 받아들여서 >> List로 변환
            self.fname_list0 = []
            self.fname_list = []
            self.c_dir = []
            self.c_dir.append(os.path.dirname(fname[0]))
            self.c_fld = []
            self.c_fld.append(str(self.c_dir[0]).split('/')[-1])
            for fname_item in fname:                            # 다중파일 선택 시 차례대로 파일이름추출
                self.fname_list.append(os.path.basename(fname_item))
            charac1 = '('
            charac2 = ')'
            charac = '()'
            ii = 0
            for fname_item in self.fname_list:
                if charac1 in fname_item or charac2 in fname_item:
                    oldpath = self.c_dir[0] + '/' + fname_item
                    for x in range(len(charac)):                        
                        fname_item = fname_item.replace(charac[x], "")
                    newpath = self.c_dir[0] + '/' + fname_item
                    os.rename(oldpath, newpath)
                    self.fname_list[ii] = fname_item
                self.txtedt.append(fname_item + '   is selected')
                ii += 1
            self.fselect = 1
            self.txtedt.verticalScrollBar().setValue(20000)
            return self.c_dir, self.c_fld, self.fname_list, self.fselect
        except:
            self.fselect = 0
            self.fname_list = []
            self.c_dir = []
            self.c_fld = []
            return self.c_dir, self.c_fld, self.fname_list, self.fselect

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    # ui = Ui_MainWindow()
    # ui.show()
    sys.exit(app.exec_())
