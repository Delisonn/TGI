import os

from qt_core import *


class SvgPushLabel(QLabel):
    def __init__(
            self,
            height=30,
            width=40,
            icon_path="",
            icon_color="black",
            btn_color="#252634",
            btn_hover="#2c2d3e",
            btn_pressed="#35364a",
    ):
        super().__init__()

        # Set default parameters
        self.setMaximumHeight(height)
        self.setMinimumHeight(height)

        # Cursor parameter
        self.width = width
        self.icon_path = icon_path
        self.icon_color = icon_color
        self.btn_color = btn_color
        self.btn_hover = btn_hover
        self.btn_pressed = btn_pressed

        # Set style
        self.setStyle(
            btn_color=self.btn_color,
            btn_hover=self.btn_hover,
            btn_pressed=self.btn_pressed,
        )



    def setStyle(
            self,
            btn_color="#252634",
            btn_hover="#2c2d3e",
            btn_pressed="#35364a",
    ):
        style = f"""
        QPushButton {{
            background-color: {btn_color};
            border: none;
        }}
        QPushButton:hover {{
            background-color: {btn_hover};
        }}

        QPushButton:pressed {{
            background-color: {btn_pressed};
        }}
        """
        self.setStyleSheet(style)

    def paintEvent(self, event):
        # Return default style
        QPushButton.paintEvent(self, event)

        # painter
        qp = QPainter()
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing)
        qp.setPen(Qt.NoPen)

        rect = QRect(0, 0, self.width, self.height())

        self.draw_icon(qp, self.icon_path, rect, self.icon_color)

        qp.end()

    def draw_icon(self, qp, image, rect, color):
        # Format PAth
        app_path = os.path.abspath(os.getcwd())
        folder = ":/images/icons/"
        path = os.path.join(folder)
        icon_path = os.path.normpath(os.path.join(path, image))

        # Draw icon
        icon = QPixmap(icon_path)
        painter = QPainter(icon)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(icon.rect(), color)
        qp.drawPixmap(
            (rect.width() - icon.width()) / 2,
            (rect.height() - icon.height()) / 2,
            icon
        )
        painter.end()
