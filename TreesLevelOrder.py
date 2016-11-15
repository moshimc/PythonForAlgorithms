import collections

def levelOrderPrint(treeRoot):
    
    if not treeRoot:
        return
    
    # Root = 1
    currentLevelNodeCount = 1
    nextLevelNodeCount = 0
    
    # Create our Deque from our root node
    treeNodes = collections.deque([treeRoot])
    
    # Since we have a root we start at 1, and once we traverse all nodes and children we will have 0
    while len(treeNodes) > 0:
        
        currentNode = treeNodes.popleft()
        print(currentNode.val, end="")
        currentLevelNodeCount -= 1
        
        if currentNode.left:
            treeNodes.append(currentNode.left)
            nextLevelNodeCount += 1
        
        if currentNode.right:
            treeNodes.append(currentNode.right)
            nextLevelNodeCount += 1
            
        if currentLevelNodeCount == 0:
            print('\n')
            currentLevelNodeCount, nextLevelNodeCount = nextLevelNodeCount, currentLevelNodeCount
