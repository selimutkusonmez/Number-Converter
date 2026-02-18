import sys
import subprocess
from PyQt6.QtCore import Qt,QRegularExpression,QSize
from PyQt6.QtWidgets import (
     QApplication,QWidget,QMainWindow,QLineEdit,QPushButton,QTextEdit,QLabel,QGridLayout,QFrame,QTableWidget,QTableWidgetItem,QGroupBox,QComboBox,QMessageBox,QFileDialog,QListWidget,QTabWidget,QVBoxLayout,QStatusBar,QSizePolicy,QHBoxLayout)
from PyQt6.QtGui import QIcon,QPixmap,QIntValidator,QDoubleValidator,QRegularExpressionValidator,QKeyEvent,QPainter,QFontDatabase,QFont,QAction,QActionGroup

from modules.assets.style.style_reader import read_style
from modules.logic.converter import converter
from modules.logic.label_replacer import label_replacer
from config import JPG_PATH

class MainUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.light_theme_action_function()
        self.input_1_label_currenttext_changed()
    
    def init_ui(self):

        self.setWindowIcon(QIcon(JPG_PATH))

        self.setWindowTitle("Binary Converter")
        self.setFixedSize(500,300)

        self.main_ui_central_widget = QWidget()
        self.setCentralWidget(self.main_ui_central_widget)

        self.main_ui_central_widget_layout = QGridLayout()
        self.main_ui_central_widget.setLayout(self.main_ui_central_widget_layout)

        self.label = QLabel("NUMBER CONVERTER")
        self.label.setObjectName("main_label")
        self.main_ui_central_widget_layout.addWidget(self.label,0,0,Qt.AlignmentFlag.AlignCenter)

        #Upper Groupbox
        self.upper_groupbox = QGroupBox("Input")
        self.upper_groupbox.setFixedHeight(125)
        self.upper_groupbox.setProperty("class","groupbox")
        self.setObjectName("upper_groupbox")

        self.upper_groupbox_layout = QHBoxLayout()
        self.upper_groupbox.setLayout(self.upper_groupbox_layout)
        self.main_ui_central_widget_layout.addWidget(self.upper_groupbox,1,0)

        self.input_1_label = QComboBox()
        self.input_1_label.setFixedWidth(100)
        self.input_1_label.addItems(["Binary","Decimal","Octal","Hex"])
        self.input_1_label.currentTextChanged.connect(self.input_1_label_currenttext_changed)
        self.upper_groupbox_layout.addWidget(self.input_1_label)

        self.input_1 = QLineEdit()
        self.input_1.setObjectName("input")
        self.input_1.setPlaceholderText("Default : Binary")
        self.upper_groupbox_layout.addWidget(self.input_1,3)

        self.convert_button = QPushButton("Convert")
        self.convert_button.clicked.connect(self.convert_button_function)
        self.upper_groupbox_layout.addWidget(self.convert_button,1)

        #Lower Groupbox
        self.lower_groupbox = QGroupBox("Output")
        self.lower_groupbox.setProperty("class","groupbox")
        self.setObjectName("lower_groupbox")
        self.lower_groupbox.setFixedHeight(100)

        self.lower_groupbox_layout = QGridLayout()
        self.lower_groupbox.setLayout(self.lower_groupbox_layout)
        self.main_ui_central_widget_layout.addWidget(self.lower_groupbox,2,0)

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

        #MenuBar
        menu_bar = self.menuBar()

        #File Menu
        file_menu = menu_bar.addMenu("File")
        restart_app_action = QAction("Restart App",self)
        restart_app_action.setShortcut("Ctrl+R")
        restart_app_action.triggered.connect(self.restart_app_action_function)
        file_menu.addAction(restart_app_action)

        #Settings Menu
        settings_menu = menu_bar.addMenu("Settings")
        theme_menu = settings_menu.addMenu("Theme")
        theme_action_group = QActionGroup(self)

        light_theme_action = QAction("Light Theme")
        light_theme_action.setShortcut("Ctrl+L")
        light_theme_action.setChecked(True)
        light_theme_action.setCheckable(True)
        theme_menu.addAction(light_theme_action)
        theme_action_group.addAction(light_theme_action)
        light_theme_action.triggered.connect(self.light_theme_action_function)

        dark_theme_action = QAction("Dark Theme")
        dark_theme_action.setShortcut("Ctrl+D")
        dark_theme_action.setCheckable(True)
        theme_menu.addAction(dark_theme_action)
        theme_action_group.addAction(dark_theme_action)
        dark_theme_action.triggered.connect(self.dark_theme_action_function)

    def restart_app_action_function(self):
        QApplication.quit()
        subprocess.Popen([sys.executable, *sys.argv])
    
    def dark_theme_action_function(self):
        self.setStyleSheet(read_style("main_ui_dark_theme.qss"))

    def light_theme_action_function(self):
        self.setStyleSheet(read_style("main_ui_light_theme.qss"))

    def input_1_label_currenttext_changed(self):
        label_1,label_2,label_3,regex = label_replacer(self.input_1_label.currentText())
        self.input_1.setValidator(regex)
        self.output_1_label.setText(label_1)
        self.output_2_label.setText(label_2)
        self.output_3_label.setText(label_3)
        self.input_1.setText("")
        self.output_1.setText("")
        self.output_2.setText("")
        self.output_3.setText("")
        self.statusBar().showMessage(self.input_1_label.currentText())

    def convert_button_function(self):
        output_1,output_2,output_3 = converter(self.input_1_label.currentText(),self.input_1.text())
        self.output_1.setText(output_1)
        self.output_2.setText(output_2)
        self.output_3.setText(output_3)

        self.statusBar().showMessage("Number converted")