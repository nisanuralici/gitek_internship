# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 10:03:16 2023
@author: Nisanur
"""

# PyQt5 kütüphanesinden gerekli modüllerin import edilmesi
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QIcon

# ImageDisplayApp adında bir sınıf oluşturuluyor ve QMainWindow sınıfından türetiliyor.
class ImageDisplayApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # initUI fonksiyonunun çağrılması
        self.initUI() #bütün elemanları ekliyoruz

    # Kullanıcı arayüzünün oluşturulduğu fonksiyon
    def initUI(self):
        # Pencere başlığının ayarlanması
        self.setWindowTitle('Goruntuler')
        # Pencere boyutunun ayarlanması (sol üst köşe, genişlik, yükseklik)
        self.setGeometry(100, 100, 400, 300)
        self.setWindowIcon(QIcon('mario.png'))
        # Merkezi bir widget oluşturuluyor ve QMainWindow'a setCentralWidget ile atanıyor.
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        # Dikey bir düzen oluşturuluyor
        self.layout = QVBoxLayout()

        # Resim görüntüsünün gösterileceği QLabel oluşturuluyor
        self.image_label = QLabel(self)
        self.layout.addWidget(self.image_label)

        # Düğmelerin oluşturulması ve işlevlerinin bağlanması
        self.button1 = QPushButton('Original', self)
        self.button1.clicked.connect(self.show_image1)
        self.layout.addWidget(self.button1)

        self.button2 = QPushButton('Gray', self)
        self.button2.clicked.connect(self.show_image2)
        self.layout.addWidget(self.button2)

        self.button3 = QPushButton('Threshold', self)
        self.button3.clicked.connect(self.show_image3)
        self.layout.addWidget(self.button3)

        self.button4 = QPushButton('Blur', self)
        self.button4.clicked.connect(self.show_image4)
        self.layout.addWidget(self.button4)

        # Merkezi widget'a düzenin atanması
        self.central_widget.setLayout(self.layout)

    # Resimleri görüntülemek için kullanılacak fonksiyonlar
    def show_image1(self):
        pixmap = QPixmap('original.jpg')  
        self.image_label.setPixmap(pixmap)
        self.image_label.setScaledContents(True)
        #self.resize(pixmap.width(), pixmap.height())  # Pencere boyutunu resim boyutuna ayarla

    def show_image2(self):
        pixmap = QPixmap('gray.png')  
        self.image_label.setPixmap(pixmap)
        self.image_label.setScaledContents(True)
        
    def show_image3(self):
        pixmap = QPixmap('threshold.png')  
        self.image_label.setPixmap(pixmap)
        self.image_label.setScaledContents(True)
        
    def show_image4(self):
        pixmap = QPixmap('blur.png')  
        self.image_label.setPixmap(pixmap)
        self.image_label.setScaledContents(True)

# Uygulamanın başlatılması ve çalıştırılması
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ImageDisplayApp()
    window.show()
    sys.exit(app.exec_())
