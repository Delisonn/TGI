id_pr = __import__('wmi').WMI().Win32_Processor()[0].processorId
import resources
from qt_core import *
from aiohttp import ClientSession
from datetime import datetime
from mysql.connector import connect

from scripts import *
from windows import UI_MainWindow, Window, Window_For_Auth, Message


class MainWindow(QMainWindow):
    def __init__(self, loop=None):
        super().__init__()
        self.dragPos = None
        self.setWindowTitle('Tg inviter')

        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

        def moveWindow(event: QMouseEvent):
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.move_frame.mouseMoveEvent = moveWindow

        # Установите прозрачность фона
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        # Установите без границ
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)

        # Toggle button
        self.ui.toggle_button.clicked.connect(self.toggle_button)

        # Btn home
        self.ui.btn_1.clicked.connect(self.show_page_setup)

        self.ui.btn_2.clicked.connect(self.show_page_parse)
        # Filling comboboxes on the page with data
        self.ui.btn_2.clicked.connect(self.setDataCombobox)

        self.ui.btn_3.clicked.connect(self.show_page_spam)

        self.ui.btn_4.clicked.connect(self.show_page_invite)
        # Filling comboboxes on the page with data
        self.ui.btn_4.clicked.connect(self.setDataCombobox)

        self.window_for_auth = Window_For_Auth(self)
        self.window_for_auth.hide()

        self.window = Window(self)
        self.window.hide()
        # Btn parsing users
        self.ui.ui_pages.pars_btn.clicked.connect(self.parseUsers)

        # Btn add client
        self.ui.ui_pages.add_btn.clicked.connect(self.addClient)
        # self.ui.ui_pages.add_btn.clicked.connect(self.addClientAuto)

        # Btn invite to chat
        self.ui.ui_pages.invite_btn_chats.clicked.connect(self.inviteToChat)
        # Btn invite to channel
        self.ui.ui_pages.invite_btn_channels.clicked.connect(self.inviteToChannel)
        # Btn spam to users
        self.ui.ui_pages.spam_btn.clicked.connect(self.spamToUsers)

        self.show()

        self.ui.hide_button.clicked.connect(lambda: self.showMinimized())
        self.loop = loop or asyncio.get_event_loop()

    def showWindowMessage(self, text_top='Успешно', text_content='Хуй пойми что', icon_path='', color='white'):
        self.window_message = Message(self)
        self.window_message.style(color=color)
        self.window_message.label_top_text.setText(text_top)
        self.window_message.label_content.setText(text_content)
        self.window_message.pixmap = QPixmap(self.window_message.path + icon_path)
        self.window_message.label_top_svg.setPixmap(self.window_message.pixmap)
        self.window_message.resize(self.size())
        self.window_message.move(self.width() - 210, self.height() - 140)
        self.window_message.show()

    # @qasync.asyncSlot()
    # async def addClientAuto(self):
    # 	self.ui.ui_pages.add_btn.setEnabled(False)
    # 	try:
    # 		# await tg.addClientAuto(self)
    # 		tgm_accounts = await tg.checkAccounts()
    # 		if not tgm_accounts:
    # 			self.showWindowMessage('Ошибка', 'Нет авторизованных аккаунтов!', 'error.svg', color='#D52020')
    # 			return
    #
    # 		# for account in tgm_accounts:
    # 		# print(account)
    # 		self.create_dialog_code()
    #
    # 	# while not tg.auth2 or tg.temp:
    # 	# 	pass
    # 	# if not tg.temp:
    # 	# 	continue
    # 	except Exception as e:
    # 		# TODO: Вывод уведомления про некорректные данные, скорее всего сделаю чтобы понимать какие
    # 		print(e)
    # 		self.showWindowMessage('Ошибка', 'Не удалось добавить аккаунт!', 'error.svg', color='#D52020')
    # 		self.ui.ui_pages.add_btn.setEnabled(True)

    @qasync.asyncSlot()
    async def addClient(self):
        self.ui.ui_pages.add_btn.setEnabled(False)
        try:
            await tg.addClient(
                api_id=self.ui.ui_pages.id_ldt.text(),
                api_hash=self.ui.ui_pages.hash_ldt.text(),
                phone=self.ui.ui_pages.num_ldt.text()
            )
            if tg.add_auth:
                self.showWindowMessage('Успешно', 'Аккаунт успешно добавлен!', 'info.svg')
                await asyncio.sleep(2)
                self.ui.ui_pages.add_btn.setEnabled(True)
            else:
                self.create_dialog_code()
        except Exception as e:
            # TODO: Вывод уведомления про некорректные данные, скорее всего сделаю чтобы понимать какие
            print(e)
            self.showWindowMessage('Ошибка', 'Не удалось добавить аккаунт!', 'error.svg', color='#D52020')
            self.ui.ui_pages.add_btn.setEnabled(True)

    @qasync.asyncSlot()
    async def parseUsers(self):
        self.ui.ui_pages.pars_btn.setEnabled(False)
        try:
            # self.showWindowMessage('Успешно', 'Парсинг начался! Подождите...', 'info.svg')
            time_load = await tg.enteringUsers(self.ui.ui_pages.pars_box.currentData())
            self.showWindowMessage('Успешно',
                                   f'Парсинг прошёл успешно за {int(time_load)} с.! Следущяя попытка доступна через 5 сек.',
                                   'info.svg')
        except Exception as e:
            print(f'Slot error: {e}')
            self.showWindowMessage('Ошибка', 'Не удалось выполнить парсинг! Для следующей попытки подождите 5 сек.',
                                   'error.svg', color='#D52020')
        await asyncio.sleep(5)
        self.ui.ui_pages.pars_btn.setEnabled(True)

    @qasync.asyncSlot()
    async def inviteToChat(self):
        self.ui.ui_pages.invite_btn_chats.setEnabled(False)
        try:
            await tg.inviteToChat(self.ui.ui_pages.invite_box_chats.currentData(), self)
        except Exception as e:
            print(f'Slot error: {e}')
            self.showWindowMessage('Ошибка', 'Не удалось выполнить инвайт!', 'error.svg', color='#D52020')
        await asyncio.sleep(3)
        self.ui.ui_pages.invite_btn_chats.setEnabled(True)

    @qasync.asyncSlot()
    async def inviteToChannel(self):
        self.ui.ui_pages.invite_btn_channels.setEnabled(False)
        try:
            await tg.inviteToChannel(self.ui.ui_pages.invite_box_channels.currentData(), self)
        except Exception as e:
            print(f'Slot error: {e}')
            self.showWindowMessage('Ошибка', 'Не удалось выполнить инвайт!', 'error.svg', color='#D52020')
        await asyncio.sleep(3)
        self.ui.ui_pages.invite_btn_channels.setEnabled(True)

    @qasync.asyncSlot()
    async def spamToUsers(self):
        self.ui.ui_pages.spam_btn.setEnabled(False)
        try:
            message = self.ui.ui_pages.spam_edit.text()
            if message:
                await tg.spamToUsers(message, self)
            else:
                self.showWindowMessage('Ошибка', 'Попытка отправить пустое сообщение!', 'error.svg', color='#D52020')
        except Exception as e:
            print(f'Slot error: {e}')
            self.showWindowMessage('Ошибка', 'Не удалось выполнить инвайт!', 'error.svg', color='#D52020')
        await asyncio.sleep(3)
        self.ui.ui_pages.spam_btn.setEnabled(True)

    # Set data to combobox
    def setDataCombobox(self):
        self.ui.ui_pages.pars_box.clear()
        self.ui.ui_pages.invite_box_chats.clear()
        self.ui.ui_pages.invite_box_channels.clear()
        for g in tg.groups:
            self.ui.ui_pages.pars_box.addItem(g.title, g)
            self.ui.ui_pages.invite_box_chats.addItem(g.title, g)
        for c in tg.channels:
            self.ui.ui_pages.invite_box_channels.addItem(c.title, c)

    def mousePressEvent(self, event: QMouseEvent):
        self.dragPos = event.globalPos()

    def auth_main_acc(self):
        self.window_for_auth.resize(self.size())
        self.window_for_auth.show()

    def create_dialog_code(self):
        self.window.resize(self.size())
        self.window.show()

    def resetSelection(self):
        for btn in self.ui.left_menu.findChildren(QPushButton):
            try:
                btn.setActive(False)
            except:
                pass

    def show_page_setup(self):
        self.resetSelection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_setup)
        self.ui.top_label_left.setText("Добавить аккаунт")
        self.ui.btn_1.setActive(True)

    def show_page_spam(self):
        self.resetSelection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_spam)
        self.ui.top_label_left.setText("Спамить")
        self.ui.btn_3.setActive(True)

    def show_page_parse(self):
        self.resetSelection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_invite_chat)
        self.ui.top_label_left.setText("Спарсить участников")
        self.ui.btn_2.setActive(True)

    def show_page_invite(self):
        self.resetSelection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_invite_channel)
        self.ui.top_label_left.setText("Добавить в канал/чат")
        self.ui.btn_4.setActive(True)

    def toggle_button(self):
        # Get menu width
        menu_width = self.ui.left_menu.width()

        # Check width
        width = 70
        if menu_width == 70:
            width = 240

        # Start animation
        self.animation = QPropertyAnimation(self.ui.left_menu, b"minimumWidth")
        self.animation.setStartValue(menu_width)
        self.animation.setEndValue(width)
        self.animation.setDuration(500)
        self.animation.setEasingCurve(QEasingCurve.InOutCirc)
        self.animation.start()


