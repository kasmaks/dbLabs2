import random
import os
from . import staticData
from . import globalValue
from . import client

r = client.r


def change_menu(mode):
    globalValue.selected = 0
    globalValue.is_admin = False
    globalValue.is_simple_user = False
    globalValue.is_starting_menu = False
    globalValue.is_list_for_sending = False
    globalValue.is_worker = False
    if mode == 'admin':
        globalValue.is_admin = True
    if mode == 'simple':
        globalValue.is_simple_user = True
    if mode == 'start':
        globalValue.is_starting_menu = True
    if mode == 'send_message':
        globalValue.is_list_for_sending = True
    if mode == 'worker':
        globalValue.is_worker = True


def show_menu(str=""):

    os.system('cls||clear')
    import win32gui
    w = win32gui
    print(w.GetWindowText(w.GetForegroundWindow()))
    if str != "":
        print(str)
    print("Choose an option:")
    iterator = 0
    if globalValue.is_starting_menu:
        for el in staticData.start_menu:
            print("{1} {0}. {3} {0} {2}".format(iterator, ">" if globalValue.selected == iterator else " ",
                                                "<" if globalValue.selected == iterator else " ", el))
            iterator = iterator+1
        return
    if globalValue.is_list_for_sending:
        globalValue.list_of_users = r.smembers(staticData.list_of_users)
        for user in globalValue.list_of_users:
            if globalValue.selected == iterator:
                globalValue.user_that_need_to_get_message = user
            print("{1} {0}. {3} {0} {2}".format(iterator, ">" if globalValue.selected == iterator else " ",
                                                "<" if globalValue.selected == iterator else " ", user))
            iterator = iterator + 1
        return
    if globalValue.is_simple_user:
        for el in staticData.simple_user_deals:

            print("{1} {0}. {3} {0} {2}".format(iterator, ">" if globalValue.selected == iterator else " ",
                                                "<" if globalValue.selected == iterator else " ", el))
            iterator = iterator + 1
        return
    if globalValue.is_admin:
        for el in staticData.admin_deals:
            print("{1} {0}. {3} {0} {2}".format(iterator, ">" if globalValue.selected == iterator else " ",
                                                "<" if globalValue.selected == iterator else " ", el))
            iterator = iterator + 1
        return

    if globalValue.is_worker:
        worker = r.pubsub()
        worker.subscribe(staticData.list_of_created_messages)
        while True:
            message = worker.get_message()
            if message:
                print(message['data'])
                end = r.llen(staticData.queue) - 1
                list_messages_for_checking = r.lrange(staticData.queue, 0, end)
                for el in list_messages_for_checking:
                    r.lpop(staticData.queue)
                    r.lpop(staticData.list_of_created_messages)
                    r.rpush(staticData.checking_on_spam, el)
                end = r.llen(staticData.checking_on_spam)
                our_data_for_checking_on_spam = r.lrange(staticData.checking_on_spam, 0, end)
                i = 0
                for element in our_data_for_checking_on_spam:
                    our_message = r.hgetall(our_data_for_checking_on_spam[i])
                    our_spammer = our_message['_from']
                    random.seed()

                    if random.randint(0, 9) % 2 == 1:

                        r.rpush(staticData.delivered_messages, our_data_for_checking_on_spam[i])
                        print("Approved Message, "+our_data_for_checking_on_spam[i])
                        r.lpop(staticData.checking_on_spam)
                        p = r.pipeline()

                        p.publish("get_"+our_message['_to'], "income message from " + our_message['_from'])

                    else:
                        print(random.random() % 2)
                        r.rpush(staticData.blocked_messages, our_data_for_checking_on_spam[i])
                        r.lpop(staticData.checking_on_spam)
                        print("It is a spam " + our_data_for_checking_on_spam[i])
                        r.zincrby(staticData.list_of_spammers, 1, our_spammer)
                    i += 1

