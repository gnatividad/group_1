# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'my_crud2.ui'
#
# Created: Wed Mar 23 12:48:37 2016
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(558, 310)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_3)
        self.txtId = QtGui.QLineEdit(self.centralwidget)
        self.txtId.setEnabled(False)
        self.txtId.setObjectName(_fromUtf8("txtId"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.txtId)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label)
        self.txtFirstName = QtGui.QLineEdit(self.centralwidget)
        self.txtFirstName.setEnabled(False)
        self.txtFirstName.setObjectName(_fromUtf8("txtFirstName"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.txtFirstName)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_2)
        self.txtLastName = QtGui.QLineEdit(self.centralwidget)
        self.txtLastName.setEnabled(False)
        self.txtLastName.setObjectName(_fromUtf8("txtLastName"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.txtLastName)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_6)
        self.txtCourse = QtGui.QLineEdit(self.centralwidget)
        self.txtCourse.setEnabled(False)
        self.txtCourse.setObjectName(_fromUtf8("txtCourse"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.txtCourse)
        self.txtYear = QtGui.QLineEdit(self.centralwidget)
        self.txtYear.setEnabled(False)
        self.txtYear.setObjectName(_fromUtf8("txtYear"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.txtYear)
        self.txtSection = QtGui.QLineEdit(self.centralwidget)
        self.txtSection.setEnabled(False)
        self.txtSection.setObjectName(_fromUtf8("txtSection"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.txtSection)
        self.horizontalLayout_3.addLayout(self.formLayout)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.btnClear = QtGui.QPushButton(self.centralwidget)
        self.btnClear.setObjectName(_fromUtf8("btnClear"))
        self.verticalLayout.addWidget(self.btnClear)
        self.pushButton_10 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
        self.verticalLayout.addWidget(self.pushButton_10)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        spacerItem = QtGui.QSpacerItem(20, 18, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btnFirst = QtGui.QPushButton(self.centralwidget)
        self.btnFirst.setObjectName(_fromUtf8("btnFirst"))
        self.horizontalLayout.addWidget(self.btnFirst)
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_5 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem1 = QtGui.QSpacerItem(20, 17, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.pushButton_6 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.horizontalLayout_2.addWidget(self.pushButton_6)
        self.pushButton_7 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.horizontalLayout_2.addWidget(self.pushButton_7)
        self.pushButton_8 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.horizontalLayout_2.addWidget(self.pushButton_8)
        self.pushButton_9 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.horizontalLayout_2.addWidget(self.pushButton_9)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        spacerItem2 = QtGui.QSpacerItem(20, 28, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 558, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionAdd_Record = QtGui.QAction(MainWindow)
        self.actionAdd_Record.setObjectName(_fromUtf8("actionAdd_Record"))
        self.actionUpdate = QtGui.QAction(MainWindow)
        self.actionUpdate.setObjectName(_fromUtf8("actionUpdate"))
        self.actionDelete = QtGui.QAction(MainWindow)
        self.actionDelete.setObjectName(_fromUtf8("actionDelete"))
        self.actionSave_2 = QtGui.QAction(MainWindow)
        self.actionSave_2.setObjectName(_fromUtf8("actionSave_2"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionSearch = QtGui.QAction(MainWindow)
        self.actionSearch.setIconVisibleInMenu(True)
        self.actionSearch.setObjectName(_fromUtf8("actionSearch"))
        self.actionSave_3 = QtGui.QAction(MainWindow)
        self.actionSave_3.setObjectName(_fromUtf8("actionSave_3"))
        self.actionExit_2 = QtGui.QAction(MainWindow)
        self.actionExit_2.setObjectName(_fromUtf8("actionExit_2"))
        self.menuFile.addAction(self.actionSearch)
        self.menuFile.addAction(self.actionSave_3)
        self.menuFile.addAction(self.actionExit_2)
        self.menuEdit.addAction(self.actionAdd_Record)
        self.menuEdit.addAction(self.actionDelete)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.btnClear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.txtLastName.clear)
        QtCore.QObject.connect(self.btnClear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.txtId.clear)
        QtCore.QObject.connect(self.btnClear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.txtFirstName.clear)
        QtCore.QObject.connect(self.actionExit_2, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QObject.connect(self.btnClear, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.txtId.setEnabled)
        QtCore.QObject.connect(self.btnClear, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.txtFirstName.setEnabled)
        QtCore.QObject.connect(self.btnClear, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.txtLastName.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_3.setText(_translate("MainWindow", "ID Number:", None))
        self.label.setText(_translate("MainWindow", "First Name:", None))
        self.label_2.setText(_translate("MainWindow", "Last Name:", None))
        self.label_4.setText(_translate("MainWindow", "Course:", None))
        self.label_5.setText(_translate("MainWindow", "Year:", None))
        self.label_6.setText(_translate("MainWindow", "Section:", None))
        self.btnClear.setText(_translate("MainWindow", "Clear", None))
        self.pushButton_10.setText(_translate("MainWindow", "Search", None))
        self.pushButton.setText(_translate("MainWindow", "Exit", None))
        self.btnFirst.setText(_translate("MainWindow", "First", None))
        self.pushButton_3.setText(_translate("MainWindow", "Next", None))
        self.pushButton_4.setText(_translate("MainWindow", "Previous", None))
        self.pushButton_5.setText(_translate("MainWindow", "Last", None))
        self.pushButton_6.setText(_translate("MainWindow", "Add Record", None))
        self.pushButton_7.setText(_translate("MainWindow", "Edit", None))
        self.pushButton_8.setText(_translate("MainWindow", "Update", None))
        self.pushButton_9.setText(_translate("MainWindow", "Delete", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))
        self.actionSave.setText(_translate("MainWindow", "Save", None))
        self.actionAdd_Record.setText(_translate("MainWindow", "Add Record", None))
        self.actionUpdate.setText(_translate("MainWindow", "Update", None))
        self.actionDelete.setText(_translate("MainWindow", "Delete Record", None))
        self.actionSave_2.setText(_translate("MainWindow", "Save", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionSearch.setText(_translate("MainWindow", "Search", None))
        self.actionSave_3.setText(_translate("MainWindow", "Save", None))
        self.actionExit_2.setText(_translate("MainWindow", "Exit", None))

