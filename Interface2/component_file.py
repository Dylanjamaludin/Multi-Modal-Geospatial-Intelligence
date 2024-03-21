import sys
from PyQt6.QtCore import Qt, QSize,QRect, pyqtSignal
from PyQt6.QtGui import QIcon,QFont, QFontDatabase, QPainter,QBrush,QColor
from PyQt6.QtWidgets import QStyleOptionTabWidgetFrame
from PyQt6.QtWidgets import (
    QApplication,
    QBoxLayout,
    QTabBar,
    QToolBar,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QSpacerItem,
    QHBoxLayout,
    QWidget,
    QScrollArea,
    QDockWidget,
    QSizePolicy,
    QGridLayout,
    QFrame,
    QTabWidget,
    QPlainTextEdit
)

class PlainTextEdit(QPlainTextEdit):
    def __init__(self, parent =None):
        super().__init__(parent=parent)

        self.setStyleSheet('''
        PlainTextEdit
        {
            border-radius: 0;
            border-top:2px solid #494949;
            border-bottom: 2px solid #494949;
            border-right:0;
            border-left:0;
            color:#FFFFFF;
        }
        
        ''')

class UserMessage(QWidget):
    def __init__(self, message, parent=None):
        super().__init__(parent=parent)
        self.setContentsMargins(0,0,0,0)
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

        self.icon_label = QLabel(self)
        icon_pixmap = QIcon('feather/group1.svg').pixmap(QSize(40, 40))
        self.icon_label.setPixmap(icon_pixmap)
        self.icon_label.setFixedSize(40, 40)
        self.icon_label.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)

        self.username_label = QLabel("You", self)
        self.username_label.setFont(QFont('Arial', 14, QFont.Weight.Bold))
        self.username_label.setStyleSheet("color: #FFFFFF;")

        self.message_content = QLabel(message, self)
        self.message_content.setFont(QFont('Arial', 14, QFont.Weight.ExtraLight))
        self.message_content.setWordWrap(True)
        self.message_content.setStyleSheet("color: #FFFFFF;")
        
        self.top_layout = QHBoxLayout()
        self.top_layout.setContentsMargins(0, 0, 0, 0)
        self.top_layout.addWidget(self.icon_label)
        self.top_layout.addSpacing(15)

        self.top_layout.addWidget(self.username_label, Qt.AlignmentFlag.AlignLeft)
        #self.top_layout.addStretch()

        self.bottom_layout = QHBoxLayout()
        self.bottom_layout.setContentsMargins(0, 0, 0, 0)

        self.bottom_layout_spacer = QSpacerItem(55, 0, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        self.bottom_layout.addItem(self.bottom_layout_spacer)
        self.bottom_layout.addWidget(self.message_content, Qt.AlignmentFlag.AlignLeft)

        self.layout.addLayout(self.top_layout)
        self.layout.addLayout(self.bottom_layout)
        #self.layout.addWidget(self.message_content)

        self.setLayout(self.layout)

class chat(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.index = 0

        self.font1 = QFont('Arial')
        self.font1.setPixelSize(13)
        self.font1.setWeight(1000)
        self.setFont(self.font1)

        self.tab_layout = QVBoxLayout()
        self.setContentsMargins(20, 20, 20, 20)
        self.tab_layout.setSpacing(20)

        self.chat_box = PlainTextEdit()
        self.chat_box.setReadOnly(True)
        self.chat_scroll_area = QScrollArea()
        self.chat_scroll_area.setStyleSheet('''
        QScrollArea
        {
            padding:0;
            background: #202020;
            border-top: 2px solid #494949;
            border-bottom: 2px solid #494949;
            border-radius:0;
            margin:0;
        }
        
        QScrollBar:vertical 
        {
             border: 2px solid transparent;
             background: transparent;
             width: 15px;
             margin: 22px 0 22px 0;
             border-radius:6px;
         }
         QScrollBar::handle:vertical {
             background: #494949;
             border:2px solid transparent;
             min-height: 20px;
             border-radius:5px;
         }
        
         QScrollBar::add-line:vertical {
             border: 2px solid transparent;
             background: transparent;
             height: 20px;
             border-radius:5px;
             subcontrol-position: bottom;
             subcontrol-origin: margin;
         }
        
         QScrollBar::sub-line:vertical {
             border: 2px solid transparent;
             background: transparent;
             height: 20px;
             border-radius:5px;
             subcontrol-position: top;
             subcontrol-origin: margin;
         }
         QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
             border: 2px solid transparent;
             width: 3px;
             height: 3px;
             border-radius:3px;
             background: transparent;
         }
        
         QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
             background: none;
         }
        ''')
        self.chat_scroll_area.setWidgetResizable(True)
        self.chat_scroll_widget = QWidget()
        self.chat_scroll_layout = QVBoxLayout(self.chat_scroll_widget)
        self.chat_scroll_layout.setContentsMargins(0, 15, 0, 15)
        self.chat_scroll_layout.setSpacing(40)
        #self.chat_scroll_layout.setAlignment(Qt.AlignmentFlag.AlignTop.AlignLeft)
        self.chat_scroll_layout.addStretch()

        # self.chat_scroll_layout.addWidget(self.chat_box)
        self.chat_scroll_area.setWidget(self.chat_scroll_widget)

        self.chat_input_layout = QHBoxLayout()
        self.chat_input_layout.setAlignment(Qt.AlignmentFlag.AlignTop.AlignLeft)
        self.chat_input_layout.setContentsMargins(0,0,0,0)
        self.chat_input_layout.setSpacing(5)

        self.attach_icon_button = icon_button(initial_icon='feather/paperclip.svg',button_square_len=34,icon_square_len=22)

        self.chat_input = LineEdit()
        self.chat_input.enter_pressed.connect(self.send_message)
        self.chat_input.setPlaceholderText("Type here!")
        self.send_button = icon_button(initial_icon='feather/arrow-up.svg', icon_square_len=22, button_square_len=34)
        self.send_button.clicked.connect(self.send_message)

        self.chat_input_layout.addWidget(self.attach_icon_button)
        self.chat_input_layout.addWidget(self.chat_input)
        self.chat_input_layout.addWidget(self.send_button)


        self.tab_layout.addWidget(self.chat_scroll_area)
        self.tab_layout.addLayout(self.chat_input_layout)
        self.setLayout(self.tab_layout)
        #
        # tab_title = f"Tab {chat_widget.count() + 1}"
        # chat_widget.addTab(tab, QIcon('icons/worldIcon.png'), tab_title)
    def send_message(self):
        message = self.chat_input.text()
        if message:
            user_message_widget = UserMessage(message)
            self.chat_scroll_layout.addWidget(user_message_widget,alignment=Qt.AlignmentFlag.AlignTop)
            self.chat_scroll_layout.insertWidget(self.index, user_message_widget,0,Qt.AlignmentFlag.AlignLeft.AlignTop)
            self.index+=1

            self.save_message(message)
            self.chat_input.clear()
            self.chat_scroll_area.verticalScrollBar().setValue(self.chat_scroll_area.verticalScrollBar().maximum())
            self.update() 

            # TODO: Integrate with model
        # self.receive_message("Model response here...")

        # TODO: Method for recieving model response
        # def receive_message(self, message):
        #     self.chat_box.appendPlainText(message)
        #     self.save_message(message)

    def save_message(self, message):
        with open("chat_history.txt", "a") as file:
            file.write(f"{message}\n")

    def load_chat_history(self):
        try:
            with open("chat_history.txt", "r") as file:
                for line in file:
                    self.chat_box.appendPlainText(line.strip())
        except FileNotFoundError:
            pass
class TitleBar(QFrame):
    def __init__(self,title='',parent=None):
        super().__init__(parent=parent)
        self.setStyleSheet('''
                background-color: #2D2D2D;
                border: 2px solid #494949;
                border-radius: 10px;
                padding-right: 4px;
                padding-left:4px;
                ''')
        self.font1 = QFont('Arial')
        self.font1.setPixelSize(13)
        self.font1.setWeight(1000)
        self.setFont(self.font1)
        self.setFixedHeight(38)
        self.layoutSub = QHBoxLayout(self)
        self.layoutSub.setContentsMargins(0, 0, 0, 0)
        self.layoutSub.setSpacing(4)
        self.layoutSub.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        self.layoutSub.addStretch()

        self.titlebar_button1 = icon_button(icon_square_len=16, initial_icon='feather(3px)/help-circle.svg',
                                       button_square_len=28, type='type2')
        self.titlebar_button2 = icon_button(icon_square_len=16, initial_icon='feather(3px)/sliders.svg',
                                       button_square_len=28, type='type2')
        self.titlebar_button3 = icon_button(icon_square_len=16, initial_icon='feather(3px)/settings.svg',
                                            button_square_len=28, type='type2')

        self.titlebar_title = QLabel(title)
        self.titlebar_title.setStyleSheet('''
                    color: #FFFFFF;
                    margin: 0px;
                    border: 0px;
                    ''')
        self.titlebar_title.setFont(self.font1)
        #note 3 spacers are added becasue there are 3 buttons on the right that are 28px by 28px, but the spacing between them
        #is 4px, so the spacer item size must be 32 px bc there isn't any space between the spacers.
        self.spacer1 = QSpacerItem(32, 32, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.spacer2 = QSpacerItem(32, 32, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.spacer3 = QSpacerItem(32, 32, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)


        self.layoutSub.addItem(self.spacer1)
        self.layoutSub.addItem(self.spacer2)
        self.layoutSub.addItem(self.spacer3)

        self.layoutSub.addWidget(self.titlebar_title, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.layoutSub.addStretch()
        self.layoutSub.addWidget(self.titlebar_button1)
        self.layoutSub.addWidget(self.titlebar_button2)
        self.layoutSub.addWidget(self.titlebar_button3)
class DockTitleBar(QFrame):
    def __init__(self,title='',parent=None):
        super().__init__(parent=parent)
        self.setStyleSheet('''
                background-color: #2D2D2D;
                border: 2px solid #494949;
                border-radius: 10px;
                padding-right: 4px;
                padding-left:4px;
                ''')
        self.font1 = QFont('Arial')
        self.font1.setPixelSize(13)
        self.font1.setWeight(1000)
        self.setFont(self.font1)
        self.setFixedHeight(38)
        self.layoutSub = QHBoxLayout(self)
        self.layoutSub.setContentsMargins(0, 0, 0, 0)
        self.layoutSub.setSpacing(4)
        #self.layoutSub.setAlignment(Qt.AlignmentFlag.AlignVCenter)

        self.titlebar_exit = icon_button(icon_square_len=16, initial_icon='feather(3px)/x.svg',
                                       button_square_len=28, type='type2', exit=True)
        self.titlebar_float = icon_button(icon_square_len=16, initial_icon='feather(3px)/arrow-up-right.svg',
                                       button_square_len=28, type='type2')

        self.titlebar_title = QLabel(title)
        self.titlebar_title.setStyleSheet('''
                    color: #FFFFFF;
                    margin: 0 2px 0 0 ;
                    border: 0px;
                    ''')
        self.titlebar_title.setFont(self.font1)
        #note 3 spacers are added becasue there are 3 buttons on the right that are 28px by 28px, but the spacing between them
        #is 4px, so the spacer item size must be 32 px bc there isn't any space between the spacers.
        self.spacer1 = QSpacerItem(32, 32, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.spacer2 = QSpacerItem(32, 32, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        self.layoutSub.addWidget(self.titlebar_exit)
        self.layoutSub.addWidget(self.titlebar_float, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.layoutSub.addStretch()
        self.layoutSub.addWidget(self.titlebar_title)
        self.layoutSub.addItem(self.spacer1)
        self.layoutSub.addItem(self.spacer2)
        self.layoutSub.addStretch()





class TabWidget(QTabWidget):
    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self.font1 = QFont('Arial')
        self.font1.setPixelSize(14)
        self.font1.setWeight(1000)
        self.setMovable(True)
        self.setFont(self.font1)
        self.setContentsMargins(0,0,0,0)
        self.setStyleSheet('''
        QTabWidget QWidget
        {
            border: none;
        }
        
        QTabWidget QFrame
        {
            border: none;
        }
        
        QTabWidget::pane 
        {
            margin-top:-2px;
            border: none;
            background: #202020;
            border-top:2px solid #494949;
            border-bottom-left-radius:10px;
            border-bottom-right-radius:10px;
        }
        
        QTabWidget::tab-bar
        {
            top:0px;
            bottom:0px;
            border:none;
            padding:0px;
            margin:1.5px;
            alignment:left;
        }
        
        QTabBar::tab:top 
        {
            top:0px;
            color:#FFFFFF;
            background:#202020;
            border: 2px solid #494949;
            border-top-right-radius:10px;
            border-top-left-radius:10px;
            margin-top:0px;
            margin-left:6px;
            margin-right:0px;
            margin-bottom:0px;
            /*total height of the tab must be 38px, but the borders of the tab belong to a frame so */
            padding-left:7px;
            padding-bottom:0;
            padding-top:0;
            padding-right:7px;
            height:34px;
            width:125px;
        }
        
        /*commented because it does not render fast enough when moving tabs around*/
        /*QTabBar::tab::first
        {
            margin-left: 8px;
            margin-right:1.5px;
        }
        QTabBar::tab::only-one
        {
            margin-left: 8px;
            margin-right:1.5px;
        }*/
        
        QTabBar
        {
            
        }
        QTabBar::tab:selected {
            /*background:#202020;*/
            font-family: Arial;
            font-size: 14px; 
            font-weight: 1000;
            border-bottom: 2px solid #202020;
        }
        
        QTabBar::tab:!selected
        {
            background: #494949;
            border-bottom: 2px solid #494949;
            
        }
        QTabBar::tab:!selected:hover
        {
            background: #03B5A9;
            border: 2px solid #03B5A9;
            border-bottom: 2px solid #494949;
        
        }
        QTabBar::close-button
        {
            background: transparent;
            subcontrol-position: right;
            image: url(feather(3px)/x.svg);v
        }

        QTabBar::close-button:hover
        {
            border-radius:10px;
            background:#494949;
        }
        
        QTabBar::close-button:pressed
        {
            border-radius:10px;
            background:#FF0000;
        }
        
        QTabBar QToolButton
        {
            background-color: #202020;
            border-image: none;
            border: 2px solid #202020;
            border-radius:10px;
            padding:8px;
            margin-bottom:4px;
            margin-right:1px;
            margin-top:0;
            margin-left:1px;
        }
        
        QTabBar QToolButton:hover 
        {
            background-color: #2d2d2d;
            border: 2px solid #2d2d2d;
        }
        
        QTabBar QToolButton:pressed 
        {
            
            background-color: #03B5A9;
            border: 2px solid #03B5A9;
        }
        
        QTabBar::scroller 
        { /* the width of the scroll buttons */
            width:74px;
        }
        
        QTabBar::tear
        {
            background:none;
            border:none;
        } 
        
        QTabBar QToolButton::right-arrow 
        {
            image: url(feather(3px)/arrow-right.svg);
        }
        
        QTabBar QToolButton::left-arrow 
        {
            image: url(feather(3px)/arrow-left.svg);
        }
        
        QTabBar QToolButton::left-arrow:disabled 
        {
            image: url(feather(3px)/arrow-left-disabled.svg)
        }
        
        QTabBar QToolButton::right-arrow:disabled 
        {
            image: url(feather(3px)/arrow-right-disabled.svg)
        }
        ''')
        self.setTabsClosable(True)
        self.tabCloseRequested.connect(self.removeTab2)
        self.index = 0

        #delete from here
        self.addTab2(widget=chat())
        self.addTab2(widget=chat())
        #to here

        self.addButton = icon_button(initial_icon='feather(3px)/plus.svg',icon_square_len=16, button_square_len=34)

        corner_widget = QWidget()
        corner_widget.setContentsMargins(0,0,0,0)
        corner_widget_layout = QHBoxLayout()
        corner_widget_layout.setContentsMargins(0,0,4,4)
        corner_widget_layout.setSpacing(0)
        corner_widget_layout.addWidget(self.addButton, alignment=Qt.AlignmentFlag.AlignBottom)
        corner_widget.setLayout(corner_widget_layout)
        self.setCornerWidget(corner_widget, Qt.Corner.TopRightCorner)

        #DELETE THIS, CONNEC THSI WHEN YOU CREATE A A CHAT BOX FILE
        self.addButton.clicked.connect(lambda : self.addTab2(widget=chat()))

        # self.test = QHBoxLayout()
        # spacer = QSpacerItem(8,8,QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        # self.test.addWidget(self.addButton)
        # self.test.addItem(spacer)

        self.setUsesScrollButtons(True)
        

    def removeTab2(self, index):
        self.removeTab(index)
        self.index= self.index - 1
    def addTab2(self,title=('Tab'),widget =None):
        if title=='Tab':
            title = title + " " + str(self.index +1)
        if widget == None:  widget = QWidget(parent=None)
        temp = self.index

        icon = QIcon('feather(2.5px)/globe.svg')
        self.insertTab(temp,widget, icon, title)
        # self.tabBar().tabButton(temp, QTabBar().ButtonPosition.RightSide).setFixedSize(QSize(24, 24))
        self.index += 1

class LineEdit (QLineEdit):
    enter_pressed = pyqtSignal()
    def __init__(self):
        super().__init__(parent = None)


        self.setFixedHeight(34)
        self.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        font1 = QFont('Arial')
        font1.setPixelSize(13)
        self.setFont(font1)
        self.setStyleSheet('''
        LineEdit
        {
            background: #202020;
            padding: none 16px;
            border: 2px solid #494949;
            border-radius:10px;
            color: #FFFFFF;
        }
        ''')

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Return or event.key() == Qt.Key.Key_Enter:
            self.enter_pressed.emit()
        else:
            super().keyPressEvent(event)

class Label (QLabel):
    def __init__(self,text=""):
        super().__init__(text=text,parent = None)

        self.setFixedHeight(34)
        font1 = QFont('Arial')
        font1.setPixelSize(13)
        self.setFont(font1)
        self.setWordWrap(False)
        self.setObjectName("Label")
        self.setStyleSheet('''
        Label
        {
            background: #202020;
            padding: 0 16px;
            border-top:0;
            border-bottom:2px solid #494949;
            border-right:0;
            border-left:0;
            border-radius:0;
            color: #FFFFFF;
        }
        ''')
class docks(QDockWidget):
    def __init__(self, title, widget_to_dock, parent=None):
        super().__init__(title,parent)
        self.setAllowedAreas(Qt.DockWidgetArea.AllDockWidgetAreas)
        self.setWindowTitle(title)

        font1 = QFont('Arial')
        font1.setPixelSize(13)
        font1.setWeight(1000)
        self.setFont(font1)
        self.setMinimumSize(300,200)

        self.frame = QFrame()
        self.frame_layout = QVBoxLayout(self.frame)

        # self.frame.setLayout(self.frame_layout)
        self.frame.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.frame.setContentsMargins(0,0,0,0)
        self.frame_layout.setContentsMargins(10,10,10,10,)
        self.frame_layout.setSpacing(0)
        self.frame_layout.addWidget(widget_to_dock)
        self.setWidget(self.frame)

        self.setFloating(False)
        self.titlebar = DockTitleBar(title)
        self.widget().setObjectName("widget")
        self.setTitleBarWidget(self.titlebar)
        self.titlebar.titlebar_exit.clicked.connect(lambda: self.close())
        self.titlebar.titlebar_float.clicked.connect(lambda: self.setFloating(True))

        self.topLevelChanged.connect(lambda x: self.floatHandler(x))

        self.setStyleSheet('''
        QDockWidget 
        { 
            background: #494949;
            color:#ffffff;
            titlebar-close-icon: url(feather(3px)/x.svg);
            titlebar-normal-icon: url(feather(3px)/arrow-up-right.svg);
        }
        
        QDockWidget #widget
        {
            color:#ffffff;
            background: #202020;
            margin-top:2px;
            border: 2px solid #494949;
            border-radius:10px;
        } 
        
        /*this will change the contents of the qdock widget too bc all widgets are QWidgets 
        I STRONGLY recommend changing/styling those widgets instead of inheriting this stylesheet
        so THIS MUST BE FIXED*/
        QDockWidget QWidget
        {
            color:#ffffff;
            background: #202020;
            border: 2px solid transparent;
            border-radius:8px;
        } 
        
        /*QDockWidget::title 
        {
            background: #2D2D2D; 
            text-align: center;
            border: 2px solid #494949;
            border-radius: 10px;
            padding:2px;
        }
        
        QDockWidget::close-button, QDockWidget::float-button 
        {
            border: 0px solid transparent;
            background: #2D2D2D;
            icon-size: 28px;
            width:16px;
            border-radius:10px;
            padding:6px;
            margin:4px;
        }
        
        QDockWidget::float-button
        {
            subcontrol-position: top left;
            subcontrol-origin: margin;
            position: absolute;
            top: 0px; left: 34px;
            icon: url(feather(3px)/arrow-up-right.svg);
            
        }
        
        QDockWidget::close-button {
            subcontrol-position: top left;
            subcontrol-origin: margin;
            position: absolute;
            top: 0px; left: 2px;
            icon: url(feather(3px)/x.svg);
        }
        
        QDockWidget::float-button:hover {
            icon: url(feather(3px)/arrow-up-right.svg);
            background:#494949;
        }
        
        QDockWidget::close-button:hover {
            icon: url(feather(3px)/x.svg);
            background:#494949;
        }
        QDockWidget::float-button:pressed {
            icon: url(feather(3px)/arrow-up-right.svg);
            background:#03B5A9;
        }
        
        QDockWidget::close-button:pressed {
            icon: url(feather(3px)/x.svg);
            background:#ff0000;
        }*/
        ''')
    def floatHandler(self, x):
        if x:
            self.setTitleBarWidget(None)
        else:
            self.setTitleBarWidget(self.titlebar)
            self.titlebar.titlebar_exit.clicked.connect(lambda: self.close())
            self.titlebar.titlebar_float.clicked.connect(lambda: self.setFloating(True))

class icon_button (QPushButton):

    #constructor for the icon_button object
    #parameters configure the button's style
    def __init__(self, initial_icon='feather/activity.svg', icon_square_len = 20, button_square_len= 34, type='type1',exit=False, toggle=False):


        #call parent constructor, QPushButton
        super().__init__()

        # FONTS
        # id = QFontDatabase.addApplicationFont(
        #     '/Users/basmattiejamaludin/Documents/Notes/Python/PyQt6/SFProTTF/SFProText-HeavyItalic.ttf')
        # if id < 0: print('error')
        # families = QFontDatabase.applicationFontFamilies(id)
        # self.setFont(QFont(families[0], 12))

        self.initial_icon = initial_icon #set icon path parameter to object attribute
        self.setIcon(QIcon(self.initial_icon)) #set icon for button
        self.setIconSize(QSize(icon_square_len, icon_square_len)) #set icon size
        self.setFixedSize(QSize(button_square_len,button_square_len)) #set button size

        # if the button is an exit button, style it this way
        if (exit == True and type == 'type1'):
            self.setIcon(QIcon('feather(3px)/x.svg'))
            self.setStyleSheet('''
            icon_button
            {
                background-color: transparent;
                border-radius: 10px;
                border:0px;
                margin:0px;
            }
            
            icon_button:hover {
                background-color: #494949;
            }
            
            icon_button:pressed
            {
                background-color: #FF0000;
            }
            ''')
        elif (exit == True and type == 'type2'):
            self.setIcon(QIcon('feather(3px)/x.svg'))
            self.setStyleSheet('''
            icon_button
            {
                background-color: transparent;
                border-radius: 10px;
                border:0px;
                margin:0px;
            }

            icon_button:hover {
                background-color: #494949;
            }

            icon_button:pressed
            {
                background-color: #FF0000;
            }
            ''')

        #all other buttons are styled this way
        elif (exit==False and type=='type1'):
            self.setStyleSheet('''
            icon_button
            {
                background-color: #202020;
                margin:0px;
                border-radius: 10px;
                border:0px;
            }
            icon_button:hover 
            {
                background-color: #2d2d2d;
            }
            icon_button:pressed
            {
                background-color: #03B5A9;
            }
            ''')
        elif (exit == False and type == 'type2'):
            self.setStyleSheet('''
            icon_button
            {
                background-color: #2d2d2d;
                margin:0px;
                border-radius: 10px;
                border:0px;
            }
            icon_button:hover 
            {
                background-color: #494949;
            }
            icon_button:pressed
            {
                background-color: #03B5A9;
            }
            ''')