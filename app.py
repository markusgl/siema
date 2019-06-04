from flask import Flask, render_template, request
from knowledge_graph import KnowledgeGraph
import google_docs as gdocs

app = Flask(__name__)
kg = KnowledgeGraph()


@app.route("/", methods=['POST'])
def welcome():
    data = request.get_json()
    print(data)
    intent = data['queryResult']['intent']['displayName']
    message_text = data['queryResult']['queryText']
    
    #if intent == 'read_measurements':
        # TODO read from sheets
    if intent == 'write_measurements':
        gdocs.insert_text(message_text)
        # TODO write to sheets

    #machine_name = data['queryResult']['parameters']['Machine_name']
    #print(f' Machine name: {machine_name}')
    #kg.add_relationship('Fehler', machine_name, 'fehler')
    return render_template('index.html'), 200


if __name__ == '__main__':
    app.run()
