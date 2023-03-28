from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import cv2
from pathlib import Path
import os
import datetime
import csv
from csv import *
import os
import shutil
#import pandas as pd
#import numpy

class MainWindow(object):     
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(985, 560)
        MainWindow.setMouseTracking(False)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setStyleSheet("")
        self.m_central_widget = QtWidgets.QWidget(MainWindow)
        self.m_central_widget.setStyleSheet("")
        self.m_central_widget.setObjectName("centralwidget")
        self.m_scroll_area = QtWidgets.QScrollArea(self.m_central_widget)
        self.m_scroll_area.setGeometry(QtCore.QRect(0, 0, 991, 711))
        self.m_scroll_area.setWidgetResizable(True)
        self.m_scroll_area.setObjectName("scroll_area")
        self.m_scroll_area_widget_contents = QtWidgets.QWidget()
        self.m_scroll_area_widget_contents.setGeometry(QtCore.QRect(0, 0, 989, 709))
        self.m_scroll_area_widget_contents.setObjectName("scroll_area_widget_contents")

#############################################################################################################
# label

        self.m_logo_autaza = QtWidgets.QLabel(self.m_scroll_area_widget_contents)
        self.m_logo_autaza.setGeometry(QtCore.QRect(0, 0, 1001, 561))
        self.m_logo_autaza.setStyleSheet("image: url(:/img/images/Autaza.png);")
        self.m_logo_autaza.setText("")
        self.m_logo_autaza.setObjectName("label")
        
        self.m_choose_mode = QtWidgets.QLabel(self.m_scroll_area_widget_contents)
        self.m_choose_mode.setGeometry(QtCore.QRect(20, 0, 241, 41))
        self.m_choose_mode.setStyleSheet("\n"
"font: 75 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(3, 3, 156);")
        self.m_choose_mode.setObjectName("choose_mode")
        
        self.m_scroll_area2 = QtWidgets.QScrollArea(self.m_scroll_area_widget_contents)
        self.m_scroll_area2.setGeometry(QtCore.QRect(120, 100, 378, 381))
        self.m_scroll_area2.setStyleSheet("background:transparent;")
        self.m_scroll_area2.setWidgetResizable(True)
        self.m_scroll_area2.setObjectName("scroll_area2")
        self.m_scroll_area_widget_contents2 = QtWidgets.QWidget()
        self.m_scroll_area_widget_contents2.setGeometry(QtCore.QRect(0, 0, 379, 379))
        self.m_scroll_area_widget_contents2.setObjectName("scroll_area_widget_contents2")
        self.m_grid_layout = QtWidgets.QGridLayout(self.m_scroll_area_widget_contents2)
        self.m_grid_layout.setObjectName("gridLayout")
        self.m_print_image = QtWidgets.QLabel(self.m_scroll_area_widget_contents2)
        self.m_print_image.setText("")
        self.m_print_image.setAlignment(QtCore.Qt.AlignCenter)
        self.m_print_image.setObjectName("print_image")
        self.m_grid_layout.addWidget(self.m_print_image, 0, 0, 1, 1)
        self.m_scroll_area2.setWidget(self.m_scroll_area_widget_contents2)
        self.m_scroll_area.setWidget(self.m_scroll_area_widget_contents)
        
#############################################################################################################
# checkBox

        self.m_check_on = QtWidgets.QCheckBox(self.m_scroll_area_widget_contents)
        self.m_check_on.setGeometry(QtCore.QRect(40, 50, 61, 21))
        self.m_check_on.setStyleSheet("color: rgb(11, 11, 11);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.m_check_on.setCheckable(False)
        self.m_check_on.clicked.connect(self.disableMessage)
        self.m_check_on.setObjectName("checkBox")
        
        self.m_check_off = QtWidgets.QCheckBox(self.m_scroll_area_widget_contents)
        self.m_check_off.setGeometry(QtCore.QRect(130, 50, 81, 21))
        self.m_check_off.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.m_check_off.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);")
        self.m_check_off.setCheckable(True)
        self.m_check_off.setChecked(True)
        self.m_check_off.setAutoRepeat(True)
        self.m_check_off.setTristate(False)
        self.m_check_off.setObjectName("check_off")
        self.m_check_off.setDisabled(True)

