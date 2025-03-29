import json
import os
import ast
from dotenv import load_dotenv
from openai import OpenAI

from firestore_service import get_feedback, get_personalization, get_analysis, save_feedback

def get_performance_context(data):
    print(data)
    data = json.dumps(ast.literal_eval(data["analysis"]), indent=2)
    data = json.loads(data)
    for entry in data:
        feedbacks = entry.get("feedbacks", [])
        # Membuat list mistakes berdasarkan feedback_desc
        mistakes = [fb.get("feedback_desc", "") for fb in feedbacks]
        entry["mistakes"] = mistakes
        # Hapus key "feedbacks"
        if "feedbacks" in entry:
            del entry["feedbacks"]
    return json.dumps(data, indent=4)

def getOutputLLM(exercise_id, type):
    last_feedback = get_feedback(exercise_id, type)
    print(last_feedback)
    if last_feedback:
        return last_feedback[0]
    else:
        performance_data = get_analysis(exercise_id)
        performance = "Current session of squat performance analysis:\n" + get_performance_context(performance_data)

        personalization = ""
        if type == "performance_personalization":
            personalization = get_personalization(exercise_id)
            personalization = "User Personalization:\n" + personalization["personalization"]

        system_prompt = """
Based on the following context, create motivational messages/words to maintain and even increase the user's motivation to maintain the user's consistency in doing self-squat exercises to prevent the user from experiencing muscle weakness in old age.

Keep your tone positive, empathetic, and encouraging. Generate the following data as the output that will be responded to:

1. **performance_feedback**: Based on the current session of performance data from context, only list IMPROPER/FAILED reps. Provide constructive feedback to improve their form or execution. Focus on providing feedback in explaining the errors made by users based on the system pose analysis. IMPROPER is a Squat performed with an incorrect posture but is still considered a successful squat, while FAILED is a Squat that does not fulfill all the phases (Stand - Transition - Squat) required in one rep.
2. **motivation**: Contains suggestions to maintain and increase the user's motivation to continue squat training based on the data context. Consider the Motivation that has been given to the user in the previous session along with the interaction provided by the user in creating the motivation message.
3. **safety**: Provide a safety or health-related recommendation based on the health conditions data.
4. **suggestion**: based on the analysis of the data context, suggest to the user the composition of the number of reps that the user can perform for the next session. Make it clear to increase, decrease, or stick with maximizing performance.

context:
{user_personalization}

{performance_data}

ONLY OUTPUT RAW JSON. Use this structure:
{format_structure}
"""

        format_structure = """
{
    "performance_feedback": str,
    "motivation": str,
    "safety": str,
    "suggestion": str
}"""
        system_prompt = system_prompt.format(
            user_personalization=personalization,
            performance_data=performance,
            format_structure=format_structure
        )

        print(system_prompt)
        
        load_dotenv()
        client = OpenAI(
            api_key=os.getenv("DEEPSEEK_API"),
            base_url="https://api.deepseek.com",
        )

        messages = [{"role": "user", "content": system_prompt}]

        response = client.chat.completions.create(
            model="deepseek-reasoner",
            messages=messages,
            # response_format={
            #     'type': 'json_object'
            # }
        )

        # data = json.loads(response.choices[0].message.content)
        # data['type'] = type

        # save_feedback(exercise_id=exercise_id, data=data)

        # return json.loads(response.choices[0].message.content)
        cleaned_json_string = response.choices[0].message.content.strip("```json").strip("```").strip()
        # print(response.choices[0].message.content)
        # print(json.loads(cleaned_json_string))
        return json.loads(cleaned_json_string)






# load_dotenv()
# client = OpenAI(
#     api_key=os.getenv("DEEPSEEK_API"),
#     base_url="https://api.deepseek.com",
# )

# messages = [{"role": "user", "content": system_prompt}]

# response = client.chat.completions.create(
#     model="deepseek-reasoner",
#     messages=messages
# )

# print(response)
# print(response.choices[0].message.content)
# print(response.choices[0].message.reasoning_content)
# print(json.loads(response.choices[0].message.content))