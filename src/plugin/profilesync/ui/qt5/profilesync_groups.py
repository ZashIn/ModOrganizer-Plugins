# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Repos\ModOrganizer-Plugins\src\plugin\profilesync\ui\profilesync_groups.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_profileSyncGroupsTabWidget(object):
    def setupUi(self, profileSyncGroupsTabWidget):
        profileSyncGroupsTabWidget.setObjectName("profileSyncGroupsTabWidget")
        profileSyncGroupsTabWidget.resize(360, 360)
        profileSyncGroupsTabWidget.setMinimumSize(QtCore.QSize(360, 360))
        self.verticalLayout = QtWidgets.QVBoxLayout(profileSyncGroupsTabWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.infoWidget = QtWidgets.QWidget(profileSyncGroupsTabWidget)
        self.infoWidget.setObjectName("infoWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.infoWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.infoLabel = QtWidgets.QLabel(self.infoWidget)
        self.infoLabel.setWordWrap(True)
        self.infoLabel.setObjectName("infoLabel")
        self.verticalLayout_4.addWidget(self.infoLabel)
        self.verticalLayout.addWidget(self.infoWidget)
        self.profileListWidget = QtWidgets.QWidget(profileSyncGroupsTabWidget)
        self.profileListWidget.setObjectName("profileListWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.profileListWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.profileList = QtWidgets.QListWidget(self.profileListWidget)
        self.profileList.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.profileList.setObjectName("profileList")
        self.verticalLayout_3.addWidget(self.profileList)
        self.verticalLayout.addWidget(self.profileListWidget)

        self.retranslateUi(profileSyncGroupsTabWidget)
        QtCore.QMetaObject.connectSlotsByName(profileSyncGroupsTabWidget)

    def retranslateUi(self, profileSyncGroupsTabWidget):
        _translate = QtCore.QCoreApplication.translate
        profileSyncGroupsTabWidget.setWindowTitle(_translate("profileSyncGroupsTabWidget", "Form"))
        self.infoLabel.setText(_translate("profileSyncGroupsTabWidget", "Every profile selected within the same group will synchronise their mod list order. When creating a new group, the first profile selected is the starting order. Each profile can only be a member of one group."))
