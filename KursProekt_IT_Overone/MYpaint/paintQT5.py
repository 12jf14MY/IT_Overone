from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys



# Класс создание главного Окна
class Window(QMainWindow):


    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # Название окна
        self.setWindowTitle("===ГАРЦУЮЩИЙ КАРАНДАШиК===")

        # Размер главного окна
        self.resize(1000, 1000)

        # создаем устройство рисования
        self.image = QImage(self.size(), QImage.Format_RGB32)

        # преобразование цвет дисплея в белый
        self.image.fill(Qt.white)

        # иконка
        self.setWindowIcon(QIcon('pen.jpg'))

        # Переменные данные========================================================================
        # рисовать по умолчанию нельзя. Ниже будет цикл когда нажата клавиша мыши тогда и рисуем
        self.drawing = False
        # Размер кисти по умолчанию
        self.brushSize = 2
        # цвет черный по умолчанию
        self.brushColor = Qt.black

        # QPoint объект для отслеживания точки
        self.lastPoint = QPoint()

        # Создаем меню=================================================================
        mainMenu = self.menuBar()

        # СОздаем меню Файл где будет сохранение и очистка
        fileMenu = mainMenu.addMenu("Файл")

        # Размер кисти в грав меню
        b_size = mainMenu.addMenu("Размер карандашика ")

        # Цвет карандаша в главном меню
        b_color = mainMenu.addMenu("Цвет карандашика")

        # Заливка холста
        b_holst = mainMenu.addMenu("Цвет холста")


        # Заполняем главное меню ============================================================
        # создаем действие сохранить (строчка с названием сохранить)
        saveAction = QAction("Сохр Ctrl + S", self)
        # действию сохранить назначаем горячие клавиши
        saveAction.setShortcut("Ctrl + S")
        # добавляем действие сохранения в меню файл
        fileMenu.addAction(saveAction)
        # наделяем стручку сохранения спообностью сохранения
        saveAction.triggered.connect(self.save)

        # создаем действие очистки
        clearAction = QAction("Очистка Ctrl + C", self)
        # добавляем горячие клавиши к действию очистки
        clearAction.setShortcut("Ctrl + C")
        # добавляем очистку в меню файл
        fileMenu.addAction(clearAction)
        # наделяем стручку очистки спообностью очистки
        clearAction.triggered.connect(self.clear)

        # размеры кисти===========================================================================
        # создаем 4 пикселя
        pix_4 = QAction("4 px", self)
        # добавляем то что создали в меню размер кисти
        b_size.addAction(pix_4)
        # наделяем способностью к тому что создали
        pix_4.triggered.connect(self.Pixel_4)

        # другие типоразмеры
        pix_7 = QAction("7 px", self)
        b_size.addAction(pix_7)
        pix_7.triggered.connect(self.Pixel_7)

        pix_9 = QAction("9 px", self)
        b_size.addAction(pix_9)
        pix_9.triggered.connect(self.Pixel_9)

        pix_12 = QAction("12 px", self)
        b_size.addAction(pix_12)
        pix_12.triggered.connect(self.Pixel_12)

        pix_24 = QAction("24 px", self)
        b_size.addAction(pix_24)
        pix_24.triggered.connect(self.Pixel_24)

        pix_48 = QAction("48 px", self)
        b_size.addAction(pix_48)
        pix_48.triggered.connect(self.Pixel_48)

        # Создаем цвета карандашей=============================================================
        # создаем строчку с черным цветом
        black = QAction("Черный", self)
        # добавляем эту трочку в меню цвет карандаша
        b_color.addAction(black)
        # добавляем способность этой строчке быть черной
        black.triggered.connect(self.blackColor)

        # так же для других цветов
        white = QAction("Белый", self)
        b_color.addAction(white)
        white.triggered.connect(self.whiteColor)

        green = QAction("Зеленый", self)
        b_color.addAction(green)
        green.triggered.connect(self.greenColor)

        yellow = QAction("Желтый", self)
        b_color.addAction(yellow)
        yellow.triggered.connect(self.yellowColor)

        red = QAction("Красный", self)
        b_color.addAction(red)
        red.triggered.connect(self.redColor)

        blue = QAction("Синий", self)
        b_color.addAction(blue)
        blue.triggered.connect(self.blueColor)

        # Создаем цвета холста=============================================================
        # создаем строчку с черным цветом
        black_h = QAction("Черный", self)
        # добавляем эту трочку в меню цвет карандаша
        b_holst.addAction(black_h)
        # добавляем способность этой строчке быть черной
        black_h.triggered.connect(self.black_holst)

        # так же для других цветов
        green_h = QAction("Зеленый", self)
        b_holst.addAction(green_h)
        green_h.triggered.connect(self.green_holst)

        yellow_h = QAction("Желтый", self)
        b_holst.addAction(yellow_h)
        yellow_h.triggered.connect(self.yellow_holst)

        red_h = QAction("Красный", self)
        b_holst.addAction(red_h)
        red_h.triggered.connect(self.red_holst)

        blue_h = QAction("Синий", self)
        b_holst.addAction(blue_h)
        blue_h.triggered.connect(self.blue_holst)


    # метод проверки клика мыши для начала и конца рисования==========================
    def mousePressEvent(self, event):

        # если нажата левая клавиша мыши
        if event.button() == Qt.LeftButton:
            # значит можно рисовать (истина)
            self.drawing = True
            # и рисуем от точки до точки до точки где находится курсор во время клика
            self.lastPoint = event.pos()

    # Метод проверки активности мыши===========================================================
    def mouseMoveEvent(self, event):

        # проверка, если нажата левая кнопка мыши и мы рисуем что то
        if (event.buttons() & Qt.LeftButton) & self.drawing:
            # то на дисплеи окна рисуется рисунок
            painter = QPainter(self.image)

            # и рисунок рисуется с параметрами которые выбрали
            painter.setPen(QPen(self.brushColor, self.brushSize,
                                Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))

            # рисуем линию от предыдущей точки до текущей
            # это одна линия
            painter.drawLine(self.lastPoint, event.pos())

            # рисуем по контуру движения мыши
            self.lastPoint = event.pos()
            # обновляем для отображения в окне
            self.update()

    # Функция с методом если у нас левая клавиша не нажата============================
    def mouseReleaseEvent(self, event):

        if event.button() == Qt.LeftButton:
            # то ничего не рисуется
            self.drawing = False

    # функция рисования ====================================================================
    def paintEvent(self, event):
        # создаем холст
        canvasPainter = QPainter(self)

        # рисуем на холсте
        canvasPainter.drawImage(self.rect(), self.image, self.image.rect())

    # функция сохранения рисунка ====================================================================
    def save(self):
        # форматы сохранения
        filePath, _ = QFileDialog.getSaveFileName(self, "Save Image", "",
                                                  "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ")

        if filePath == "":
            return
        self.image.save(filePath)

    # функция очистки холста ==============================================================
    def clear(self):
        # делаем холст белым
        self.image.fill(Qt.white)
        # обновляем
        self.update()

    # функция заливки холста ==============================================================
    # делаем холст черным
    def black_holst(self):
        self.image.fill(Qt.black)
        self.update()

    # делаем холст зеленым
    def green_holst(self):
        self.image.fill(Qt.green)
        self.update()

    def yellow_holst(self):
        self.image.fill(Qt.yellow)
        self.update()

    def red_holst(self):
        self.image.fill(Qt.red)
        self.update()

    def blue_holst(self):
        self.image.fill(Qt.blue)
        self.update()

    # функции размера пера ====================================================================
    def Pixel_4(self):
        self.brushSize = 4

    def Pixel_7(self):
        self.brushSize = 7

    def Pixel_9(self):
        self.brushSize = 9

    def Pixel_12(self):
        self.brushSize = 12

    def Pixel_24(self):
        self.brushSize = 24

    def Pixel_48(self):
        self.brushSize = 48

    # функции цвета пера =======================================================================
    def blackColor(self):
        self.brushColor = Qt.black

    def whiteColor(self):
        self.brushColor = Qt.white

    def greenColor(self):
        self.brushColor = Qt.green

    def yellowColor(self):
        self.brushColor = Qt.yellow

    def redColor(self):
        self.brushColor = Qt.red

    def blueColor(self):
        self.brushColor = Qt.blue


    # функция с запросом для выхода=============================================================
    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Докладываю',
                                     "Вы действительно хотите на выход без сохнанения ?", QMessageBox.Yes |
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
if __name__ == '__main__':

# создаем приложения Pyqt5
    App = QApplication(sys.argv)

# создаем объект класса window
    window2 = Window()

# выполняем на экран window
    window2.show()

# чистый выход из приложения Pyqt5
    sys.exit(App.exec())

# это конец >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>