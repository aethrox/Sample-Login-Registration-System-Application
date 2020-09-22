from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtTest
from PyQt5 import QtCore
import sys
import sqlite3

# Fonts
fontTitle = QtGui.QFont("Fjalla One", 26)
fontTitle2 = QtGui.QFont("Economica", 36)

#Images
windowBackground = "image/6.jpg"
windowIcon = "image/2.png"

link = sqlite3.connect("login.db")
cursor = link.cursor()

class mainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setWindowIcon(QtGui.QIcon(windowIcon))
        self.setFixedSize(440,600)

        ####################################################
        self.loginTitle = QtWidgets.QLabel("Login")
        self.loginTitle.setFont(fontTitle)
        self.loginTitle.setStyleSheet("color: white;")
        self.loginTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.username = QtWidgets.QLineEdit()
        self.username.setPlaceholderText("Username")
        self.password = QtWidgets.QLineEdit()
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.loginBtn = QtWidgets.QPushButton("Login")
        self.loginBtn.clicked.connect(self.login)
        self.loginBtn.setStyleSheet("background-color: transparent;")
        ####################################################

        self.regBtn = QtWidgets.QPushButton("Create a new account ?")
        self.regBtn.clicked.connect(self.registerOpen)
        self.regBtn.setStyleSheet("border: 0px transparent; color: white; background-color: transparent; font-size: 10px;")

        horizontal = QtWidgets.QHBoxLayout()
        vertical = QtWidgets.QVBoxLayout()

        vertical1 = QtWidgets.QVBoxLayout()

        ####################################################
        vertical.addStretch()
        vertical.addStretch()
        vertical.addWidget(self.loginTitle)
        vertical.addStretch()
        vertical.addWidget(self.username)
        vertical.addWidget(self.password)
        vertical.addWidget(self.loginBtn)
        vertical.addWidget(self.regBtn)
        vertical.addStretch()
        vertical.addStretch()
        ####################################################

        horizontal.addStretch()
        horizontal.addLayout(vertical)
        horizontal.addLayout(vertical1)
        horizontal.addStretch()

        oImage = QtGui.QImage(windowBackground)
        # resize Image to widgets size
        sImage = oImage.scaled(QtCore.QSize(440,600))
        palette = QtGui.QPalette()
        # 10 = Windowrole
        palette.setBrush(10, QtGui.QBrush(sImage))

        main = QtWidgets.QWidget()
        self.setCentralWidget(main)
        main.setLayout(horizontal)
        self.setPalette(palette)
        self.show()
    def login(self):
        users = cursor.execute(f"SELECT username,password FROM users WHERE username = '{self.username.text()}'")
        link.commit()
        try:
            for user in users.fetchall():
                self.user = user
            if ((self.username.text() == self.user[0]) and (self.password.text() == self.user[1])):
                QtWidgets.QMessageBox.information(self,"Login","Login Success!")
                self.home = window()
                self.home.show()
                self.setHidden(True)
            elif ((len(self.username.text()) < 1) or (len(self.password.text()) < 1)):
                QtWidgets.QMessageBox.critical(self,"Login","Username or password field is empty!")
            else:
                QtWidgets.QMessageBox.critical(self,"Login","Username or password wrong!")
        except AttributeError:
            QtWidgets.QMessageBox.critical(self,"Login","Username or password wrong!")
    def registerOpen(self):
        self.regOpen = registerWindow()
        self.regOpen.show()
        self.setHidden(True)
