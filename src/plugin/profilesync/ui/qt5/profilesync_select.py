# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Repos\ModOrganizer-Plugins\src\plugin\profilesync\ui\profilesync_select.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_profileSelectWidget(object):
    def setupUi(self, profileSelectWidget):
        profileSelectWidget.setObjectName("profileSelectWidget")
        profileSelectWidget.resize(405, 70)
        self.verticalLayout = QtWidgets.QVBoxLayout(profileSelectWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupSelectWidget = QtWidgets.QWidget(profileSelectWidget)
        self.groupSelectWidget.setObjectName("groupSelectWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupSelectWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupCreateWidget = QtWidgets.QWidget(self.groupSelectWidget)
        self.groupCreateWidget.setObjectName("groupCreateWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupCreateWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.newGroupLabel = QtWidgets.QLabel(self.groupCreateWidget)
        self.newGroupLabel.setObjectName("newGroupLabel")
        self.horizontalLayout.addWidget(self.newGroupLabel)
        self.newGroupText = QtWidgets.QLineEdit(self.groupCreateWidget)
        self.newGroupText.setObjectName("newGroupText")
        self.horizontalLayout.addWidget(self.newGroupText)
        self.newGroupButton = QtWidgets.QPushButton(self.groupCreateWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newGroupButton.sizePolicy().hasHeightForWidth())
        self.newGroupButton.setSizePolicy(sizePolicy)
        self.newGroupButton.setObjectName("newGroupButton")
        self.horizontalLayout.addWidget(self.newGroupButton)
        self.verticalLayout_2.addWidget(self.groupCreateWidget)
        self.selectWidget = QtWidgets.QWidget(self.groupSelectWidget)
        self.selectWidget.setObjectName("selectWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.selectWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupSelect = QtWidgets.QComboBox(self.selectWidget)
        self.groupSelect.setObjectName("groupSelect")
        self.horizontalLayout_2.addWidget(self.groupSelect)
        self.groupDeleteButton = QtWidgets.QPushButton(self.selectWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupDeleteButton.sizePolicy().hasHeightForWidth())
        self.groupDeleteButton.setSizePolicy(sizePolicy)
        self.groupDeleteButton.setObjectName("groupDeleteButton")
        self.horizontalLayout_2.addWidget(self.groupDeleteButton)
        self.verticalLayout_2.addWidget(self.selectWidget)
        self.verticalLayout.addWidget(self.groupSelectWidget)

        self.retranslateUi(profileSelectWidget)
        QtCore.QMetaObject.connectSlotsByName(profileSelectWidget)

    def retranslateUi(self, profileSelectWidget):
        _translate = QtCore.QCoreApplication.translate
        profileSelectWidget.setWindowTitle(_translate("profileSelectWidget", "Form"))
        self.newGroupLabel.setText(_translate("profileSelectWidget", "New Group"))
        self.newGroupButton.setText(_translate("profileSelectWidget", "Create"))
        self.groupDeleteButton.setText(_translate("profileSelectWidget", "Delete"))
