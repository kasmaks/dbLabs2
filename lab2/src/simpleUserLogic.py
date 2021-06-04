from . import message
from . import globalValue
from . import staticData
from . import client

r = client.r


def send_a_message():
    print(globalValue.logined_user)
    print(globalValue.user_that_need_to_get_message)
    print("send_a_message")
    our_message = input()
    message.create_message(globalValue.logined_user, globalValue.user_that_need_to_get_message, our_message)


def read_income_messages():
    print("read_income_messages")
    end = r.llen(staticData.delivered_messages)
    list_of_delivered_messages = r.lrange(staticData.delivered_messages, 0, end)

    list_of_messages_needed_to_be_read = []
    for el in list_of_delivered_messages:
        if "_to_"+globalValue.logined_user in el:
            list_of_messages_needed_to_be_read.append(el)
            r.rpush(staticData.read_messages, el)
            r.lrem(staticData.delivered_messages, 1, el)
    list_of_messages_needed_to_be_read_with_message_body = []
    for el in list_of_messages_needed_to_be_read:
        message_object = r.hgetall(el)
        message_obj_as_an_dict = {"_from": message_object["_from"], "_to": message_object["_to"],
                                  "body": message_object["body"], "date": message_object["date_of_creating"]}
        list_of_messages_needed_to_be_read_with_message_body.append(message_obj_as_an_dict)
    for el in list_of_messages_needed_to_be_read_with_message_body:
        print("from: " + el['_from'])
        print("to: " + el['_to'])
        print("date of sending: " + el['date'])
        print("message: " + el['body'])
    input()


def messages_are_checking_for_spam():
    print("messages_are_checking_for_spam")
    end = r.llen(staticData.checking_on_spam)
    list_of_delivered_messages = r.lrange(staticData.checking_on_spam, 0, end)

    list_of_messages_needed_to_be_read = []
    for el in list_of_delivered_messages:
        if "_from_" + globalValue.logined_user in el:
            list_of_messages_needed_to_be_read.append(el)
    list_of_messages_needed_to_be_read_with_message_body = []
    for el in list_of_messages_needed_to_be_read:
        message_object = r.hgetall(el)
        message_obj_as_an_dict = {"_from": message_object["_from"], "_to": message_object["_to"],
                                  "body": message_object["body"], "date": message_object["date_of_creating"]}
        list_of_messages_needed_to_be_read_with_message_body.append(message_obj_as_an_dict)

    for el in list_of_messages_needed_to_be_read_with_message_body:
        print("from: " + el['_from'])
        print("to: " + el['_to'])
        print("date of sending: " + el['date'])
        print("message: " + el['body'])

    input()


def messages_are_blocked_due_to_spam():
    print("messages_are_blocked_due_to_spam")   
    end = r.llen(staticData.blocked_messages)
    list_of_delivered_messages = r.lrange(staticData.blocked_messages, 0, end)

    list_of_messages_needed_to_be_read = []
    for el in list_of_delivered_messages:
        if "_from_" + globalValue.logined_user in el:
            list_of_messages_needed_to_be_read.append(el)
    list_of_messages_needed_to_be_read_with_message_body = []
    for el in list_of_messages_needed_to_be_read:
        message_object = r.hgetall(el)
        message_obj_as_an_dict = {"_from": message_object["_from"], "_to": message_object["_to"],
                                  "body": message_object["body"], "date": message_object["date_of_creating"]}
        list_of_messages_needed_to_be_read_with_message_body.append(message_obj_as_an_dict)

    for el in list_of_messages_needed_to_be_read_with_message_body:
        print("from: " + el['_from'])
        print("to: " + el['_to'])
        print("date of sending: " + el['date'])
        print("message: " + el['body'])
    input()


def sent_but_not_read_messages():
    print("sent_but_not_read_messages")
    end = r.llen(staticData.delivered_messages)
    list_of_delivered_messages = r.lrange(staticData.delivered_messages, 0, end)

    list_of_messages_needed_to_be_read = []
    for el in list_of_delivered_messages:
        if "_from_" + globalValue.logined_user in el:
            list_of_messages_needed_to_be_read.append(el)
    list_of_messages_needed_to_be_read_with_message_body = []
    for el in list_of_messages_needed_to_be_read:
        message_object = r.hgetall(el)
        message_obj_as_an_dict = {"_from": message_object["_from"], "_to": message_object["_to"],
                                  "body": message_object["body"], "date": message_object["date_of_creating"]}
        list_of_messages_needed_to_be_read_with_message_body.append(message_obj_as_an_dict)

    for el in list_of_messages_needed_to_be_read_with_message_body:
        print("from: " + el['_from'])
        print("to: " + el['_to'])
        print("date of sending: " + el['date'])
        print("message: " + el['body'])
    input()
