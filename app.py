from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def welcome():
    data = request.get_json()
    machine_name = data['queryResult']['parameters']['Machine_name']
    print(f' Machine-name: {machine_name}')
    return render_template('index.html'), 200


if __name__ == '__main__':
    app.run()
