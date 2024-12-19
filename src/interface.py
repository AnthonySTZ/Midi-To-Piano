import hou  # type: ignore
from PySide2.QtWidgets import QDialog, QVBoxLayout, QPushButton, QLineEdit, QSizePolicy
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
        self.resize(300, 150)

    def set_ui(self) -> None:
        self.setStyleSheet(
            """
            font-size: 11pt;
            """
        )
        central_layout = QVBoxLayout()
        self.setLayout(central_layout)

        self.file_path_edit = QLineEdit()
        self.file_path_edit.setPlaceholderText("Enter MIDI file path...")
        self.file_path_edit.setStyleSheet(
            """
            QLineEdit{
                padding: 2px;
            }
            """
        )
        central_layout.addWidget(self.file_path_edit)

        self.browse_file = QPushButton("Browse Midi file")
        self.browse_file.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        central_layout.addWidget(self.browse_file)

        self.accept_btn = QPushButton("Accept")
        central_layout.addWidget(self.accept_btn)


def create_window():
    window = MainWindow()
    window.show()
    return window
