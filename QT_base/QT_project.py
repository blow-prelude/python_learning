import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QHBoxLayout, QLabel
from PyQt5.QtCore import Qt


# 3个子窗口的共性功能
class BaseFunctionWindow(QMainWindow):
    def __init__(self, main_window, title):
        super().__init__()
        self.main_window = main_window
        self.setWindowTitle(title)
        self.resize(600, 400)

        # 返回按钮
        self.back_button = QPushButton("Back")
        self.back_button.clicked.connect(self.return_to_main_window)
        self.back_button.setFixedSize(100,50)

        # 将返回按钮设置在界面右侧

    def return_to_main_window(self):
        """返回主界面"""
        self.main_window.show()
        self.close()


# 主窗口，中间竖直排列3个按钮，点击后进入不同的功能界面
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(1000,800)

        # 在主界面竖直居中排列3个botton

        # 分别创建3个按钮
        self.button1 = QPushButton("deploy", self)
        self.button1.clicked.connect(lambda: self.switch_to_window(self.deploy_window))
        self.button1.setFixedSize(100, 50)
        # self.button1.setStyleSheet("background-color: white; color: black; font-size: 20px;")

        self.button2 = QPushButton("first_gamer", self)
        self.button2.clicked.connect(lambda: self.switch_to_window(self.first_gamer_window))
        self.button2.setFixedSize(100, 50)

        self.button3 = QPushButton("secong_gamer", self)
        self.button3.clicked.connect(lambda: self.switch_to_window(self.second_gamer_window))
        self.button3.setFixedSize(100, 50)

        # 创建主界面布局
        layout = QVBoxLayout()
        layout.addWidget(self.button1)  
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)

        # 设置主界面布局
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


        # 创建子界面
        self.deploy_window = DeployPage(self, "delpoy")
        self.first_gamer_window = Gamer(self, "first_gamer")
        self.second_gamer_window = Gamer(self, "second_gamer")



    def switch_to_window(self, target_window):
        """切换到指定窗口"""
        target_window.show()
        self.hide()



# 自定义放置棋子界面
class DeployPage(BaseFunctionWindow):
    def __init__(self, main_window, lecture_title):
        super().__init__(main_window, lecture_title)



# 人机对弈界面
class Gamer(BaseFunctionWindow):
    def __init__(self, main_window, lecture_title):
        super().__init__(main_window, lecture_title)

    

def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
