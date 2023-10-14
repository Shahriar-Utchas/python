def simple_reflex_agent(percept):
    print('Perception Received: '+ str(percept))
    location = percept[0]
    status = percept[1]
    if status =='Dirty':
        action = 'Suck'
    elif location == 'A':
        action = 'Right'
    elif location =='B':
        action = 'Left'
    return action

import random
Location = random.choice(['A','B'])
Condition = random.choice(['Clean','Dirty'])

while True:
    action= simple_reflex_agent((Location,Condition))
    print('Action Performed: '+ action)
    cmd = input('Get Perception (yes/no): ')
    if(cmd == 'no' or cmd != 'yes'): break
    if action == 'Right':
        Location = 'B'
        Condition = random.choice(['Clean','Dirty'])
    elif action== 'Left':
        Location = 'A'
        Condition = random.choice(['Clean','Dirty'])
    else:
        Condition = 'Clean'