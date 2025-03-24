import json
import subprocess


def run_ollama(prompt_template, model="deepseek-r1"):
    """
    Run the LLaMA model locally using Ollama with a specific prompt and JSON data.

    Parameters:
        prompt_template (str): The template for the prompt.
        json_data (dict): The JSON data to include in the prompt.
        model (str): The name of the model to use.

    Returns:
        str: The model's response.
    """
    # Format the JSON data as a string
    # json_input = json.dumps(json_data, indent=4)


    # Combine the prompt template with the JSON input
    prompt = f"{prompt_template}"

    # Run the Ollama command
    try:
        result = subprocess.run(
            ["ollama", "run", model],
            input=prompt,
            text=True,
            capture_output=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"Error running the model: {e.stderr}"


if __name__ == "__main__":
    # Define the prompt template
    PROMPT_TEMPLATE = (
        """
        # Instructions
        
        You are an AI Assistant specialized in exercise coaching and motivation. Your task is to provide feedback and personalized motivational messages based on the user's performance analysis and their personal details. Consider the user's goals, preferences, and history to make the feedback effective and tailored to their needs.
        
        ## Step to Follow
        
        1. **Performance Feedback:**
            - Analyze the user's squat performance data, focusing on areas stated as "IMPROPER" or "FAILED".
            - Provide constructive feedback to improve their form or execution.
            - Detailed feedback on the user's squat performance.
            - Focus on providing feedback in explaining the errors made by users based on the system pose analysis.
        2. **Personalized Motivation:**
            - Consider the user's 'User Personalization' data to craft motivational messages tailored to their needs.
            - Consider also the Motivation and Feedback that has been given to the user in the previous session along with the interaction provided by the user in creating motivational message.
        3. **Tone and Style:**
            - Keep your tone positive, empathetic, and encouraging.
            - Use simple language, avoiding overly technical terms unless necessary.
        4. **Health Considerations:**
            - Respect the user's medical history and suggest modifications if needed, ensuring the exercise is safe and sustainable.
        5. Do not include any additional text, commentary, or explanations outside of the JSON format.
        
        
        ## Input
        
        - **User Personalization:**
        
        {
          "User Personalization": {
            "User Identification": {
              "Name": "Miyu_9",
              "Age": 51,
              "Gender": "Female",
              "Height": 156,
              "Weight": 68
            },
            "Discipline & Exercise Habits": {
              "Weekly Frequency": "1 time",
              "Duration": "30-60 minutes",
              "Regular Schedule": "Yes",
              "Consistency Difficulty": "Somewhat easy"
            },
            "Progress and Achievements": {
              "Participated Structured Program": "Yes",
              "Progress Result": "Very good",
              "Greatest Achievement": "Lost 19 kg of weight in 2 months through consistent training"
            },
            "Intrinsic and Extrinsic Motivation": {
              "Main Reason": [
                "To reduce stress or anxiety",
                "For physical appearance"
              ],
              "Motivation Type": "External rewards",
              "Support Need": "Yes"
            },
            "Mental Health and Emotions": {
              "Emotional State": "Bad",
              "Stress Level": "Often",
              "Exercise Helps Stress": "Yes"
            },
            "Social Support": {
              "Supportive Friends/Family": "Yes",
              "Training with Others": "Sometimes",
              "Support Importance": "Not very important"
            },
            "Medical History and Physical Condition": {
              "Injury History": "Minor injury",
              "Current Medication": "Yes",
              "Respiratory/Cardiovascular Issues": "Yes"
            }
          }
        }
        
        - **Squat Performance:**
        
        {
          "Squat Performance Analysis": [
            {
              "repetition": 0,
              "state": "IMPROPER",
              "feedback": [
                "Your knees are too low, making them closer to your toes",
                "Your back is not forward enough"
              ]
            },
            {
              "repetition": 1,
              "state": "FAILED",
              "feedback": [
                "Your back is not forward enough"
              ]
            },
            {
              "repetition": 2,
              "state": "CORRECT",
              "feedback": []
            },
            {
              "repetition": 3,
              "state": "FAILED",
              "feedback": [
                "Your back is leaning too forward"
              ]
            },
            {
              "repetition": 4,
              "state": "FAILED",
              "feedback": [
                "Your knees are too low, making them closer to your toes",
                "Your back is leaning too forward"
              ]
            },
            {
              "repetition": 5,
              "state": "CORRECT",
              "feedback": []
            },
            {
              "repetition": 6,
              "state": "CORRECT",
              "feedback": []
            },
            {
              "repetition": 7,
              "state": "CORRECT",
              "feedback": []
            },
            {
              "repetition": 8,
              "state": "FAILED",
              "feedback": [
                "Your knees are too low, making them closer to your toes"
              ]
            },
            {
              "repetition": 9,
              "state": "IMPROPER",
              "feedback": [
                "Your knees are too low, making them closer to your toes"
              ]
            }
          ]
        }
        
        - **History Performance:**
        
        [
          {
            "session": "s_001",
            "date": "01/01/2025",
            "performance": [
              {
                "repetition": 0,
                "state": "CORRECT",
                "feedback": []
              },
              {
                "repetition": 1,
                "state": "CORRECT",
                "feedback": []
              },
              {
                "repetition": 2,
                "state": "CORRECT",
                "feedback": []
              },
              {
                "repetition": 3,
                "state": "FAILED",
                "feedback": [
                  "Your back is not forward enough"
                ]
              },
              {
                "repetition": 4,
                "state": "CORRECT",
                "feedback": []
              },
              {
                "repetition": 5,
                "state": "IMPROPER",
                "feedback": [
                  "Your back is leaning too forward"
                ]
              },
              {
                "repetition": 6,
                "state": "IMPROPER",
                "feedback": [
                  "Your thighs drop too below your knees",
                  "Your back is not forward enough"
                ]
              },
              {
                "repetition": 7,
                "state": "FAILED",
                "feedback": [
                  "Your knees are too low, making them closer to your toes",
                  "Your back is not forward enough"
                ]
              }
            ]
          },
          {
            "session": "s_002",
            "date": "03/01/2025",
            "performance": [
              {
                "repetition": 0,
                "state": "CORRECT",
                "feedback": []
              },
              {
                "repetition": 1,
                "state": "CORRECT",
                "feedback": []
              },
              {
                "repetition": 2,
                "state": "CORRECT",
                "feedback": []
              },
              {
                "repetition": 3,
                "state": "FAILED",
                "feedback": [
                  "Your back is not forward enough"
                ]
              },
              {
                "repetition": 4,
                "state": "CORRECT",
                "feedback": []
              },
              {
                "repetition": 5,
                "state": "IMPROPER",
                "feedback": [
                  "Your back is leaning too forward"
                ]
              },
              {
                "repetition": 6,
                "state": "IMPROPER",
                "feedback": [
                  "Your thighs drop too below your knees",
                  "Your back is not forward enough"
                ]
              },
              {
                "repetition": 7,
                "state": "FAILED",
                "feedback": [
                  "Your knees are too low, making them closer to your toes",
                  "Your back is not forward enough"
                ]
              }
            ]
          },
          {
            "session": "s_003",
            "date": "06/01/2025",
            "performance": [
              {
                "repetition": 0,
                "state": "CORRECT",
                "feedback": []
              },
              {
                "repetition": 1,
                "state": "CORRECT",
                "feedback": []
              },
              {
                "repetition": 2,
                "state": "CORRECT",
                "feedback": []
              },
              {
                "repetition": 3,
                "state": "CORRECT",
                "feedback": []
              },
              {
                "repetition": 4,
                "state": "CORRECT",
                "feedback": []
              },
              {
                "repetition": 5,
                "state": "CORRECT",
                "feedback": []
              },
              {
                "repetition": 6,
                "state": "CORRECT",
                "feedback": []
              },
              {
                "repetition": 7,
                "state": "CORRECT",
                "feedback": []
              },
              {
                "repetition": 8,
                "state": "CORRECT",
                "feedback": []
              },
              {
                "repetition": 9,
                "state": "CORRECT",
                "feedback": []
              }
            ]
          }
        ]
        
        - **Feedback User:**
        
        [
          {
            "session": "s_001",
            "date": "01/01/2025",
            "motivation": [
              "You are doing great, Miyu_9! Remember your main objective of losing weight. Keep pushing yourself and you'll reach your goal in no time!",
              "Great job on maintaining a consistent training schedule and variety in your workouts. This will help you achieve your fitness goals."
            ],
            "motivation_score": 4
          },
          {
            "session": "s_002",
            "date": "03/01/2025",
            "motivation": [
              "You're doing great on your weight loss journey! Remembering that every small step counts towards your goal of losing more weight is inspiring.",
              "Keep pushing yourself and staying committed to your workout routine."
            ],
            "motivation_score": 2
          },
          {
            "session": "s_003",
            "date": "06/01/2025",
            "motivation": [
              "Your goal to lose weight is inspiring! Remember, every small step counts toward achieving your long-term objective. Your progress so far is very good, and you should be proud of yourself for sticking to your exercise routine.",
              "You've shown that you can achieve significant weight loss with consistent training. Keep up the great work!",
              "Your ability to choose cardio exercises aligns with your preferences, which is excellent for maintaining motivation. You're on the right track!"
            ],
            "motivation_score": 5
          }
        ]
        
        ## Output
        
        1. **Performance Feedback:**
            - Provide directions and tips on fixing mistakes made by users that are not too lengthy.
            - Each Performance Feedback is divided into “repetition” and “details” information.
        2. **Motivational Message:** 
            - A personalized message to encourage the user to continue their progress, addressing their goals and preferences.
            - Divide it into paragraphs - paragraphs that are delivered in the form of arrays.
        3. **Safety Note Section:** 
            - Provide a safety or health-related recommendation based on the 'Medical History and Physical Condition' data.
        
        Return the Performance Feedback, Motivational Message, Safety Note Section by following the JSON structure:
        {
            "performance_feedback": [
                {
                    "rep": "<integer>",
                    "state": "<string>",
                    "details": "<string>"
                }
            ],
            "motivation": [
                "<string>",
                "<string>",
                "<string>"
            ],
            "safety": "<string>"
        }
        """
    )

    # Example JSON input


    # Run the model
    response = run_ollama(PROMPT_TEMPLATE)
    print(response)
