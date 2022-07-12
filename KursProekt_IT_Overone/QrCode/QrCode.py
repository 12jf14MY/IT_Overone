# нужно для начала установить pip install qrcode


from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import qrcode

import sys


# Класс изображения для QR-кода=================================================================
class Image(qrcode.image.base.BaseImage):

    # конструктор===========================================================
    def __init__(self, border, width, box_size):
        # назначение border
        self.border = border

        # назначение width
        self.width = width

        # назначение box size
        self.box_size = box_size

        # создаем размер size
        size = (width + border * 2) * box_size

        # создаем изображение
        self._image = QImage(size, size, QImage.Format_RGB16)

        # исходное изображение белое
        self._image.fill(Qt.white)

    # pixmap функция=================================================================
    def pixmap(self):
        # возвращаем изображение
        return QPixmap.fromImage(self._image)

    # функция создания прямоугольника================================================
    def drawrect(self, row, col):
        # создание объекта painter
        painter = QPainter(self._image)

        # создаем прямоугольник
        painter.fillRect(
            (col + self.border) * self.box_size,
            (row + self.border) * self.box_size,
            self.box_size, self.box_size,
            QtCore.Qt.black)

    # Класс главное окно=======================================================================================


class Window(QMainWindow):

    # конструктор
    def __init__(self):
        QMainWindow.__init__(self)

        # Название окна
        self.setWindowTitle("Создай свой QR Код")

        # геометрия окна
        self.resize(300, 300)

        # иконка
        self.setWindowIcon(QIcon('qr-kod.jpg'))

        # создание этикетки для отображения qr-кода
        self.label = QLabel(self)

        # создание строки для получения текста
        self.edit = QLineEdit(self)

        # добавление действия при нажатии клавиши Enter
        self.edit.returnPressed.connect(self.handleTextEntered)

        # установка шрифта для редактирования строки
        self.edit.setFont(QFont('Times', 12))

        # выравнивание параметров
        self.edit.setAlignment(Qt.AlignCenter)

        # создание вертикального макета
        layout = QVBoxLayout(self)

        # добавление этикетки к слою
        layout.addWidget(self.label)

        # добавление  строки в макет
        layout.addWidget(self.edit)

        # создание объекта QWidget
        widget = QWidget()

        # sустановка макета для QWidget
        widget.setLayout(layout)

        # установка виджета в качестве центрального виджета главного окна
        self.setCentralWidget(widget)

    # метод, вызываемый редактированием строки================================================================
    def handleTextEntered(self):
        # берем текст
        text = self.edit.text()
        # созданием из него пиксельную карту qr-кода
        qr_image = qrcode.make(text, image_factory=Image).pixmap()
        # изображение qr-кода прикрепляем к окну
        self.label.setPixmap(qr_image)

    # функция с запросом для выхода=============================================================
    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Докладываю',
                                     "Вы действительно хотите на выход?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    # Функция для отбражения окна по центру монитора ===================================================
    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


# ВЫПОЛНЕНИЕ <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# создаем приложения Pyqt5
app = QApplication(sys.argv)

# создаем объект window класса Window
window = Window()

# выполняем window
window.show()

# чистый выход из приложения Pyqt5
sys.exit(app.exec_())

# А это уже  конец >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
