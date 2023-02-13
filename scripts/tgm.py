import asyncio
from random import uniform, shuffle

import sys
import configparser
import csv
import time
import aiofiles
import os

from typing import Optional
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerEmpty, InputChannel
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError, UsernameNotOccupiedError, \
    UserIdInvalidError

'''Old accounts
19319991 42062edaec3a04a60774c93f99baf97a 48886266681
12311426 1e724fcb879e638febe016211cea4efe 249904642515
16941904 80874c932df626b55011ab260a4acef3 27765060552
'''
'''
29301725 09859a91e8c664f96b65538c97c97cc2 18199144033
28811418 212541cc0a7312a52f30015530903cd7 12366087890
24192071 778e9349692fc66ee8e619e259ec1ad0 639089506304
29277598 517e69e5a57620763c216e034a27322f 14389072468
'''


class Tgm(object):
    def __init__(self):
        self.client: Optional[TelegramClient] = None
        self.phone: str = ''
        self.auth: bool = False
        self.groups: list = []
        self.users: list = []
        self.channels: list = []

        # self.client2: Optional[TelegramClient] = None
        # self.phone2: str = ''
        # self.auth2: bool = False
        # self.temp = False

        self.add_client: Optional[TelegramClient] = None
        self.add_api_id: str = ''
        self.add_api_hash: str = ''
        self.add_phone: str = ''
        self.add_auth: bool = False

    async def mainConnect(self):
        cpass = configparser.RawConfigParser()
        cpass.read('config.data')
        api_id = cpass['main']['id']
        api_hash = cpass['main']['hash']
        self.phone = cpass['main']['phone']
        self.client = TelegramClient(self.phone, api_id, api_hash)
        await self.client.connect()
        # Check authentication
        self.auth = await self.client.is_user_authorized()
        if not self.auth:
            await self.client.send_code_request(self.phone)

    async def authWithCode(self, tgm_code):
        try:
            # passw = input('[+] Enter the password: ') # TODO: add the possibility of authorization with a password
            await self.client.sign_in(self.phone, tgm_code)
            self.auth = True
        except:
            self.auth = False

    @staticmethod
    def configSetup(xid, xhash, xphone):
        cpass = configparser.RawConfigParser()
        cpass.add_section('main')
        cpass.set('main', 'id', xid)
        cpass.set('main', 'hash', xhash)
        cpass.set('main', 'phone', xphone)
        with open('config.data', 'w') as setup:
            cpass.write(setup)
        del cpass

    # sript from click button "Add account"
    async def addClient(self, api_id: str, api_hash: str, phone: str):
        self.add_api_id = api_id
        self.add_api_hash = api_hash
        self.add_phone = phone.replace('+', '').replace(' ', '')
        self.add_client = TelegramClient(self.add_phone, self.add_api_id, self.add_api_hash)
        await self.add_client.connect()
        self.add_auth = await self.add_client.is_user_authorized()
        if not self.add_auth:
            await self.add_client.send_code_request(self.add_phone)
        else:
            async with aiofiles.open('list_tgm_accounts.txt', 'a') as file:
                await file.write(f'{self.add_api_id} {self.add_api_hash} {self.add_phone}\n')
            await self.add_client.disconnect()

    async def addClientAuth(self, tgm_code):
        try:
            # passw = input('[+] Enter the password: ') # TODO: add the possibility of authorization with a password
            await self.add_client.sign_in(self.add_phone, tgm_code)
            self.add_auth = True
            async with aiofiles.open('list_tgm_accounts.txt', 'a') as file:
                await file.write(f'{self.add_api_id} {self.add_api_hash} {self.add_phone}\n')
            await self.add_client.disconnect()
        except Exception as e:
            print(e)
            self.add_auth = False

    # Get 200 groups from account
    async def getGroups(self):
        result = await self.client(GetDialogsRequest(
            offset_date=None,
            offset_id=0,
            offset_peer=InputPeerEmpty(),
            limit=200,
            hash=0
        ))
        chats = [i for i in result.chats]
        groups = []
        for chat in chats:
            try:
                if chat.megagroup:
                    groups.append(chat)
            except:
                continue
        self.groups = groups

    async def getChannels(self):
        result = await self.client(GetDialogsRequest(
            offset_date=None,
            offset_id=0,
            offset_peer=InputPeerEmpty(),
            limit=200,
            hash=0
        ))
        chats = [i for i in result.chats]
        groups = []
        for chat in chats:
            try:
                if chat.broadcast:
                    groups.append(chat)
            except:
                continue
        self.channels = groups

    # Parsing all users from selected chat
    async def enteringUsers(self, target_group):
        s = time.time()
        all_participants = await self.client.get_participants(target_group)
        with open('members.csv', 'w', encoding='UTF-8') as file:
            writer = csv.writer(file, delimiter=',', lineterminator='\n')
            writer.writerow(['username', 'user id', 'access hash', 'name', 'group', 'group id'])
            for user in all_participants:
                if user.username:
                    username = user.username
                else:
                    continue
                first_name = user.first_name if user.first_name else ''
                last_name = user.last_name if user.last_name else ''
                name = f'{first_name} {last_name}'.strip()
                writer.writerow([username, user.id, user.access_hash, name, target_group.title, target_group.id])
        return time.time() - s

    def readingUsers(self):
        self.users = []
        with open('members.csv', encoding='UTF-8') as f:
            rows = csv.reader(f, delimiter=',', lineterminator='\n')
            next(rows, None)
            for row in rows:
                user = {
                    'username': row[0],
                    'id': int(row[1]),
                    'access_hash': int(row[2]),
                    'name': row[3]
                }
                self.users.append(user)
        shuffle(self.users)

    @staticmethod
    async def checkAccounts():
        list_tgm_accounts = 'list_tgm_accounts.txt'
        if os.path.exists(list_tgm_accounts):
            async with aiofiles.open(list_tgm_accounts, 'r', encoding='UTF-8') as f:
                return [tgm_account for tgm_account in [i.rstrip('\r\n') for i in await f.readlines()]]
        else:
            print('you need to create file ' + list_tgm_accounts + ' with telegram ids')
            return

    async def inviteToChat(self, target_group, main_self):
        tgm_accounts = await self.checkAccounts()
        if not tgm_accounts:
            main_self.showWindowMessage('Ошибка', 'Нет авторизованных аккаунтов!', 'error.svg', color='#D52020')
            return
        self.readingUsers()
        count = 0
        complited_count = 0
        i = 0
        try:
            for tgm_account in tgm_accounts:
                api_id, api_hash, phone = tgm_account.split()
                client2 = TelegramClient(phone, api_id, api_hash)
                await client2.connect()
                if not await client2.is_user_authorized():
                    continue
                for user in list(self.users):
                    count += 1
                    print(count)
                    # if count % 10 == 0:
                    await asyncio.sleep(uniform(5.0, 30.0))
                    try:
                        user_to_add = await client2.get_input_entity(user['username'])
                        target_group_entity = await client2.get_entity(
                            InputChannel(target_group.id, target_group.access_hash))
                        await client2(InviteToChannelRequest(channel=target_group_entity, users=[user_to_add]))
                        complited_count += 1
                    # await asyncio.sleep(1)
                    except PeerFloodError:
                        print(f'{phone} [!!] Getting Flood Error from telegram')
                        exc_type, exc_value, exc_traceback = sys.exc_info()
                        print(f'{phone} [!!] {exc_value}')
                        break
                    except UserPrivacyRestrictedError:
                        exc_type, exc_value, exc_traceback = sys.exc_info()
                        print(f'{phone} [!] {exc_value}')
                    except UsernameNotOccupiedError:
                        print(f'{phone} [!] The user has not have Username. Skipping.')
                        exc_type, exc_value, exc_traceback = sys.exc_info()
                        print(f'{phone} [!] {exc_value}')
                    except UserIdInvalidError:
                        print(f'{phone} [!] Invalid User ID. Skipping.')
                        exc_type, exc_value, exc_traceback = sys.exc_info()
                        print(f'{phone} [!] {exc_value}')
                    except AttributeError:
                        exc_type, exc_value, exc_traceback = sys.exc_info()
                        print(f'{phone} [!] {exc_value}')
                        if str(exc_value) == '"NoneType" object has no attribute "id"':
                            break
                    except:
                        print(f'{phone} [!?] Unexpected Error')
                        exc_type, exc_value, exc_traceback = sys.exc_info()
                        print(f'{phone} [!?] {exc_value}')
                    self.users.remove(user)
                await client2.disconnect()
                i += 1
            main_self.showWindowMessage('Успешно', f'Инвайт окончен! Добавлено {complited_count} из {count} ',
                                        'info.svg')
        except Exception as e:
            print(f'Error:  {e}')

    async def inviteToChannel(self, target_group, main_self):
        tgm_accounts = await self.checkAccounts()
        if not tgm_accounts:
            main_self.showWindowMessage('Ошибка', 'Нет авторизованных аккаунтов!', 'error.svg', color='#D52020')
            return
        self.readingUsers()
        complited_count = 0
        count = 0
        i = 0
        try:
            for tgm_account in tgm_accounts:
                api_id, api_hash, phone = tgm_account.split()
                client3 = TelegramClient(phone, api_id, api_hash)
                await client3.connect()
                if not await client3.is_user_authorized():
                    continue
                for user in list(self.users):
                    count += 1
                    print(count)
                    try:
                        user_to_add = await client3.get_input_entity(user['username'])
                        target_group_entity = await client3.get_entity(
                            InputChannel(target_group.id, target_group.access_hash))
                        await client3(InviteToChannelRequest(channel=target_group_entity, users=[user_to_add]))
                        complited_count += 1
                    # await asyncio.sleep(1.4)
                    except PeerFloodError:
                        print(f'{phone} [!!] Getting Flood Error from telegram.')
                        break
                    except UserPrivacyRestrictedError:
                        print(f'{phone} [!] The user\'s privacy settings do not allow you to do this. Skipping.')
                    except:
                        exc_type, exc_value, exc_traceback = sys.exc_info()
                        print(f'{phone} [!?] Unexpected Error')
                        print(f'{phone} [!?] {exc_value}')
                    self.users.remove(user)
                await client3.disconnect()
                i += 1
            main_self.showWindowMessage('Успешно', f'Инвайт окончен! Добавлено {complited_count} из {count} ',
                                        'info.svg')
        except Exception as e:
            print(f'Error:  {e}')

    async def spamToUsers(self, message, main_self):
        tgm_accounts = await self.checkAccounts()
        if not tgm_accounts:
            main_self.showWindowMessage('Ошибка', 'Нет авторизованных аккаунтов!', 'error.svg', color='#D52020')
            return
        self.readingUsers()
        complited_count = 0
        count = 0
        i = 0
        try:
            for tgm_account in tgm_accounts:
                api_id, api_hash, phone = tgm_account.split()
                client4 = TelegramClient(phone, api_id, api_hash)
                await client4.connect()
                if not await client4.is_user_authorized():
                    continue
                for user in list(self.users):
                    count += 1
                    await asyncio.sleep(uniform(5.0, 30.0))
                    try:
                        receiver = await client4.get_input_entity(user['username'])
                        await client4.send_message(receiver, message)
                        complited_count += 1
                    except PeerFloodError:
                        print(f'{phone} [!!] Getting Flood Error from telegram.')
                        break
                    except UserPrivacyRestrictedError:
                        print(f'{phone} [!] The user\'s privacy settings do not allow you to do this. Skipping.')
                    except:
                        exc_type, exc_value, exc_traceback = sys.exc_info()
                        print(f'{phone} [!?] Unexpected Error')
                        print(f'{phone} [!?] {exc_value}')
                    self.users.remove(user)
                i += 1
        except Exception as e:
            print(f'Error:  {e}')


tg = Tgm()
