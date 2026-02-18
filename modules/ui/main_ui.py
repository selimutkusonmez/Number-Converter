import sys
from PyQt6.QtCore import Qt,QRegularExpression,QSize
from PyQt6.QtWidgets import (
     QApplication,QWidget,QMainWindow,QLineEdit,QPushButton,QTextEdit,QLabel,QGridLayout,QFrame,QTableWidget,QTableWidgetItem,QGroupBox,QComboBox,QMessageBox,QFileDialog,QListWidget,QTabWidget,QVBoxLayout,QStatusBar,QSizePolicy,QHBoxLayout)
from PyQt6.QtGui import QIcon,QPixmap,QIntValidator,QDoubleValidator,QRegularExpressionValidator,QKeyEvent,QPainter,QFontDatabase,QFont

from modules.assets.style.style_reader import read_style

class MainUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):

        self.setWindowTitle("Binary Converter")
        self.setFixedSize(500,300)

        self.main_ui_central_widget = QWidget()
        self.setCentralWidget(self.main_ui_central_widget)
        self.main_ui_central_widget_layout = QGridLayout()
        self.main_ui_central_widget.setLayout(self.main_ui_central_widget_layout)

        self.label = QLabel("NUMBER CONVERTER")
        self.label.setObjectName("main_label")
        self.main_ui_central_widget_layout.addWidget(self.label,0,0,Qt.AlignmentFlag.AlignCenter)

        self.upper_groupbox = QGroupBox("Input")
        self.upper_groupbox.setFixedHeight(125)
        self.upper_groupbox.setProperty("class","groupbox")
        self.setObjectName("upper_groupbox")
        self.upper_groupbox_layout = QHBoxLayout()
        self.upper_groupbox.setLayout(self.upper_groupbox_layout)
        self.main_ui_central_widget_layout.addWidget(self.upper_groupbox,1,0)

        self.input_1_label = QComboBox()
        self.input_1_label.setFixedWidth(100)
        self.input_1_label.addItems(["Binary","Decimal","Hexadecimal","Octal"])
        self.upper_groupbox_layout.addWidget(self.input_1_label)

        self.input_1 = QLineEdit()
        self.input_1.setObjectName("input")
        self.input_1.setPlaceholderText("Default : Binary")
        self.upper_groupbox_layout.addWidget(self.input_1,3)

        self.convert_button = QPushButton("Convert")
        self.upper_groupbox_layout.addWidget(self.convert_button,1)

        self.lower_groupbox = QGroupBox("Output")
        self.lower_groupbox.setProperty("class","groupbox")
        self.setObjectName("lower_groupbox")
        self.lower_groupbox.setFixedHeight(100)
        self.lower_groupbox_layout = QGridLayout()
        self.lower_groupbox.setLayout(self.lower_groupbox_layout)
        self.main_ui_central_widget_layout.addWidget(self.lower_groupbox,2,0)
        self.lower_groupbox_layout.setVerticalSpacing(1)

        self.output_1_label = QLabel("Decimal")
        self.output_1_label.setProperty("class","label")
        self.lower_groupbox_layout.addWidget(self.output_1_label,0,0,Qt.AlignmentFlag.AlignCenter)

        self.output_1 = QLineEdit()
        self.output_1.setReadOnly(True)
        self.output_1.setProperty("class","output")
        self.lower_groupbox_layout.addWidget(self.output_1,1,0)

        self.output_2_label = QLabel("Hexadecimal")
        self.output_2_label.setProperty("class","label")
        self.lower_groupbox_layout.addWidget(self.output_2_label,0,1,Qt.AlignmentFlag.AlignCenter)

        self.output_2 = QLineEdit()
        self.output_2.setReadOnly(True)
        self.output_2.setProperty("class","output")
        self.lower_groupbox_layout.addWidget(self.output_2,1,1)

        self.output_3_label = QLabel("Octal")
        self.output_3_label.setProperty("class","label")
        self.lower_groupbox_layout.addWidget(self.output_3_label,0,2,Qt.AlignmentFlag.AlignCenter)

        self.output_3 = QLineEdit()
        self.output_3.setReadOnly(True)
        self.output_3.setProperty("class","output")
        self.lower_groupbox_layout.addWidget(self.output_3,1,2)

        self.setStatusBar(QStatusBar())
        self.statusBar().showMessage("App Ready")

        self.setStyleSheet(read_style("main_ui.qss"))

        