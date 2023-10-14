def simple_reflex_agent(percept):
    print('Perception Received: '+ str(percept))
    smoke_detector = percept[0]
    temp_detector = percept[1]
    if smoke_detector =='Smoke' and temp_detector == 'High Temp':
        action = 'Sound Alarm, Water'
    elif smoke_detector =='Smoke' and temp_detector == 'Low Temp':
        action = 'Sound Alarm'
    elif smoke_detector =='No Smoke' and temp_detector == 'High Temp':
        action = 'Water Alarm'
    else:
        action = 'Nothing'
    return action


import random
Smoke_detector = random.choice(['Smoke','No Smoke'])
Temp_detector  = random.choice(['High Temp','Low Temp'])

while True:
    action = simple_reflex_agent((Smoke_detector, Temp_detector))
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
