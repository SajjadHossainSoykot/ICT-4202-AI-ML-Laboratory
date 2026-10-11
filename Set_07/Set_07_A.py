"""ICT-4202 AI & ML Laboratory — Set 07, Question 1.
FOL relations and siblings
Run: python Set_07/Set_07_A.py
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

parents={('Rahman','Hasan'),('Rahman','Nabila'),('Hasan','Rafi'),
         ('Nabila','Tania'),('Rafi','Samia')}
def grandchildren_of(person):
    return sorted({z for x,z in grandparent_relations(parents) if x==person})
def grandparent(x,z):
    return (x,z) in grandparent_relations(parents)
def siblings(x,y):
    return x!=y and tuple(sorted((x,y))) in siblings_relations(parents)
print_relations(parents)
for name in ['Rahman','Hasan','Nabila','Rafi']:
    print(f'grandchildren_of({name}): {grandchildren_of(name)}')
print('grandparent(Rahman,Rafi)=',grandparent('Rahman','Rafi'))
print('siblings(Hasan,Nabila)=',siblings('Hasan','Nabila'))
print('siblings(Hasan,Hasan)=',siblings('Hasan','Hasan'))
assert not siblings('Hasan','Hasan')
