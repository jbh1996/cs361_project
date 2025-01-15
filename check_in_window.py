# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFormLayout, QHeaderView,
    QLabel, QMainWindow, QMenuBar, QSizePolicy,
    QStatusBar, QTabWidget, QTableView, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1276, 1019)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(-20, 0, 1281, 961))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tableView = QTableView(self.tab)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(350, 10, 591, 881))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.formLayoutWidget = QWidget(self.tab_2)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(240, 100, 671, 531))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignmentFlag.AlignCenter)
        self.formLayout.setContentsMargins(0, 4, 0, 0)
        self.checkBox = QCheckBox(self.formLayoutWidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.checkBox.setIconSize(QSize(50, 50))

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.checkBox)

        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.checkBox_2 = QCheckBox(self.formLayoutWidget)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.checkBox_2)

        self.label_4 = QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.checkBox_3 = QCheckBox(self.formLayoutWidget)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.checkBox_3)

        self.label_3 = QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_3)

        self.checkBox_4 = QCheckBox(self.formLayoutWidget)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.checkBox_4)

        self.label_5 = QLabel(self.formLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_5)

        self.checkBox_5 = QCheckBox(self.formLayoutWidget)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.checkBox_5)

        self.label_6 = QLabel(self.formLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_6)

        self.checkBox_6 = QCheckBox(self.formLayoutWidget)
        self.checkBox_6.setObjectName(u"checkBox_6")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.checkBox_6)

        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1276, 42))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Check In Progress by Group", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Check In Sheet", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Export and Close", None))
    # retranslateUi

