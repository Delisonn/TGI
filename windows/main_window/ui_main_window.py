from qt_core import *

from scripts import *

from pages import Ui_app_pages
from widgets import PyPushButton, SvgPushButton


class Message(QFrame):
	def __init__(self, *args, **kwargs):
		super(Message, self).__init__(*args, **kwargs)

		self.resize(200, 100)
		self.setMaximumSize(200, 100)
		self.setStyleSheet('''background-color: transparent;
                        ''')

		self.layout_top = QFrame()
		self.layout_top.setFixedHeight(30)

		self.layout_top_hor = QHBoxLayout(self.layout_top)
		self.layout_top.setStyleSheet('''
                                background-color: #2c2d3e; 
                                border-top-left-radius: 15px;  
                                border-top-right-radius: 15px;  
                                ''')
		self.layout_top_hor.setContentsMargins(0, 0, 0, 0)
		self.layout_top_hor.setSpacing(0)

		self.layout_spacing = QFrame(self.layout_top)
		self.layout_spacing.setMinimumWidth(100)

		self.layout_content = QFrame()
		self.layout_content.setStyleSheet("background-color: #2c2d3e; border-bottom-right-radius: 15px; ")
		self.layout_content_hor = QHBoxLayout(self.layout_content)
		self.layout_content_hor.setContentsMargins(0, 0, 0, 0)
		self.layout_content_hor.setSpacing(0)

		self.ver = QVBoxLayout(self)
		self.ver.setContentsMargins(0, 0, 0, 0)
		self.ver.setSpacing(0)

		self.label_top_svg = QLabel(self)
		# self.label_top.setText("Успешнo!")
		self.path = ':/images/icons/'
		self.pixmap = QPixmap(self.path + 'info.svg')
		self.label_top_svg.setPixmap(self.pixmap)
		self.label_top_svg.setContentsMargins(10, 0, 0, 0)

		self.label_top_text = QLabel(self)
		# self.label_top.setText("Успешнo!")
		# self.label_top_text.setText("Успешно!")
		self.color = "white"

		self.label_top_text.style()
		self.label_top_text.setContentsMargins(5, 0, 0, 0)

		self.label_content = QLabel(self)
		# self.label_content.setText("Успешная авторизация!")
		self.label_content.setStyleSheet('''QLabel{
                             color: white;
                             font: 700 11pt
                             Segoe UI;
                             font-weight: 400;}
                             ''')
		self.label_content.setWordWrap(True)

		self.but = SvgPushButton(
			height=30,
			width=30,
			btn_color="#2c2d3e",
			btn_hover="#393a4f",
			icon_color="white",
			icon_path="close.svg",
		)

		self.but.clicked.connect(lambda: self.doClose())

		self.layout_top_hor.addWidget(self.label_top_svg, 0, Qt.AlignCenter | Qt.AlignLeft)
		self.layout_top_hor.addWidget(self.label_top_text, 0, Qt.AlignCenter | Qt.AlignLeft)
		self.layout_top_hor.addWidget(self.layout_spacing)
		self.layout_top_hor.addWidget(self.but, 0, Qt.AlignTop | Qt.AlignRight)
		self.layout_content_hor.addWidget(self.label_content, 0, Qt.AlignCenter | Qt.AlignCenter)

		self.ver.addWidget(self.layout_top)
		self.ver.addWidget(self.layout_content)

		self.effect = QGraphicsOpacityEffect(self)
		self.setGraphicsEffect(self.effect)
		self.animation = QPropertyAnimation(self.effect, b'opacity')
		self.animation.setDuration(1000)

		QTimer().singleShot(5000, lambda: self.doClose())

		# self.but.clicked.connect(lambda: self.doClose())

		# try:
		# 	self.animation.finished.disconnect(self.close)
		# except:
		# 	pass
		# self.animation.stop()
		# self.animation.setStartValue(0)
		# self.animation.setEndValue(1)
		# self.animation.start()
		self.doShow()

	def style(self,
	          color="white"):
		style = f'''QLabel{{
                            color: {color};   
                            font: 700 10pt 
                            Segoe UI bold;
                            font-weight: 800;}}
                            '''
		self.setStyleSheet(style)

	def doShow(self):
		try:
			self.animation.finished.disconnect(self.close)
		except:
			pass
		self.animation.stop()
		self.animation.setStartValue(0)
		self.animation.setEndValue(1)
		self.animation.start()

	def doClose(self):
		self.animation.stop()
		self.animation.finished.connect(self.close)  # Закройте окно, когда анимация будет завершена
		# Диапазон прозрачности постепенно уменьшается с 1 до 0.
		self.animation.setStartValue(1)
		self.animation.setEndValue(0)
		self.animation.start()


