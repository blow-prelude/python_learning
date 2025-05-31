import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout,QGridLayout, QWidget, QPushButton
# import PyQt5.QtCore as Qt

# 函数说明：layout.addWidget(widget, *args, alignment=None)
# 参数说明：
#         - widget：需要添加到布局中的控件对象，例如 QPushButton、QLabel 等。
#         - *args：
#           - 若使用网格布局 (QGridLayout)，应指定以下参数：
#               - row：控件所在的行号（从 0 开始）。
#               - column：控件所在的列号（从 0 开始）。
#               - rowspan：控件占据的行数（可选，默认为 1）。
#               - colspan：控件占据的列数（可选，默认为 1）。
#           - 若使用其他布局（如 QVBoxLayout、QHBoxLayout），无需指定额外参数。控件按照布局顺序自动排列。
#         - alignment：控件的对齐方式（可选），适用于所有布局类型，包括：
#           - 垂直对齐：
#               - Qt.AlignTop（顶部对齐）
#               - Qt.AlignBottom（底部对齐）
#               - Qt.AlignVCenter（垂直居中）
#           - 水平对齐：
#               - Qt.AlignLeft（左对齐）
#               - Qt.AlignRight（右对齐）
#               - Qt.AlignHCenter（水平居中）
#           - 完全居中：
#               - Qt.AlignCenter（水平和垂直都居中）


# 函数功能：将控件添加到布局中，支持自定义对齐方式和布局管理。
# 函数说明：layout.addWidget(widget, *args, alignment=None)
# 参数说明：
#         - widget：需要添加到布局中的控件对象，例如 QPushButton、QLabel 等。
#         - *args：
#           - 若使用网格布局 (QGridLayout)，应指定以下参数：
#               - row：控件所在的行号（从 0 开始）。
#               - column：控件所在的列号（从 0 开始）。
#               - rowspan：控件占据的行数（可选，默认为 1）。
#               - colspan：控件占据的列数（可选，默认为 1）。
#           - 若使用其他布局（如 QVBoxLayout、QHBoxLayout），无需指定额外参数。控件按照布局顺序自动排列。
#         - alignment：控件的对齐方式（可选），适用于所有布局类型，包括：
#           - 垂直对齐：
#               - Qt.AlignTop（顶部对齐）
#               - Qt.AlignBottom（底部对齐）
#               - Qt.AlignVCenter（垂直居中）
#           - 水平对齐：
#               - Qt.AlignLeft（左对齐）
#               - Qt.AlignRight（右对齐）
#               - Qt.AlignHCenter（水平居中）
#           - 完全居中：
#               - Qt.AlignCenter（水平和垂直都居中）
#


'''
# QMainWindow是一个主窗口类，是一个特殊的QWidget
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # QVBoxLayout  是垂直管理器，
        # 使用addWidget 添加部件时，按照顺序从上往下自动排列
        vbox = QVBoxLayout()
        button1 = QPushButton("Button 1")
        button2 = QPushButton("Button 2")
        button3 = QPushButton("Button 3")
        vbox.addWidget(button1)
        vbox.addWidget(button2)
        vbox.addWidget(button3)

        # 创建一个QWidget的容器，承载其他部件和布局
        # QWidget 是所有用户界面对象的基类，几乎所有的部件都派生自 QWidget。可以作为一个容器，用于放置其他部件或布局。
        central_widget = QWidget()
        # 将vbox设置为该容器的布局
        central_widget.setLayout(vbox)
        # 将central_widget设置为中心部件，确保显示
        self.setCentralWidget(central_widget)

if __name__ == "__main__":
    # 创建一个应用程序对象,负责管理应用程序的控制流和主要设置
    app = QApplication(sys.argv)
    # 实例化自定义窗口
    window = MainWindow()
    # 显示窗口
    window.show()
    # 进入应用程序的事件循环，直到主动关闭
    sys.exit(app.exec_())
'''


