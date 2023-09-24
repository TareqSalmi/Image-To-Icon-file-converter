import os
import sys

from PIL import Image
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap  # Import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QFileDialog, QProgressBar, QVBoxLayout, QTextEdit


class ConverterThread(QThread):
    update_progress = pyqtSignal(int)
    update_status = pyqtSignal(str)

    def __init__(self, files):
        super().__init__()
        self.files = files

    def run(self):
        total_files = len(self.files)
        for i, file_path in enumerate(self.files):
            try:
                img = Image.open(file_path)
                icon = img.convert("RGBA")
                icon_path = os.path.splitext(file_path)[0] + '.ico'
                icon.save(icon_path, format='ICO')
                self.update_status.emit(f'Image {i + 1} Successfully Converted')
            except Exception as e:
                self.update_status.emit(f'Image {i + 1} failed to convert. Error: {str(e)}')
            finally:
                self.update_progress.emit((i + 1) * 100 // total_files)


class ConverterApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Image To Icon Converter")
        self.setGeometry(100, 100, 400, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.convert_button = QPushButton("Convert Image")
        self.convert_button.clicked.connect(self.convertImages)

        self.icon_button = QPushButton("Select Icon")
        self.icon_button.clicked.connect(self.selectIcon)  # Connect icon selection

        self.progress_bar = QProgressBar(self)
        self.progress_bar.setValue(0)

        self.status_box = QTextEdit(self)
        self.status_box.setReadOnly(True)

        vbox = QVBoxLayout()
        vbox.addWidget(self.convert_button)
        vbox.addWidget(self.icon_button)  # Add icon selection button
        vbox.addWidget(self.progress_bar)
        vbox.addWidget(self.status_box)

        self.central_widget.setLayout(vbox)

        self.selected_icon = None  # Store the selected icon pixmap

    def selectIcon(self):
        options = QFileDialog.Options()
        icon_path, _ = QFileDialog.getOpenFileName(self, "Select Icon", "", "Icon Files (*.ico);;All Files (*)",
                                                   options=options)
        if icon_path:
            self.selected_icon = QPixmap(icon_path)
            self.setWindowIcon(QIcon(self.selected_icon))

    def convertImages(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder with Images")
        if folder_path:
            files = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if
                     file.lower().endswith(('.png', '.jpg'))]
            if files:
                self.converter_thread = ConverterThread(files)
                self.converter_thread.update_progress.connect(self.progress_bar.setValue)
                self.converter_thread.update_status.connect(self.updateStatusBox)
                self.converter_thread.start()
            else:
                self.updateStatusBox("No image files found in the selected folder")
        else:
            self.updateStatusBox("No folder selected")

    def updateStatusBox(self, message):
        current_text = self.status_box.toPlainText()
        self.status_box.setPlainText(current_text + "\n" + message)
        self.status_box.verticalScrollBar().setValue(self.status_box.verticalScrollBar().maximum())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    converter = ConverterApp()
    converter.show()
    sys.exit(app.exec_())
