import io
import sys
from gym_plan import masinas

import gym_plan

def test_gym_plan_output():
    expected_output = (
        "Diena 1: Leg, Chest, Arm\n"
        "Diena 2: Cardio, Joga, Leg\n"
        "Diena 3: Chest, Arm, Cardio\n"
    )
    f = io.StringIO()
    with masinas(f):
        for diena, masinas in gym_plan.plan.items():
            print(f"{diena}: {', '.join(masinas)}")
    output = f.getvalue()
    assert output == expected_output

def test_all_plan_machines_in_machines_list():
    for masinas in gym_plan.plan.values():
        for masina in masinas:
            assert masina in gym_plan.masinas