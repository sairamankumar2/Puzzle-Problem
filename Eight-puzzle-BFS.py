import time
col=3

class Node:
    def __init__(self, p):
        self.children=[]
        self.parent=None
        self.puzzle=p[:]
        self.x=0
    
    def printPuzzle(self):
        print()
        m=0
        for i in range(col):
            for j in range(col):
                print(self.puzzle[m],end=" ")
                m+=1
            print()
    
    def movetoright(self):
        if ((self.x)%col < (col-1)):
            pc=self.puzzle[:]
            pc[self.x],pc[self.x+1]=pc[self.x+1],pc[self.x]
            child=Node(pc)
            self.children.append(child)
            child.parent=self

    def movetoleft(self):
        if ((self.x) % col > 0):
            pc = self.puzzle[:]
            pc[(self.x)], pc[(self.x) - 1] = pc[(self.x) - 1], pc[(self.x)]
            child = Node(pc)
            self.children.append(child)
            child.parent = self

    def moveup(self):
        if ((self.x) -3 > 0):
            pc = self.puzzle[:]
            pc[(self.x)], pc[(self.x) -3] = pc[(self.x) -3], pc[(self.x)]
            child = Node(pc)
            self.children.append(child)
            child.parent = self

    def movedown(self):
        if ((self.x) +3 <9):
            pc = self.puzzle[:]
            pc[(self.x)], pc[(self.x) + 3] = pc[(self.x) + 3], pc[(self.x)]
            child = Node(pc)
            self.children.append(child)
            child.parent = self
	
    def goaltest(self):
        isGoal=True
        for i in range(len(self.puzzle)):
            if i!=self.puzzle[i]:
                isGoal=False
                return isGoal
        return isGoal


    def expandNode(self):
        for i in range(len(self.puzzle)):
            if self.puzzle[i]==0:
                self.x=i
        self.movetoright()
        self.movedown()
        self.movetoleft()
        self.moveup()

    def isunsolvable(self):
    	count=0
    	for i in range(8):
    		for j in range(i,9):
    			if self.puzzle[i] > self.puzzle[j] and self.puzzle[j]!=0:
    				count+=1
    	if count%2==1:
    		return True
    	else:
    		return False




class search:
    def __init__(self):
        pass

    def breadthFirstSearch(self,root):
        openlist=[]
        visited=set()
        openlist.append(root)
        visited.add(tuple(root.puzzle))
        while(True):
            currentNode=openlist.pop(0)
            if currentNode.goaltest():
                    pathtosolution= search.pathtrace(currentNode)
                    print(len(visited))
                    return pathtosolution
            currentNode.expandNode()
            for i in range(len(currentNode.children)):
                currentchild=currentNode.children[i]
                if (not (tuple(currentchild.puzzle) in visited)) :
                    openlist.append(currentchild)
                    visited.add(tuple(currentchild.puzzle))
            
    def pathtrace(n):
        current=n
        path=[]
        #print("Tracing Path")
        path.append(current)
        while current.parent!=None:
            current=current.parent
            path.append(current)
        return path


if __name__== "__main__":
	puzzle=[int(x) for x in input().split()]
	root=Node(puzzle)
	if root.isunsolvable():
	    print("No solution Found")
	    
	else:
		s=search()
		print("Finding Solution")
		start=time.time()
		solution=s.breadthFirstSearch(root)
		end=time.time()
		solution.reverse()
		for i in range(len(solution)):
			solution[i].printPuzzle()
		print("No of steps required to solve the puzzle",len(solution)-1)
		print("Time Taken",end-start)
	    
