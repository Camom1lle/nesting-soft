from PyQt5 import QtCore, QtGui, QtWidgets
import ezdxf
from ezdxf.entities import Polyline
from PyQt5.QtGui import QPalette, QPixmap, QFont

class DXFGenerator(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Автоматизация раскладки [тест 12.7.6]")
        self.layout = QtWidgets.QGridLayout()
        self.setLayout(self.layout)
        self.setGeometry(100, 100, 600, 400)
        self.setMinimumSize(780, 460)

        font = QFont()
        font.setPointSize(16)

        width_label = QtWidgets.QLabel("Ширина:")
        width_label.setFont(font)
        self.width_input = QtWidgets.QLineEdit()
        self.width_input.setFixedSize(600, 50)
        height_label = QtWidgets.QLabel("Длина:")
        height_label.setFont(font)
        self.height_input = QtWidgets.QLineEdit()
        self.height_input.setFixedSize(600, 50)

        generate_button = QtWidgets.QPushButton("Создать файл")
        generate_button.setFixedSize(180, 50)
        generate_button.setFont(font)
        generate_button.clicked.connect(self.generate_dxf)

        self.open_file_dialog_button = QtWidgets.QPushButton("Укажите файл")
        self.open_file_dialog_button.setFixedSize(180, 50)
        self.open_file_dialog_button.setFont(font)
        self.open_file_dialog_button.clicked.connect(self.open_file_dialog)

        self.layout.addWidget(self.open_file_dialog_button, 0, 0, 1, 2)
        self.layout.addWidget(width_label, 1, 0)
        self.layout.addWidget(self.width_input, 1, 1)
        self.layout.addWidget(height_label, 2, 0)
        self.layout.addWidget(self.height_input, 2, 1)
        self.layout.addWidget(generate_button, 3, 0, 1, 2)

    def generate_dxf(self):
        width = float(self.width_input.text())
        height = float(self.height_input.text())

        # Open the DXF file, or create a new one if the filename is empty
        doc = ezdxf.new("R2010")
        msp = doc.modelspace()

        # Add the line to the document
        msp.add_lwpolyline([(0, 0), (width-5, 0), (width-5, height-5),  (0, height-5), (0, 0)])

        # Save the document
        doc.saveas("new.dxf")
        print("DXF file generated.")

    def open_file_dialog(self):
        file_dialog = QtWidgets.QFileDialog(self)
        file_dialog.setFileMode(QtWidgets.QFileDialog.ExistingFile)

        if file_dialog.exec_():
            print("File selected:", file_dialog.selectedFiles()[0])

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = DXFGenerator()
    window.show()
    app.exec_()