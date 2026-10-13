"""ICT-4202 AI & ML Laboratory — Set 10, Question 1.
Integrated knowledge-based agent
Run: python Set_10/Set_10_A.py
"""

rules = [
    ({"TemperatureHigh"}, "Hot"),
    ({"Hot", "Humid"}, "Uncomfortable"),
    ({"Uncomfortable"}, "FanOn"),
    ({"Rain"}, "Humid")
]

cases = [
    ("TemperatureHigh only", {"TemperatureHigh"}),
    ("TemperatureHigh + Humid", {"TemperatureHigh", "Humid"}),
    ("TemperatureHigh + Rain", {"TemperatureHigh", "Rain"})
]

for name, given in cases:
    known = set(given)
    print("\n", name)
    print("Given facts:", given)

    while True:
        changed = False
        for premises, conclusion in rules:
            if premises <= known and conclusion not in known:
                known.add(conclusion)
                print(premises, "=>", conclusion)
                changed = True
        if not changed:
            break

    print("Inferred facts:", known - given)
    print("Final facts:", known)
    print("FanOn?", "FanOn" in known)
