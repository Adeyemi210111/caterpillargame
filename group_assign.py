
def choice(new):
    import random
    choice = random.choice(members)
    new.append(choice)
    members.remove(choice)
    return new

def group1():
    y = 0
    while y < 4:
        choice(groupA)
        y = y + 1
    for i in groupA:
        print(i, 'is in group 1')

def group2():
    y = 0
    while y < 4:
        choice(groupB)
        y = y + 1
    for i in groupB:
        print(i, 'is in group 2')

def group3():
    y = 0
    while y < 4:
        choice(groupC)
        y = y + 1
    for i in groupC:
        print(i, 'is in group 3')

def group4():
    y = 0
    while y < 5:
        choice(groupD)
        y = y + 1
    for i in groupD:
        print(i, 'is in group 4')

members = ['Oluwatobi', 'Abiodun', 'fauziyat', 'Oluwadara', 'Caleb', 
'Ladetunji', 'Utibe', 'soteju', 'Ayodele', 'Irewolede', 'ibrahim', 
'Ayedun', 'Mistura', 'Taiwo', 'Oseafiana', 'James', 'Oluranti']
groupA = []
groupB = []
groupC = []
groupD = []

group1()
group2()
group3()
group4()


    
    
