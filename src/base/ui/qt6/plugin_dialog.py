# Form implementation generated from reading ui file 'D:\Repos\ModOrganizer-Plugins\src\base\ui\plugin_dialog.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_pluginDialog(object):
    def setupUi(self, pluginDialog):
        pluginDialog.setObjectName("pluginDialog")
        pluginDialog.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        pluginDialog.resize(238, 53)
        self.pluginLayout = QtWidgets.QVBoxLayout(pluginDialog)
        self.pluginLayout.setObjectName("pluginLayout")
        self.titleWidget = QtWidgets.QWidget(parent=pluginDialog)
        self.titleWidget.setMaximumSize(QtCore.QSize(16777215, 30))
        self.titleWidget.setObjectName("titleWidget")
        self.titleLayout = QtWidgets.QHBoxLayout(self.titleWidget)
        self.titleLayout.setContentsMargins(0, 0, 0, 0)
        self.titleLayout.setObjectName("titleLayout")
        self.dialogTitleLabel = QtWidgets.QLabel(parent=self.titleWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dialogTitleLabel.sizePolicy().hasHeightForWidth())
        self.dialogTitleLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.dialogTitleLabel.setFont(font)
        self.dialogTitleLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.dialogTitleLabel.setObjectName("dialogTitleLabel")
        self.titleLayout.addWidget(self.dialogTitleLabel)
        self.dialogVersionLabel = QtWidgets.QLabel(parent=self.titleWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dialogVersionLabel.sizePolicy().hasHeightForWidth())
        self.dialogVersionLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.dialogVersionLabel.setFont(font)
        self.dialogVersionLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.dialogVersionLabel.setObjectName("dialogVersionLabel")
        self.titleLayout.addWidget(self.dialogVersionLabel)
        self.pluginLayout.addWidget(self.titleWidget)
        self.contentWidget = QtWidgets.QWidget(parent=pluginDialog)
        self.contentWidget.setObjectName("contentWidget")
        self.contentLayout = QtWidgets.QVBoxLayout(self.contentWidget)
        self.contentLayout.setContentsMargins(0, 0, 0, 0)
        self.contentLayout.setSpacing(0)
        self.contentLayout.setObjectName("contentLayout")
        self.pluginLayout.addWidget(self.contentWidget)

        self.retranslateUi(pluginDialog)
        QtCore.QMetaObject.connectSlotsByName(pluginDialog)

    def retranslateUi(self, pluginDialog):
        _translate = QtCore.QCoreApplication.translate
        pluginDialog.setWindowTitle(_translate("pluginDialog", "Form"))
        self.dialogTitleLabel.setText(_translate("pluginDialog", "Dialog Title"))
        self.dialogVersionLabel.setText(_translate("pluginDialog", "dialogVersion"))
