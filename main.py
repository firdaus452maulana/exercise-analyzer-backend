from flask import Flask, render_template, request
from flask_restful import Api, Resource
from json import loads

from dictionary_feedback_2 import get_feedback_words

app = Flask(__name__)
api = Api(app)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        file = request.files.get('file')
        data = loads(file.read())
        # data_update = {
        #     "data": data,
        #     "feedback_db": get_feedback_words()
        # }
        words = get_feedback_words()
        failed = {
            "feedback" : -1,
            "feedback_desc": words[-1][0],
            "feedback_recommendation": words[-1][1],
            "feedback_form": words[-1][2]
        }
        for item in data:
            for feedback in item['feedbacks']:
                feedback['feedback_desc'] = words[feedback['feedback']][0]
                feedback['feedback_recommendation'] = words[feedback['feedback']][1]
                feedback['feedback_form'] = words[feedback['feedback']][2]
            if item['state'] == 'FAILED':
                item['feedbacks'].append(failed)

        # print(data[0])
        # print(type(data))
        # return render_template('show.html', data=data_update)
        return data
    	# return render_template('show.html', data=data_update)

    return render_template('index.html')

# @app.route('/', methods=['GET', 'POST'])
# def callLlm():
#     if request.method == "POST":


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
