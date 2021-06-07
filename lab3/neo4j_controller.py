from controller import Controller
from neo4j_model import Neo4jServer
from user_view import View


class Neo4jController(object):
    def __init__(self):
        self.__server = Neo4jServer()
        self.__menu = 'Neo4j menu'
        self.loop = True
        self.start()

    def start(self):
        from string_data import menu_list
        try:
            while self.loop:
                choice = Controller.make_choice(menu_list[self.__menu].keys(), self.__menu)
                Controller.considering_choice(self, choice, list(menu_list[self.__menu].values()))
        except Exception as e:
            View.show_error(str(e))

    def get_users_with_tagged_messages(self):
        res = self.__server.get_users_with_tagged_messages(*Controller.get_func_arguments(
            self.__server.get_users_with_tagged_messages))
        print(res)
        View.print_list("Users: ", res)

    def shortest_way_between_users(self):
        res = self.__server.shortest_way_between_users(*Controller.get_func_arguments(
            self.__server.shortest_way_between_users))
        View.show_way(res)

    def get_users_with_n_long_relations(self):
        res = self.__server.get_users_with_n_long_relations(*Controller.get_func_arguments(
            self.__server.get_users_with_n_long_relations))
        View.print_list("Pairs of users: ", res)

    def get_users_which_have_only_spam_conversation(self):
        res = self.__server.get_users_wicth_have_only_spam_conversation()
        View.print_list("Pairs of users: ", res)

    def get_unrelated_users_with_tagged_messages(self):
        res = self.__server.get_unrelated_users_with_tagged_messages(*Controller.get_func_arguments(
            self.__server.get_unrelated_users_with_tagged_messages))
        View.print_list("Groups of unrelated users: ", res)
