from flask import Flask, render_template, request
from flask_restful import Api, Resource
from json import loads

from dictionary_feedback import get_feedback_words

app = Flask(__name__)
api = Api(app)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        file = request.files.get('file')
        data = loads(file.read())
        data_update = {
            "data": data,
            "feedback_db": get_feedback_words()
        }
        # print(data[0])
        # print(type(data))
        return render_template('show.html', data=data_update)
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
