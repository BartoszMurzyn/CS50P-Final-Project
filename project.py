import random

EXERCISE_LIBRARY = {
    #Exercises Library with division for main and accessories
    "chest":{
        "main":["Floor Press", "Bench Press", "Incline Bench Press"],
        "acc":["DB Flyes", "Hammer Chest Press", "DB Bench Press", "DB Incline Bench Press", "Push Up"]
    },

    "back":{
        "main":["Bend Over Row", "Pendlay Row", "Pull Up", "Chin Up"],
        "acc":["DB Row", "TRX Row", "Inverted Row", "Hammer Row", "Lats Pulldown", "Cable Row"]
    },

    "quads":{
        "main":["Back Squat", "Front Squat", "Hack Squat"],
        "acc":["Lunges", "Bulgarian Squats", "DB Split Squats", "Legs Extension"]
    },

    "hams":{
        "main":["Deadlift", "TrapBar Deadlift", "Romanian Deadlift"],
        "acc":["KB RDL", "KB Deadlift", "Single Leg RDL", "Hams Curls"]
    },

    "glutes":{
        "main":["Hip Thrust", "Glute Bridge",],
        "acc":["Single Leg Hip Thrust", "Single Leg Glute Bridge", "GHD Hip Extension"]
    },

    "shoulders":{
        "main":["Over Head Press", "Landmine Shoulder Press"],
        "acc":["Lateral Raises", "DB Shoulder Press", "Cable Raises", "Facepulls"]
    },

    "arms":{
        "acc":["Biceps Curls", "Biceps Hammer Curls", "Cable Biceps Curls","Triceps Cable Extension",
               "Triceps French Press", "Dips", "Over Head Triceps Extension" ]
    },

    "core":{
        "acc":["Cable Crunch", "Hollow Body", "Side Plank", "Plank", "DeadBug"]
    }
}
REPS_RANGES = {
    "strength": {"reps_min": 3,"reps_max": 6, "sets_min": 3, "sets_max": 6},
    "hypertrophy": {"reps_min": 3,"reps_max": 12, "sets_min": 3, "sets_max": 5},
    "bodyweight": {"duration": "15-30sec", "sets": "3-4"}
}

def main():
    weight,frequency,goal = get_input()
    plan = generate_plan(weight,frequency,goal)
    output_plan(plan)


def get_input():
    """Gets user input and saves 3 variables: Weight, Training Frequency and Training Goal"""
    print("Welcome to Beginners Gym Workout Planner!")
    weight = input("What is your current weight? ")
    frequency = int(input("How often do you plan to workout?\n 2 times\n 3 times\n 4 times? "))
    goal = input("What is your goal?\n 1.Strength\n 2.Hypertrophy ").lower()

    if not weight.isnumeric():
        raise ValueError("Weight has to be a number")
    if frequency not in [2,3,4]:
        raise ValueError("Training frequency must be between 2 or 4")
    if goal not in ['strength', "hypertrophy"]:
        raise ValueError("Goal has to be one of two given")

    return weight,frequency,goal

def select_exercise(muscle_group,exercise_type = "acc", amount=1):
    """Helper function to get random exercises from Exercise Library with given amount of exercises"""
    exercise = EXERCISE_LIBRARY.get(muscle_group).get(exercise_type).copy()
    selected_exercises = random.sample(exercise, amount)
    return selected_exercises


