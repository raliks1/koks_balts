machines = ["Leg", "Chest", "Arm", "Cardio", "Joga"]

plan = {
    "Diena 1": ["Leg", "Chest", "Arm"],
    "Diena 2": ["Cardio", "Joga", "Leg"],
    "Diena 3": ["Chest", "Arm", "Cardio"]
}

for diena, masinas in plan.items():
    print(f"{diena}: {', '.join(masinas)}")

# test_gym_plan.py

import io
import sys
from contextlib import redirect_stdout

# Import the gym_plan module using absolute import
import gym_plan

def test_gym_plan_output():
    expected_output = (
        "Diena 1: Leg, Chest, Arm\n"
        "Diena 2: Cardio, Joga, Leg\n"
        "Diena 3: Chest, Arm, Cardio\n"
    )
    f = io.StringIO()
    # Re-run the print loop and capture output
    with redirect_stdout(f):
        for diena, masinas in gym_plan.plan.items():
            print(f"{diena}: {', '.join(masinas)}")
    output = f.getvalue()
    assert output == expected_output

def test_all_plan_machines_in_machines_list():
    for masinas in gym_plan.plan.values():
        for masina in masinas:
            assert masina in gym_plan.machines