"""ICT-4202 AI & ML Laboratory — Set 10, Question 1.
Integrated knowledge-based agent
Run: python Set_10/Set_10_A.py
"""


def forward_chain(initial_facts, rules):
    """Data-driven inference: rules are (premise-set, conclusion) pairs."""
    known = set(initial_facts)
    trace = []
    while True:
        newly_added = False
        for premises, conclusion in rules:
            if premises.issubset(known) and conclusion not in known:
                known.add(conclusion)
                trace.append((sorted(premises), conclusion))
                newly_added = True
        if not newly_added:
            break
    return known, trace

def print_inference(label, initial, rules):
    known, trace = forward_chain(initial, rules)
    print(f"\n{label} | Initial facts: {sorted(initial)}")
    for i, (prem, conclusion) in enumerate(trace, 1):
        print(f"  {i}. {prem}  =>  {conclusion}")
    if not trace: print("  No new rule fired.")
    print('Final facts:', sorted(known))
    return known, trace

rules=[({'TemperatureHigh'},'Hot'),({'Hot','Humid'},'Uncomfortable'),
       ({'Uncomfortable'},'FanOn'),({'Rain'},'Humid')]
cases=[('TemperatureHigh only',{'TemperatureHigh'}),
       ('TemperatureHigh + Humid',{'TemperatureHigh','Humid'}),
       ('TemperatureHigh + Rain',{'TemperatureHigh','Rain'})]
for title,given in cases:
    known,trace=print_inference(title,given,rules)
    print('Given (asserted):',sorted(given))
    print('Derived (inferred):',sorted(known-given),'| FanOn?', 'FanOn' in known)