def get_exercises(frequency):
    """Gives a list of exercises depending on users frequency"""

    sessions = []
    main_muscle_groups = ["chest","back","quads","shoulders","glutes",]
    acc_muscle_groups = ["back","quads","chest","glutes","shoulders","hams","arms"]

    for num in range(frequency):
        session = {"main":[], "accessory":[], "core":[]}

        main_exercise_1 = main_muscle_groups[num % len(main_muscle_groups)]
        main_exercise_2 = main_muscle_groups[(num + 1) % len(main_muscle_groups)]

        session['main'].append(select_exercise(main_exercise_1, "main",1)[0])
        session['main'].append(select_exercise(main_exercise_2, "main",1)[0])

        if frequency == 2:
            for acc in range(0,5):
                session["accessory"].append(select_exercise((acc_muscle_groups[acc]))[0])
        elif frequency == 3:
            for acc in range(0,4):
                session["accessory"].append(select_exercise((acc_muscle_groups[acc]))[0])
        elif frequency == 4:
            for acc in range(0,3):
                session["accessory"].append(select_exercise((acc_muscle_groups[acc]))[0])

        session["core"].append(select_exercise("core")[0])

        sessions.append(session)

    return sessions


def generate_plan(weight, frequency, goal):
    sessions_per_week = get_exercises(frequency)  # Get sessions based on frequency
    plan = []

    for week in range(1, 5):  # Loop through 4 weeks
        weekly_sessions = []  # Store all sessions for this week

        for session in sessions_per_week:  # Loop through each session
            session_plan = {"main": [], "accessory": [], "core": []}

            # Process main exercises
            for exercise in session["main"]:
                progression = apply_progression("main", goal, week, int(weight))
                session_plan["main"].append({
                    "exercise": exercise,
                    "sets": progression["sets"],
                    "reps": progression["reps"],
                    "load": progression["load"]
                })

            # Process accessory exercises
            for exercise in session["accessory"]:
                progression = apply_progression("accessory", goal, week, int(weight))
                session_plan["accessory"].append({
                    "exercise": exercise,
                    "sets": progression["sets"],
                    "reps": progression["reps"],
                    "load": progression["load"]
                })

            # Process core exercises
            for exercise in session["core"]:
                progression = apply_progression("core", goal, week, int(weight))
                session_plan["core"].append({
                    "exercise": exercise,
                    "sets": progression["sets"],
                    "reps": progression["reps"],
                    "load": progression["load"]
                })

            weekly_sessions.append(session_plan)  # Add the session to the week

        plan.append({"Week": week, "Sessions": weekly_sessions})  # Add week to the plan
    return plan

def apply_progression(exercise_type, goal,week, weight ):
    """Makes progression for each exercise depending on users weight"""
    progression = {"sets":0, "reps":0, "load": 0}
    if exercise_type == "main":
        if goal == "strength":
                progression["reps"] = 3 + week
                progression["sets"] = 5
                progression["load"] = round(weight * (0.7 + 0.025 * week),2)
        else:
                progression["reps"] = 6 + week
                progression["sets"] = 4
                progression["load"] = round(weight * (0.5 + 0.05 * week), 2)

    elif exercise_type == "accessory":
        if goal == "strength":
                progression["reps"] = 8 + week
                progression["sets"] = 3
                progression["load"] = round(weight * (0.1 + 0.02 * week), 2)
        else:
                progression["reps"] = 6 + week
                progression["sets"] = 3
                progression["load"] = round(weight * (0.15 + 0.02 * week), 2)

    elif exercise_type == "core":
        progression["reps"] = "15-30s/12reps"
        progression["sets"] = 3
        progression["load"] = "Bodyweight"

    return progression

def output_plan(whole_plan):
    for week in whole_plan: #Looping through each week
        print(f"Week: {week["Week"]:}")
        for number, session in enumerate(week["Sessions"], start= 1): #Looping through each session
            print(f"Training {number}:")
            print(f" {'Category':<15} {'Exercise':<30} {'Sets':<5} {'Reps':<15} {'Load':<10}")
            for category, exercises in session.items(): #Looping through each category
                for exercise in exercises: #Looping through each exercise in each category
                    exercise_name = exercise['exercise']
                    sets = exercise['sets']
                    reps = exercise['reps']
                    load = exercise['load']
                    print(f" {category:<15} {exercise_name:<30} {sets:<5} {reps:<15} {load:<10}")
            print()
    print()

if __name__ == "__main__":
    main()
