#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QWidget, QMessageBox, QPushButton, QLineEdit,
    QInputDialog, QApplication, QLabel, QHBoxLayout, QVBoxLayout)
from PyQt5.QtCore import Qt
from math import sqrt, sin, cos
from cmath import rect, pi, polar, phase, sqrt as csqrt


 
def cube_root(number):
    negative = False
    if number < 0:
        negative = True
        number = abs(number)
    minimum = 0
    maximum = number + 1
    middle = (number + 1) / 2
    while not(number - 0.000000001 < middle ** 3 < number + 0.000000001):
        if middle ** 3 > number:
            maximum = middle
        else:
            minimum = middle
        middle = (maximum + minimum) / 2
    if negative:
        middle = - middle
    return middle    
        
def cubic_equation(a, b, c, d):
    p = (3 * a * c - b ** 2) / (3 * a ** 2)
    q = (2 * b ** 3 - 9 * a * b * c + 27 * a ** 2 * d) / (27 * a ** 3)
    Q = (p / 3) ** 3 + (q / 2) ** 2
    if Q >= 0:
        root = rect(sqrt(Q), 0)
    else:
        root = csqrt(Q)
    z = - q / 2 + root
    alpha = cube_root(abs(z)) * rect(cos(phase(z) / 3), sin(phase(z) / 3))
    betha = -p/(3 * alpha)
    zed = sqrt(3) * (alpha - betha) / 2
    y_options = [alpha + betha,
         -(alpha + betha) / 2 + rect(-polar(zed)[1], polar(zed)[0]),
         -(alpha + betha) / 2 - rect(-polar(zed)[1], polar(zed)[0])]
    x = [str(y - b / (3 * a)) for y in y_options]
    return ', '.join(x)
class Example(QWidget):
        

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):


        l1 = QLabel('Кубическое уравнение имеет вид:\nax^3 + bx^2 + cx + d = 0\nВведите значения a, b, c и d, используя кнопки ниже,\nпосле чего получите результат, нажав\nсоответствующую кнопку', self)
        
        
        btna = QPushButton('a', self)
        btna.clicked.connect(self.showDialoga)        
        
        
        btnb = QPushButton('b', self)
        btnb.clicked.connect(self.showDialogb)        


        btnc = QPushButton('c', self)
        btnc.clicked.connect(self.showDialogc)


        btnd = QPushButton('d', self)
        btnd.clicked.connect(self.showDialogd)
        
        
        result = QPushButton('Результат', self)
        result.clicked.connect(self.showResult)
        
        hbox1 = QHBoxLayout()
        hbox1.addWidget(l1)
        
        hbox2 = QHBoxLayout()
        hbox2.addStretch(9)
        hbox2.addWidget(btna)
        hbox2.addWidget(btnb)
        hbox2.addWidget(btnc)
        hbox2.addWidget(btnd)
        

        
        hbox3 = QHBoxLayout()
        hbox3.addWidget(result)         

        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        
        self.setLayout(vbox)

        self.setGeometry(500, 500, 308, 150)
        self.setWindowTitle('Input dialog')
        self.show()


    def showDialoga(self):
        text, ok = QInputDialog.getText(self, 'a', 'Введите значение a:')
        if ok:
            self.a = int(text)
    
    def showDialogb(self):
        text, ok = QInputDialog.getText(self, 'b', 'Введите значение b:')
        if ok:
            self.b = int(text)
    
    def showDialogc(self):
        text, ok = QInputDialog.getText(self, 'c', 'Введите значение c:')
        if ok:
            self.c = int(text)

    def showDialogd(self):
        text, ok = QInputDialog.getText(self, 'd', 'Введите значение d:')
        if ok:
            self.d = int(text)
    def showResult(self):
        
        reply = QMessageBox.question(self, 'Результат', cubic_equation(self.a, self.b, self.c, self.d) + "\nЕсли вы хотите выйти, нажмите 'Yes'. Если продолжить - 'No'.", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            sys.exit()
        else:
            self.show()
        
if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())