from knowledge_graph import KnowledgeGraph


def test_add_node_by_name():
    kg = KnowledgeGraph()
    kg.add_node_by_name('DMG mori CMX')


def test_add_relationship():
    kg = KnowledgeGraph()
    kg.add_relationship('DMG mori CMX', 'Heidenhain TNC 640', 'related_to')


def test_search_node_by_name():
    kg = KnowledgeGraph()
    kg.search_node_by_name('DMG mori CMX')
