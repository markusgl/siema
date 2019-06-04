from flask import Flask, render_template, request
from knowledge_graph import KnowledgeGraph

app = Flask(__name__)
kg = KnowledgeGraph()


@app.route("/", methods=['POST'])
def welcome():
    data = request.get_json()
    machine_name = data['queryResult']['parameters']['Machine_name']
    print(f' Machine-name: {machine_name}')
    kg.add_relationship('Fehler', machine_name, 'fehler')
    return render_template('index.html'), 200


if __name__ == '__main__':
    app.run()
