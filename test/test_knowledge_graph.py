from knowledge_graph import KnowledgeGraph


def test_add_node_by_name():
    kg = KnowledgeGraph()
    kg.add_node_by_name('superlux1000')


def test_add_relationship():
    kg = KnowledgeGraph()
    kg.add_relationship('Fehler', 'Superlux1000', 'Überhitzt')
