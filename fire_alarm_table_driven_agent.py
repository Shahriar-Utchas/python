table={('Smoke','High Temp'):    'Sound Alarm, Water Alarm',
       ('Smoke','Low Temp'):     'Sound Alarm',
       ('No Smoke','High Temp'): 'Water Alarm',
       ('No Smoke','Low Temp'):  'No Alarm'}

percepts=[] 
def table_driven_agent(percept):
    print('Perception Received: '+ str(percept))
    percepts.append(percept)
    action = lookup(percept,table)
    return action

def lookup(p,t):
    return t[p]


import random
Smoke_detector = random.choice(['Smoke','No Smoke'])
Temp_detector  = random.choice(['High Temp','Low Temp'])

while True:
    action = table_driven_agent((Smoke_detector, Temp_detector))
    print('Action Performed: '+ action)
    cmd = input('Get Perception (yes/no): ')
    if(cmd != 'yes'): break
    if action == 'Sound Alarm, Water Alarm':
        Smoke_detector = 'No Smoke'
        Temp_detector  = 'Low Temp'
    elif action == 'Sound Alarm':
        Smoke_detector = 'No Smoke'
        Temp_detector  = random.choice(['High Temp','Low Temp'])
    elif action == 'Water Alarm':
        Temp_detector  = 'Low Temp'
        Smoke_detector = random.choice(['Smoke','No Smoke'])
    else:
        Smoke_detector = 'No Smoke'
        Temp_detector  = 'Low Temp'