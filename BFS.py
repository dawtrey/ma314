from collections import deque
from Graph import Graph

# Breadth-first search
def BFS(graph,s):
    # reset colors to white
    for u in graph.V:
        u.color = "white"
        u.pi = None
    s.color = "gray"
    s.d = 0
    s.pi = None
    Q = deque()
    Q.append(s)
    while Q:
        u = Q.popleft()
        for v in graph.Adj[u.id]:
            if v.color == "white":
                v.color = "gray"
                v.d = u.d+1
                v.pi = u
                Q.append(v)
        u.color = "black" 
        
# Display result of BFS
def display(G):
	for v in G.V:
		s = str(v.id) + ": " + str(v.d)
		print(s)	
		
# Print shortest path
def print_path(G,s,v):
    if v.id != s.id and v.pi == None:
        print("vertex", v.id, "is not reachable")
    else:
        Q = deque()
        while v.pi != None:
            Q.appendleft(v.id)
            v = v.pi
        Q.appendleft(v.id)
        print(Q)
    
if __name__ == '__main__':
        
	# Road network example from the lecture
	G = Graph()
	# Create vertices
	for i in range(0,27):
		G.add_node()
	# Create horizontal edges
	G.add_edge_using_ids(0,1)
	G.add_edge_using_ids(1,2)
	G.add_edge_using_ids(2,3)
	G.add_edge_using_ids(3,4)
	G.add_edge_using_ids(4,5)
	G.add_edge_using_ids(6,7)
	G.add_edge_using_ids(7,8)
	G.add_edge_using_ids(9,10)
	G.add_edge_using_ids(10,11)
	G.add_edge_using_ids(11,12)
	G.add_edge_using_ids(13,14)
	G.add_edge_using_ids(14,15)
	G.add_edge_using_ids(16,17)
	G.add_edge_using_ids(18,19)
	G.add_edge_using_ids(19,20)
	G.add_edge_using_ids(21,22)
	G.add_edge_using_ids(22,23)
	G.add_edge_using_ids(24,25)
	# Create vertical edges
	G.add_edge_using_ids(2,6)
	G.add_edge_using_ids(3,7)
	G.add_edge_using_ids(4,8)
	G.add_edge_using_ids(6,9)
	G.add_edge_using_ids(7,10)
	G.add_edge_using_ids(8,11)
	G.add_edge_using_ids(9,13)
	G.add_edge_using_ids(10,14)
	G.add_edge_using_ids(11,15)
	G.add_edge_using_ids(12,16)
	G.add_edge_using_ids(14,18)
	G.add_edge_using_ids(15,19)
	G.add_edge_using_ids(16,20)
	G.add_edge_using_ids(18,21)
	G.add_edge_using_ids(19,22)
	G.add_edge_using_ids(20,23)
	G.add_edge_using_ids(21,24)
	G.add_edge_using_ids(22,25)
	G.add_edge_using_ids(25,26)

	v7 = G.get_node(7)
	BFS(G, v7)
	display(G)
	
	print_path(G,G.get_node(7),G.get_node(0))
