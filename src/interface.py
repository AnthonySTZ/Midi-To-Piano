import hou  # type: ignore
from PySide2.QtWidgets import QDialog, QWidget, QVBoxLayout, QPushButton
from PySide2.QtCore import Qt


def getHoudiniWindow():
    win = hou.ui.mainQtWindow()
    return win


class MainWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.set_window_settings()
        self.set_ui()

    def set_window_settings(self) -> None:
        self.setParent(hou.ui.mainQtWindow(), Qt.Window)
        self.setWindowTitle("Midi Piano")
        self.resize(300, 200)

    def set_ui(self) -> None:
        central_layout = QVBoxLayout()
        self.setLayout(central_layout)

        self.browse_file = QPushButton("Browse Midi file")
        central_layout.addWidget(self.browse_file)


def create_window():
    window = MainWindow()
    window.show()
    return window
