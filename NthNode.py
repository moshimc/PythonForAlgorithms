class Node:
    
    def __init__(self, value):
        self.value = value
        self.nextnode = None

    def nth_to_last_node(index, node):
        
        reversedNodes = []
        nextNode = node
        requestedNode = None
        
        # loop through nodes until end, pushing throughout
        while nextNode != None:
            reversedNodes.append(nextNode)
            nextNode = nextNode.nextnode
        
        # once we get to end we push index # of times and return the final node
        for i in range(index):
            requestedNode = reversedNodes.pop()

        print(requestedNode.value)
