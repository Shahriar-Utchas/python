romanian_map = {
    'Arad': {'Sibiu':140, 'Zerind':75, 'Timisoara':118},
    'Zerind': {'Arad':75, 'Oradea':71},
    'Oradea': {'Zerind':71, 'Sibiu': 151},
    'Sibiu': {'Arad':140, 'Oradea':151, 'Fagaras':99, 'Rimnicu':80},
    'Timisoara': {'Arad': 118, 'Lugoj':111},
    'Lugoj': {'Timisoara':111, 'Mehadia':70},
    'Mehadia': {'Lugoj': 70, 'Drobeta':75},
    'Drobeta': {'Mehadia':75, 'Craiova':120},
    'Craiova': {'Drobeta': 120, 'Rimnicu': 146, 'Pitesti': 138},
    'Rimnicu': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
    'Fagaras': {'Sibiu':99, 'Bucharest':211},
    'Pitesti': {'Rimnicu': 97, 'Craiova':138, 'Bucharest':101},
    'Bucharest': {'Fagaras':211, 'Pitesti': 101, 'Giurgiu':90, 'Urziceni':85},
    'Giurgiu': {'Bucharest': 90},
    'Urziceni': {'Bucharest': 85, 'Vaslui':142, 'Hirsova':98},
    'Hirsova': {'Urziceni':98, 'Eforie':86},
    'Eforie': {'Hirsova':86},
    'Vaslui': {'Iasi': 92, 'Urziceni':142},
    'Iasi': {'Vaslui':92, 'Neamt': 87},
    'Neamt': {'Iasi':87}
}

def bfs(start, goal, G):
    expanded= [] # to store the order of nodes expanded
    frontier = [{'Name':start,'Path cost':0, 'Path':[start]}]

    while len(frontier) > 0:
        print('***Frontier', end=': ')
        for node in frontier: print(node['Name'], end = ' - ')
        unode  = frontier.pop(0)     # selceting the node to expand
        u = unode['Name']

        expanded.append(u)
        print('***')
        print("Expanding: "+u)

        # expand u
        for v in G[u].keys():# ['Sibiu', 'Zerind', 'Timisoara']
            if v not in expanded: # process if v is not expanded yet
                print(v+" generated.")
                cost = unode['Path cost'] + G[u][v]
                path =  unode['Path']+ [v]
                vnode = {'Name': v,'Path cost': cost,'Path': path}
                # goal test
                if v == goal:
                    print(expanded)
                    return vnode # breaking from while
                frontier.append(vnode)# store the generated node in the frontier

    print('Failed')

bfs('Arad', 'Bucharest', romanian_map) # change the soure and destination

def dfs(start, goal, G):
    expanded = []  # to store the order of nodes expanded
    stack = [{'Name': start, 'Path cost': 0, 'Path': [start]}]

    while stack:
        print('***Stack', end=': ')
        for node in stack:
            print(node['Name'], end=' - ')

        unode = stack.pop()  # selecting the node to expand
        u = unode['Name']

        if u == goal:
            print(expanded)
            return vnode  # breaking from while
            stack.append(vnode)  # store the generated node in the stack

        expanded.append(u)
        print('***')
        print("Expanding: " + u)

        # expand u
        for v in G[u].keys():  # ['Sibiu', 'Zerind', 'Timisoara']
            if v not in expanded:  # process if v is not expanded yet
                print(v + " generated.")
                cost = unode['Path cost'] + G[u][v]
                path = unode['Path'] + [v]
                vnode = {'Name': v, 'Path cost': cost, 'Path': path}
                stack.append(vnode)


    print('Failed')
dfs('Arad', 'Bucharest', romanian_map) # change the soure and destination
