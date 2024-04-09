# Get words about feedback
def get_feedback_words():
    words = {
        -1: "",
        0: ["Your back is leaning too forward", "When performing squats, it is important to keep your back straight "
                                                "as well as bend forward slightly. Try to focus on placing your "
                                                "weight in your heels and keeping your chest lifted. This will help "
                                                "maintain balance and prevent unnecessary pressure on the lower back."],
        1: ["Your back is not forward enough", "To improve your squat posture, it is important to keep your back "
                                               "straight and your chest lifted. Try to imagine that you are sitting "
                                               "on a low chair, with your weight on your heels and your knees in "
                                               "line with your feet. Also make sure your head and neck are in a "
                                               "neutral position."],
        2: ["Your knees are too low, making them closer to your toes",
            "When performing squats, keeping your thighs from dropping lower than your knees is key to avoiding "
            "injury. It is also very important to maintain the position of the soles of the feet so that they "
            "always touch the surface. And try to push your hips back."],
        3: ["Your thighs drop too below your knees",
            "It is important to keep the thighs parallel to the knees. Try to push the hips back and down until "
            "the thighs align with the knee position and form around 90-degree angle, while keeping the knees "
            "parallel to the feet."]
    }

    return words
