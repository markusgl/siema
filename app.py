from flask import Flask, render_template, request, jsonify
from knowledge_graph import KnowledgeGraph
import google_docs as gdocs
import google_sheets as gsheets

app = Flask(__name__)
kg = KnowledgeGraph()


@app.route("/", methods=['GET', 'POST'])
def welcome():
    data = request.get_json()
    #print(data)
    intent = data['queryResult']['intent']['displayName']
    message_text = data['queryResult']['queryText']
    actual_value = data['queryResult']['parameters']['float_measure']
    print(f'Intent: {intent}')
    print(f'Message text: {message_text}')

    if intent == 'write_measurement':
        #print(type(actual_value))
        #print(f'Actual value: {actual_value}')
        #gdocs.insert_text(message_text)
        gsheets.write_actual_size(actual_value)

        response = {
            "fulfillmentMessages": [
                {
                    "text": {
                        "text": [
                            "Der Wert " + actual_value + " wurde eingetragen."
                        ]
                    }
                }
            ],
        }

        return jsonify(response)
    elif intent == 'read_measurements':
        spec_value = gsheets.get_spec_size()
        #print(f'Spec value: {spec_value}')

        response = {
            "fulfillmentText": "Zu welcher Uhrzeit?",
            "fulfillmentMessages": [
                {
                    "text": {
                        "text": [
                            "Das Istmaß beträgt: " + spec_value
                        ]
                    }
                }
            ],
        }
        return jsonify(response)

    return render_template('index.html'), 200


if __name__ == '__main__':
    app.run()
