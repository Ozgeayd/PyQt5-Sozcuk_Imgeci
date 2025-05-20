import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtCore import QFile, QTextStream
from Ui_GörselProgramlamaDersProje import Ui_Form1
from Ui_GörselProgramlamaDersProje3 import Ui_Form

class window(QtWidgets.QMainWindow):
    def __init__(self):
        super(window,self).__init__()

        self.ui=Ui_Form()
        self.ui.setupUi(self)



        self.ui.buton2.clicked.connect(self.ackaydet)
        self.ui.buton3.clicked.connect(self.ackaydet)
        self.ui.buton5.clicked.connect(self.kes)
        self.ui.buton7.clicked.connect(self.yapistir)
        self.ui.buton10.clicked.connect(self.bold)
        self.ui.buton11.clicked.connect(self.italik)
        self.ui.buton4.clicked.connect(self.kapat)
        self.ui.buton1.clicked.connect(self.yeni)
        

    def yeni(self):
        self.close()  # Mevcut pencereyi kapat
        self.__init__()  # Yeni pencereyi başlat
        self.show()  # Yeni pencereyi göster
    def kapat(self):
        self.ai.close()
    def kes(self):
        self.ui.textEdit.cut()
    def yapistir(self):
        self.ui.textEdit.paste()
    def bold(self):
        cursor = self.ui.textEdit.textCursor()
        fmt = cursor.charFormat()

        if fmt.fontWeight() == QtGui.QFont.Bold:
          fmt.setFontWeight(QtGui.QFont.Normal)
        else:
          fmt.setFontWeight(QtGui.QFont.Bold)
        cursor.setCharFormat(fmt)
    def italik(self):
        cursor = self.ui.textEdit.textCursor()
        fmt = cursor.charFormat()

        if fmt.fontItalic():
            fmt.setFontItalic(False)
        else:
            fmt.setFontItalic(True)
        
        cursor.setCharFormat(fmt)
    def ackaydet(self):

        self.ai = QtWidgets.QWidget()  # QWidget oluşturuyoruz
        self.ui_form1 = Ui_Form1()  # Ui_Form1'i oluşturuyoruz
        self.ui_form1.setupUi(self.ai)  # Form1'i QWidget'e yerleştiriyoruz

        self.ai.show() 
        self.ui_form1.buton2.clicked.connect(self.kaydet)
        self.ui_form1.buton1.clicked.connect(self.ac)

    
    def ac(self):
        """Dosyayı açma fonksiyonu"""
        dosya_adi = self.ui_form1.lineEdit.text()  # LineEdit'ten dosya adı
        dosya_uzantisi = self.ui_form1.comboBox.currentText()  # ComboBox'tan dosya uzantısı

        if dosya_adi and dosya_uzantisi:
            try:
                # Dosya uzantısı ile birlikte tam dosya adını oluştur
                dosya_yolu = f"{dosya_adi}.{dosya_uzantisi}"
                
                # Dosya yolu ile dosyayı açmak için QFileDialog kullan
                options = QFileDialog.Options()
                file_path, _ = QFileDialog.getOpenFileName(self, "Dosya Aç", dosya_yolu, 
                                                            "Text Files (*.txt);;All Files (*)", options=options)

                if file_path:  # Eğer dosya yolu seçildiyse
                    with open(file_path, 'r', encoding='utf-8') as file:
                        content = file.read()  # Dosyayı oku
                        self.ui.textEdit.setPlainText(content)  # QTextEdit'e içeriği yaz
                    QMessageBox.information(self, "Başarılı", "Dosya başarıyla açıldı.")
                else:
                    QMessageBox.warning(self, "Hata", "Dosya açılamadı.")
            except Exception as e:
                QMessageBox.warning(self, "Hata", f"Bir hata oluştu: {e}")
        else:
            QMessageBox.warning(self, "Eksik Bilgi", "Dosya adı ve uzantısı gereklidir.")


    def kaydet(self):
        """Dosyayı kaydetme fonksiyonu"""
        dosya_adi = self.ui_form1.lineEdit.text()  # LineEdit'ten dosya adı
        dosya_uzantisi = self.ui_form1.comboBox.currentText()  # ComboBox'tan dosya uzantısı

        if dosya_adi and dosya_uzantisi:
            try:
                # Dosya uzantısı ile birlikte tam dosya adını oluştur
                dosya_yolu = f"{dosya_adi}.{dosya_uzantisi}"

                # Kaydetmek için dosya yolu seç
                options = QFileDialog.Options()
                file_path, _ = QFileDialog.getSaveFileName(self, "Dosya Kaydet", dosya_yolu, 
                                                           "Text Files (*.txt);;All Files (*)", options=options)

                if file_path:  # Eğer dosya yolu seçildiyse
                    file = QFile(file_path)
                    if file.open(QFile.WriteOnly | QFile.Text):
                        text_stream = QTextStream(file)
                        text = self.ui.textEdit.toPlainText()  # QTextEdit widget'ındaki metni al
                        text_stream << text  # Metni dosyaya yaz
                        file.close()  # Dosyayı kapat
                        QMessageBox.information(self, "Başarılı", "Metin başarıyla kaydedildi.")
                    else:
                        QMessageBox.warning(self, "Hata", "Dosya açılamadı.")
                else:
                    QMessageBox.warning(self, "Hata", "Dosya adı girilmedi.")
            except Exception as e:
                QMessageBox.warning(self, "Hata", f"Bir hata oluştu: {e}")
        else:
            QMessageBox.warning(self, "Eksik Bilgi", "Dosya adı ve uzantısı gereklidir.")



    


def app():
    app = QtWidgets.QApplication(sys.argv)
    screen = window()
    screen.show()
    sys.exit(app.exec_())
app()