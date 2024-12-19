import os
import piano
import hou  # type: ignore
from PySide2.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QPushButton,
    QLineEdit,
    QSizePolicy,
    QFileDialog,
    QLabel,
    QHBoxLayout,
    QWidget,
)
from PySide2.QtCore import Qt
import hou_nodes


class MainWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.set_window_settings()
        self.set_ui()
        self.set_functionnals()

    def set_window_settings(self) -> None:
        self.setParent(hou.ui.mainQtWindow(), Qt.Window)
        self.setWindowTitle("Midi Piano")
        self.resize(400, 150)

    def set_ui(self) -> None:
        self.setStyleSheet(
            """
            font-size: 11pt;
            """
        )
        central_layout = QVBoxLayout()
        self.setLayout(central_layout)

        infos_label = QLabel(
            "Be sure to have a 'note' attribute on your points in range 0-87"
        )
        central_layout.addWidget(infos_label)

        file_layout = QHBoxLayout()
        file_widget = QWidget()
        file_widget.setLayout(file_layout)
        central_layout.addWidget(file_widget)

        file_path_label = QLabel("MIDI Path :")
        file_layout.addWidget(file_path_label)

        self.file_path_edit = QLineEdit()
        self.file_path_edit.setPlaceholderText("Enter MIDI file path...")
        self.file_path_edit.setStyleSheet(
            """
            QLineEdit{
                padding: 2px;
            }
            """
        )
        file_layout.addWidget(self.file_path_edit)

        frame_layout = QHBoxLayout()
        frame_widget = QWidget()
        frame_widget.setLayout(frame_layout)
        central_layout.addWidget(frame_widget)

        frame_label = QLabel("Start frame :")
        frame_layout.addWidget(frame_label)

        self.start_frame_edit = QLineEdit()
        self.start_frame_edit.setPlaceholderText("Enter start frame...")
        self.start_frame_edit.setText(str(hou_nodes.get_start_frame()))
        self.start_frame_edit.setStyleSheet(
            """
            QLineEdit{
                padding: 2px;
            }
            """
        )
        frame_layout.addWidget(self.start_frame_edit)

        self.browse_file_btn = QPushButton("Browse Midi file")
        self.browse_file_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        central_layout.addWidget(self.browse_file_btn)

        self.accept_btn = QPushButton("Accept")
        central_layout.addWidget(self.accept_btn)

    def set_functionnals(self) -> None:
        self.browse_file_btn.pressed.connect(self.browse_file)
        self.accept_btn.pressed.connect(self.accept_file)

    def browse_file(self) -> None:
        file_path = QFileDialog.getOpenFileName(
            self, "Open Midi File", "", "Midi Files (*.mid)"
        )
        if file_path:
            self.file_path_edit.setText(file_path[0])

    def accept_file(self) -> None:
        file_path: str = self.file_path_edit.text()
        start_frame: str = self.start_frame_edit.text()
        if not os.path.exists(file_path):
            return

        if not file_path.endswith(".mid"):
            return

        if not start_frame.isnumeric():
            start_frame = hou_nodes.get_start_frame()

        piano.run(file_path, int(start_frame))
        self.close()


def create_window():
    window = MainWindow()
    window.show()
    return window


create_window()
