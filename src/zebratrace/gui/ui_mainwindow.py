# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_build\mainwindow.ui'
#
# Created: Tue Dec 25 22:02:53 2012
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
        MainWindow.resize(892, 631)
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
        self.tabPreferences.setMinimumSize(QtCore.QSize(280, 0))
        self.tabPreferences.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tabPreferences.setTabPosition(QtGui.QTabWidget.North)
        self.tabPreferences.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabPreferences.setElideMode(QtCore.Qt.ElideMiddle)
        self.tabPreferences.setObjectName(_fromUtf8("tabPreferences"))
        self.tabOptions = QtGui.QWidget()
        self.tabOptions.setObjectName(_fromUtf8("tabOptions"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.tabOptions)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.groupBox_2 = QtGui.QGroupBox(self.tabOptions)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setCheckable(False)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.numberCurves = QtGui.QSpinBox(self.groupBox_2)
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
        self.gridLayout.addWidget(self.numberCurves, 0, 1, 1, 1)
        self.label_1 = QtGui.QLabel(self.groupBox_2)
        self.label_1.setObjectName(_fromUtf8("label_1"))
        self.gridLayout.addWidget(self.label_1, 1, 0, 1, 1)
        self.curveResolution = QtGui.QDoubleSpinBox(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.curveResolution.sizePolicy().hasHeightForWidth())
        self.curveResolution.setSizePolicy(sizePolicy)
        self.curveResolution.setSingleStep(0.01)
        self.curveResolution.setProperty("value", 1.0)
        self.curveResolution.setObjectName(_fromUtf8("curveResolution"))
        self.gridLayout.addWidget(self.curveResolution, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.curveWidthMin = QtGui.QDoubleSpinBox(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.curveWidthMin.sizePolicy().hasHeightForWidth())
        self.curveWidthMin.setSizePolicy(sizePolicy)
        self.curveWidthMin.setMaximum(1000.0)
        self.curveWidthMin.setSingleStep(0.1)
        self.curveWidthMin.setProperty("value", 0.1)
        self.curveWidthMin.setObjectName(_fromUtf8("curveWidthMin"))
        self.gridLayout.addWidget(self.curveWidthMin, 2, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.curveWidthMax = QtGui.QDoubleSpinBox(self.groupBox_2)
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
        self.gridLayout.addWidget(self.curveWidthMax, 3, 1, 1, 1)
        self.label_8 = QtGui.QLabel(self.groupBox_2)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 4, 0, 1, 1)
        self.nodeReduction = QtGui.QSpinBox(self.groupBox_2)
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
        self.gridLayout.addWidget(self.nodeReduction, 4, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 3)
        self.horizontalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout_5.addWidget(self.groupBox_2)
        self.groupBox_3 = QtGui.QGroupBox(self.tabOptions)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_4 = QtGui.QLabel(self.groupBox_3)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.rangeMin = QtGui.QDoubleSpinBox(self.groupBox_3)
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
        self.gridLayout_2.addWidget(self.rangeMin, 0, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.groupBox_3)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)
        self.rangeMax = QtGui.QDoubleSpinBox(self.groupBox_3)
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
        self.gridLayout_2.addWidget(self.rangeMax, 1, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox_3)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1)
        self.lineEditX = QtGui.QLineEdit(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditX.sizePolicy().hasHeightForWidth())
        self.lineEditX.setSizePolicy(sizePolicy)
        self.lineEditX.setText(_fromUtf8(""))
        self.lineEditX.setObjectName(_fromUtf8("lineEditX"))
        self.gridLayout_2.addWidget(self.lineEditX, 2, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.groupBox_3)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_2.addWidget(self.label_7, 3, 0, 1, 1)
        self.lineEditY = QtGui.QLineEdit(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditY.sizePolicy().hasHeightForWidth())
        self.lineEditY.setSizePolicy(sizePolicy)
        self.lineEditY.setToolTip(_fromUtf8(""))
        self.lineEditY.setText(_fromUtf8(""))
        self.lineEditY.setObjectName(_fromUtf8("lineEditY"))
        self.gridLayout_2.addWidget(self.lineEditY, 3, 1, 1, 1)
        self.checkBox = QtGui.QCheckBox(self.groupBox_3)
        self.checkBox.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.gridLayout_2.addWidget(self.checkBox, 4, 1, 1, 1)
        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 3)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.verticalLayout_5.addWidget(self.groupBox_3)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem3)
        self.tabPreferences.addTab(self.tabOptions, _fromUtf8(""))
        self.tabInfo = QtGui.QWidget()
        self.tabInfo.setEnabled(True)
        self.tabInfo.setObjectName(_fromUtf8("tabInfo"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tabInfo)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.groupBox = QtGui.QGroupBox(self.tabInfo)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.infoText = QtGui.QPlainTextEdit(self.groupBox)
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
        self.verticalLayout_3.addWidget(self.infoText)
        self.verticalLayout_4.addWidget(self.groupBox)
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
        self.menubar.setGeometry(QtCore.QRect(0, 0, 892, 18))
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
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.numberCurves, self.curveResolution)
        MainWindow.setTabOrder(self.curveResolution, self.curveWidthMin)
        MainWindow.setTabOrder(self.curveWidthMin, self.curveWidthMax)
        MainWindow.setTabOrder(self.curveWidthMax, self.nodeReduction)
        MainWindow.setTabOrder(self.nodeReduction, self.rangeMin)
        MainWindow.setTabOrder(self.rangeMin, self.rangeMax)
        MainWindow.setTabOrder(self.rangeMax, self.lineEditX)
        MainWindow.setTabOrder(self.lineEditX, self.lineEditY)
        MainWindow.setTabOrder(self.lineEditY, self.checkBox)
        MainWindow.setTabOrder(self.checkBox, self.buttonTrace)
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
        self.groupBox_2.setTitle(QtGui.QApplication.translate("MainWindow", " Curves:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Number of Curves (<b>n</b>):", None, QtGui.QApplication.UnicodeUTF8))
        self.numberCurves.setToolTip(QtGui.QApplication.translate("MainWindow", "<b>i</b> = 1... <b>n</b>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_1.setText(QtGui.QApplication.translate("MainWindow", "Resolution:", None, QtGui.QApplication.UnicodeUTF8))
        self.curveResolution.setToolTip(QtGui.QApplication.translate("MainWindow", "\"Number of nodes to calculate per 1 curve\" = k * \"bitmap width\" * resolution, where \"k\" is variable (a) range to SVG viewbox width ratio (k=1, generally)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Min Line Width:", None, QtGui.QApplication.UnicodeUTF8))
        self.curveWidthMin.setToolTip(QtGui.QApplication.translate("MainWindow", "In SVG resolution units (number of \"SVG units per pixel\"), which is close to 1px of bitmap per resolution unit", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Max Line Width:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "Node Reduction:", None, QtGui.QApplication.UnicodeUTF8))
        self.nodeReduction.setToolTip(QtGui.QApplication.translate("MainWindow", "Node reduction tolerance", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("MainWindow", "Functions:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Min (<b>a</b>) value:", None, QtGui.QApplication.UnicodeUTF8))
        self.rangeMin.setToolTip(QtGui.QApplication.translate("MainWindow", "Minimum value for (a) variable", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Max (<b>a</b>) value:", None, QtGui.QApplication.UnicodeUTF8))
        self.rangeMax.setToolTip(QtGui.QApplication.translate("MainWindow", "Maximum value for (a) variable", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Function <b>X(a)</b>:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditX.setToolTip(QtGui.QApplication.translate("MainWindow", "Use (a),( i) and (n) as parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "Function <b>Y(a)</b>:", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setToolTip(QtGui.QApplication.translate("MainWindow", "Function X(a) means function of radius and Y(a) means function of angle in polar coordinates", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("MainWindow", "Polar Coordinates", None, QtGui.QApplication.UnicodeUTF8))
        self.tabPreferences.setTabText(self.tabPreferences.indexOf(self.tabOptions), QtGui.QApplication.translate("MainWindow", "Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Trace Information:", None, QtGui.QApplication.UnicodeUTF8))
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