_ = ...


def main():
    global _
    _ = __import__('time').time()
    app = QApplication()
    loop = qasync.QEventLoop(app)
    loop2 = asyncio.get_event_loop()
    asyncio.set_event_loop(loop)
    asyncio.set_event_loop(loop2)

    window = MainWindow(loop)
    window.show()
    with loop:
        loop2.run_until_complete(main1(window, loop2))
        loop.run_forever()


async def main1(window: MainWindow, loop2) -> None:
    global id_pr
    async with __import__('aiofiles').open('key.txt', 'r') as f:
        key = (await f.readline()).rstrip('\r\n')
    async with ClientSession() as session:
        async with session.get('..............................') as response:
            html = await response.json()
            date = datetime.strptime(html['datetime'], '%Y-%m-%dT%H:%M:%S.%f%z')
            exterminated_date = datetime(date.year, date.month, date.day)
    with connect(
            host='......................',
            user='...........', password='.............',
            database='...........'
    ) as connection:
        with connection.cursor() as cursor:
            try:
                cursor.execute(f'INSERT INTO access(key_fk, id_pr) VALUES("{key}", "{id_pr}");')
                connection.commit()
            except Exception as e:
                print(e)
                pass
            cursor.execute(
                f'SELECT a.`key_fk`, k.`date`, a.`id_pr` FROM `keys` k INNER JOIN `access` a ON k.`key_pk` = a.`key_fk` WHERE k.`key_pk` = "{key}";')
            result = cursor.fetchone()
            if not result:
                exit()
            key_fk_bd, date_bd, id_pr_bd = result
            if key_fk_bd != key or date_bd <= exterminated_date or id_pr_bd != id_pr:
                exit()
    try:
        # Checking for the existence of a "config.data" file
        if not __import__('os').path.exists('config.data'):
            # Calling a dialog box for entering authorization data
            window.auth_main_acc()
        else:
            try:
                # Trying connection to account
                await tg.mainConnect()
                # Check authorization
                if tg.auth:
                    print(f'{"%.3f" % (__import__("time").time() - _)} seconds')
                    window.ui.top_label_right.setText(f'Account: {tg.phone}')
                    await tg.getGroups()
                    await tg.getChannels()
                else:
                    # if not authorized, calling a dialog box for entering authorization code
                    window.create_dialog_code()
            except Exception as e:
                print(f'Error: {e}')
                # TODO: Window error incorrectly data log in
                # if incorrectly data log in file "config.data"
                window.auth_main_acc()  # Calling a dialog box for entering authorization data
    except Exception as e:
        print(f'Error: {e}')
        exit()


if __name__ == "__main__":
    main()
