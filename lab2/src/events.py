import msvcrt
import os
from . import globalValue
from . import menu
from . import staticData
from . import adminUserLogic
from . import simpleUserLogic
from . import authorization
from . import window
from datetime import datetime
from . import client

r = client.r


def up():
    if globalValue.current_window == window.get_name_of_active_window():
        while msvcrt.kbhit():
            msvcrt.getch()
        if globalValue.selected == 0:
            menu.show_menu()
            return
        globalValue.selected -= 1
        menu.show_menu()


def down():
    if globalValue.current_window == window.get_name_of_active_window():
        while msvcrt.kbhit():
            msvcrt.getch()
        if globalValue.is_list_for_sending:
            if globalValue.selected == len(globalValue.list_of_users) - 1:
                menu.show_menu()
                return
            globalValue.selected += 1
            menu.show_menu()
            return
        if globalValue.is_admin:
            if globalValue.selected == len(staticData.admin_deals)-1:
                menu.show_menu()
                return
            globalValue.selected += 1
            menu.show_menu()
            return
        if globalValue.is_simple_user:
            if globalValue.selected == len(staticData.simple_user_deals)-1:
                menu.show_menu()
                return
            globalValue.selected += 1
            menu.show_menu()
            return
        if globalValue.is_starting_menu:
            if globalValue.selected == len(staticData.start_menu)-1:
                menu.show_menu()
                return
            globalValue.selected += 1
            menu.show_menu()
            return


def shift():
    if globalValue.current_window == window.get_name_of_active_window():
        if globalValue.is_admin and staticData.admin_deals[globalValue.selected] != 'Exit':
            if staticData.admin_deals[globalValue.selected] == 'Log events':
                adminUserLogic.log_events()
            if staticData.admin_deals[globalValue.selected] == 'List of users that are online':
                adminUserLogic.list_of_online_users()
            if staticData.admin_deals[globalValue.selected] == 'Rating of active users':
                adminUserLogic.rating_of_active_users()
            if staticData.admin_deals[globalValue.selected] == 'Rating of active spammers':
                adminUserLogic.rating_of_active_spammers()
            menu.show_menu()
        elif globalValue.is_admin and staticData.admin_deals[globalValue.selected] == 'Exit':
            menu.change_menu('start')
            globalValue.selected = 0
            menu.show_menu()
        elif globalValue.is_simple_user and staticData.simple_user_deals[globalValue.selected] != 'Exit':
            if staticData.simple_user_deals[globalValue.selected] == 'Send a message':
                menu.change_menu('send_message')
                menu.show_menu()

            if staticData.simple_user_deals[globalValue.selected] == 'Read income messages':
                simpleUserLogic.read_income_messages()
            if staticData.simple_user_deals[globalValue.selected] == 'Messages that are being checked for spam':
                simpleUserLogic.messages_are_checking_for_spam()
            if staticData.simple_user_deals[globalValue.selected] == 'Messages that are blocked due to spam':
                simpleUserLogic.messages_are_blocked_due_to_spam()
            if staticData.simple_user_deals[globalValue.selected] == 'Messages that were not read yet':
                simpleUserLogic.sent_but_not_read_messages()
            menu.show_menu()
        elif globalValue.is_simple_user and staticData.simple_user_deals[globalValue.selected] == 'Exit':
            date = str(datetime.today())
            log = globalValue.logined_user + " " + date + " user logged out"
            r.rpush(staticData.log_events, log)
            menu.change_menu('start')
            globalValue.selected = 0
            menu.show_menu()

        elif globalValue.is_starting_menu and staticData.start_menu[globalValue.selected] != 'Exit':
            if staticData.start_menu[globalValue.selected] == 'Admin':
                menu.change_menu('admin')
                authorization.user_auth()
                globalValue.selected = 0
                menu.show_menu()
            elif staticData.start_menu[globalValue.selected] == 'Simple User':
                menu.change_menu('simple')
                authorization.user_auth()
                globalValue.selected = 0
                menu.show_menu()
            elif staticData.start_menu[globalValue.selected] == 'Worker':
                menu.change_menu('worker')
                globalValue.selected = 0
                menu.show_menu()
        elif globalValue.is_starting_menu and staticData.start_menu[globalValue.selected] == 'Exit':
            os.abort()
        elif globalValue.is_list_for_sending:
            simpleUserLogic.send_a_message()
            menu.change_menu("simple")
            menu.show_menu()
