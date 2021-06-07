from controller import Controller
from emulation import EmulationController
from neo4j_controller import Neo4jController
from user_view import View
from faker import Faker
import random


def emulation():

    fake = Faker()
    users_count = 7
    users = [fake.profile(fields=['username'], sex=None)['username'] for u in range(users_count)]
    threads = []
    try:

        for i in range(users_count):
            threads.append(EmulationController(users[i], users, users_count, random.randint(1, 2)))
        for thread in threads:
            thread.start()

    except Exception as e:
        View.show_error(str(e))
    finally:
        for thread in threads:
            if thread.is_alive():
                thread.stop()


if __name__ == "__main__":
    choice = Controller.make_choice(["Neo4j", "Emulation"], "Program mode")
    if choice == 0:
        Neo4jController()
    elif choice == 1:
        emulation()