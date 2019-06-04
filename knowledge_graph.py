import os
import json

from py2neo import Graph, Relationship, Node, NodeMatcher

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


class KnowledgeGraph:
    def __init__(self):
        path = os.path.realpath(ROOT_DIR + '/neo4j_creds.json')
        with open(path) as f:
            data = json.load(f)
        username = data['username']
        password = data['password']
        self.graph = Graph(host="localhost", username=username, password=password)

    def add_node_by_name(self, name):
        node = Node('test', name=name)
        self.graph.create(node)

        return node

    def get_node_by_name(self, name):
        matcher = NodeMatcher(self.graph)
        node = matcher.match(name=name).first()

        return node

    def add_relationship(self, node1, node2, rel_type=''):
        first_node = self.get_node_by_name(node1)
        second_node = self.get_node_by_name(node2)

        if not first_node:
            first_node = self.add_node_by_name(node1)
        if not second_node:
            second_node = self.add_node_by_name(node2)

        self.graph.create(Relationship(first_node, rel_type, second_node))

    def search_node_by_name(self, node_name):
        # replace white spaces
        _node_name = node_name.replace(" ", "")

        query = 'MATCH (n) WHERE n.name={node_name} RETURN n;'
        result = self.graph.run(query,
                                node_name=_node_name,
                                ).data()

        if result:
            node = result[0]['n.name']
        else:
            node = None

        return node
