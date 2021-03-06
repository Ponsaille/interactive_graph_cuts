
#return True if sink visited, False if not
#if sink is not visited, then the residual Graph is finished
def bfs(residualGraph, source, sink, parentNode):
    queue = []
    # To check the nodes we've already explored
    explored = [False] * len(residualGraph) #fill visited list
    # adding the start_state in the fringe
    queue.append(source)
    explored[source] = True

    while queue:
        currentNode = queue.pop(0)
        for nextNode, value in enumerate(residualGraph[currentNode]):
            if explored[nextNode] == False and value > 0:
                queue.append(nextNode)
                explored[nextNode] = True
                #print(nextNode, " ", currentNode)
                parentNode[nextNode] = currentNode

    #If we still find a path from source to sink in the residual graph, return True to run ford fulkerson
    if explored[sink] :
        return True
    else :
        return False