from neo4j_controller import Neo4jController
from controller import Controller, Tags
from neo4j_model import Neo4jServer

menu_list = {
    'Neo4j menu': {
        'Print tagged messages (random tag)': Neo4jController.get_users_with_tagged_messages,
        'Print N long relations': Neo4jController.get_users_with_n_long_relations,
        'Print Shortest way': Neo4jController.shortest_way_between_users,
        'Print Only spam': Neo4jController.get_users_which_have_only_spam_conversation,
        'Print Tagged messages without relations': Neo4jController.get_unrelated_users_with_tagged_messages,
        'Exit': Controller.stop_loop,
    }
}


neo4j = Neo4jServer()
special_parameters = {
    'tags': '('+', '.join(x.name for x in list(Tags))+')(Enter csv)',
    'First username': ' ',
    'Second username': ' '
}
