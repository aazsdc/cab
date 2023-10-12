# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\pythonProject1\GUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(519, 574)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(160, 520, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.listView = QtWidgets.QListView(Dialog)
        self.listView.setGeometry(QtCore.QRect(10, 90, 281, 181))
        self.listView.setObjectName("listView")
        self.toolButton = QtWidgets.QToolButton(Dialog)
        self.toolButton.setGeometry(QtCore.QRect(20, 20, 51, 31))
        self.toolButton.setObjectName("ranking")
        self.toolButton_2 = QtWidgets.QToolButton(Dialog)
        self.toolButton_2.setGeometry(QtCore.QRect(90, 20, 51, 31))
        self.toolButton_2.setObjectName("data browse")
        self.toolButton_3 = QtWidgets.QToolButton(Dialog)
        self.toolButton_3.setGeometry(QtCore.QRect(170, 20, 51, 31))
        self.toolButton_3.setObjectName("전처리select")
        self.toolButton_4 = QtWidgets.QToolButton(Dialog)
        self.toolButton_4.setGeometry(QtCore.QRect(250, 20, 51, 31))
        self.toolButton_4.setObjectName("Algorithm-if u can")
        self.toolButton_5 = QtWidgets.QToolButton(Dialog)
        self.toolButton_5.setGeometry(QtCore.QRect(340, 20, 81, 31))
        self.toolButton_5.setObjectName("select layser/sigmoid/softmax ..etc")
        self.listView_2 = QtWidgets.QListView(Dialog)
        self.listView_2.setGeometry(QtCore.QRect(10, 290, 281, 171))
        self.listView_2.setObjectName("listView_2")
        self.listView_3 = QtWidgets.QListView(Dialog)
        self.listView_3.setGeometry(QtCore.QRect(10, 470, 281, 31))
        self.listView_3.setObjectName("listView_3")
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(330, 70, 118, 23))
        self.progressBar.setProperty("value", 100)
        self.progressBar.setObjectName("progressBar")
        self.graphicsView = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(310, 110, 151, 91))
        self.graphicsView.setObjectName("graphicsView")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.toolButton.setText(_translate("Dialog", "ranking"))
        self.toolButton_2.setText(_translate("Dialog", "data browse"))
        self.toolButton_3.setText(_translate("Dialog", "전처리select"))
        self.toolButton_4.setText(_translate("Dialog", "Algorithm-if u can"))
        self.toolButton_5.setText(_translate("Dialog", "select layser/sigmoid/softmax ..etc"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