'''
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        grid_layout = QGridLayout()
        button0 = QPushButton("Button 0")
        button1 = QPushButton("Button 1")
        button2 = QPushButton("Button 2")
        button3 = QPushButton("Button 3")
        button4 = QPushButton("Button 4")
        button5 = QPushButton("Button 5")
        button6 = QPushButton("Button 6")
        button7 = QPushButton("Button 7")
        button8 = QPushButton("Button 8")
        grid_layout.addWidget(button0, 0, 0)
        grid_layout.addWidget(button1, 0, 1)        
        grid_layout.addWidget(button2, 0, 2)        
        grid_layout.addWidget(button3, 1, 0)        # 第二行第一列
        grid_layout.addWidget(button4, 1, 1)        # 第二行第二列
        grid_layout.addWidget(button5, 1, 2)
        grid_layout.addWidget(button6, 2, 0)
        grid_layout.addWidget(button7, 2, 1)
        grid_layout.addWidget(button8, 2, 2)
        # grid_layout.addWidget(button5, 1, 2, 1, 2)  # 第二行的第三和第四列

        central_widget = QWidget()
        central_widget.setLayout(grid_layout)
        self.setCentralWidget(central_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
'''

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QMenuBar, QToolBar, QStatusBar, QAction, QTextEdit, \
    QFileDialog


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        ###################################################
        # （1）创建菜单栏，并添加一个菜单
        menubar = self.menuBar()
        file_menu = menubar.addMenu('File')

        # （2）创建操作类，农添加到菜单栏
        new_action = QAction('New', self)
        open_action = QAction('Open', self)
        save_action = QAction('Save', self)
        exit_action = QAction('Exit', self)
        file_menu.addAction(new_action)
        file_menu.addAction(open_action)
        file_menu.addAction(save_action)
        file_menu.addSeparator()  # 分隔线
        file_menu.addAction(exit_action)

        # （3）连接菜单项和工具按钮的槽函数
        new_action.triggered.connect(self.newFile)
        open_action.triggered.connect(self.openFile)
        save_action.triggered.connect(self.saveFile)
        exit_action.triggered.connect(self.exitApp)
        ###################################################
        # （1）创建工具栏
        toolbar = self.addToolBar('Toolbar')

        # （2）在工具栏中，添加工具按钮
        new_button = toolbar.addAction('New')  # 用于清空（当前）文本编辑框
        open_button = toolbar.addAction('Open')  # 用于打开txt文本并添加到文本编辑框
        save_button = toolbar.addAction('Save')  # 用于保存文本编辑框到txt文本

        # （3）连接菜单项和工具按钮的槽函数
        new_button.triggered.connect(self.newFile)
        open_button.triggered.connect(self.openFile)
        save_button.triggered.connect(self.saveFile)
        ###################################################
        # （1）创建状态栏
        statusbar = self.statusBar()

        # （2）在状态栏中显示消息: 'Ready' 是要显示的文本消息，3000 是消息显示的时间（以毫秒为单位），即3秒。
        statusbar.showMessage('Ready', 3000)
        ###################################################
        # 创建文本编辑框
        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)  # 将文本编辑框设置为主窗口的中心组件

    def newFile(self):
        self.text_edit.clear()  # 清空文本编辑框

    def openFile(self):
        try:
            # 打开文件对话框 ———— 选择txt文件并读取内容，然后显示在文本编辑框中
            file_dialog = QFileDialog(self)
            file_path, _ = file_dialog.getOpenFileName()
            if file_path:
                with open(file_path, 'r', encoding='utf-8') as file:
                    file_contents = file.read()
                    self.text_edit.setPlainText(file_contents)
        except Exception as e:
            print(f"Error opening file: {str(e)}")

    def saveFile(self):
        try:
            # 保存文件对话框 ———— 将文本编辑框中的内容保存到txt文件中
            file_dialog = QFileDialog(self)
            file_path, _ = file_dialog.getSaveFileName()
            if file_path:
                with open(file_path, 'w') as file:
                    file_contents = self.text_edit.toPlainText()
                    file.write(file_contents)
        except Exception as e:
            print(f"Error saving file: {str(e)}")

    def exitApp(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle('PyQt Text Editor')
    window.setGeometry(100, 100, 800, 300)
    window.show()
    sys.exit(app.exec_())


