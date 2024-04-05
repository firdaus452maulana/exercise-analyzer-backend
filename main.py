from flask import Flask, render_template, request
from flask_restful import Api, Resource
from json import loads

app = Flask(__name__)
api = Api(app)


@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == "POST":
        file = request.files.get('file')
        data = loads(file.read())
        # print(data[0])
        # print(type(data))
        return render_template('show.html', data=data)
    return render_template('index.html')
