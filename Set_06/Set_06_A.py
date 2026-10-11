"""ICT-4202 AI & ML Laboratory — Set 06, Question 1.
Exam eligibility inference
Run: python Set_06/Set_06_A.py
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

rules = [({'Registered'},'Student'),({'Student'},'HasID'),
         ({'Student','PaidFee'},'ExamEligible'),
         ({'ExamEligible'},'CanEnterExamHall')]
facts1,trace1=print_inference('Case 1: Registered only',{'Registered'},rules)
facts2,trace2=print_inference('Case 2: Registered + PaidFee',{'Registered','PaidFee'},rules)
assert 'CanEnterExamHall' not in facts1 and 'CanEnterExamHall' in facts2

import itertools
print('  P      Q      P -> Q')
for p, q in itertools.product([False, True], repeat=2):
    implication = (not p) or q
    print(f'{str(p):5}  {str(q):5}  {implication}')
