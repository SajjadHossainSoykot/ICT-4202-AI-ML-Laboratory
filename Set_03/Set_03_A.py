"""ICT-4202 AI & ML Laboratory — Set 03, Question 1.
FOL family relationships
Run: python Set_03/Set_03_A.py
"""

from itertools import combinations

def children_of(person, parents):
    return sorted({child for parent, child in parents if parent == person})

def grandparent_relations(parents):
    return sorted({(x, z) for x, y in parents for middle, z in parents if y == middle})

def siblings_relations(parents):
    result = set()
    for p in {person for person, child in parents}:
        children = children_of(p, parents)
        for x, y in combinations(children, 2):
            result.add((x, y))  # Canonical unordered pair: no duplicates/self-pairs.
    return sorted(result)

def print_relations(parents):
    people = sorted({x for pair in parents for x in pair})
    print('Parent facts:', sorted(parents))
    print('Children queries:')
    for name in people:
        kids = children_of(name, parents)
        if kids: print(f'  children_of({name}) = {kids}')
    print('Grandparent relations:', grandparent_relations(parents))
    print('Sibling relations (unordered):', siblings_relations(parents))

parents = {('Ali','Babu'),('Ali','Rina'),('Babu','Karim'),
           ('Rina','Sumi'),('Karim','Nila')}
print_relations(parents)
print('Example binding: Parent(Ali,Babu) and Parent(Babu,Karim) => Grandparent(Ali,Karim)')
assert ('Ali','Karim') in grandparent_relations(parents)
assert ('Babu','Rina') in siblings_relations(parents)
