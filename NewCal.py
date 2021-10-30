# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Study\FE\Python\me-repos\NewCal.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

dot = False

class Ui_MainWindow(object):
        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(450, 685)
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setStyleSheet("*{\n"
        " background:#6a9389\n"
        "}\n"
        "\n"
        "QLabel\n"
        "{\n"
        "color:white;\n"
        "background:#6a9389\n"
        "}\n"
        "\n"
        "QPushButton\n"
        "{\n"
        "color:rgb(68, 68, 68);\n"
        "border-radius: 35.5px;\n"
        "background: #a3e7d6\n"
        "}\n"
        "\n"
        "QPushButton:hover\n"
        "{\n"
        "background: white;\n"
        "color: rgb(68, 68, 68)\n"
        "}\n"
        "")
                self.centralwidget.setObjectName("centralwidget")
                self.outputlabel = QtWidgets.QLabel(self.centralwidget)
                self.outputlabel.setGeometry(QtCore.QRect(5, 20, 440, 101))
                font = QtGui.QFont()
                font.setFamily("Microsoft YaHei")
                font.setPointSize(48)
                self.outputlabel.setFont(font)
                self.outputlabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
                self.outputlabel.setObjectName("outputlabel")
                self.frame = QtWidgets.QFrame(self.centralwidget)
                self.frame.setGeometry(QtCore.QRect(0, 129, 450, 555))
                self.frame.setStyleSheet("QFrame\n"
        "{\n"
        "border-radius: 50px;\n"
        "background: #86bcaf\n"
        "}")
                self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame.setObjectName("frame")
                self.c = QtWidgets.QPushButton(self.frame, clicked = lambda: self.press_it("c"))
                self.c.setGeometry(QtCore.QRect(30, 30, 75, 75))
                font = QtGui.QFont()
                font.setFamily("Microsoft YaHei")
                font.setPointSize(22)
                self.c.setFont(font)
                self.c.setObjectName("c")
                self.ce = QtWidgets.QPushButton(self.frame, clicked = lambda: self.remove_it())
                self.ce.setGeometry(QtCore.QRect(130, 30, 75, 75))
                font = QtGui.QFont()
                font.setFamily("Microsoft YaHei")
                font.setPointSize(22)
                self.ce.setFont(font)
                self.ce.setObjectName("ce")
                self.divide = QtWidgets.QPushButton(self.frame, clicked = lambda: self.press_it("/"))
                self.divide.setGeometry(QtCore.QRect(240, 30, 75, 75))
                font = QtGui.QFont()
                font.setFamily("Microsoft YaHei")
                font.setPointSize(22)
                self.divide.setFont(font)
                self.divide.setObjectName("divide")
                self.times = QtWidgets.QPushButton(self.frame, clicked = lambda: self.press_it("*"))
                self.times.setGeometry(QtCore.QRect(345, 30, 75, 75))
                font = QtGui.QFont()
                font.setFamily("Microsoft YaHei")
                font.setPointSize(22)
                self.times.setFont(font)
                self.times.setObjectName("times")
                self.plus = QtWidgets.QPushButton(self.frame, clicked = lambda: self.press_it("+"))
                self.plus.setGeometry(QtCore.QRect(345, 135, 75, 75))
                font = QtGui.QFont()
                font.setFamily("Microsoft YaHei")
                font.setPointSize(22)
                self.plus.setFont(font)
                self.plus.setObjectName("plus")
                self.minus = QtWidgets.QPushButton(self.frame, clicked = lambda: self.press_it("-"))
                self.minus.setGeometry(QtCore.QRect(345, 240, 75, 75))
                font = QtGui.QFont()
                font.setFamily("Microsoft YaHei")
                font.setPointSize(22)
                self.minus.setFont(font)
                self.minus.setObjectName("minus")
                self.equal = QtWidgets.QPushButton(self.frame, clicked = lambda: self.math_it())
                self.equal.setGeometry(QtCore.QRect(345, 344, 75, 181))
                font = QtGui.QFont()
                font.setFamily("Microsoft YaHei")
                font.setPointSize(22)
                self.equal.setFont(font)
                self.equal.setStyleSheet("*{\n"
        "color:white;\n"
        "background:rgb(68, 68, 68)\n"
        "}\n"
        "QPushButton:hover\n"
        "{\n"
        "background: rgb(106, 147, 137);\n"
        "color: white;\n"
        "}\n"
        "")
                self.equal.setObjectName("equal")
                self.seven = QtWidgets.QPushButton(self.frame, clicked = lambda: self.press_it("7"))
                self.seven.setGeometry(QtCore.QRect(30, 135, 75, 75))
                font = QtGui.QFont()
                font.setFamily("Microsoft YaHei")
                font.setPointSize(22)
                self.seven.setFont(font)
                self.seven.setStyleSheet("*{\n"
        "color:white;\n"
        "background: #86bcaf\n"
        "}\n"
        "QPushButton:hover\n"
        "{\n"
        "background: white;\n"
        "color: rgb(68, 68, 68)\n"
        "}\n"
        "")
                self.seven.setObjectName("seven")
                self.eight = QtWidgets.QPushButton(self.frame, clicked = lambda: self.press_it("8"))
                self.eight.setGeometry(QtCore.QRect(135, 135, 75, 75))
                font = QtGui.QFont()
                font.setFamily("Microsoft YaHei")
                font.setPointSize(22)
                self.eight.setFont(font)
                self.eight.setStyleSheet("*{\n"
        "color:white;\n"
        "background: #86bcaf\n"
        "}\n"
        "QPushButton:hover\n"
        "{\n"
        "background: white;\n"
        "color: rgb(68, 68, 68)\n"
        "}\n"
        "")
                self.eight.setObjectName("eight")
                self.nine = QtWidgets.QPushButton(self.frame, clicked = lambda: self.press_it("9"))
                self.nine.setGeometry(QtCore.QRect(240, 135, 75, 75))
                font = QtGui.QFont()
                font.setFamily("Microsoft YaHei")
                font.setPointSize(22)
                self.nine.setFont(font)
                self.nine.setStyleSheet("*{\n"
        "color:white;\n"
        "background: #86bcaf\n"
        "}\n"
        "QPushButton:hover\n"
        "{\n"
        "background: white;\n"
        "color: rgb(68, 68, 68)\n"
        "}\n"
        "")
                self.nine.setObjectName("nine")
                self.six = QtWidgets.QPushButton(self.frame, clicked = lambda: self.press_it("6"))
                self.six.setGeometry(QtCore.QRect(240, 240, 75, 75))
                font = QtGui.QFont()
                font.setFamily("Microsoft YaHei")
                font.setPointSize(22)
                self.six.setFont(font)
                self.six.setStyleSheet("*{\n"
        "color:white;\n"
        "background: #86bcaf\n"
        "}\n"
        "QPushButton:hover\n"
        "{\n"
        "background: white;\n"
        "color: rgb(68, 68, 68)\n"
        "}\n"
        "")
                self.six.setObjectName("six")
                self.four = QtWidgets.QPushButton(self.frame, clicked = lambda: self.press_it("4"))
                self.four.setGeometry(QtCore.QRect(30, 240, 75, 75))
                font = QtGui.QFont()
                font.setFamily("Microsoft YaHei")
                font.setPointSize(22)
                self.four.setFont(font)
                self.four.setStyleSheet("*{\n"
        "color:white;\n"
        "background: #86bcaf\n"
        "}\n"
        "QPushButton:hover\n"
        "{\n"
        "background: white;\n"
        "color: rgb(68, 68, 68)\n"
        "}\n"
        "")
                self.four.setObjectName("four")
                self.five = QtWidgets.QPushButton(self.frame, clicked = lambda: self.press_it("5"))
                self.five.setGeometry(QtCore.QRect(135, 240, 75, 75))
                font = QtGui.QFont()
                font.setFamily("Microsoft YaHei")
                font.setPointSize(22)
                self.five.setFont(font)
                self.five.setStyleSheet("*{\n"
        "color:white;\n"
        "background: #86bcaf\n"
        "}\n"
        "QPushButton:hover\n"
        "{\n"
        "background: white;\n"
        "color: rgb(68, 68, 68)\n"
        "}\n"
        "")
                self.five.setObjectName("five")
                self.two = QtWidgets.QPushButton(self.frame, clicked = lambda: self.press_it("2"))
                self.two.setGeometry(QtCore.QRect(135, 340, 75, 75))
                font = QtGui.QFont()
                font.setFamily("Microsoft YaHei")
                font.setPointSize(22)
                self.two.setFont(font)
                self.two.setStyleSheet("*{\n"
        "color:white;\n"
        "background: #86bcaf\n"
        "}\n"
        "QPushButton:hover\n"
        "{\n"
        "background: white;\n"
        "color: rgb(68, 68, 68)\n"
        "}\n"
        "")
                self.two.setObjectName("two")
                self.three = QtWidgets.QPushButton(self.frame, clicked = lambda: self.press_it("3"))
                self.three.setGeometry(QtCore.QRect(240, 340, 75, 75))
                font = QtGui.QFont()
                font.setFamily("Microsoft YaHei")
                font.setPointSize(22)
                self.three.setFont(font)
                self.three.setStyleSheet("*{\n"
        "color:white;\n"
        "background: #86bcaf\n"
        "}\n"
        "QPushButton:hover\n"
        "{\n"
        "background: white;\n"
        "color: rgb(68, 68, 68)\n"
        "}\n"
        "")
                self.three.setObjectName("three")
                self.one = QtWidgets.QPushButton(self.frame, clicked = lambda: self.press_it("1"))
                self.one.setGeometry(QtCore.QRect(30, 340, 75, 75))
                font = QtGui.QFont()
                font.setFamily("Microsoft YaHei")
                font.setPointSize(22)
                self.one.setFont(font)
                self.one.setStyleSheet("*{\n"
        "color:white;\n"
        "background: #86bcaf\n"
        "}\n"
        "QPushButton:hover\n"
        "{\n"
        "background: white;\n"
        "color: rgb(68, 68, 68)\n"
        "}\n"
        "")
                self.one.setObjectName("one")
                self.zero = QtWidgets.QPushButton(self.frame, clicked = lambda: self.press_it("0"))
                self.zero.setGeometry(QtCore.QRect(44, 450, 180, 75))
                font = QtGui.QFont()
                font.setFamily("Microsoft YaHei")
                font.setPointSize(22)
                self.zero.setFont(font)
                self.zero.setStyleSheet("*{\n"
        "color:white;\n"
        "background: #86bcaf\n"
        "}\n"
        "QPushButton:hover\n"
        "{\n"
        "background: white;\n"
        "color: rgb(68, 68, 68)\n"
        "}\n"
        "")
                self.zero.setObjectName("zero")
                self.dot = QtWidgets.QPushButton(self.frame, clicked = lambda: self.dot_it())
                self.dot.setGeometry(QtCore.QRect(240, 450, 75, 75))
                font = QtGui.QFont()
                font.setFamily("Microsoft YaHei")
                font.setPointSize(22)
                self.dot.setFont(font)
                self.dot.setStyleSheet("*{\n"
        "color:white;\n"
        "background: #86bcaf\n"
        "}\n"
        "QPushButton:hover\n"
        "{\n"
        "background: white;\n"
        "color: rgb(68, 68, 68)\n"
        "}\n"
        "")
                self.dot.setObjectName("dot")
                self.frame.raise_()
                self.outputlabel.raise_()
                MainWindow.setCentralWidget(self.centralwidget)

                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def remove_it(self):
                global dot
                screen = self.outputlabel.text()
                if screen [-1] == ".":
                        dot = False
                screen = screen[:-1]
                self.outputlabel.setText(screen)
        
        def math_it(self):
                screen = self.outputlabel.text()
                try:
                        answer = eval(screen)
                        self.outputlabel.setText(str(answer))
                except:
                        self.outputlabel.setText("ERROR")


        def dot_it(self):
                global dot  
                screen = self.outputlabel.text()                
                if dot == False:
                        if not screen[-1].isnumeric():
                                pass
                        else:
                                screen = f'{screen}.'
                                self.outputlabel.setText(screen)
                                dot = True
                elif dot == True:
                        pass

                else:
                        pass
                
                        
                
        def press_it(self, pressed):
                global dot
                screen = self.outputlabel.text()
                if pressed == "c":
                        self.outputlabel.setText("0")
                elif not pressed.isnumeric():
                        dot = False
                        self.outputlabel.setText(f'{self.outputlabel.text()}{pressed}')
                else:
                        if self.outputlabel.text() == "0":
                                self.outputlabel.setText("")
                        self.outputlabel.setText(f'{self.outputlabel.text()}{pressed}')

        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
                self.outputlabel.setText(_translate("MainWindow", "0"))
                self.c.setText(_translate("MainWindow", "c"))
                self.ce.setText(_translate("MainWindow", "ce"))
                self.divide.setText(_translate("MainWindow", "÷"))
                self.times.setText(_translate("MainWindow", "x"))
                self.plus.setText(_translate("MainWindow", "+"))
                self.minus.setText(_translate("MainWindow", "-"))
                self.equal.setText(_translate("MainWindow", "="))
                self.seven.setText(_translate("MainWindow", "7"))
                self.eight.setText(_translate("MainWindow", "8"))
                self.nine.setText(_translate("MainWindow", "9"))
                self.six.setText(_translate("MainWindow", "6"))
                self.four.setText(_translate("MainWindow", "4"))
                self.five.setText(_translate("MainWindow", "5"))
                self.two.setText(_translate("MainWindow", "2"))
                self.three.setText(_translate("MainWindow", "3"))
                self.one.setText(_translate("MainWindow", "1"))
                self.zero.setText(_translate("MainWindow", "0"))
                self.dot.setText(_translate("MainWindow", "."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
