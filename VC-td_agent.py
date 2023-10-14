table={('A','Clean'):'Right',
       ('A','Dirty'):'Suck',
       ('B','Clean'):'Left',
       ('B','Dirty'):'Suck'}

percepts=[]  # to store percept sequence
def table_driven_agent(percept):
    print('Perception Received: '+ str(percept))
    percepts.append(percept) # updating percept history
    action = lookup(percept,table) # searching for action
    return action

def lookup(p,t):
    return t[p]

# lets simulate the agent
import random
Location = random.choice(['A','B'])
Condition = random.choice(['Clean','Dirty'])

while True: # to perceieve environment repeatedly
    action = table_driven_agent((Location, Condition))
    print('Action Performed: '+ action)
    cmd = input('Get Perception (yes/no): ')
    if(cmd != 'yes'): break
    if action == 'Right':
        Location = 'B'
        Condition = random.choice(['Clean','Dirty'])
    elif action == 'Left':
        Location = 'A'
        Condition = random.choice(['Clean','Dirty'])
    else:
        Condition = 'Clean'