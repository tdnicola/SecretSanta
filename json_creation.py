from dataclasses import dataclass
import json

new_list = []


@dataclass
class Person:
    name: str
    phone: int
    previousMatches: new_list


# creating list
santaList = []
# appending instances to list
person1 = Person('Tony', 111, ['Tony', 'Monika', 'Deke', 'Patrick', 'Haley'])
person2 = Person('Zach', 222, ['Zach', 'Deke', 'Tony'])
person3 = Person('Haley', 333, ['Haley', 'Marie', 'Steve', 'Patrick', 'Tony'])
person4 = Person('Patrick', 444, ['Patrick',
                 'Tony', 'Haley', 'Dystiny', 'Marie'])
person5 = Person(
    'Marie', 555, ['Marie', 'Monika', 'Haley', 'Steve', 'Patrick'])
person6 = Person('Deke', 666, ['Deke', 'Steve', 'Marie', 'Tony', 'Monika'])
person7 = Person(
    'Monika', 777, ['Monika', 'Marie', 'Dystiny', 'Haley', 'Deke'])
person8 = Person(
    'Steve', 888, ['Steve', 'Monika', 'Patrick', 'Zach', 'Dystiny'])
person9 = Person('Dystiny', 999, ['Dystiny', 'Patrick', 'Zach', 'Steve'])

santaList.extend([person1, person2, person3, person4,
                 person5, person6, person7, person8, person9])

# Serializing json
json_object = json.dumps(santaList, indent=4, default=vars)

# Writing to sample.json
with open("sample.json", "w") as outfile:
    outfile.write(json_object)
print(santaList)
