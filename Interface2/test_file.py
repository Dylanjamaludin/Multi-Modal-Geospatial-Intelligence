from component_file import*
from chatbox_file import *
from PyQt6.QtGui import QPixmap, QPicture
class MainWindow (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Test Window")
        self.setMinimumSize(1000,600)
        self.setStyleSheet('''
        QMainWindow
        {
            background-color: #494949;
        }
        QMainWindow::separator 
        {
            width:1px;
            background-color: #494949;
        }
        ''')
        font1 = QFont('Arial')
        font1.setPixelSize(13)
        font1.setWeight(1000)
        font2 = QFont('Arial')
        font2.setPixelSize(13)

        layout = QVBoxLayout()

        self.titlebar = TitleBar("Chat Box")

        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.addWidget(self.titlebar)

        chatbox_frame = QFrame()
        self.chatbox_layout = QVBoxLayout(chatbox_frame)
        chatbox_frame.setLayout(self.chatbox_layout)
        chatbox_frame.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.chatbox_layout.setContentsMargins(0,12,0,0)
        self.chatbox_layout.setSpacing(0)
        chatbox_frame.setStyleSheet('''
        QFrame {
            background: #202020;
            border: 2px solid #494949;
            border-radius:10px;
        }
            ''')
        icon1 = QIcon('feather(2.5px)/globe.svg')
        icon2 = QIcon('feather(2.5px)/globe.svg')
        icon3 = QIcon('feather(2.5px)/globe.svg')

        #self.tabs = TabWidget(parent=None)
        self.tabs = TabWidget(parent=None)
        # self.tabs.setTabsClosable(False)
        # self.tabs.tabCloseRequested.connect(lambda index: self.tabs.removeTab(index))
        # self.closeButton = icon_button(icon_square_len=16, button_square_len=28,exit=True)
        # self.closeButton1 = icon_button(icon_square_len=16, button_square_len=28, exit=True)
        # self.closeButton2 = icon_button(icon_square_len=16, button_square_len=28, exit=True)
        #
        # self.addButton = icon_button(icon_square_len=16, button_square_len=28, initial_icon='feather(3px)/plus.svg')
        #
        # self.tabs.setCornerWidget(self.addButton,Qt.Corner.TopLeftCorner)


        # tab = QWidget(parent=None)
        # self.tabs.addTab(tab, icon1, 'Test 1')
        # tab2 = QWidget()
        # self.tabs.tabBar().setTabButton(0, QTabBar.ButtonPosition.RightSide, self.closeButton)
        # self.tabs.addTab(tab2,icon2,  'Test 2')
        # self.tabs.tabBar().setTabButton(1, QTabBar.ButtonPosition.RightSide, self.closeButton1)
        # tab3 = QWidget()
        # self.tabs.addTab(tab3,icon3,  'Test 3')
        # self.tabs.tabBar().setTabButton(2, QTabBar.ButtonPosition.RightSide, self.closeButton2)



        #layout.addWidget(self.tabs)
        self.chatbox_layout.addWidget(self.tabs)

        # self.chatbox_input_layout = QHBoxLayout()
        # self.chatbox_input_clip_button = icon_button(initial_icon='feather/paperclip.svg')
        # self.chatbox_input_send_button = icon_button(initial_icon='feather/send.svg')
        # self.chatbox_input_lineEdit = LineEdit()
        # self.chatbox_input_lineEdit.setPlaceholderText('Type Here!')
        #
        # self.chatbox_input_layout.addWidget(self.chatbox_input_clip_button)
        # self.chatbox_input_layout.addWidget( self.chatbox_input_lineEdit)
        # self.chatbox_input_layout.addWidget(self.chatbox_input_send_button)

        self.test = DockTitleBar('test')
        self.test2 = TitleBar("test")
        layout.addWidget(self.test)
        layout.addWidget(self.test2)

        testF = QFrame()
        testF.setObjectName('frameTest')
        testF.setFixedSize(40,40)
        testF.setStyleSheet('''
        #frameTest{
            background: #202020;
            border: 2px solid #2d2d2d;
            border-radius:20px;}
        ''')
        testF_layout= QHBoxLayout()
        testF_layout.setContentsMargins(0,0,0,0)
        testF_layout.setSpacing(0)

        testF_icon = QLabel()
        testF_icon.setAlignment(Qt.AlignmentFlag.AlignCenter)
        icon5 = QIcon("feather(2.5px)/user.svg").pixmap(QSize(24, 24))
        testF_icon.setPixmap(icon5)

        testF_layout.addWidget(testF_icon)
        test2 = icon_button(initial_icon='feather(2.5px)/user.svg', icon_square_len=24, button_square_len=40)
        test2.setDisabled(True)
        testF.setLayout(testF_layout)

        #test slider
        test1 = Slider(Qt.Orientation.Horizontal)
        test1.setMinimum(0)
        test1.setMaximum(10)

        layout.addWidget(test1)
        
        # self.label = Label("Test")
        # self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # #self.label.setSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        # self.label2 = QLabel("Test")
        # self.label2.setAlignment(Qt.AlignmentFlag.AlignLeft)
        # self.label2.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        # layout.addWidget(self.label)
        # layout.addWidget(self.label2)

        #self.chatbox_layout.addLayout(self.chatbox_input_layout)

        layout.addWidget(chatbox_frame)

        widget = QWidget()
        widget.setLayout(layout)
        #widget.setLayout(self.mainLayout)
        self.setCentralWidget(widget)

        placeholder = QLabel("Test")
        placeholder2 = QLabel("Test")
        placeholder3 = QLabel("Test")

        self.dockwidget = DockWidget('Dock', placeholder)
        self.dockwidget2 = DockWidget('Dock', placeholder2)
        self.dockwidget3 = DockWidget('Dock', placeholder3)

        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.dockwidget)
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.dockwidget2)
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea,self.dockwidget3)

app = QApplication(sys.argv)
window= MainWindow()
window.show()
app.exec()