class Dialog(QFrame):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.parent = parent

		self.lbl = QLabel("Код")
		self.lbl.setFixedWidth(200)
		self.lbl.setObjectName(u"lbl")
		self.lbl.setContentsMargins(0, 0, 0, 10)
		self.lbl.setStyleSheet("QLabel{\n"
		                       "	font: 700 14pt \"Segoe UI\";\n"
		                       "	color: rgb(255, 255, 255);\n"
		                       "}\n")
		self.lineEdit = QLineEdit()
		self.val_num = QRegularExpressionValidator("[0-9]{5}")
		self.lineEdit.setValidator(self.val_num)
		self.lineEdit.setStyleSheet(u"QLineEdit{\n"
		                            "	background-color: rgb(37, 38, 52);\n"
		                            "	padding: 8px;\n"
		                            "	border: 2px solid #c3ccdf;\n"
		                            "	border-radius:  10px;\n"
		                            "	color: rgb(255, 255, 255);\n"
		                            "	font: 700 14pt \"Segoe UI\";\n"
		                            "}\n")

		self.buttonCancel = QPushButton('Отменить')
		self.buttonCancel.setCursor(Qt.PointingHandCursor)
		self.buttonCancel.setStyleSheet("QPushButton{\n"
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
		self.buttonApply = QPushButton('Подтвердить')
		self.buttonApply.setCursor(Qt.PointingHandCursor)
		self.buttonApply.setStyleSheet("QPushButton{\n"
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

		self.layout = QGridLayout(self)
		self.layout.addWidget(self.lbl, 0, 0, 1, 2, alignment=Qt.AlignCenter | Qt.AlignBottom)
		self.layout.addWidget(self.lineEdit, 0, 0, 3, 2, alignment=Qt.AlignCenter)
		self.layout.addWidget(self.buttonCancel, 4, 0)
		self.layout.addWidget(self.buttonApply, 4, 1)

		self.buttonApply.clicked.connect(self.apply)
		self.buttonCancel.clicked.connect(self._reject)

	@qasync.asyncSlot()
	async def apply(self):
		if self.parent.parent().objectName() == 'dialog_for_auth' or not tg.auth:
			await tg.authWithCode(self.lineEdit.text())
			if tg.auth:
				await tg.getGroups()
				await tg.getChannels()
				self.lineEdit.setText('')
				self.closeEvent(self)
				try:
					self.parent.parent().closeEvent(self.parent.parent())
					self.parent.parent().parent.parent().ui.top_label_right.setText(f'Account: {tg.phone}')
					self.parent.parent().parent.parent().showWindowMessage('Успешно',
					                                                       'Вход в основной аккаунт выполнен!',
					                                                       'info.svg')
				except:
					self.parent.parent().ui.top_label_right.setText(f'Account: {tg.phone}')
					self.parent.parent().showWindowMessage('Успешно',
					                                       'Вход в основной аккаунт выполнен!',
					                                       'info.svg')
				return
		# elif tg.temp:
		# 	...
		# 	if await tg.addClientAuthAuto(self.lineEdit.text()):
		# 		self.lineEdit.setText('')
		# 		self.closeEvent(self)
		# 		return
		else:
			await tg.addClientAuth(self.lineEdit.text())
			if tg.add_auth:
				self.parent.parent().ui.ui_pages.add_btn.setEnabled(True)
				self.lineEdit.setText('')
				self.closeEvent(self)
				self.parent.parent().showWindowMessage('Успешно', 'Аккаунт успешно добавлен!', 'info.svg')
				return
		self.lineEdit.setPlaceholderText('An invalid code was entered.')
		try:
			self.parent.parent().showWindowMessage('Ошибка', 'Не удалось добавить аккаунт!', 'error.svg')
		except:
			self.parent.parent().parent.parent().showWindowMessage('Ошибка', 'Не удалось добавить аккаунт!', 'error.svg')
		self.lineEdit.setText('')

	@qasync.asyncSlot()
	async def _reject(self):
		if not tg.auth:
			exit()
		try:
			self.parent.parent().buttonApply_auth.setEnabled(True)
		except:
			try:
				self.parent.parent().ui.ui_pages.add_btn.setEnabled(True)
			except:
				pass
			await tg.add_client.disconnect()
			__import__('os').remove(f'{tg.add_phone}.session')
		finally:
			self.parent.hide()

	def closeEvent(self, event):
		self.parent.hide()


class Dialog_For_Auth(QFrame):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.parent = parent
		self.setMinimumSize(300, 400)

		self.id_lbl = QLabel("Id")
		self.id_lbl.setObjectName(u"id_lbl")
		self.id_lbl.setContentsMargins(130, 0, 0, 0)
		self.id_lbl.setStyleSheet("QLabel{\n"
		                          "	font: 700 14pt \"Segoe UI\";\n"
		                          "	color: rgb(255, 255, 255);\n"
		                          "}\n")
		self.id_lnd = QLineEdit()
		self.val_id = QRegularExpressionValidator("[0-9]{15}")
		self.id_lnd.setValidator(self.val_id)
		self.id_lnd.setObjectName(u"id_lnd")
		self.id_lnd.setContentsMargins(0, 0, 0, 0)
		self.id_lnd.setStyleSheet(u"QLineEdit{\n"
		                          "	background-color: rgb(37, 38, 52);\n"
		                          "	padding: 8px;\n"
		                          "	border: 2px solid #c3ccdf;\n"
		                          "	border-radius:  10px;\n"
		                          "	color: rgb(255, 255, 255);\n"
		                          "	font: 700 14pt \"Segoe UI\";\n"
		                          "}\n")

		self.hash_lbl = QLabel("Hash")
		self.hash_lbl.setObjectName(u"hash_lbl")
		self.hash_lbl.setContentsMargins(130, 0, 0, 0)
		self.hash_lbl.setStyleSheet("QLabel{\n"
		                            "	font: 700 14pt \"Segoe UI\";\n"
		                            "	color: rgb(255, 255, 255);\n"
		                            "}\n")
		self.hash_lnd = QLineEdit()
		self.val_hash = QRegularExpressionValidator("[a-z0-9]{32}")
		self.hash_lnd.setValidator(self.val_hash)
		self.hash_lnd.setObjectName(u"hash_lnd")
		self.hash_lnd.setStyleSheet(u"QLineEdit{\n"
		                            "	background-color: rgb(37, 38, 52);\n"
		                            "	padding: 8px;\n"
		                            "	border: 2px solid #c3ccdf;\n"
		                            "	border-radius:  10px;\n"
		                            "	color: rgb(255, 255, 255);\n"
		                            "	font: 700 14pt \"Segoe UI\";\n"
		                            "}\n")

		self.num_lbl = QLabel("Num")
		self.num_lbl.setObjectName(u"num_lbl")
		self.num_lbl.setContentsMargins(130, 0, 0, 0)
		self.num_lbl.setStyleSheet("QLabel{\n"
		                           "	font: 700 14pt \"Segoe UI\";\n"
		                           "	color: rgb(255, 255, 255);\n"
		                           "}\n")
		self.num_lnd = QLineEdit()
		self.val_num = QRegularExpressionValidator(r"[0-9\s\+]{24}")
		self.num_lnd.setValidator(self.val_num)
		self.num_lnd.setObjectName(u"num_lnd")
		self.num_lnd.setStyleSheet(u"QLineEdit{\n"
		                           "	background-color: rgb(37, 38, 52);\n"
		                           "	padding: 8px;\n"
		                           "	border: 2px solid #c3ccdf;\n"
		                           "	border-radius:  10px;\n"
		                           "	color: rgb(255, 255, 255);\n"
		                           "	font: 700 14pt \"Segoe UI\";\n"
		                           "}\n")

		self.buttonCancel_auth = QPushButton('Отменить')
		self.buttonCancel_auth.setCursor(Qt.PointingHandCursor)
		self.buttonCancel_auth.setStyleSheet("QPushButton{\n"
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
		self.buttonApply_auth = QPushButton('Подтвердить')
		self.buttonApply_auth.setCursor(Qt.PointingHandCursor)
		self.buttonApply_auth.setStyleSheet("QPushButton{\n"
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

		self.layout = QGridLayout(self)
		self.layout.addWidget(self.id_lbl, 0, 0, 1, 0, alignment=Qt.AlignLeft)
		self.layout.addWidget(self.id_lnd, 1, 0, 2, 2, alignment=Qt.AlignCenter)
		self.layout.addWidget(self.hash_lbl, 2, 0, 3, 0, alignment=Qt.AlignLeft)
		self.layout.addWidget(self.hash_lnd, 3, 0, 4, 2, alignment=Qt.AlignCenter)
		self.layout.addWidget(self.num_lbl, 4, 0, 5, 0, alignment=Qt.AlignLeft)
		self.layout.addWidget(self.num_lnd, 5, 0, 6, 2, alignment=Qt.AlignCenter)
		self.layout.addWidget(self.buttonCancel_auth, 10, 0)
		self.layout.addWidget(self.buttonApply_auth, 10, 1)

		self.buttonApply_auth.clicked.connect(self.apply)
		self.buttonCancel_auth.clicked.connect(self._reject)

	@qasync.asyncSlot()
	async def apply(self):
		# Setup to config data
		if self.id_lnd.text() and self.hash_lnd.text() and self.num_lnd.text():
			self.buttonApply_auth.setEnabled(False)
			tg.configSetup(self.id_lnd.text(), self.hash_lnd.text(), self.num_lnd.text())
			window = Window(self)
			try:
				await tg.mainConnect()
			except:
				self.buttonApply_auth.setEnabled(True)
				self.parent.parent().showWindowMessage('Ошибка', 'Введены некорректные данные!', 'error.svg', color='#D52020')
				return
			window.resize(self.size())
			window.show()

	@qasync.asyncSlot()
	async def _reject(self):
		self.parent.close()
		try:
			try:
				await tg.client.disconnect()
			except:
				pass
			__import__('os').remove(f'{tg.phone}.session')
			__import__('os').remove('config.data')
		except:
			pass
		__import__('sys').exit()

	def closeEvent(self, event):
		self.parent.hide()


class Window_For_Auth(QFrame):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.setObjectName(u"window_for_auth")
		self.setStyleSheet("""#window_for_auth {
                                     background-color: rgba(33, 32, 32, 0.9);
                                     color: #bfbfbf;
                                     border-radius: 15px;
                                     }""")

		self.dialog = Dialog_For_Auth(self)
		self.dialog.setObjectName(u"dialog_for_auth")
		self.dialog.setStyleSheet("""#dialog_for_auth{
                                     background-color: #32344f;
                                     color: #bfbfbf;
                                     border-radius: 10px;
                                     border: 2px solid #c3ccdf;
                                     }""")

		gridLayout = QGridLayout(self)
		gridLayout.addWidget(self.dialog, 1, 1, 1, 1)

		gridLayout.setColumnStretch(0, 1)
		gridLayout.setColumnStretch(1, 2)
		gridLayout.setColumnStretch(2, 1)
		gridLayout.setRowStretch(0, 1)
		gridLayout.setRowStretch(1, 2)
		gridLayout.setRowStretch(2, 1)

	def closeWindow(self):
		self.close()


class Window(QFrame):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.setObjectName(u"window")
		self.setStyleSheet("""#window {
                                     background-color: rgba(33, 32, 32, 0.9);
                                     color: #bfbfbf;
                                     }""")

		self.dialog = Dialog(self)
		self.dialog.setObjectName(u"dialog")
		self.dialog.setStyleSheet("""#dialog{
                                     background-color: #32344f;
                                     color: #bfbfbf;
                                     border-radius: 10px;
                                     border: 2px solid #c3ccdf;
                                     }""")

		gridLayout = QGridLayout(self)
		gridLayout.addWidget(self.dialog, 1, 1, 1, 1)

		gridLayout.setColumnStretch(0, 1)
		gridLayout.setColumnStretch(1, 2)
		gridLayout.setColumnStretch(2, 1)
		gridLayout.setRowStretch(0, 1)
		gridLayout.setRowStretch(1, 2)
		gridLayout.setRowStretch(2, 1)


class UI_MainWindow(object):
	def __init__(self):
		self.toggle_button = None
		self.top_bar = None
		self.content = None
		self.left_menu = None
		self.central_frame = None
		self.main_layout = None

	def setup_ui(self, parent):
		if not parent.objectName():
			parent.setObjectName("MainWindow")

		parent.resize(1000, 580)
		parent.setMinimumSize(900, 500)
		self.parent = parent

		# Central widget
		self.main_frame = QFrame()
		self.central_frame = QFrame(self.main_frame)

		self.main_frame_ver = QVBoxLayout(self.main_frame)
		self.main_frame_ver.setContentsMargins(0, 0, 0, 0)
		self.main_frame_ver.setSpacing(0)

		# For move window
		self.area_for_goes = QFrame(self.main_frame)
		self.area_for_goes.setMinimumHeight(30)
		self.area_for_goes.setMaximumHeight(30)

		# Move window frame
		self.move_frame = QFrame(self.area_for_goes)
		self.move_frame.setMinimumHeight(30)
		self.move_frame.setMaximumHeight(30)
		self.area_for_goes.setStyleSheet(
			"background-color: #181922; color: #6272a4; border-top-left-radius: 15px; border-top-right-radius: 15px;")

		# Manage button window frame
		self.frame_manage_buttons = QFrame(self.area_for_goes)
		self.frame_manage_buttons.setMinimumHeight(30)
		self.frame_manage_buttons.setMaximumHeight(30)
		self.frame_manage_buttons.setMinimumWidth(70)
		self.frame_manage_buttons.setMaximumWidth(70)
		self.frame_manage_buttons.setStyleSheet("background-color: #181922; color: #6272a4;")

		self.frame_manage_buttons_hor = QHBoxLayout(self.frame_manage_buttons)
		self.frame_manage_buttons_hor.setContentsMargins(0, 0, 0, 0)
		self.frame_manage_buttons_hor.setSpacing(0)

		# -=======Create buttons========-
		# Close button
		self.close_button = SvgPushButton(
			height=30,
			width=35,
			btn_color="#181922",
			icon_color="white",
			icon_path="close.svg"
		)

		# MinMax button
		# self.min_max_button = SvgPushButton(
		#     height=30,
		#     width=35,
		#     btn_color="#181922",
		#     icon_color="white",
		#     icon_path="collapse.svg"
		# )

		# Hide button
		self.hide_button = SvgPushButton(
			height=30,
			width=35,
			btn_color="#181922",
			icon_color="white",
			icon_path="minus.svg"
		)

		# Create area for buttons
		self.area_for_goes_hor = QHBoxLayout(self.area_for_goes)
		self.area_for_goes_hor.setContentsMargins(0, 0, 0, 0)

		# Add buttons widget to frame
		self.frame_manage_buttons_hor.addWidget(self.hide_button)
		# self.frame_manage_buttons_hor.addWidget(self.min_max_button)
		self.frame_manage_buttons_hor.addWidget(self.close_button)

		# Main layout
		self.main_layout = QHBoxLayout(self.central_frame)
		self.main_layout.setContentsMargins(0, 0, 0, 0)
		self.main_layout.setSpacing(0)

		# -=======Left menu======-
		self.left_menu = QFrame()
		self.left_menu.setStyleSheet("background-color: #252634; border-bottom-left-radius: 15px")
		self.left_menu.setMaximumWidth(70)
		self.left_menu.setMinimumWidth(70)
		self.left_menu.setContentsMargins(0, 0, 0, 0)

		# Left menu layout
		self.left_menu_layout = QVBoxLayout(self.left_menu)
		self.left_menu_layout.setContentsMargins(0, 0, 0, 0)
		self.left_menu_layout.setSpacing(0)

		# Top frame menu
		self.left_menu_top_frame = QFrame()
		self.left_menu_top_frame.setMinimumHeight(50)
		self.left_menu_top_frame.setObjectName("left_menu_top_frame")

		# Top frame layout
		self.left_menu_top_layout = QVBoxLayout(self.left_menu_top_frame)
		self.left_menu_top_layout.setContentsMargins(0, 0, 0, 0)
		self.left_menu_top_layout.setSpacing(0)

		# Top btns
		self.toggle_button = PyPushButton(
			text="Скрыть меню",
			icon_path="left_menu.svg"
		)
		self.btn_1 = PyPushButton(
			text="Добавить аккаунт",
			is_active=True,
			icon_path="add-account.svg"
		)
		self.btn_2 = PyPushButton(
			text="Парсить участников",
			icon_path="invite_chat.svg"
		)
		self.btn_3 = PyPushButton(
			text="Спамить в лс",
			icon_path="spam.svg"
		)
		self.btn_4 = PyPushButton(
			text="Пригласить в чат/группу",
			icon_path="invite_channel.svg"
		)

		# Add btns to layout
		self.left_menu_top_layout.addWidget(self.toggle_button)
		self.left_menu_top_layout.addWidget(self.btn_1)
		self.left_menu_top_layout.addWidget(self.btn_2)
		self.left_menu_top_layout.addWidget(self.btn_3)
		self.left_menu_top_layout.addWidget(self.btn_4)

		# Menu spacer
		self.left_menu_spacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

		# Label version
		self.left_menu_label_version = QLabel("v1.0.0")
		self.left_menu_label_version.setAlignment(Qt.AlignCenter)
		self.left_menu_label_version.setMinimumHeight(30)
		self.left_menu_label_version.setMaximumHeight(30)
		self.left_menu_label_version.setStyleSheet("color: #c3ccdf")

		# Add to layout
		self.left_menu_layout.addWidget(self.left_menu_top_frame)
		self.left_menu_layout.addItem(self.left_menu_spacer)
		self.left_menu_layout.addWidget(self.left_menu_label_version)

		# Content
		self.content = QFrame()
		self.content.setStyleSheet("background-color: #35364a; border-bottom-right-radius: 15px")

		# Content layout
		self.content_layout = QVBoxLayout(self.content)
		self.content_layout.setContentsMargins(0, 0, 0, 0)
		self.content_layout.setSpacing(0)

		# -=========TopBar========-
		self.top_bar = QFrame()
		self.top_bar.setMinimumHeight(30)
		self.top_bar.setMaximumHeight(30)
		self.top_bar.setStyleSheet("background-color: #252634; color: #6272a4; border-bottom-right-radius: 0px")
		self.top_bar_layout_ver = QVBoxLayout(self.top_bar)
		self.top_bar_layout_ver.setSpacing(0)
		self.top_bar_layout_ver.setContentsMargins(0, 0, 0, 0)

		# For bottom labels
		self.area_for_labels = QFrame(self.top_bar)
		self.area_for_labels.setMinimumHeight(30)
		self.area_for_labels.setMaximumHeight(30)
		self.area_for_labels.setStyleSheet("background-color: #252634; color: #6272a4;")

		# left label
		self.top_label_left = QLabel("Добавить аккаунт")

		# top spacer
		self.top_spacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

		# Right Label
		self.top_label_right = QLabel("| Top Right label")
		self.top_label_right.setStyleSheet("font: 700 9pt 'Segoe UI'")

		# Create area for labels
		self.area_for_labels_hor = QHBoxLayout(self.area_for_labels)
		self.area_for_labels_hor.setContentsMargins(10, 0, 10, 0)

		# Add labels widget to frame
		self.area_for_labels_hor.addWidget(self.top_label_left)
		self.area_for_labels_hor.addItem(self.top_spacer)
		self.area_for_labels_hor.addWidget(self.top_label_right)

		# Add frame to layout
		self.area_for_goes_hor.addWidget(self.move_frame)
		self.area_for_goes_hor.addWidget(self.frame_manage_buttons)
		self.top_bar_layout_ver.addWidget(self.area_for_labels)

		# -======App pages=======-
		self.pages = QStackedWidget()
		self.pages.setStyleSheet("font-size: 24pt; color: #f8f8f2")
		self.ui_pages = Ui_app_pages()
		self.ui_pages.setupUi(self.pages)
		self.pages.setCurrentWidget(self.ui_pages.page_setup)

		# -======BottomBar=======-
		self.bottom_bar = QFrame()
		self.bottom_bar.setMinimumHeight(30)
		self.bottom_bar.setMaximumHeight(30)
		self.bottom_bar.setStyleSheet("background-color: #252634; color: #6272a4;")

		self.bottom_bar_layout = QHBoxLayout(self.bottom_bar)
		self.bottom_bar_layout.setContentsMargins(10, 0, 10, 0)

		# left label
		self.bottom_label_left = QLabel("TG Author: @delisoon")

		# top spacer
		self.bottom_spacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

		# Right Label
		self.bottom_label_right = QLabel("© 2023")
		self.bottom_label_right.setStyleSheet("font: 700 9pt 'Segoe UI'")

		# Add to layout
		self.bottom_bar_layout.addWidget(self.bottom_label_left)
		self.bottom_bar_layout.addItem(self.bottom_spacer)
		self.bottom_bar_layout.addWidget(self.bottom_label_right)

		# Add to content layout
		self.content_layout.addWidget(self.top_bar)
		self.content_layout.addWidget(self.pages)
		self.content_layout.addWidget(self.bottom_bar)

		# Add widgets to app
		self.main_layout.addWidget(self.left_menu)
		self.main_layout.addWidget(self.content)

		self.main_frame_ver.addWidget(self.area_for_goes)
		self.main_frame_ver.addWidget(self.central_frame)

		# self.hide_button.clicked.connect(parent.hide)
		# self.min_max_button.clicked.connect(self.showMaximized)
		self.close_button.clicked.connect(self.clientDisconnect)

		# Set central widget
		parent.setCentralWidget(self.main_frame)

	@qasync.asyncSlot()
	async def clientDisconnect(self):
		try:
			await tg.client.disconnect()
		except:
			pass
		finally:
			self.parent.close()
			__import__('sys').exit()
