from PyQt6.QtWidgets import QMainWindow, QListWidget, QVBoxLayout, QHBoxLayout, QPushButton, QWidget
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QAction, QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setFixedSize(QSize(400, 300))
        self.selected_option = None

        load_save_action = QAction("&Load Save", self)
        load_save_action.setStatusTip("Load a backup save file.")
        load_save_action.setCheckable(True)
        
        save_action = QAction("&Save", self)
        save_action.setStatusTip("Save this game.")
        save_action.setCheckable(True)
        
        save_as_action = QAction("Save &As", self)
        save_as_action.setStatusTip("Save this game elsewhere.")
        save_as_action.setCheckable(True)
        
        menu = self.menuBar()
        file_menu = menu.addMenu("&File")
        file_menu.addAction(load_save_action)
        file_menu.addAction(save_action)
        file_menu.addAction(save_as_action)
        
        layout = QVBoxLayout()
        self.log = QListWidget()
        
        secondary_layout = QHBoxLayout()
        self.options = QListWidget()
        self.options.itemSelectionChanged.connect(self.__set_selected_option__)
        self.submit = QPushButton(text="Go")
        
        secondary_layout.addWidget(self.options)
        secondary_layout.addWidget(self.submit)
        layout.addWidget(self.log)
        layout.addLayout(secondary_layout)
        
        self.setWindowTitle("World War Alpaca")

        root = QWidget()
        root.setLayout(layout)
        self.setCentralWidget(root)
        
        self.__set_options__(["Hello", "Bonsoir"], self.loop)
        
    def __add_entry__(self, entry_text):
        self.log.addItem(entry_text)
        
    def __set_options__(self, options: list, callback):
        self.options.clear()
        self.options.addItems(options)
        self.submit.clicked.connect(callback)
    
    def __set_selected_option__(self):
        item = self.options.currentItem()
        if item is not None:
            self.selected_option = item.text()
            
    def __get__selected_option(self):
        self.options.clearSelection()
        option = self.selected_option
        self.selected_option = None
        return option
    
    def loop(self):
        self.__add_entry__(self.__get__selected_option())
            
        self.__set_options__(["Hello", "Bonsoir"], self.loop)
        
        