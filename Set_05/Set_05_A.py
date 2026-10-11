"""ICT-4202 AI & ML Laboratory — Set 05, Question 1.
Three-room cleaning agent
Run: python Set_05/Set_05_A.py
"""

# The question does not set initial conditions: these are an explicit reproducible example.
environment={'A':'Dirty','B':'Clean','C':'Dirty'}
locations=['A','B','C']
location='A'
print('Initial state (illustrative):', environment,'| starting at',location)
for step in range(1,14):
    percept=(location,environment[location])
    if all(s=='Clean' for s in environment.values()): action='NoOp'
    elif environment[location]=='Dirty': action='Suck'
    else: action='MoveRight'  # Cyclic route A -> B -> C -> A
    if action=='Suck': environment[location]='Clean'
    elif action=='MoveRight': location=locations[(locations.index(location)+1)%3]
    print(f'{step:02d} | location={percept[0]} | percept={percept} | action={action:9} | after={environment}')
    if action=='NoOp': break
assert all(s=='Clean' for s in environment.values())