class window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Home")
        self.setWindowIcon(QtGui.QIcon(windowIcon))
        self.setFixedSize(440,600)

        self.text = QtWidgets.QLabel("Login Success!")
        self.text.setFont(fontTitle2)
        self.text.setStyleSheet("color: white;")
        self.btn = QtWidgets.QPushButton("Log Out",self)
        self.btn.clicked.connect(self.logout)
        self.btn.setGeometry(20,20,50,30)
        self.btn.setStyleSheet("background-color: transparent;")
        
        horizontal = QtWidgets.QHBoxLayout()
        vertical = QtWidgets.QVBoxLayout()

        ####################################################
        vertical.addStretch()
        vertical.addWidget(self.text)
        vertical.addStretch()
        ####################################################

        horizontal.addStretch()
        horizontal.addLayout(vertical)
        horizontal.addStretch()

        oImage = QtGui.QImage(windowBackground)
        # resize Image to widgets size
        sImage = oImage.scaled(QtCore.QSize(440,600))
        palette = QtGui.QPalette()
        # 10 = Windowrole
        palette.setBrush(10, QtGui.QBrush(sImage))

        self.setLayout(horizontal)
        self.setPalette(palette)
        self.show()
    def logout(self):
        self.close()
        self.loginOpen = mainWindow()
        self.loginOpen.show() 
class registerWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Register")
        self.setWindowIcon(QtGui.QIcon(windowIcon))
        self.setFixedSize(440,600)

        self.back = QtWidgets.QPushButton("<  Back",self)
        self.back.clicked.connect(self.turnBack)
        self.back.setGeometry(20,20,60,25)
        self.back.setStyleSheet("background-color: transparent;")

        ####################################################
        self.registerTitle = QtWidgets.QLabel("Register")
        self.registerTitle.setFont(fontTitle)
        self.registerTitle.setStyleSheet("color: white;")
        self.registerTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.usernameReg = QtWidgets.QLineEdit()
        self.usernameReg.setPlaceholderText("Username")
        self.passwordReg = QtWidgets.QLineEdit()
        self.passwordReg.setPlaceholderText("Password")
        self.registerBtn = QtWidgets.QPushButton("Register")
        self.registerBtn.clicked.connect(self.register)
        self.registerBtn.setStyleSheet("background-color: transparent;")
        ####################################################

        horizontal = QtWidgets.QHBoxLayout()
        vertical = QtWidgets.QVBoxLayout()

        ####################################################
        vertical.addStretch()
        vertical.addStretch()
        vertical.addWidget(self.registerTitle)
        vertical.addStretch()
        vertical.addWidget(self.usernameReg)
        vertical.addWidget(self.passwordReg)
        vertical.addWidget(self.registerBtn)
        vertical.addStretch()
        vertical.addStretch()
        ####################################################

        horizontal.addStretch()
        horizontal.addLayout(vertical)
        horizontal.addStretch()

        oImage = QtGui.QImage(windowBackground)
        # resize Image to widgets size
        sImage = oImage.scaled(QtCore.QSize(440,600))
        palette = QtGui.QPalette()
        # 10 = Windowrole
        palette.setBrush(10, QtGui.QBrush(sImage))

        self.setLayout(horizontal)
        self.setPalette(palette)
        self.show()
    def register(self):
        users = cursor.execute(f"SELECT username,password FROM users WHERE username = '{self.usernameReg.text()}'")
        link.commit()
        for user in users.fetchall():
            self.user = list(user)  
        if (self.usernameReg.text() != self.user[0]):
            cursor.execute("INSERT INTO users (username,password) VALUES (?,?)",(self.usernameReg.text(),self.passwordReg.text()))
            link.commit()
            QtWidgets.QMessageBox.information(self,"Register","Registration Successful!")
        elif ((self.usernameReg.text() == self.user[0])):
            QtWidgets.QMessageBox.critical(self,"Register","Such a username already exists!")
        elif ((len(self.usernameReg.text()) < 1) and (len(self.passwordReg.text()) < 1)):
            QtWidgets.QMessageBox.critical(self,"Register","Username or password field is empty!")
    def turnBack(self):
        self.loginOpen = mainWindow()
        self.loginOpen.show()
        self.close()
stylesheet = ("""
QPushButton {
    color: white;
    border: 2px solid white;
    border-radius: 5px;
    width: 20px;
    height: 20px;
    background-color: black;
}
QPushButton:hover {
    color: red;
    border: 2px solid red;
}
QLineEdit {
    border: 2px solid white;
    border-radius: 5px;
}
""")
app = QtWidgets.QApplication(sys.argv)
app.setStyleSheet(stylesheet)
main = mainWindow()
sys.exit(app.exec_())   
