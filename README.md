# __Beginner’s Gym Workout Planner__
#### Video Demo:  <https://youtu.be/zL3SGklAYNE>

## __Description__
The Beginner’s Gym Workout Planner is a Python-based program designed to create a personalized 4-week training plan. It generates structured workout sessions based on the user’s weight, weekly training frequency, and fitness goal (strength or hypertrophy). The program includes a variety of exercises for different muscle groups, ensures progressive overload, and prints the plan in an organized table format.
 Project structure :
 - project.py
 - test_project.py
 - requirements.txt
 - README.md

## __Libraries__

__RANDOM__ : This module implements pseudo-random number generators for various distributions.. [(Readmore)](https://docs.python.org/3/library/random.html)


## **Installing Libraries**
there is a a requirements.txt file that has all the libraries used.

and simply can be install by this pip command:

```pip install -r requirements.txt```

## __How to Use__

```
```python project.py```
```Follow the prompts to input your details.```
```Review and follow the generated workout plan.```
```
## __Features__

	•	Custom Training Plans: Tailors workouts to user preferences (frequency and goal).
	•	Progressive Overload: Adjusts sets, reps, and loads weekly for consistent progress.
	•	Diverse Exercises: Includes both main and accessory exercises for balanced training.
	•	Core Workouts: Incorporates core exercises in every session.


## __Program Workflow__

	1.	Input Collection: User enters weight, training frequency, and goal.
	2.	Session Creation: Random exercises are chosen based on frequency and categories.
	3.	Plan Generation: A progressive 4-week plan is generated with increasing difficulty.
	4.	Plan Output: The workout plan is displayed in a clear, structured format.

### __main()__ __function__ :
Acts as the entry point of the program. It gathers user inputs, generates the workout plan, and outputs it.


#### __get_input()__ __function__ : Collects and validates user inputs for weight, training frequency, and fitness goal..
	•	Inputs Collected:
	•	Weight (numeric).
	•	Training frequency (2, 3, or 4 sessions per week).
	•	Fitness goal (strength or hypertrophy).
	•	Validation: Ensures inputs are valid; raises errors for invalid values.
#### __select_exercise(muscle_group, exercise_type="acc", amount=1)__ function :Randomly selects exercises from the library for a given muscle group and type (main or accessory).
Parameters:
	•	muscle_group: The target muscle group (e.g., chest, back).
	•	exercise_type: Type of exercise (“main” or “acc”). Default is “acc”.
	•	amount: Number of exercises to select. Default is 1.
	•	Output: A list of randomly selected exercises.
#### **get_exercises(frequency)** function: Creates a structured list of exercises for each training session based on user-selected frequency (2, 3, or 4 sessions per week).
Process:
	•	Loops through the weekly sessions and selects exercises for main, accessory, and core categories.
	•	Adjusts the number of accessory exercises based on training frequency.
	•	Output: A list of session dictionaries with main, accessory, and core exercises.
#### **generate_plan(weight, frequency, goal) function** : Builds a 4-week progressive workout plan using user inputs.
    •	Calls get_exercises() to get the base sessions.
	•	Loops through 4 weeks to apply progressive overload using apply_progression().
	•	Constructs session details, including sets, reps, and load for each exercise.
	•	Output: A detailed 4-week workout plan.
#### **apply_progression(exercise_type, goal, week, weight) function** : Calculates progressive overload for each exercise based on its type, user’s goal, weight, and the current week.
	•	Parameters:
        •	exercise_type: Type of exercise (main, accessory, or core).
        •	goal: User’s fitness goal (strength or hypertrophy).
        •	week: Current week of the plan.
        •	weight: User’s weight, used to scale loads.
	•	Output: A dictionary with sets, reps, and load for the exercise.
#### **output_plan(whole_plan) function** : Outputs the workout plan in a well-formatted table for each week and session.
•	Loops through each week and session in the plan.
	•	Displays exercise details (name, sets, reps, load) grouped by category (main, accessory, core).
	•	Output: Prints the plan in the terminal.

### Author : Bartosz Murzyn.
