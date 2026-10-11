"""ICT-4202 AI & ML Laboratory — Set 01, Question 1.
Simple reflex vacuum and PEAS
Run: python Set_01/Set_01_A.py
"""

def vacuum_policy(location, rooms):
    if all(status == 'Clean' for status in rooms.values()):
        return 'NoOp'
    if rooms[location] == 'Dirty':
        return 'Suck'
    return 'Left' if location == 'B' else 'Right'

rooms = {'A': 'Dirty', 'B': 'Clean'}
location = 'B'
trace = []
for step in range(1, 12):
    percept = (location, rooms[location])
    action = vacuum_policy(location, rooms)
    trace.append((step, percept, action, dict(rooms)))
    print(f'Step {step}: percept={percept}, action={action}, rooms(before)={rooms}')
    if action == 'NoOp': break
    if action == 'Suck': rooms[location] = 'Clean'
    elif action == 'Left': location = 'A'
    elif action == 'Right': location = 'B'
print('Final environment:', rooms)
assert all(v == 'Clean' for v in rooms.values())
assert trace[-1][2] == 'NoOp'
