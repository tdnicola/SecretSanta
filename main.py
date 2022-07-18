import json
import random

cont = 0
secret_santa_list = []
names = []

f = open('sample.json')
santa_list = json.load(f)

for name in santa_list:
    names.append(name['name'])

while cont == 0:
    redo = False
    possible_santa = names.copy()

    for i in range(0, len(names)):
        recip = random.randint(0, len(possible_santa) - 1)
        x = 0

        while (x == 0):
            if names[i] in santa_list[recip]['previousMatches']:
                if len(possible_santa) == 1:
                    redo = True
                    x = 1
                else:
                    recip = random.randint(0, len(possible_santa) - 1)
            else:
                x = 1
        if redo != True:
            secret_santa_list.append(
                {"secretSanta": santa_list[recip]['name'], "phone": santa_list[recip]["phone"], "giftTo": names[i]})
            possible_santa.pop(recip)
            cont = 1
        else:
            cont = 0

print(secret_santa_list)
print('Copy and past below into extension:')
print('Hello there, your Secret Santa person is {name}.')
for gifter in secret_santa_list:
    print(f"{gifter['phone']}, {gifter['giftTo']} ")
