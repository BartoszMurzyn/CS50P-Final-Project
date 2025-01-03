from project import select_exercise, get_input, get_exercises, apply_progression, generate_plan, output_plan, EXERCISE_LIBRARY
from unittest.mock import patch

def test_select_exercise():
    exercise = select_exercise("chest", "main", 1)
    assert len(exercise) == 1
    assert exercise[0] in EXERCISE_LIBRARY["chest"]["main"]

    # Test accessory selection
    exercise = select_exercise("back", "acc", 2)
    assert len(exercise) == 2
    for ex in exercise:
        assert ex in EXERCISE_LIBRARY["back"]["acc"]


def test_get_input():
    with patch("builtins.input", side_effect=["80", "3", "strength"]):
        weight, frequency, goal = get_input()
        assert weight == "80"
        assert frequency == 3
        assert goal == "strength"

def test_get_exercises():
    sessions = get_exercises(3)
    assert len(sessions) == 3  # 3 sessions for a frequency of 3

    for session in sessions:
        assert "main" in session
        assert "accessory" in session
        assert "core" in session

        assert len(session["main"]) == 2  # Always 2 main exercises
        assert len(session["core"]) == 1  # Always 1 core exercise


def test_apply_progression():
    progression = apply_progression("main", "strength", 1, 100)
    assert progression["sets"] == 5
    assert progression["reps"] == 4  # 3 base + week (1)
    assert progression["load"] > 0

    progression = apply_progression("accessory", "hypertrophy", 2, 80)
    assert progression["sets"] == 3
    assert progression["reps"] == 8  # 6 base + week (2)
    assert progression["load"] > 0

    progression = apply_progression("core", "strength", 3, 70)
    assert progression["sets"] == 3
    assert progression["reps"] == "15-30s/12reps"
    assert progression["load"] == "Bodyweight"

def test_generate_plan():
        plan = generate_plan(100, 3, "strength")
        assert len(plan) == 4  # 4 weeks
        for week in plan:
            assert "Week" in week
            assert "Sessions" in week
            assert len(week["Sessions"]) == 3  # 3 sessions per week for frequency = 3
