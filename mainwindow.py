# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

from PyQt5.QtGui import *
from PyQt5.QtCore import *
import os
import pandas as pd
import cv2
import numpy as np
import json
class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(959, 891)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        '''4 candidate imgs'''
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(199, 153, 720, 251))
        self.groupBox.setObjectName("groupBox")
        self.label_x1 = QtWidgets.QLabel(self.groupBox)
        self.label_x1.setGeometry(QtCore.QRect(0, 21, 180, 231))
        self.label_x1.setText("")
        self.label_x1.setObjectName("label_x1")
        self.label_x2 = QtWidgets.QLabel(self.groupBox)
        self.label_x2.setGeometry(QtCore.QRect(180, 21, 180, 231))
        self.label_x2.setText("")
        self.label_x2.setObjectName("label_x2")
        self.label_x3 = QtWidgets.QLabel(self.groupBox)
        self.label_x3.setGeometry(QtCore.QRect(360, 21, 180, 231))
        self.label_x3.setText("")
        self.label_x3.setObjectName("label_x3")
        self.label_x4 = QtWidgets.QLabel(self.groupBox)
        self.label_x4.setGeometry(QtCore.QRect(540, 21, 180, 231))
        self.label_x4.setText("")
        self.label_x4.setObjectName("label_x4")
        '''4 true imgs'''
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(199, 553, 720, 251))
        self.groupBox_3.setObjectName("groupBox")
        self.label_y1 = QtWidgets.QLabel(self.groupBox_3)
        self.label_y1.setGeometry(QtCore.QRect(0, 21, 180, 231))
        self.label_y1.setText("")
        self.label_y1.setObjectName("label_y1")
        self.label_y2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_y2.setGeometry(QtCore.QRect(180,21, 180, 231))
        self.label_y2.setText("")
        self.label_y2.setObjectName("label_y2")
        self.label_y3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_y3.setGeometry(QtCore.QRect(360, 21, 180, 231))
        self.label_y3.setText("")
        self.label_y3.setObjectName("label_y3")
        self.label_y4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_y4.setGeometry(QtCore.QRect(540, 21, 180, 231))
        self.label_y4.setText("")
        self.label_y4.setObjectName("label_y4")
        '''cast img'''
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(9, 153, 180, 251))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_c = QtWidgets.QLabel(self.groupBox_2)
        self.label_c.setGeometry(QtCore.QRect(0, 21, 181, 231))
        self.label_c.setText("")
        self.label_c.setObjectName("label_4")

        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(630, 400, 68, 41))
        self.commandLinkButton.setObjectName("commandLinkButton")

        self.commandLinkButton2 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton2.setGeometry(QtCore.QRect(630, 800, 68, 41))
        self.commandLinkButton2.setObjectName("commandLinkButton2")

        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 70, 583, 30))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.toolButton = QtWidgets.QToolButton(self.widget)
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout.addWidget(self.toolButton)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout.addWidget(self.lineEdit_2)
        self.toolButton_2 = QtWidgets.QToolButton(self.widget)
        self.toolButton_2.setObjectName("toolButton_2")
        self.horizontalLayout.addWidget(self.toolButton_2)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout.addWidget(self.lineEdit_3)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 799, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.num = 10
        self.mov = 0
        self.cast= 0
        self.galleries_df = pd.read_csv('/media/hyy/新加卷/eccv/ECCVchallenge/testGalleriesDF.csv')


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        '''connect button & event'''
        self.toolButton.clicked.connect(self.on_click1_mov)
        self.toolButton_2.clicked.connect(self.on_click2_cast)
        self.pushButton_3.clicked.connect(self.on_click3_ok)
        self.commandLinkButton.clicked.connect(self.on_click4_next)
        self.commandLinkButton2.clicked.connect(self.on_click5_next)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Top Rank"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Cast"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Truth"))
        self.commandLinkButton.setText(_translate("MainWindow", "next"))
        self.commandLinkButton2.setText(_translate("MainWindow", "next"))
        self.label.setText(_translate("MainWindow", "Movie"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.label_2.setText(_translate("MainWindow", "Cast"))
        self.toolButton_2.setText(_translate("MainWindow", "..."))
        self.label_3.setText(_translate("MainWindow", "top"))
        self.pushButton_3.setText(_translate("MainWindow", "ok"))

    '''MOUSE CLICK'''

    def on_click1_mov(self):
        global mov_dir
        mov_dir = QFileDialog.getExistingDirectory(self, 'chose movie', data_dir)
        print('mov_dir:{}'.format(mov_dir))
        mov_dir_l = mov_dir.split('/')
        self.mov=mov_dir_l[-1]
        self.lineEdit.setText(mov_dir_l[-1])

    def on_click2_cast(self):
        cast_dir, cast_imgType = QFileDialog.getOpenFileNames(self, 'choose_cast', os.path.join(mov_dir, 'cast'))

        print('cast_dir:{}'.format(cast_dir))
        cast_dir_l = cast_dir[0].split('/')
        self.lineEdit_2.setText(cast_dir_l[-1])
        self.cast=cast_dir_l[-1]
        # 利用qlabel显示图片
        png = QtGui.QPixmap(cast_dir[0]).scaled(self.label_c.width(), self.label_c.height())
        self.label_c.setPixmap(png)

    def on_click3_ok(self):
        self.num = self.lineEdit_3.text()

        self.line_re=self.match_line()
        self.groupBox.setTitle("Top Rank 4")
        #self.show_4(self.line_re,0)
        self.show_4_crop(self.line_re, 0)
        self.i=0
        self.true_i=0
        get_true=self.get_label()
        name=self.mov+'_'+self.cast
        name=name.split('.')[0]

        self.true_list=list(get_true[name])
        self.show_true()


    def on_click4_next(self):
        if self.i+4<len(self.line_re):
            self.i= self.i+4
            titel='Top Rank '+str(self.i+4)
            self.groupBox.setTitle(titel)
            #self.show_4(self.line_re, self.i)
            self.show_4_crop(self.line_re, self.i)
        else:
            reply = QMessageBox.question(self, 'Message', 'There is no more candidates!', QMessageBox.Yes)

    '''true next'''
    def on_click5_next(self):

        self.true_i=self.true_i+4
        print(self.true_i)
        if self.true_i +1> len(self.true_list):
            self.true_i=0
        self.show_true()

    def show_true(self):
        im_id = self.true_list[self.true_i]
        im_id = im_id.split('_')
        movie = im_id[0]
        id = im_id[1]
        cand = self.galleries_df.query('movie==@movie and id==@id')
        for chosen_index in list(cand.index):
            chosen_se = cand.loc[chosen_index]
            im_name = chosen_se['imname']
            cand_person_box = chosen_se['x1': 'del_y'].as_matrix()
            im_path = os.path.join(data_dir, movie, 'candidates', im_name)
            png = crop_image_2qimg(im_path, cand_person_box)
            png = QtGui.QPixmap(png).scaled(self.label_x1.width(), self.label_x1.height())
            self.label_y1.setPixmap(png)


        if self.true_i+2 > len(self.true_list):
            self.true_i=0
            return 0
        else:
            im_id = self.true_list[self.true_i+1]
            im_id = im_id.split('_')
            movie = im_id[0]
            id = im_id[1]
            cand = self.galleries_df.query('movie==@movie and id==@id')
            for chosen_index in list(cand.index):
                chosen_se = cand.loc[chosen_index]
                im_name = chosen_se['imname']
                cand_person_box = chosen_se['x1': 'del_y'].as_matrix()
                im_path = os.path.join(data_dir, movie, 'candidates', im_name)
                png = crop_image_2qimg(im_path, cand_person_box)
                png = QtGui.QPixmap(png).scaled(self.label_x1.width(), self.label_x1.height())
                self.label_y2.setPixmap(png)

        if self.true_i + 3 > len(self.true_list):
            self.true_i = 0
            return 0
        else:
            im_id = self.true_list[self.true_i+2]
            im_id = im_id.split('_')
            movie = im_id[0]
            id = im_id[1]
            cand = self.galleries_df.query('movie==@movie and id==@id')
            for chosen_index in list(cand.index):
                chosen_se = cand.loc[chosen_index]
                im_name = chosen_se['imname']
                cand_person_box = chosen_se['x1': 'del_y'].as_matrix()
                im_path = os.path.join(data_dir, movie, 'candidates', im_name)
                png = crop_image_2qimg(im_path, cand_person_box)
                png = QtGui.QPixmap(png).scaled(self.label_x1.width(), self.label_x1.height())
                self.label_y3.setPixmap(png)

        if self.true_i + 4 > len(self.true_list):
            self.true_i = 0
            return 0
        else:
            im_id = self.true_list[self.true_i+3]
            im_id = im_id.split('_')
            movie = im_id[0]
            id = im_id[1]
            cand = self.galleries_df.query('movie==@movie and id==@id')
            for chosen_index in list(cand.index):
                chosen_se = cand.loc[chosen_index]
                im_name = chosen_se['imname']
                cand_person_box = chosen_se['x1': 'del_y'].as_matrix()
                im_path = os.path.join(data_dir, movie, 'candidates', im_name)
                png = crop_image_2qimg(im_path, cand_person_box)
                png = QtGui.QPixmap(png).scaled(self.label_x1.width(), self.label_x1.height())
                self.label_y4.setPixmap(png)

    def show_4(self,line_re,i):
        ''''''
        if i<len(line_re):
            im_id = line_re[i]
            im_id = im_id.split('_')
            movie = im_id[0]
            id = im_id[1]
            cand = self.galleries_df.query('movie==@movie and id==@id')
            for chosen_index in list(cand.index):
                chosen_se = cand.loc[chosen_index]
                im_name = chosen_se['imname']
                im_path = os.path.join(data_dir, movie, 'candidates', im_name)
                png = QtGui.QPixmap(im_path).scaled(self.label_x1.width(), self.label_x1.height())
                self.label_x1.setPixmap(png)
        ''''''
        if i+1 < len(line_re):
            im_id = line_re[i+1]
            im_id = im_id.split('_')
            movie = im_id[0]
            id = im_id[1]
            cand = self.galleries_df.query('movie==@movie and id==@id')
            for chosen_index in list(cand.index):
                chosen_se = cand.loc[chosen_index]
                im_name = chosen_se['imname']
                im_path = os.path.join(data_dir, movie, 'candidates', im_name)
                png = QtGui.QPixmap(im_path).scaled(self.label_x2.width(), self.label_x2.height())
                self.label_x2.setPixmap(png)
        ''''''
        if i+2 <len(line_re):
            im_id = line_re[i+2]
            im_id = im_id.split('_')
            movie = im_id[0]
            id = im_id[1]
            cand = self.galleries_df.query('movie==@movie and id==@id')
            for chosen_index in list(cand.index):
                chosen_se = cand.loc[chosen_index]
                im_name = chosen_se['imname']
                im_path = os.path.join(data_dir, movie, 'candidates', im_name)
                png = QtGui.QPixmap(im_path).scaled(self.label_x3.width(), self.label_x3.height())
                self.label_x3.setPixmap(png)
        ''''''
        if i + 3 < len(line_re):
            im_id = line_re[i+3]
            im_id = im_id.split('_')
            movie = im_id[0]
            id = im_id[1]
            cand = self.galleries_df.query('movie==@movie and id==@id')
            for chosen_index in list(cand.index):
                chosen_se = cand.loc[chosen_index]
                im_name = chosen_se['imname']
                im_path = os.path.join(data_dir, movie, 'candidates', im_name)
                png = QtGui.QPixmap(im_path).scaled(self.label_x4.width(), self.label_x4.height())
                self.label_x4.setPixmap(png)


    def show_4_crop(self,line_re,i):
        ''''''
        if i<len(line_re):
            im_id = line_re[i]
            im_id = im_id.split('_')
            movie = im_id[0]
            id = im_id[1]
            cand = self.galleries_df.query('movie==@movie and id==@id')
            for chosen_index in list(cand.index):
                chosen_se = cand.loc[chosen_index]
                im_name = chosen_se['imname']
                cand_person_box = chosen_se['x1': 'del_y'].as_matrix()
                im_path = os.path.join(data_dir, movie, 'candidates', im_name)
                png = crop_image_2qimg(im_path, cand_person_box)
                png = QtGui.QPixmap(png).scaled(self.label_x1.width(), self.label_x1.height())
                self.label_x1.setPixmap(png)
        else:
            i=0
        ''''''
        if i+1 < len(line_re):
            im_id = line_re[i+1]
            im_id = im_id.split('_')
            movie = im_id[0]
            id = im_id[1]
            cand = self.galleries_df.query('movie==@movie and id==@id')
            for chosen_index in list(cand.index):
                chosen_se = cand.loc[chosen_index]
                im_name = chosen_se['imname']
                cand_person_box = chosen_se['x1': 'del_y'].as_matrix()
                im_path = os.path.join(data_dir, movie, 'candidates', im_name)
                png=crop_image_2qimg(im_path,cand_person_box)
                png = QtGui.QPixmap(png).scaled(self.label_x2.width(), self.label_x2.height())
                self.label_x2.setPixmap(png)
        else:
            i=0
        ''''''
        if i+2 <len(line_re):
            im_id = line_re[i+2]
            im_id = im_id.split('_')
            movie = im_id[0]
            id = im_id[1]
            cand = self.galleries_df.query('movie==@movie and id==@id')
            for chosen_index in list(cand.index):
                chosen_se = cand.loc[chosen_index]
                im_name = chosen_se['imname']
                cand_person_box = chosen_se['x1': 'del_y'].as_matrix()
                im_path = os.path.join(data_dir, movie, 'candidates', im_name)
                png = crop_image_2qimg(im_path, cand_person_box)
                png = QtGui.QPixmap(png).scaled(self.label_x3.width(), self.label_x3.height())
                self.label_x3.setPixmap(png)
        else:
            i=0
        ''''''
        if i + 3 < len(line_re):
            im_id = line_re[i+3]
            im_id = im_id.split('_')
            movie = im_id[0]
            id = im_id[1]
            cand = self.galleries_df.query('movie==@movie and id==@id')
            for chosen_index in list(cand.index):
                chosen_se = cand.loc[chosen_index]
                im_name = chosen_se['imname']
                cand_person_box = chosen_se['x1': 'del_y'].as_matrix()
                im_path = os.path.join(data_dir, movie, 'candidates', im_name)
                png = crop_image_2qimg(im_path, cand_person_box)
                png = QtGui.QPixmap(png).scaled(self.label_x4.width(), self.label_x4.height())
                self.label_x4.setPixmap(png)
        else:
            i=0


    '''return ['tt0070735_0234',..,] a list ,find the movie and the num line'''
    def match_line(self):
        c=self.mov+'_'+self.cast
        c=c.split('.')
        c=c[0]
        r_dir='/home/hyy/ECCVC/output/test_result2.txt'
        r=open(r_dir,'r')
        for line in r.readlines():
            line=line.split(' ')
            if c == line[0]:
                re=line[1].split(',')
                return re

    def get_label(self):
        jsonpath='/media/hyy/新加卷/eccv/ECCVchallenge/test_label.json'
        with open(jsonpath) as f:
            data = json.load(f)
        gt_dict = {}
        for key, value in data.items():
            gt_dict[key] = set(value)
        #print(gt_dict)
        return gt_dict


def crop_image_2qimg(im_path, box, wh=True):
    """
    Crop image with location indicated by the 'box'
    ---
    param:
        im_path: path to the original image
        box: ndarray or list with shape (4,)
        wh: boolean variable that indicates the coordinates mode of the box
    return:
        ndarray that contain the cropped image
    """

    if wh:
        x1, y1, w, h = box
        x2 = x1 + w
        y2 = y1 + h
    else:
        x1, y1, x2, y2 = box
    if x1<0:
        x1=0
    if y1<0:
        y1=0
    im2 = cv2.imread(im_path)
    im3 = im2[y1:y2, x1:x2]

    height, width, bytesPerComponent = im3.shape

    '''
    width = im3.shape[1]  # 获取图片宽度
    height = im3.shape[0]  # 获取图片高度

    pixmap = QtGui.QPixmap(width, height)  # 根据已知的高度和宽度新建一个空的QPixmap,
    qimg = pixmap.toImage()  # 将pximap转换为QImage类型的qimg

    # 循环读取cv_image的每个像素的r,g,b值，构成qRgb对象，再设置为qimg内指定位置的像素
    for row in range(0, height):
        for col in range(0, width):
            r = im3[row, col, 0]
            g = im3[row, col, 1]
            b = im3[row, col, 2]

            pix = qRgb(r, g, b)
            qimg.setPixel(col, row, pix)'''



    bgra = np.zeros([height, width, 4], dtype=np.uint8)
    bgra[:, :, 0:3] = im3
    return QtGui.QImage(bgra.data, width, height, QtGui.QImage.Format_RGB32)

    return image






if __name__ == "__main__":
    import sys

    global data_dir
    global i
    i = 0
    from PyQt5.QtGui import QIcon

    data_dir = '/media/hyy/新加卷/eccv/ECCVchallenge/test'




    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())
