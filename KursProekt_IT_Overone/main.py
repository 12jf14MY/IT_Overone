import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


# from PyQt5 import  QtCore, QtGui, QtWidgets
# from paintQT5 import window
# import MYpaint.paintQT5
# from MYpaint.paintQT5 import Window


# Класс создания главного Окна курсового проекта********************************************************************
class MYWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.IinitUI()

    def IinitUI(self):

        # Название окна
        self.setWindowTitle("Диплом IT OVERONE Майсеёнок Юрий")

        # Размер главного окна
        self.resize(1000, 500)

        # иконка
        self.setWindowIcon(QIcon('diplom.jpeg'))

        self.lbl = QLabel(
            'Всем привет, это моя дипломная работа, ниже можно \nиспытать проекты. (наведя курсор мыши на кнопку, \nвысветится  подсказка о проекте)',
            self)
        self.lbl.setGeometry(50, -200, 900, 600)
        # self.lbl.move(50, 30)
        # self.lbl2 = QLabel('<u>Ещё одна метка</u>', self)
        # self.lbl2.move(50, 50)

        self.font = QFont()  # создаём объект шрифта
        self.font.setFamily("Rubik")  # название шрифта
        self.font.setPointSize(16)  # размер шрифта
        # self.font.setUnderline(True)  # подчёркивание
        self.lbl.setFont(self.font)  # задаём шрифт метке

        # вызов функции кнопок
        self.UiComponents()

    # функция кнопок=============================================================================================
    def UiComponents(self):

        # Создаем кнопки проекта

        # Кнопка paint*****************************************************************
        push_paint = QPushButton("ГАРЦУЮЩИЙ КАРАНДАШиК", self)
        # размеры и координаты кнопки
        push_paint.setGeometry(50, 200, 400, 80)
        # добавляем цветовой эффект
        c1_effect = QGraphicsColorizeEffect()
        c1_effect.setColor(Qt.red)
        push_paint.setGraphicsEffect(c1_effect)
        push_paint.setFont(QFont('Arial', 14))  # шрифт и высота текста
        # подсказка к кнопке
        push_paint.setToolTip('Это програмка-рисовалка, аналог <b>paint</b>')
        #  При нажатии кнопки запускается функция 1
        # push_paint.setCheckable(True)
        push_paint.clicked.connect(self.fun1)

        # Кнопка QrCode***************************************************************************
        push_QrCode = QPushButton("СОЗДАЙ СВОЙ QrCode", self)
        # размеры и координаты кнопки
        push_QrCode.setGeometry(550, 200, 400, 80)
        # добавляем цветовой эффект
        c2_effect = QGraphicsColorizeEffect()
        c2_effect.setColor(Qt.blue)
        push_QrCode.setGraphicsEffect(c2_effect)
        push_QrCode.setFont(QFont('Arial', 14))  # шрифт и высота текста
        # подсказка к кнопке
        push_QrCode.setToolTip(
            'Это програмка для создания QR кода на любой введенный текст, \nможно создать QR визитную карточку, либо QR места проживания и т.д.')
        #  При нажатии кнопки запускается функция 2
        push_QrCode.clicked.connect(self.fun2)

        # Кнопка browse**************************************************************************
        push_browse = QPushButton("Браузер", self)
        # размеры и координаты кнопки
        push_browse.setGeometry(550, 350, 400, 80)
        # добавляем цветовой эффект
        c3_effect = QGraphicsColorizeEffect()
        c3_effect.setColor(Qt.black)
        push_browse.setGraphicsEffect(c3_effect)
        push_browse.setFont(QFont('Arial', 14))  # шрифт и высота текста
        # подсказка к кнопке
        push_browse.setToolTip('Браузер с поисковой системой http://www.google.com/')
        #  При нажатии кнопки запускается функция 3
        push_browse.clicked.connect(self.fun3)

        # Кнопка calc******************************************************************************
        push_calc = QPushButton("Калькулятор", self)
        # размеры и координаты кнопки
        push_calc.setGeometry(50, 350, 400, 80)
        # добавляем цветовой эффект
        c4_effect = QGraphicsColorizeEffect()
        c4_effect.setColor(Qt.green)
        push_calc.setGraphicsEffect(c4_effect)
        push_calc.setFont(QFont('Arial', 14))  # шрифт и высота текста
        # подсказка к кнопке
        push_calc.setToolTip('Обычный простой калькулятор ')
        #  При нажатии кнопки запускается функция 4
        push_calc.clicked.connect(self.fun4)

    # Функции запуска проектов при нажатии кнопок************************************************
    def fun1(self):

        # импорт кода из файла
        from MYpaint.paintQT5 import Window
        # создаем объект класса window из файла paintQT5
        self.window2 = Window()
        # выполняем на экран window
        self.window2.show()

    def fun2(self):
        # импорт кода из файла
        from QrCode.QrCode import WindowQ
        # создаем объект класса window из файла
        self.window1 = WindowQ()
        # выполняем на экран window
        self.window1.show()

    def fun3(self):
        # импорт кода из файла

        # import MYwebbrowser.browse
        from browse.browse import MainW
        # self.App = QApplication(sys.argv)
        # создаем объект класса window из файла
        self.mainWin = MainW()
        # выполняем на экран window
        self.mainWin.show()
        # self.sys.exit(App.exec())


    def fun4(self):
        # импорт кода калькулятора из файла

        from calc.calc import WindowV
        # self.App = QApplication(sys.argv)
        # создаем объект класса window из файла
        self.win1 = WindowV()
        # выполняем на экран window
        self.win1.show()
        # self.sys.exit(App.exec())


    # функция с запросом для выхода=============================================================
    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Докладываю',
                                     "Вы действительно хотите выйти?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    # Функция для отбражения окна по центру ===================================================
    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


# ВЫПОЛНЕНИЕ <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# if __name__ == '__main__':
# создаем приложения Pyqt5
App = QApplication(sys.argv)

# создаем объект класса window
win = MYWindow()

# выполняем window на экран
win.show()

#    чистый выход из приложения Pyqt5
sys.exit(App.exec())

# это конец >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
