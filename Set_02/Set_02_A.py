"""ICT-4202 AI & ML Laboratory — Set 02, Question 1.
Forward chaining with weather facts
Run: python Set_02/Set_02_A.py
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

rules = [({'Cloudy'},'Rain'), ({'Rain'},'WetGround'),
         ({'WetGround'},'Slippery'), ({'Slippery'},'DriveSlowly'),
         ({'Rain','Cold'},'WearJacket')]
no_cold, t1 = print_inference('Case A: without Cold', {'Cloudy'}, rules)
with_cold, t2 = print_inference('Case B: with Cold', {'Cloudy','Cold'}, rules)
print('WearJacket without Cold?', 'WearJacket' in no_cold)
print('WearJacket with Cold?', 'WearJacket' in with_cold)
assert 'WearJacket' not in no_cold and 'WearJacket' in with_cold
