import pprint
count = {}

inv = {'bronze coin': 14, 'silver coin': 15, 'cakes': 1, 'Sweet rolls': 2, \
       'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

dragonLoot = ['gold coin', 'silver coin', 'dagger', 'magic dagger', 'ruby', 'gold coin']
dragonLoot2 = ['gold coin', 'dragon scale', 'dragon axe', 'dragon bone']

def displayInventory(inv):
    print('Inventory:')
    for k, v in inv.items():
        pprint.pprint(str(k) + ' ' + str(v))
    total = 0
    for i in inv.values():
        total = total + int(i)
    pprint.pprint('The total number of items is: ' + str(total))

def addToInventory(inv, loot):
    for i in loot:
        if i in inv:
            inv[i] += 1
        else:
            inv[i] = 1

    return(inv)
            


displayInventory(inv)
print()
print('Dragon loot added below:')
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
print()
print('Dragon loot 2 added below:')
inv = addToInventory(inv, dragonLoot2)
displayInventory(inv)


