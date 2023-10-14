model = {'A':'Unknown', 'B':'Unknown'}
world_state = 'Bad'
action = 'Unknown'

def update_state(action, percept, model):
    location = percept[0]
    status = percept[1]
    model[location] = status #udate the model based on current perception

    global world_state
    #udate the model based on action
    if action == 'Suck':
        model[location]='Clean'
    # model checking to update world state
    if model['A']=='Clean' and model['B']=='Clean':
        world_state = 'Good'
    else:
        world_state = 'Bad'
    return world_state


def model_based_reflex_agent(percept):
    location = percept[0]
    status = percept[1]

    global world_state,action,model

    if world_state == 'Good':
        action = 'Pause'
        return action
    elif status == 'Dirty':
        action = 'Suck'
    elif location == 'A':
        action = 'Right'
    elif location == 'B':
        action = 'Left'
    world_state = update_state(action, percept, model)
    print('Perception: '+str(percept))
    print('Action Performed: '+ action)
    print('Model: '+str(model))
    print('State: '+str(world_state))
    return action

import random
Location = random.choice(['A','B'])
Condition= random.choice(['Clean','Dirty'])

while True:
    print('*****')
    action = model_based_reflex_agent((Location,Condition))
    if action == 'Right':
        Location = 'B'
        Condition = random.choice(['Clean','Dirty'])
    elif action == 'Left':
        Location = 'A'
        Condition = random.choice(['Clean','Dirty'])
    elif action == 'Suck':
        Condition = 'Clean'
    elif action == 'Pause':
        cmd = input('Stopped. Do restart? (yes/no): ')
        if(cmd == 'no' or cmd != 'yes'): break
        Location = random.choice(['A','B'])
        Condition = random.choice(['Clean','Dirty'])
        model = {'A':'Unknown', 'B':'Unknown'}
        world_state = 'Bad'
        action = 'Unknown'