import time
from datetime import datetime
from . import globalValue
from . import menu
from . import client
from. import UserObject
from.  import staticData

r = client.r


def user_auth(string=""):
    if string != "":
        print(string)

    print("Please enter your username:")
    if globalValue.is_admin:
        print(", Admin")
    login = input()
    globalValue.logined_user = login
    if globalValue.is_admin:
        print("Please enter your password, admin:")
        password = input()
    user_object = r.hgetall(login)
    if user_object == {} or user_object is None:
        print("Account has been created")
        if globalValue.is_admin:
            UserObject.create_user(globalValue.logined_user, globalValue.is_admin, password)
            menu.change_menu('admin')
        if not globalValue.is_admin:
            UserObject.create_user(globalValue.logined_user, globalValue.is_admin)
            p = r.pubsub()
            p.subscribe("get_" + globalValue.logined_user)
            menu.change_menu('simple')
            date = str(datetime.today())
            log = globalValue.logined_user + " " + date + " user logged in"
            r.rpush(staticData.log_events, log)

    else:
        if globalValue.is_admin:
            try:
                if user_object['password'] != password:
                    user_auth("You have entered not correct password")

                else:
                    menu.change_menu('admin')

                    return True
            except KeyError:
                menu.change_menu('simple')
                print("You are not an admin, you are a simple user")
                p = r.pubsub()
                menu.change_menu('simple')
                date = str(datetime.today())
                log = globalValue.logined_user + " " + date + " user logged in"
                r.rpush(staticData.log_events, log)

        else:
            p = r.pubsub()
            time.sleep(5)
            menu.change_menu('simple')
            date = str(datetime.today())
            log = globalValue.logined_user + " " + date + " user logged in"
            r.rpush(staticData.log_events, log)
            return True
