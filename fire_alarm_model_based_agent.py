import random

model = {'Smoke_detector': 'unknown', 'Temp_detector': 'unknown'}
world_state = 'Danger'
action = 'No action'

def update_state(action, percept, model):
    Smoke = percept[0]
    Temp = percept[1]
    model['Smoke_detector'] = Smoke
    model['Temp_detector'] = Temp

    global world_state
    
    if action == 'Sound Alarm, Water Alarm':
            model['Smoke_detector'] = 'No Smoke'
            model['Temp_detector'] = 'Low Temp'
    if action == 'Sound Alarm':
            model['Smoke_detector'] = 'No Smoke'
    if action == 'Water Alarm':
            model['Temp_detector'] = 'Low Temp' 
    if action == 'No action':
        world_state = 'Safe'
    else:
        world_state = 'Danger'       
    return world_state

def model_based_reflex_agent(percept):
    Smoke = percept[0]
    Temp = percept[1]

    global world_state, action, model

    if world_state == 'Safe':
        action = 'No action'
    elif Smoke == 'Smoke' and Temp == 'High Temp':
        action = 'Sound Alarm, Water Alarm'
    elif Smoke == 'Smoke' and Temp == 'Low Temp':
        action = 'Sound Alarm'
    elif Smoke == 'No Smoke' and Temp == 'High Temp':
        action = 'Water Alarm'
    elif Smoke == 'No Smoke' and Temp == 'Low Temp':
        action = 'No action'

    world_state = update_state(action, percept, model)
    print('Perception: ' + str(percept))
    print('Action Performed: ' + action)
    print('Model: ' + str(model))
    print('State: ' + str(world_state))
    return action

Smoke_detector = random.choice(['Smoke', 'No Smoke'])
Temp_detector = random.choice(['High Temp', 'Low Temp'])

while True:
    print('*****')
    action = model_based_reflex_agent((Smoke_detector, Temp_detector))
    if action == 'Sound Alarm, Water Alarm':
        Smoke_detector = 'No Smoke'
        Temp_detector = 'No Temp'
    elif action == 'Sound Alarm':
        Smoke_detector = 'No Smoke'
        Temp_detector = random.choice(['High Temp', 'Low Temp'])
    elif action == 'Water Alarm':
        Smoke_detector = random.choice(['Smoke', 'No Smoke'])
        Temp_detector = 'Low Temp'
    elif action == 'No action':
        cmd = input('Continue? (yes/no): ')
        if cmd.lower() != 'yes':
            break
        Smoke_detector = random.choice(['Smoke', 'No Smoke'])
        Temp_detector = random.choice(['High Temp', 'Low Temp'])
        model = {'Smoke_detector': 'unknown', 'Temp_detector': 'unknown'}
        world_state = 'Danger'
        action = 'No action'
