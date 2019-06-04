import os
import json

from py2neo import Graph, Relationship

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


class KnowledgeGraph:
    def __init__(self):
        path = os.path.realpath(ROOT_DIR + '/neo4j_creds.json')
        with open(path) as f:
            data = json.load(f)
        username = data['username']
        password = data['password']
        self.graph = Graph(host="localhost", username=username, password=password)