############################################################################################################# 
# pushButton

        self.m_index = -1
        self.m_counter = -1
        self.m_exist = 0

        self.m_btn_single_image = QtWidgets.QPushButton(self.m_scroll_area_widget_contents)
        self.m_btn_single_image.setGeometry(QtCore.QRect(10, 500, 421, 41))
        self.m_btn_single_image.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.m_btn_single_image.setObjectName("pushButton")
        self.m_btn_single_image.clicked.connect(self.openImage)
        
        self.m_btn_multiple_image = QtWidgets.QPushButton(self.m_scroll_area_widget_contents)
        self.m_btn_multiple_image.setGeometry(QtCore.QRect(440, 500, 431, 41))
        self.m_btn_multiple_image.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.m_btn_multiple_image.setObjectName("pushButton_2")
        self.m_btn_multiple_image.clicked.connect(self.openImages)
        
        self.m_btn_manual = QtWidgets.QPushButton(self.m_scroll_area_widget_contents)
        self.m_btn_manual.setGeometry(QtCore.QRect(860, 10, 111, 28))
        self.m_btn_manual.setObjectName("pushButton_3")
        self.m_btn_manual.clicked.connect(self.openManual)
        
        self.m_btn_change_log = QtWidgets.QPushButton(self.m_scroll_area_widget_contents)
        self.m_btn_change_log.setGeometry(QtCore.QRect(860, 40, 111, 28))
        self.m_btn_change_log.setObjectName("pushButton_4")
        self.m_btn_change_log.clicked.connect(self.openChangelog)
        
        self.m_btn_log = QtWidgets.QPushButton(self.m_scroll_area_widget_contents)
        self.m_btn_log.setGeometry(QtCore.QRect(860, 70, 111, 28))
        self.m_btn_log.setObjectName("pushButton_5")
        
        self.m_btn_play = QtWidgets.QPushButton(self.m_scroll_area_widget_contents)
        self.m_btn_play.setGeometry(QtCore.QRect(890, 490, 61, 61))
        self.m_btn_play.setStyleSheet("border-image: url(:/img/images/btn.png);")
        self.m_btn_play.setText("")
        self.m_btn_play.setObjectName("pushButton_6")
        self.m_file_names = []
        self.m_btn_play.clicked.connect(self.playButton)
        
        self.m_left_arrow = QtWidgets.QPushButton(self.m_scroll_area_widget_contents)
        self.m_left_arrow.setGeometry(QtCore.QRect(720, 340, 51, 28))
        self.m_left_arrow.setObjectName("m_left_arrow")
        self.m_left_arrow.clicked.connect(self.backImage)
        
        self.m_right_arrow = QtWidgets.QPushButton(self.m_scroll_area_widget_contents)
        self.m_right_arrow.setGeometry(QtCore.QRect(780, 340, 51, 28))
        self.m_right_arrow.setObjectName("m_right_arrow")
        self.m_right_arrow.clicked.connect(self.fowardImage)
        
        self.m_reset = QtWidgets.QPushButton(self.m_scroll_area_widget_contents)
        self.m_reset.setGeometry(QtCore.QRect(720, 380, 111, 28))
        self.m_reset.setObjectName("Reset")
        self.m_reset.clicked.connect(self.resetProgram)
        
        self.m_scroll_area.setWidget(self.m_scroll_area_widget_contents)
        MainWindow.setCentralWidget(self.m_central_widget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
#############################################################################################################
# Funções
        
    def imageProcess(self):
        self.m_coord.append(f'Image{self.m_img}')
        
        self.m_pixmap_2 = cv2.cvtColor(self.m_pixmap, cv2.COLOR_BGR2GRAY)
        self.m_pixmap_2 = cv2.GaussianBlur(self.m_pixmap_2, (5,5), 0.8)
        self.m_pixmap_2 = cv2.Canny(self.m_pixmap_2, 100, 40) 
        #kernel = np.ones((2,2), np.uint8) 
        #self.m_pixmap_2 = cv2.erode(self.m_pixmap_2, kernel, iterations = 1)
        #self.m_pixmap_2 = cv2.dilate(self.m_pixmap_2, kernel, iterations = 1)
  
        self.m_file_path_new2 = Path.home().joinpath('Application/New Images', 'neweffect.bmp')
        self.m_file_path_new2 = str(self.m_file_path_new2)
        cv2.imwrite(self.m_file_path_new2, self.m_pixmap_2)

        _, _, boxes, _ = cv2.connectedComponentsWithStats(self.m_pixmap_2)
        boxes = boxes[1:]
        filtered_boxes = []
        for x,y,w,h,pixels in boxes:
                if pixels < 10000 and h < 12 and w < 12 and h > 2 and w > 2:
                        filtered_boxes.append((x,y,w,h))
        for x,y,w,h in filtered_boxes:
                cv2.rectangle(self.m_pixmap, (x-10,y-10), (x+w+10,y+h+10), (6,255,220), 2)
                self.m_coord.append(f'({x}, {y})')
        with open(self.m_file_path_csv, 'w', newline='') as file:
                writer = csv.writer(file, delimiter='\t') # O "\t" significa que não haverá delimitador.
                defect = 1
                string = ['Image1']
                image = 1
                self.m_coord.append('')
                for i in self.m_coord:
                        if i != '' and i.isalnum() is False:
                                string.append(f'Defect {defect}: {i}')
                                defect += 1
                        elif i == '':                                
                                writer = csv.writer(file, delimiter=';')
                                writer.writerow(string)
                                string = []
                                defect = 1
                                image += 1
                                string.append(f'Image{image}')
        file.close()
        self.m_img += 1
        #pd.read_csv(self.m_file_path_csv, header=None).T.to_csv(self.m_file_path_csv, header=False, index=False)
        cv2.imwrite(self.m_file_path_new, self.m_pixmap)
                
    def disableMessage(self, message):
        button = QMessageBox.critical(self, "Disabled", "The mode 'On' has not been implemented yet.")

    def pathCreation(self):
        self.date_time = datetime.datetime.now()
        self.date_time = self.date_time.strftime("%x") # Função "strtime("%x")"" pega somente a data no formato "mm/dd/yyyy"
        self.date_time = self.date_time.replace('/', '-') # O formato é transformado de "mm/dd/yyyy" para "mm-dd-yyyy"
        if self.m_index != -1:
                self.m_file_path_original = Path.home().joinpath('Application/Original Images', f'{self.date_time}_{self.m_index_iteration+1}.bmp')
                self.m_file_path_original = str(self.m_file_path_original)
                self.m_file_path_new = Path.home().joinpath('Application/New Images', f'{self.date_time}_{self.m_index_iteration+1}.bmp')
                self.m_file_path_new = str(self.m_file_path_new)
        else:
                self.m_file_path_original = Path.home().joinpath('Application/Original Images', f'{self.date_time}.bmp')
                self.m_file_path_original = str(self.m_file_path_original)
                self.m_file_path_new = Path.home().joinpath('Application/New Images', f'{self.date_time}.bmp')
                self.m_file_path_new = str(self.m_file_path_new)


    def playButton(self):
        if self.m_exist == 0:
                return
        if self.m_index == -1:
                self.singleProcess()
                self.m_pixmap = QPixmap(self.m_file_path_new)
                self.m_pixmap = self.m_pixmap.scaled(329, 329)
                self.m_print_image.setPixmap(self.m_pixmap)
        else:
                self.multipleProcess()
                self.m_pixmap = QPixmap(self.m_file_names[self.m_counter])
                self.m_pixmap = self.m_pixmap.scaled(329, 329)
                self.m_print_image.setPixmap(self.m_pixmap)

    def singleProcess(self):
        if self.m_exist == 1:
                self.pathCreation()
                self.m_pixmap = cv2.imread(self.m_filename[0])
                self.m_pixmap = cv2.resize(self.m_pixmap, (2000, 2000))  
                cv2.imwrite(self.m_file_path_original, self.m_pixmap)
                self.imageProcess()
                self.m_exist = 0
        
    def multipleProcess(self):
        self.m_index_iteration = self.m_index
        while self.m_index_iteration > -1:
                self.pathCreation()
                self.m_pixmap = cv2.imread(self.m_file_names[self.m_index_iteration])
                self.m_pixmap = cv2.resize(self.m_pixmap, (2000, 2000))  
                cv2.imwrite(self.m_file_path_original, self.m_pixmap)
                self.imageProcess()
                self.m_file_names[self.m_index_iteration] = self.m_file_path_new
                self.m_index_iteration -= 1
        self.m_exist = 0
        
    def openImage(self):
        self.m_index = -1
        self.m_counter = -1
        self.m_filename = QFileDialog.getOpenFileName(self, "Open File", "c:/", ".tiff Files (*.tiff);;.bmp Files (*.bmp)")
        if self.m_filename[0] != '':
                self.m_pixmap = QPixmap(self.m_filename[0])
                self.m_pixmap = self.m_pixmap.scaled(329, 329)
                self.m_print_image.setPixmap(self.m_pixmap)
                self.m_exist = 1    

    def openImages(self):
        tuple = QFileDialog.getOpenFileNames(self, "Open File", "c:/", ".tiff Files (*.tiff);;.bmp Files (*.bmp)")
        file_names = tuple[0]
        for i in file_names:
                if file_names != '':
                        self.m_file_names.append(i)
                        self.m_index += 1
                        self.m_counter = self.m_index
                        self.m_exist = 1
                self.m_pixmap = QPixmap(self.m_file_names[self.m_index])
                self.m_pixmap = self.m_pixmap.scaled(329, 329)
                self.m_print_image.setPixmap(self.m_pixmap)
        
    def backImage(self):
        if self.m_counter >= 1:
                self.m_counter -= 1
                self.m_pixmap = QPixmap(self.m_file_names[self.m_counter])
                self.m_pixmap = self.m_pixmap.scaled(329, 329)
                self.m_print_image.setPixmap(self.m_pixmap)
                
    def fowardImage(self):
        if self.m_counter != self.m_index:
                self.m_counter += 1
                self.m_pixmap = QPixmap(self.m_file_names[self.m_counter])
                self.m_pixmap = self.m_pixmap.scaled(329, 329)
                self.m_print_image.setPixmap(self.m_pixmap)

    def resetProgram(self):
        self.m_index = -1
        self.m_counter = -1
        self.m_file_names = []
        self.m_pixmap = ''
        self.m_pixmap_2 = ''
        self.m_exist = 0
        self.m_print_image.clear()
        self.m_coord = []
        
    def createDir(self):
        self.m_file_path_original = Path.home().joinpath('Application')
        if not os.path.exists(self.m_file_path_original):
                os.mkdir(self.m_file_path_original)
        self.m_path_changelog = Path.home().joinpath('Application/changelog.pdf')
        self.m_changelog = 'changelog.pdf'
        if not os.path.exists(self.m_path_changelog):
                shutil.copyfile(self.m_changelog, self.m_path_changelog)
        self.m_path_manual = Path.home().joinpath('Application/Manual.pdf')
        self.m_manual = 'Manual.pdf'
        if not os.path.exists(self.m_path_manual):
                shutil.copyfile(self.m_manual, self.m_path_manual)
        self.m_file_path_original = Path.home().joinpath('Application/Original Images')
        if not os.path.exists(self.m_file_path_original):
                os.mkdir(self.m_file_path_original)
        self.m_file_path_new = Path.home().joinpath('Application/New Images')
        if not os.path.exists(self.m_file_path_new):
                os.mkdir(self.m_file_path_new)
        self.m_coord = []
        self.m_img = 1
        c = 0
        self.m_file_path_csv = Path.home().joinpath(f'Application/Defects{c}.csv')
        while os.path.exists(self.m_file_path_csv) is True:
                self.m_file_path_csv = Path.home().joinpath(f'Application/Defects{c}.csv')
                if not os.path.exists(self.m_file_path_csv):
                        with open(self.m_file_path_csv, 'w', newline='') as file:
                                writer = csv.writer(file, delimiter='\t') # O "\t" significa que não haverá delimitador.                            
                                writer.writerow("")
                        file.close()
                        return
                c += 1
                
    def openChangelog(self):
        self.m_path_changelog = str(self.m_path_changelog)
        os.system(self.m_path_changelog)
        
    def openManual(self):
        self.m_path_manual = str(self.m_path_manual)
        os.system(self.m_path_manual)
                        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Autaza Capture System v1.0.0"))
        
        self.m_choose_mode.setText(_translate("MainWindow", "Choose your mode"))
        
        self.m_check_on.setText(_translate("MainWindow", "On"))
        self.m_check_off.setText(_translate("MainWindow", "Off"))

        self.m_btn_single_image.setText(_translate("MainWindow", "Single Image"))
        self.m_btn_multiple_image.setText(_translate("MainWindow", "Multiple Image"))
        self.m_btn_manual.setText(_translate("MainWindow", "Manual"))
        self.m_btn_change_log.setText(_translate("MainWindow", "changelog"))
        self.m_btn_log.setText(_translate("MainWindow", ".log"))
        self.m_left_arrow.setText(_translate("MainWindow", "<"))
        self.m_right_arrow.setText(_translate("MainWindow", ">"))
        self.m_reset.setText(_translate("MainWindow", "Reset"))


import source_rc