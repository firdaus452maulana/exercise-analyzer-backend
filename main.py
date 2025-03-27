from flask import Flask, render_template, request
from flask_restful import Api, Resource
import json
import ast

from dictionary_feedback_2 import get_feedback_words
from llm_run import getOutputLLM
from firestore_service import save_personalization, save_perform, save_evaluation, get_analysis

app = Flask(__name__)
api = Api(app)


@app.route('/analyze', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        file = request.files.get('file')
        data = json.loads(file.read())
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

        save_perform({"analysis": str(data)})
        # print(data[0])
        # print(type(data))
        # return render_template('show.html', data=data_update)
        return data
    	# return render_template('show.html', data=data_update)
    
    if request.method == "GET":
        exerciseId = request.args.get('exerciseId')
        analysis = get_analysis(exerciseId)
        return json.dumps(ast.literal_eval(analysis["analysis"]), indent=2)

    return render_template('index.html')

@app.route('/llm-feedback', methods=['GET'], strict_slashes=False)
def callLlm():
    if request.method == "GET":
        type = request.args.get('type')
        exerciseId = request.args.get('exerciseId')

        data = getOutputLLM(exercise_id=exerciseId, type=type)
        return data
        
@app.route('/submit-questionnaire', methods=['POST'])
def handle_questionnaire():
    data = request.get_json()
    exerciseId = request.args.get('exerciseId')
    data_input = {
        "personalization": json.dumps(data, indent=2)
    }
    if not data:
        return {'error': 'No JSON data provided'}, 400
    doc_id = save_personalization(exerciseId, data_input)
    return {'id': doc_id}, 201

@app.route('/submit-evaluate', methods=['POST'])
def handle_perform():
    data = request.get_json()
    exerciseId = request.args.get('exerciseId')
    type = request.args.get('type')
    if not data:
        return {'error': 'No JSON data provided'}, 400
    doc_id = save_evaluation(exerciseId, type, data)
    return {'id': doc_id}, 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4025, debug=True)
