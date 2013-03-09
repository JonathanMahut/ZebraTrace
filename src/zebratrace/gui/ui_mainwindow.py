# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_build\mainwindow.ui'
#
# Created: Sat Mar 09 18:06:18 2013
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(885, 596)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/image/images/zebra.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setMargin(9)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.topPanel = QtGui.QHBoxLayout()
        self.topPanel.setObjectName(_fromUtf8("topPanel"))
        self.labelPreview = QtGui.QLabel(self.centralwidget)
        self.labelPreview.setObjectName(_fromUtf8("labelPreview"))
        self.topPanel.addWidget(self.labelPreview)
        self.previewMode = QtGui.QComboBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.previewMode.sizePolicy().hasHeightForWidth())
        self.previewMode.setSizePolicy(sizePolicy)
        self.previewMode.setMinimumSize(QtCore.QSize(150, 0))
        self.previewMode.setObjectName(_fromUtf8("previewMode"))
        self.previewMode.addItem(_fromUtf8(""))
        self.previewMode.addItem(_fromUtf8(""))
        self.topPanel.addWidget(self.previewMode)
        spacerItem = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.topPanel.addItem(spacerItem)
        self.labelTransparency = QtGui.QLabel(self.centralwidget)
        self.labelTransparency.setObjectName(_fromUtf8("labelTransparency"))
        self.topPanel.addWidget(self.labelTransparency)
        self.sliderTransparency = QtGui.QSlider(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sliderTransparency.sizePolicy().hasHeightForWidth())
        self.sliderTransparency.setSizePolicy(sizePolicy)
        self.sliderTransparency.setMinimumSize(QtCore.QSize(150, 0))
        self.sliderTransparency.setMaximumSize(QtCore.QSize(200, 16777215))
        self.sliderTransparency.setMaximum(100)
        self.sliderTransparency.setSingleStep(1)
        self.sliderTransparency.setPageStep(10)
        self.sliderTransparency.setProperty("value", 50)
        self.sliderTransparency.setOrientation(QtCore.Qt.Horizontal)
        self.sliderTransparency.setInvertedAppearance(False)
        self.sliderTransparency.setInvertedControls(False)
        self.sliderTransparency.setObjectName(_fromUtf8("sliderTransparency"))
        self.topPanel.addWidget(self.sliderTransparency)
        spacerItem1 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.topPanel.addItem(spacerItem1)
        spacerItem2 = QtGui.QSpacerItem(5, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.topPanel.addItem(spacerItem2)
        self.topPanel.setStretch(6, 1)
        self.verticalLayout.addLayout(self.topPanel)
        self.frame = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 3, 3, 0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.splitter = QtGui.QSplitter(self.frame)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(6)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.frame_2 = QtGui.QFrame(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setContentsMargins(0, 0, 3, 0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.viewContainer = QtGui.QHBoxLayout()
        self.viewContainer.setSpacing(6)
        self.viewContainer.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.viewContainer.setObjectName(_fromUtf8("viewContainer"))
        self.horizontalLayout_3.addLayout(self.viewContainer)
        self.tabPreferences = QtGui.QTabWidget(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabPreferences.sizePolicy().hasHeightForWidth())
        self.tabPreferences.setSizePolicy(sizePolicy)
        self.tabPreferences.setMinimumSize(QtCore.QSize(240, 0))
        self.tabPreferences.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tabPreferences.setTabPosition(QtGui.QTabWidget.North)
        self.tabPreferences.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabPreferences.setElideMode(QtCore.Qt.ElideMiddle)
        self.tabPreferences.setDocumentMode(False)
        self.tabPreferences.setObjectName(_fromUtf8("tabPreferences"))
        self.tabOptions = QtGui.QWidget()
        self.tabOptions.setObjectName(_fromUtf8("tabOptions"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.tabOptions)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.boxCurves = QtGui.QGroupBox(self.tabOptions)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.boxCurves.sizePolicy().hasHeightForWidth())
        self.boxCurves.setSizePolicy(sizePolicy)
        self.boxCurves.setMinimumSize(QtCore.QSize(0, 0))
        self.boxCurves.setFlat(True)
        self.boxCurves.setCheckable(False)
        self.boxCurves.setObjectName(_fromUtf8("boxCurves"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.boxCurves)
        self.verticalLayout_8.setContentsMargins(-1, -1, 2, 0)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.formLayout_3 = QtGui.QFormLayout()
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.label = QtGui.QLabel(self.boxCurves)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.numberCurves = QtGui.QSpinBox(self.boxCurves)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.numberCurves.sizePolicy().hasHeightForWidth())
        self.numberCurves.setSizePolicy(sizePolicy)
        self.numberCurves.setMinimum(1)
        self.numberCurves.setMaximum(9999)
        self.numberCurves.setSingleStep(1)
        self.numberCurves.setProperty("value", 100)
        self.numberCurves.setObjectName(_fromUtf8("numberCurves"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.numberCurves)
        self.label_2 = QtGui.QLabel(self.boxCurves)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.curveWidthMin = QtGui.QDoubleSpinBox(self.boxCurves)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.curveWidthMin.sizePolicy().hasHeightForWidth())
        self.curveWidthMin.setSizePolicy(sizePolicy)
        self.curveWidthMin.setMaximum(1000.0)
        self.curveWidthMin.setSingleStep(0.1)
        self.curveWidthMin.setProperty("value", 0.1)
        self.curveWidthMin.setObjectName(_fromUtf8("curveWidthMin"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.FieldRole, self.curveWidthMin)
        self.label_3 = QtGui.QLabel(self.boxCurves)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.curveWidthMax = QtGui.QDoubleSpinBox(self.boxCurves)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.curveWidthMax.sizePolicy().hasHeightForWidth())
        self.curveWidthMax.setSizePolicy(sizePolicy)
        self.curveWidthMax.setToolTip(_fromUtf8(""))
        self.curveWidthMax.setMaximum(1000.0)
        self.curveWidthMax.setSingleStep(0.1)
        self.curveWidthMax.setProperty("value", 3.0)
        self.curveWidthMax.setObjectName(_fromUtf8("curveWidthMax"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.FieldRole, self.curveWidthMax)
        self.label_8 = QtGui.QLabel(self.boxCurves)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_8)
        self.nodeReduction = QtGui.QSpinBox(self.boxCurves)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nodeReduction.sizePolicy().hasHeightForWidth())
        self.nodeReduction.setSizePolicy(sizePolicy)
        self.nodeReduction.setMinimum(0)
        self.nodeReduction.setMaximum(100)
        self.nodeReduction.setSingleStep(1)
        self.nodeReduction.setProperty("value", 0)
        self.nodeReduction.setObjectName(_fromUtf8("nodeReduction"))
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.FieldRole, self.nodeReduction)
        self.label_10 = QtGui.QLabel(self.boxCurves)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.formLayout_3.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_10)
        self.curveStyle = QtGui.QComboBox(self.boxCurves)
        self.curveStyle.setObjectName(_fromUtf8("curveStyle"))
        self.curveStyle.addItem(_fromUtf8(""))
        self.curveStyle.addItem(_fromUtf8(""))
        self.curveStyle.addItem(_fromUtf8(""))
        self.curveStyle.addItem(_fromUtf8(""))
        self.curveStyle.addItem(_fromUtf8(""))
        self.formLayout_3.setWidget(4, QtGui.QFormLayout.FieldRole, self.curveStyle)
        self.verticalLayout_8.addLayout(self.formLayout_3)
        self.verticalLayout_5.addWidget(self.boxCurves)
        self.boxAdvancedPref = QtGui.QGroupBox(self.tabOptions)
        self.boxAdvancedPref.setFlat(True)
        self.boxAdvancedPref.setCheckable(True)
        self.boxAdvancedPref.setChecked(True)
        self.boxAdvancedPref.setObjectName(_fromUtf8("boxAdvancedPref"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.boxAdvancedPref)
        self.verticalLayout_7.setContentsMargins(14, -1, 0, 0)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.boxFunctions = QtGui.QGroupBox(self.boxAdvancedPref)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.boxFunctions.sizePolicy().hasHeightForWidth())
        self.boxFunctions.setSizePolicy(sizePolicy)
        self.boxFunctions.setFlat(True)
        self.boxFunctions.setCheckable(False)
        self.boxFunctions.setChecked(False)
        self.boxFunctions.setObjectName(_fromUtf8("boxFunctions"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.boxFunctions)
        self.horizontalLayout_2.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_1 = QtGui.QLabel(self.boxFunctions)
        self.label_1.setObjectName(_fromUtf8("label_1"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_1)
        self.resolution = QtGui.QDoubleSpinBox(self.boxFunctions)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resolution.sizePolicy().hasHeightForWidth())
        self.resolution.setSizePolicy(sizePolicy)
        self.resolution.setSingleStep(0.01)
        self.resolution.setProperty("value", 1.0)
        self.resolution.setObjectName(_fromUtf8("resolution"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.resolution)
        self.label_4 = QtGui.QLabel(self.boxFunctions)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_4)
        self.rangeMin = QtGui.QDoubleSpinBox(self.boxFunctions)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rangeMin.sizePolicy().hasHeightForWidth())
        self.rangeMin.setSizePolicy(sizePolicy)
        self.rangeMin.setDecimals(5)
        self.rangeMin.setMinimum(-1000.0)
        self.rangeMin.setMaximum(1000.0)
        self.rangeMin.setSingleStep(0.1)
        self.rangeMin.setProperty("value", -1.0)
        self.rangeMin.setObjectName(_fromUtf8("rangeMin"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.rangeMin)
        self.label_5 = QtGui.QLabel(self.boxFunctions)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_5)
        self.rangeMax = QtGui.QDoubleSpinBox(self.boxFunctions)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rangeMax.sizePolicy().hasHeightForWidth())
        self.rangeMax.setSizePolicy(sizePolicy)
        self.rangeMax.setDecimals(5)
        self.rangeMax.setMinimum(-1000.0)
        self.rangeMax.setMaximum(1000.0)
        self.rangeMax.setSingleStep(0.1)
        self.rangeMax.setProperty("value", 1.0)
        self.rangeMax.setObjectName(_fromUtf8("rangeMax"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.rangeMax)
        self.label_9 = QtGui.QLabel(self.boxFunctions)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_9)
        self.coordSystem = QtGui.QComboBox(self.boxFunctions)
        self.coordSystem.setObjectName(_fromUtf8("coordSystem"))
        self.coordSystem.addItem(_fromUtf8(""))
        self.coordSystem.addItem(_fromUtf8(""))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.coordSystem)
        self.label_6 = QtGui.QLabel(self.boxFunctions)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_6)
        self.lineEditX = QtGui.QLineEdit(self.boxFunctions)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditX.sizePolicy().hasHeightForWidth())
        self.lineEditX.setSizePolicy(sizePolicy)
        self.lineEditX.setText(_fromUtf8(""))
        self.lineEditX.setObjectName(_fromUtf8("lineEditX"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.lineEditX)
        self.label_7 = QtGui.QLabel(self.boxFunctions)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_7)
        self.lineEditY = QtGui.QLineEdit(self.boxFunctions)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditY.sizePolicy().hasHeightForWidth())
        self.lineEditY.setSizePolicy(sizePolicy)
        self.lineEditY.setToolTip(_fromUtf8(""))
        self.lineEditY.setText(_fromUtf8(""))
        self.lineEditY.setObjectName(_fromUtf8("lineEditY"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.lineEditY)
        self.horizontalLayout_2.addLayout(self.formLayout)
        self.verticalLayout_6.addWidget(self.boxFunctions)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
        self.verticalLayout_5.addWidget(self.boxAdvancedPref)
        self.boxInfo = QtGui.QGroupBox(self.tabOptions)
        self.boxInfo.setFlat(True)
        self.boxInfo.setObjectName(_fromUtf8("boxInfo"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.boxInfo)
        self.verticalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.labelObject = QtGui.QLabel(self.boxInfo)
        self.labelObject.setObjectName(_fromUtf8("labelObject"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.labelObject)
        self.labelNumberObject = QtGui.QLabel(self.boxInfo)
        self.labelNumberObject.setObjectName(_fromUtf8("labelNumberObject"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.labelNumberObject)
        self.labelNodes = QtGui.QLabel(self.boxInfo)
        self.labelNodes.setObjectName(_fromUtf8("labelNodes"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.labelNodes)
        self.labelNumberNodes = QtGui.QLabel(self.boxInfo)
        self.labelNumberNodes.setObjectName(_fromUtf8("labelNumberNodes"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.labelNumberNodes)
        self.verticalLayout_3.addLayout(self.formLayout_2)
        self.verticalLayout_5.addWidget(self.boxInfo)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem3)
        self.tabPreferences.addTab(self.tabOptions, _fromUtf8(""))
        self.tabInfo = QtGui.QWidget()
        self.tabInfo.setEnabled(True)
        self.tabInfo.setObjectName(_fromUtf8("tabInfo"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tabInfo)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.infoText = QtGui.QPlainTextEdit(self.tabInfo)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.infoText.sizePolicy().hasHeightForWidth())
        self.infoText.setSizePolicy(sizePolicy)
        self.infoText.setFrameShape(QtGui.QFrame.StyledPanel)
        self.infoText.setLineWidth(1)
        self.infoText.setPlainText(_fromUtf8(""))
        self.infoText.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.infoText.setBackgroundVisible(False)
        self.infoText.setCenterOnScroll(False)
        self.infoText.setObjectName(_fromUtf8("infoText"))
        self.verticalLayout_4.addWidget(self.infoText)
        self.tabPreferences.addTab(self.tabInfo, _fromUtf8(""))
        self.horizontalLayout.addWidget(self.splitter)
        self.verticalLayout.addWidget(self.frame)
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QtGui.QProgressBar.TopToBottom)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout.addWidget(self.progressBar)
        self.bottomPanel = QtGui.QHBoxLayout()
        self.bottomPanel.setObjectName(_fromUtf8("bottomPanel"))
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.bottomPanel.addItem(spacerItem4)
        self.buttonTrace = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonTrace.sizePolicy().hasHeightForWidth())
        self.buttonTrace.setSizePolicy(sizePolicy)
        self.buttonTrace.setAutoDefault(True)
        self.buttonTrace.setFlat(False)
        self.buttonTrace.setObjectName(_fromUtf8("buttonTrace"))
        self.bottomPanel.addWidget(self.buttonTrace)
        self.buttonSave = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonSave.sizePolicy().hasHeightForWidth())
        self.buttonSave.setSizePolicy(sizePolicy)
        self.buttonSave.setObjectName(_fromUtf8("buttonSave"))
        self.bottomPanel.addWidget(self.buttonSave)
        self.buttonHelp = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonHelp.sizePolicy().hasHeightForWidth())
        self.buttonHelp.setSizePolicy(sizePolicy)
        self.buttonHelp.setAutoDefault(False)
        self.buttonHelp.setObjectName(_fromUtf8("buttonHelp"))
        self.bottomPanel.addWidget(self.buttonHelp)
        self.bottomPanel.setStretch(0, 1)
        self.verticalLayout.addLayout(self.bottomPanel)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 885, 18))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menu_View = QtGui.QMenu(self.menubar)
        self.menu_View.setObjectName(_fromUtf8("menu_View"))
        MainWindow.setMenuBar(self.menubar)
        self.actionOpenBitmap = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpenBitmap.setIcon(icon1)
        self.actionOpenBitmap.setMenuRole(QtGui.QAction.NoRole)
        self.actionOpenBitmap.setObjectName(_fromUtf8("actionOpenBitmap"))
        self.actionSaveAs = QtGui.QAction(MainWindow)
        self.actionSaveAs.setObjectName(_fromUtf8("actionSaveAs"))
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setMenuRole(QtGui.QAction.QuitRole)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setMenuRole(QtGui.QAction.AboutRole)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionAboutQt = QtGui.QAction(MainWindow)
        self.actionAboutQt.setObjectName(_fromUtf8("actionAboutQt"))
        self.actionBackground = QtGui.QAction(MainWindow)
        self.actionBackground.setCheckable(True)
        self.actionBackground.setChecked(True)
        self.actionBackground.setObjectName(_fromUtf8("actionBackground"))
        self.actionBorder = QtGui.QAction(MainWindow)
        self.actionBorder.setCheckable(True)
        self.actionBorder.setChecked(True)
        self.actionBorder.setObjectName(_fromUtf8("actionBorder"))
        self.actionLoadPreset = QtGui.QAction(MainWindow)
        self.actionLoadPreset.setObjectName(_fromUtf8("actionLoadPreset"))
        self.actionSavePreset = QtGui.QAction(MainWindow)
        self.actionSavePreset.setObjectName(_fromUtf8("actionSavePreset"))
        self.actionTraceImage = QtGui.QAction(MainWindow)
        self.actionTraceImage.setCheckable(True)
        self.actionTraceImage.setChecked(True)
        self.actionTraceImage.setObjectName(_fromUtf8("actionTraceImage"))
        self.menuFile.addAction(self.actionOpenBitmap)
        self.menuFile.addAction(self.actionSaveAs)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionLoadPreset)
        self.menuFile.addAction(self.actionSavePreset)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionAboutQt)
        self.menu_View.addAction(self.actionBackground)
        self.menu_View.addAction(self.actionBorder)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menu_View.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.previewMode.setCurrentIndex(0)
        self.tabPreferences.setCurrentIndex(0)
        QtCore.QObject.connect(self.boxAdvancedPref, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.boxFunctions.setVisible)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.numberCurves, self.curveWidthMin)
        MainWindow.setTabOrder(self.curveWidthMin, self.curveWidthMax)
        MainWindow.setTabOrder(self.curveWidthMax, self.nodeReduction)
        MainWindow.setTabOrder(self.nodeReduction, self.curveStyle)
        MainWindow.setTabOrder(self.curveStyle, self.boxAdvancedPref)
        MainWindow.setTabOrder(self.boxAdvancedPref, self.resolution)
        MainWindow.setTabOrder(self.resolution, self.rangeMin)
        MainWindow.setTabOrder(self.rangeMin, self.rangeMax)
        MainWindow.setTabOrder(self.rangeMax, self.coordSystem)
        MainWindow.setTabOrder(self.coordSystem, self.lineEditX)
        MainWindow.setTabOrder(self.lineEditX, self.lineEditY)
        MainWindow.setTabOrder(self.lineEditY, self.buttonTrace)
        MainWindow.setTabOrder(self.buttonTrace, self.buttonSave)
        MainWindow.setTabOrder(self.buttonSave, self.buttonHelp)
        MainWindow.setTabOrder(self.buttonHelp, self.previewMode)
        MainWindow.setTabOrder(self.previewMode, self.sliderTransparency)
        MainWindow.setTabOrder(self.sliderTransparency, self.tabPreferences)
        MainWindow.setTabOrder(self.tabPreferences, self.infoText)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "ZebraTRACE", None, QtGui.QApplication.UnicodeUTF8))
        self.labelPreview.setText(QtGui.QApplication.translate("MainWindow", "Preview:", None, QtGui.QApplication.UnicodeUTF8))
        self.previewMode.setItemText(0, QtGui.QApplication.translate("MainWindow", "Tracing Result", None, QtGui.QApplication.UnicodeUTF8))
        self.previewMode.setItemText(1, QtGui.QApplication.translate("MainWindow", "Wireframe Overlay", None, QtGui.QApplication.UnicodeUTF8))
        self.labelTransparency.setText(QtGui.QApplication.translate("MainWindow", "Transparency:", None, QtGui.QApplication.UnicodeUTF8))
        self.sliderTransparency.setToolTip(QtGui.QApplication.translate("MainWindow", "Transparent bitmap layer", None, QtGui.QApplication.UnicodeUTF8))
        self.boxCurves.setTitle(QtGui.QApplication.translate("MainWindow", " Curves", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Number of Curves (<b>n</b>):", None, QtGui.QApplication.UnicodeUTF8))
        self.numberCurves.setToolTip(QtGui.QApplication.translate("MainWindow", "<b>i</b> = 1... <b>n</b>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Minimum Width:", None, QtGui.QApplication.UnicodeUTF8))
        self.curveWidthMin.setToolTip(QtGui.QApplication.translate("MainWindow", "In SVG resolution units (number of \"SVG units per pixel\"), which is close to 1px of bitmap per resolution unit", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Maximum Width:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "Node Reduction:", None, QtGui.QApplication.UnicodeUTF8))
        self.nodeReduction.setToolTip(QtGui.QApplication.translate("MainWindow", "Node reduction tolerance", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("MainWindow", "Style:", None, QtGui.QApplication.UnicodeUTF8))
        self.curveStyle.setItemText(0, QtGui.QApplication.translate("MainWindow", "Center Line", None, QtGui.QApplication.UnicodeUTF8))
        self.curveStyle.setItemText(1, QtGui.QApplication.translate("MainWindow", "Left End", None, QtGui.QApplication.UnicodeUTF8))
        self.curveStyle.setItemText(2, QtGui.QApplication.translate("MainWindow", "Right End", None, QtGui.QApplication.UnicodeUTF8))
        self.curveStyle.setItemText(3, QtGui.QApplication.translate("MainWindow", "Left Line", None, QtGui.QApplication.UnicodeUTF8))
        self.curveStyle.setItemText(4, QtGui.QApplication.translate("MainWindow", "Right Line", None, QtGui.QApplication.UnicodeUTF8))
        self.boxAdvancedPref.setTitle(QtGui.QApplication.translate("MainWindow", "Advanced", None, QtGui.QApplication.UnicodeUTF8))
        self.boxFunctions.setTitle(QtGui.QApplication.translate("MainWindow", "Functions", None, QtGui.QApplication.UnicodeUTF8))
        self.label_1.setText(QtGui.QApplication.translate("MainWindow", "Resolution:", None, QtGui.QApplication.UnicodeUTF8))
        self.resolution.setToolTip(QtGui.QApplication.translate("MainWindow", "\"Number of nodes to calculate per 1 curve\" = k * \"bitmap width\" * resolution, where \"k\" is variable (a) range to SVG viewbox width ratio (k=1, generally)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Min (<b>a</b>) value:", None, QtGui.QApplication.UnicodeUTF8))
        self.rangeMin.setToolTip(QtGui.QApplication.translate("MainWindow", "Minimum value for (a) variable", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Max (<b>a</b>) value:", None, QtGui.QApplication.UnicodeUTF8))
        self.rangeMax.setToolTip(QtGui.QApplication.translate("MainWindow", "Maximum value for (a) variable", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("MainWindow", "Coordinates:", None, QtGui.QApplication.UnicodeUTF8))
        self.coordSystem.setItemText(0, QtGui.QApplication.translate("MainWindow", "Cartesian", None, QtGui.QApplication.UnicodeUTF8))
        self.coordSystem.setItemText(1, QtGui.QApplication.translate("MainWindow", "Polar", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Function <b>X(a)</b>:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditX.setToolTip(QtGui.QApplication.translate("MainWindow", "Use (a),( i) and (n) as parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "Function <b>Y(a)</b>:", None, QtGui.QApplication.UnicodeUTF8))
        self.boxInfo.setTitle(QtGui.QApplication.translate("MainWindow", "Trace result details", None, QtGui.QApplication.UnicodeUTF8))
        self.labelObject.setText(QtGui.QApplication.translate("MainWindow", "Paths:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelNumberObject.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.labelNodes.setText(QtGui.QApplication.translate("MainWindow", "Nodes:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelNumberNodes.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.tabPreferences.setTabText(self.tabPreferences.indexOf(self.tabOptions), QtGui.QApplication.translate("MainWindow", "Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.tabPreferences.setTabText(self.tabPreferences.indexOf(self.tabInfo), QtGui.QApplication.translate("MainWindow", "Info", None, QtGui.QApplication.UnicodeUTF8))
        self.progressBar.setFormat(QtGui.QApplication.translate("MainWindow", "%p%", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonTrace.setToolTip(QtGui.QApplication.translate("MainWindow", "Trace the raster content", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonTrace.setText(QtGui.QApplication.translate("MainWindow", "Trace", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonTrace.setShortcut(QtGui.QApplication.translate("MainWindow", "Return", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonSave.setToolTip(QtGui.QApplication.translate("MainWindow", "Save trace result to a file", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonSave.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonHelp.setText(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_View.setTitle(QtGui.QApplication.translate("MainWindow", "&View", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpenBitmap.setText(QtGui.QApplication.translate("MainWindow", "Open Bitmap...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveAs.setText(QtGui.QApplication.translate("MainWindow", "Save &As...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+X", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAboutQt.setText(QtGui.QApplication.translate("MainWindow", "About Qt", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBackground.setText(QtGui.QApplication.translate("MainWindow", "&Background", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBorder.setText(QtGui.QApplication.translate("MainWindow", "Border &Frame", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoadPreset.setText(QtGui.QApplication.translate("MainWindow", "Load Preset...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSavePreset.setText(QtGui.QApplication.translate("MainWindow", "Save Preset...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTraceImage.setText(QtGui.QApplication.translate("MainWindow", "Trace Image", None, QtGui.QApplication.UnicodeUTF8))

import mainwindow_rc
