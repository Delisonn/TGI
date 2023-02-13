from qt_core import *

class Ui_app_pages(object):
    def setupUi(self, app_pages):
        if not app_pages.objectName():
            app_pages.setObjectName(u"app_pages")
        app_pages.resize(1056, 739)
        self.page_spam = QWidget()
        self.page_spam.setObjectName(u"page_spam")
        self.ver_spam_layout_1 = QVBoxLayout(self.page_spam)
        self.ver_spam_layout_1.setObjectName(u"verticalLayout_2")
        self.frame_spam_1 = QFrame(self.page_spam)
        self.frame_spam_1.setContentsMargins(0, 0, 0, 0)
        self.frame_spam_1.setObjectName(u"frame_7")
        self.frame_spam_1.setStyleSheet(u"QLineEdit{\n"
                                        "	background-color: rgb(37, 38, 52);\n"
                                        "	padding: 8px;\n"
                                        "	border: 2px solid #c3ccdf;\n"
                                        "	border-radius:  10px;\n"
                                        "	color: rgb(255, 255, 255);\n"
                                        "	font: 700 14pt \"Segoe UI\";\n"
                                        "}\n"
                                        "\n"
                                        "QLabel{\n"
                                        "	font: 700 14pt \"Segoe UI\";\n"
                                        "	color: rgb(255, 255, 255);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton{\n"
                                        "	background-color: rgb(37, 38, 52);\n"
                                        "	padding: 8px;\n"
                                        "	border: 2px solid #c3ccdf;\n"
                                        "	border-radius:  15px;\n"
                                        "	font: 700 14pt \"Segoe UI\";\n"
                                        "	color: rgb(255, 255, 255);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover{\n"
                                        "	background-color: #2c2d3e;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed{\n"
                                        "	background-color: #35364a;\n"
                                        "}")
        self.frame_spam_1.setFrameShape(QFrame.StyledPanel)
        self.frame_spam_1.setFrameShadow(QFrame.Raised)
        self.hor_spam_lauout_1 = QHBoxLayout(self.frame_spam_1)
        self.hor_spam_lauout_1.setObjectName(u"horizontalLayout_2")
        self.hor_spam_lauout_1.setContentsMargins(0, 0, 0, 0)
        self.hor_spam_lauout_1.setSpacing(0)

        self.frame_spam_2 = QFrame(self.frame_spam_1)
        self.frame_spam_2.setObjectName(u"frame_8")
        self.frame_spam_2.setContentsMargins(0, 0, 0, 0)
        self.frame_spam_2.setFrameShape(QFrame.StyledPanel)
        self.frame_spam_2.setFrameShadow(QFrame.Raised)
        self.ver_spam_layout_2 = QVBoxLayout(self.frame_spam_2)
        self.ver_spam_layout_2.setObjectName(u"verticalLayout_10")

        # self.horizontalLayout_2.addWidget(self.frame_8)

        self.frame_spam_3 = QFrame(self.frame_spam_1)
        self.frame_spam_3.setObjectName(u"frame_9")
        self.frame_spam_3.setFrameShape(QFrame.StyledPanel)
        self.frame_spam_3.setFrameShadow(QFrame.Raised)
        self.frame_spam_3.setContentsMargins(0, 0, 0, 0)
        self.ver_spam_layout_3 = QVBoxLayout(self.frame_spam_3)
        self.ver_spam_layout_3.setObjectName(u"verticalLayout_11")
        self.ver_spam_layout_3.setContentsMargins(0, 0, 0, 0)
        self.spam_lbl = QLabel(self.frame_spam_3)
        self.spam_lbl.setObjectName(u"pars_lbl_2")
        self.spam_lbl.setText("Сообщение для спама")
        self.spam_lbl.setContentsMargins(0, 0, 0, 0)
        self.spam_lbl.setFixedWidth(210)

        self.ver_spam_layout_3.addWidget(self.spam_lbl, 0, Qt.AlignHCenter | Qt.AlignBottom)

        self.spam_edit = QLineEdit(self.frame_spam_3)
        self.spam_edit.setObjectName(u"spam_edit")
        self.spam_edit.setMinimumWidth(400)

        self.ver_spam_layout_3.addWidget(self.spam_edit, 0, Qt.AlignHCenter | Qt.AlignTop)

        self.spam_btn = QPushButton(self.frame_spam_3)
        self.spam_btn.setObjectName(u"pars_btn")
        self.spam_btn.setCursor(Qt.PointingHandCursor)
        self.spam_btn.setText("Спамить")
        self.spam_btn.setMinimumSize(QSize(150, 30))
        self.spam_btn.setMaximumSize(QSize(150, 45))
        self.spam_btn.setCursor(Qt.PointingHandCursor)

        self.ver_spam_layout_3.addWidget(self.spam_btn, 0, Qt.AlignHCenter | Qt.AlignVCenter)

        self.hor_spam_lauout_1.addWidget(self.frame_spam_3)

        self.frame_spam_4 = QFrame(self.frame_spam_1)
        self.frame_spam_4.setObjectName(u"frame_10")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_spam_4.sizePolicy().hasHeightForWidth())
        self.frame_spam_4.setSizePolicy(sizePolicy)
        self.frame_spam_4.setMaximumSize(QSize(400, 700))
        self.frame_spam_4.setFrameShape(QFrame.StyledPanel)
        self.frame_spam_4.setFrameShadow(QFrame.Raised)
        self.frame_spam_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12 = QVBoxLayout(self.frame_spam_4)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)

        self.ver_spam_layout_1.addWidget(self.frame_spam_1)

        # self.verticalLayout_4 = QVBoxLayout(self.page_spam)
        # self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        # self.frame = QFrame(self.page_spam)
        # self.frame.setObjectName(u"frame")
        # self.frame.setMinimumSize(QSize(500, 300))
        # self.frame.setMaximumSize(QSize(500, 300))
        # self.frame.setSizeIncrement(QSize(500, 0))
        # self.frame.setBaseSize(QSize(500, 300))
        # self.frame.setStyleSheet(u"QLineEdit{\n"
        #                          "	background-color: rgb(37, 38, 52);\n"
        #                          "	padding: 8px;\n"
        #                          "	border: 2px solid #c3ccdf;\n"
        #                          "	border-radius:  10px;\n"
        #                          "	color: rgb(255, 255, 255);\n"
        #                          "	font: 700 14pt \"Segoe UI\";\n"
        #                          "}\n"
        #                          "\n"
        #                          "QLabel{\n"
        #                          "	font: 700 14pt \"Segoe UI\";\n"
        #                          "	color: rgb(255, 255, 255);\n"
        #                          "}\n"
        #                          "\n"
        #                          "QPushButton{\n"
        #                          "	background-color: rgb(37, 38, 52);\n"
        #                          "	padding: 8px;\n"
        #                          "	border: 2px solid #c3ccdf;\n"
        #                          "	border-radius:  15px;\n"
        #                          "	font: 700 14pt \"Segoe UI\";\n"
        #                          "	color: rgb(255, 255, 255);\n"
        #                          "}\n"
        #                          "\n"
        #                          "QPushButton:hover{\n"
        #                          "	background-color: #2c2d3e;\n"
        #                          "}\n"
        #                          "\n"
        #                          "QPushButton:pressed{\n"
        #                          "	background-color: #35364a;\n"
        #                          "}")
        # self.frame.setFrameShape(QFrame.StyledPanel)
        # self.frame.setFrameShadow(QFrame.Raised)
        # self.verticalLayout_5 = QVBoxLayout(self.frame)
        # self.verticalLayout_5.setSpacing(4)
        # self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        # self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        #
        #
        #
        # self.label = QLabel(self.frame)
        # self.label.setObjectName(u"label")
        # self.label.setText("Сообщение для спама")
        # self.label.setContentsMargins(0, 0, 0, 0)
        # self.label.setFixedWidth(210)
        #
        # self.verticalLayout_5.addWidget(self.label, 0, Qt.AlignHCenter | Qt.AlignBottom)
        #
        # self.lineEdit = QLineEdit(self.frame)
        # self.lineEdit.setObjectName(u"lineEdit")
        # self.lineEdit.setMinimumWidth(400)
        # self.lineEdit.setMaximumSize(QSize(100000, 16777215))
        #
        # self.verticalLayout_5.addWidget(self.lineEdit, 0, Qt.AlignHCenter | Qt.AlignTop)
        #
        # self.pushButton_2 = QPushButton(self.frame)
        # self.pushButton_2.setObjectName(u"pushButton_2")
        # self.pushButton_2.setText("Спамить")
        # self.pushButton_2.setMinimumSize(QSize(150, 30))
        # self.pushButton_2.setMaximumSize(QSize(150, 45))
        #
        # self.verticalLayout_5.addWidget(self.pushButton_2, 0, Qt.AlignHCenter | Qt.AlignVCenter)
        #
        # self.verticalLayout_4.addWidget(self.frame)

        app_pages.addWidget(self.page_spam)
        self.page_invite_channel = QWidget()
        self.page_invite_channel.setObjectName(u"page_invite_channel")
        self.verticalLayout = QVBoxLayout(self.page_invite_channel)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_3 = QFrame(self.page_invite_channel)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(
            '''QComboBox {
    font: 18pt Fira Sans Condensed;
    background-color: rgb(37, 38, 52);
    border: 3px solid #c3ccdf;
    padding: 5%;
    max-height: 30px;
    min-width: 170px;
    color: white;
    border-radius: 12px;
    box-shadow: none;
}

QComboBox::drop-down {
    border: none;
    width: 50px;
    box-shadow: none;
}

QComboBox::down-arrow {
    image: url(:/images/icons/down-arrow.png);
    color: white;
    width: 25px;
    height: 25px;
    border-width: 0px;
    box-shadow: none;
}

QComboBox::down-arrow:on {
    image: url(:/images/icons/up-arrow.png);
    transform: rotate(180deg);
    color: white;
    width: 25px;
    height: 25px;
    border-width: 0px;
    box-shadow: none;
}

QComboBox::down-arrow:pressed {
    position: relative;
    top: 1px; left: 1px;
    box-shadow: none;
}

QComboBox QListView {
    background-color: rgb(37, 38, 52);
    color: white;
    box-shadow: none;
    padding: 5%;
}

QComboBox:editable {
    background-color: #35364a;
    min-width: 200px;
    box-shadow: none;
}

QComboBox QAbstractItemView {
    border : 3px solid #c3ccdf;
    border-radius: 7px;
    box-shadow: none;
        }'''

            # u"QComboBox{\n"
            # "	background-color: rgb(37, 38, 52);\n"
            # "	padding: 8px;\n"
            # "	border: 3px solid #c3ccdf;\n"
            # "	border-radius:  10px;\n"
            # "	color: rgb(255, 255, 255);\n"
            # "	font: 700 14pt \"Segoe UI\";\n"
            # "}\n"
            # "\n"
            "QLabel{\n"
            "	font: 700 14pt \"Segoe UI\";\n"
            "	color: rgb(255, 255, 255);\n"
            "}\n"
            "\n"
            "QPushButton{\n"
            "	background-color: rgb(37, 38, 52);\n"
            "	padding: 8px;\n"
            "	border: 2px solid #c3ccdf;\n"
            "	border-radius:  15px;\n"
            "	font: 700 14pt \"Segoe UI\";\n"
            "	color: rgb(255, 255, 255);\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "	background-color: #2c2d3e;\n"
            "}\n"
            "\n"
            "QPushButton:pressed{\n"
            "	background-color: #35364a;\n"
            "}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")

        self.invite_lbl_chats = QLabel(self.frame_4)
        self.invite_lbl_chats.setFixedWidth(200)
        self.invite_lbl_chats.setObjectName(u"invite_lbl_chats")
        self.invite_lbl_chats.setText("Добавить в чат")
        self.invite_lbl_chats.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_7.addWidget(self.invite_lbl_chats, 0, Qt.AlignCenter | Qt.AlignBottom)

        self.invite_box_chats = QComboBox(self.frame_4)
        self.invite_box_chats.setCursor(Qt.PointingHandCursor)
        self.invite_box_chats.setObjectName(u"invite_box_chats")
        self.invite_box_chats.setMinimumWidth(200)
        self.invite_box_chats.addItem("1")
        self.invite_box_chats.addItem("2")
        self.invite_box_chats.addItem("3")

        self.verticalLayout_7.addWidget(self.invite_box_chats, 0, Qt.AlignHCenter | Qt.AlignTop)

        self.invite_btn_chats = QPushButton(self.frame_4)
        self.invite_btn_chats.setObjectName(u"invite_btn_chats")
        self.invite_btn_chats.setText("Добавить")
        self.invite_btn_chats.setMinimumSize(QSize(150, 30))
        self.invite_btn_chats.setMaximumSize(QSize(150, 45))
        self.invite_btn_chats.setCursor(Qt.PointingHandCursor)

        self.verticalLayout_7.addWidget(self.invite_btn_chats, 0, Qt.AlignHCenter | Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(-1, -1, -1, 9)

        self.invite_lbl_channels = QLabel(self.frame_4)
        self.invite_lbl_channels.setFixedWidth(200)
        self.invite_lbl_channels.setObjectName(u"invite_lbl_channels")
        self.invite_lbl_channels.setText("Добавить в канал")
        self.invite_lbl_channels.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_8.addWidget(self.invite_lbl_channels, 0, Qt.AlignCenter | Qt.AlignBottom)

        self.invite_box_channels = QComboBox(self.frame_5)
        self.invite_box_channels.setCursor(Qt.PointingHandCursor)
        self.invite_box_channels.setObjectName(u"invite_box_channels")
        self.invite_box_channels.setMinimumWidth(200)

        self.verticalLayout_8.addWidget(self.invite_box_channels, 0, Qt.AlignHCenter | Qt.AlignTop)

        self.invite_btn_channels = QPushButton(self.frame_5)
        self.invite_btn_channels.setObjectName(u"invite_btn_channels")
        self.invite_btn_channels.setText("Добавить")
        self.invite_btn_channels.setMinimumSize(QSize(150, 30))
        self.invite_btn_channels.setMaximumSize(QSize(150, 45))
        self.invite_btn_channels.setCursor(Qt.PointingHandCursor)

        self.verticalLayout_8.addWidget(self.invite_btn_channels, 0, Qt.AlignHCenter | Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setMaximumSize(QSize(300, 700))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_6)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addWidget(self.frame_3)

        app_pages.addWidget(self.page_invite_channel)
        self.page_invite_chat = QWidget()
        self.page_invite_chat.setObjectName(u"page_invite_chat")
        self.ver_spam_layout_1 = QVBoxLayout(self.page_invite_chat)
        self.ver_spam_layout_1.setObjectName(u"verticalLayout_2")
        self.frame_spam_1 = QFrame(self.page_invite_chat)
        self.frame_spam_1.setContentsMargins(0, 0, 0, 0)
        self.frame_spam_1.setObjectName(u"frame_7")
        self.frame_spam_1.setStyleSheet('''QComboBox {
                font: 18pt Fira Sans Condensed;
                background-color: rgb(37, 38, 52);
                border: 3px solid #c3ccdf;
                padding: 5%;
                max-height: 30px;
                min-width: 170px;
                color: white;
                border-radius: 12px;
                box-shadow: none;
            }

            QComboBox::drop-down {
                border: none;
                width: 50px;
                box-shadow: none;
            }

            QComboBox::down-arrow {
                image: url(:/images/icons/down-arrow.png);
                color: white;
                width: 25px;
                height: 25px;
                border-width: 0px;
                box-shadow: none;
            }
            
            QComboBox::down-arrow:on {
                image: url(:/images/icons/up-arrow.png);
                transform: rotate(180deg);
                color: white;
                width: 25px;
                height: 25px;
                border-width: 0px;
                box-shadow: none;
            }

            QComboBox::down-arrow:pressed {
                position: relative;
                top: 1px; left: 1px;
                box-shadow: none;
            }

            QComboBox QListView {
                background-color: rgb(37, 38, 52);
                color: white;
                box-shadow: none;
                padding: 5%;
            }

            QComboBox:editable {
                background-color: #35364a;
                min-width: 200px;
                box-shadow: none;
            }

            QComboBox QAbstractItemView {
                border : 3px solid #c3ccdf;
                border-radius: 7px;
                box-shadow: none;
                    }'''
                                        "}\n"
                                        "\n"
                                        "QLabel{\n"
                                        "	font: 700 14pt \"Segoe UI\";\n"
                                        "	color: rgb(255, 255, 255);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton{\n"
                                        "	background-color: rgb(37, 38, 52);\n"
                                        "	padding: 8px;\n"
                                        "	border: 2px solid #c3ccdf;\n"
                                        "	border-radius:  15px;\n"
                                        "	font: 700 14pt \"Segoe UI\";\n"
                                        "	color: rgb(255, 255, 255);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover{\n"
                                        "	background-color: #2c2d3e;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed{\n"
                                        "	background-color: #35364a;\n"
                                        "}")
        self.frame_spam_1.setFrameShape(QFrame.StyledPanel)
        self.frame_spam_1.setFrameShadow(QFrame.Raised)
        self.hor_spam_lauout_1 = QHBoxLayout(self.frame_spam_1)
        self.hor_spam_lauout_1.setObjectName(u"horizontalLayout_2")
        self.hor_spam_lauout_1.setContentsMargins(0, 0, 0, 0)
        self.hor_spam_lauout_1.setSpacing(0)

        self.frame_spam_2 = QFrame(self.frame_spam_1)
        self.frame_spam_2.setObjectName(u"frame_8")
        self.frame_spam_2.setContentsMargins(0, 0, 0, 0)
        self.frame_spam_2.setFrameShape(QFrame.StyledPanel)
        self.frame_spam_2.setFrameShadow(QFrame.Raised)
        self.ver_spam_layout_2 = QVBoxLayout(self.frame_spam_2)
        self.ver_spam_layout_2.setObjectName(u"verticalLayout_10")

        # self.horizontalLayout_2.addWidget(self.frame_8)

        self.frame_spam_3 = QFrame(self.frame_spam_1)
        self.frame_spam_3.setObjectName(u"frame_9")
        self.frame_spam_3.setFrameShape(QFrame.StyledPanel)
        self.frame_spam_3.setFrameShadow(QFrame.Raised)
        self.frame_spam_3.setContentsMargins(0, 0, 0, 0)
        self.ver_spam_layout_3 = QVBoxLayout(self.frame_spam_3)
        self.ver_spam_layout_3.setObjectName(u"verticalLayout_11")
        self.ver_spam_layout_3.setContentsMargins(0, 0, 0, 0)
        self.pars_lbl = QLabel(self.frame_spam_3)
        self.pars_lbl.setObjectName(u"pars_lbl_2")
        self.pars_lbl.setText("Парсить участников")
        self.pars_lbl.setContentsMargins(0, 0, 0, 0)
        self.pars_lbl.setFixedWidth(200)

        self.ver_spam_layout_3.addWidget(self.pars_lbl, 0, Qt.AlignHCenter | Qt.AlignBottom)

        self.pars_box = QComboBox(self.frame_spam_3)
        self.pars_box.setCursor(Qt.PointingHandCursor)
        self.pars_box.setObjectName(u"pars_box")
        self.pars_box.setMinimumWidth(200)

        self.ver_spam_layout_3.addWidget(self.pars_box, 0, Qt.AlignHCenter | Qt.AlignTop)

        self.pars_btn = QPushButton(self.frame_spam_3)
        self.pars_btn.setObjectName(u"pars_btn")
        self.pars_btn.setMinimumSize(QSize(0, 0))
        self.pars_btn.setMaximumSize(QSize(16777215, 45))
        self.pars_btn.setText("Спарсить")
        self.pars_btn.setMinimumSize(QSize(150, 30))
        self.pars_btn.setMaximumSize(QSize(150, 45))
        self.pars_btn.setCursor(Qt.PointingHandCursor)

        self.ver_spam_layout_3.addWidget(self.pars_btn, 0, Qt.AlignHCenter | Qt.AlignVCenter)

        self.hor_spam_lauout_1.addWidget(self.frame_spam_3)

        self.frame_spam_4 = QFrame(self.frame_spam_1)
        self.frame_spam_4.setObjectName(u"frame_10")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_spam_4.sizePolicy().hasHeightForWidth())
        self.verticalLayout_12 = QVBoxLayout(self.frame_spam_4)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)

        self.ver_spam_layout_1.addWidget(self.frame_spam_1)

        app_pages.addWidget(self.page_invite_chat)
        self.page_setup = QWidget()
        self.page_setup.setObjectName(u"page_setup")
        self.verticalLayout_3 = QVBoxLayout(self.page_setup)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_2 = QFrame(self.page_setup)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(500, 0))
        self.frame_2.setMaximumSize(QSize(500, 400))
        self.frame_2.setStyleSheet(u"QLineEdit{\n"
                                   "	background-color: rgb(37, 38, 52);\n"
                                   "	padding: 8px;\n"
                                   "	border: 2px solid #c3ccdf;\n"
                                   "	border-radius:  10px;\n"
                                   "	color: rgb(255, 255, 255);\n"
                                   "	font: 700 14pt \"Segoe UI\";\n"
                                   "}\n"
                                   "\n"
                                   "QLabel{\n"
                                   "	font: 700 14pt \"Segoe UI\";\n"
                                   "	color: rgb(255, 255, 255);\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton{\n"
                                   "	background-color: rgb(37, 38, 52);\n"
                                   "	padding: 8px;\n"
                                   "	border: 2px solid #c3ccdf;\n"
                                   "	border-radius:  15px;\n"
                                   "	font: 700 14pt \"Segoe UI\";\n"
                                   "	color: rgb(255, 255, 255);\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton:hover{\n"
                                   "	background-color: #2c2d3e;\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton:pressed{\n"
                                   "	background-color: #35364a;\n"
                                   "}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_id = QLabel(self.frame_2)
        self.label_id.setObjectName(u"label_id")
        self.label_id.setStyleSheet(u"")

        self.verticalLayout_6.addWidget(self.label_id)

        self.id_ldt = QLineEdit(self.frame_2)
        self.val_id = QRegularExpressionValidator("[0-9]{15}")
        self.id_ldt.setValidator(self.val_id)
        self.id_ldt.setObjectName(u"id_ldt")
        self.id_ldt.setStyleSheet(u"")

        self.verticalLayout_6.addWidget(self.id_ldt)

        self.label_hash = QLabel(self.frame_2)
        self.label_hash.setObjectName(u"label_hash")

        self.verticalLayout_6.addWidget(self.label_hash)

        self.hash_ldt = QLineEdit(self.frame_2)
        self.val_hash = QRegularExpressionValidator("[a-z0-9]{32}")
        self.hash_ldt.setValidator(self.val_hash)
        self.hash_ldt.setObjectName(u"hash_ldt")

        self.verticalLayout_6.addWidget(self.hash_ldt)

        self.label_num = QLabel(self.frame_2)
        self.label_num.setObjectName(u"label_num")

        self.verticalLayout_6.addWidget(self.label_num)

        self.num_ldt = QLineEdit(self.frame_2)
        self.val_num = QRegularExpressionValidator(r"[0-9\s\+]{24}")
        self.num_ldt.setValidator(self.val_num)
        self.num_ldt.setObjectName(u"num_ldt")
        self.num_ldt.setContentsMargins(0, 0, 0, 20)

        self.verticalLayout_6.addWidget(self.num_ldt)

        self.add_btn = QPushButton(self.frame_2)
        self.add_btn.setCursor(Qt.PointingHandCursor)
        self.add_btn.setObjectName(u"add_btn")
        self.add_btn.setMinimumSize(QSize(150, 30))
        self.add_btn.setMaximumSize(QSize(150, 45))
        self.add_btn.setCursor(Qt.PointingHandCursor)

        self.verticalLayout_6.addWidget(self.add_btn, 0, Qt.AlignHCenter)

        self.verticalLayout_3.addWidget(self.frame_2, 0, Qt.AlignHCenter)

        app_pages.addWidget(self.page_setup)

        self.retranslateUi(app_pages)

        QMetaObject.connectSlotsByName(app_pages)

        # setupUi

    def retranslateUi(self, app_pages):
        app_pages.setWindowTitle(QCoreApplication.translate("app_pages", u"StackedWidget", None))
        self.label_id.setText(QCoreApplication.translate("app_pages", u"ID", None))
        self.id_ldt.setPlaceholderText(
            QCoreApplication.translate("app_pages", u"\u041f\u0440\u0438\u043c\u0435\u0440 id: 5642667", None))
        self.label_hash.setText(QCoreApplication.translate("app_pages", u"Hash", None))
        self.hash_ldt.setPlaceholderText(
            QCoreApplication.translate("app_pages", u"\u041f\u0440\u0438\u043c\u0435\u0440 hash: jhgdsjdsgj436hgdsgl",
                                       None))
        self.label_num.setText(QCoreApplication.translate("app_pages", u"Number", None))
        self.num_ldt.setPlaceholderText(QCoreApplication.translate("app_pages",
                                                                   u"\u041f\u0440\u0438\u043c\u0435\u0440 \u043d\u043e\u043c\u0435\u0440\u0430 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430: +79090456",
                                                                   None))
        self.add_btn.setText(
            QCoreApplication.translate("app_pages", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
    # retranslateUi
