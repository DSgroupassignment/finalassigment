
import heapq  #import priority queue

class Graph:  #class to represent the road network
   def __init__(self):  #initializing Graph class
       self.vertices = {}  #dictionary to store vertices and edges


   def add_vertex(self, vertex_id, name):  #add a new vertex to the graph
       if vertex_id not in self.vertices:  #checking if the vertex exists
           self.vertices[vertex_id] = {'name': name, 'edges': {}}  # Adding the vertex with name and empty edge


   def add_edge(self, fromVertex_id, toVertex_id, road_id, roadLength):  # Method to add an edge between two vertices
       if fromVertex_id in self.vertices and toVertex_id in self.vertices:  # Checking if both vertices exist
           self.vertices[fromVertex_id]['edges'][toVertex_id] = {'road_id': road_id, 'road_length': roadLength}  #adding edge from 'fromVertex_id' to 'toVertex_id'
           self.vertices[toVertex_id]['edges'][fromVertex_id] = {'road_id': road_id, 'road_length': roadLength}  #adding edge from 'toVertex_id' to 'fromVertex_id'


   def shortest_path(self, startVertex_id, endVertex_id):  #finding the shortest path using Dijkstras algorithm
       distances = {vertex_id: float('inf') for vertex_id in self.vertices}  #initializing dictionary with infinity for all of vertices
       distances[startVertex_id] = 0  #setting the start vertex to 0
       priority_queue = [(0, startVertex_id)]  #initializing priority queue
       while priority_queue:  #loop until queue is empty
           current_distance, currentVertex_id = heapq.heappop(priority_queue)  #pop vertex with the shortest distance from the queue
           if current_distance > distances[currentVertex_id]:  #if the current distance is greater than the stored distanc, the code will continue
               continue
           for neighborVertex_id, edge in self.vertices[currentVertex_id]['edges'].items():  #loop through neighbors of the current vertex
               distance = current_distance + edge['road_length']  #calculate the distance to the neighbor
               if distance < distances[neighborVertex_id]:  #if the calculated distance is less, update distance
                   distances[neighborVertex_id] = distance  #update distance
                   heapq.heappush(priority_queue, (distance, neighborVertex_id))  #push the neighbor to the queue
       if distances[endVertex_id] == float('inf'):  #if there is no path found
           return None
       return distances[endVertex_id] #return shortest distance to the end vertex


Cgraph = Graph()  #graph object to represent city road network
#add vertices for cities to the graph
for i in range(1, 27):  #add 26 cities (for 26 letters)
   Cgraph.add_vertex(i, f'City {i}')


#add edges representing roads between intersections with travel times as weights
Cgraph.add_edge(1, 2, 1, 5)    # City 1 to City 2, length 5 (5 min)
Cgraph.add_edge(1, 3, 2, 15)   # City 1 to City 3, length 15 (15 min)
Cgraph.add_edge(2, 3, 3, 8)
Cgraph.add_edge(2, 4, 4, 25)
Cgraph.add_edge(3, 4, 5, 12)
Cgraph.add_edge(1, 5, 6, 12)
Cgraph.add_edge(2, 5, 7, 30)
Cgraph.add_edge(3, 6, 8, 25)
Cgraph.add_edge(4, 6, 9, 20)
Cgraph.add_edge(4, 7, 10, 8)
Cgraph.add_edge(6, 7, 11, 15)
Cgraph.add_edge(5, 8, 12, 45)
Cgraph.add_edge(4, 8, 13, 6)
Cgraph.add_edge(7, 8, 14, 13)
Cgraph.add_edge(1, 9, 15, 20)
Cgraph.add_edge(4, 9, 16, 27)
Cgraph.add_edge(5, 10, 17, 16)
Cgraph.add_edge(6, 10, 18, 10)
Cgraph.add_edge(7, 11, 19, 25)
Cgraph.add_edge(8, 11, 20, 12)
Cgraph.add_edge(9, 12, 21, 28)
Cgraph.add_edge(10, 12, 22, 15)
Cgraph.add_edge(11, 12, 23, 20)
Cgraph.add_edge(9, 13, 24, 18)
Cgraph.add_edge(10, 13, 25, 14)
Cgraph.add_edge(11, 14, 26, 20)
Cgraph.add_edge(12, 14, 27, 12)
Cgraph.add_edge(13, 14, 28, 18)


#system to find the shortest route for package distribution
def shortest_distance(start_city, end_city):  #find the shortest route from start to end
   shortest_distance = Cgraph.shortest_path(start_city, end_city)  #find the shortest distance
   return shortest_distance  #return the shortest distance


print("+--------------------------------------------------------+")
print(" Traffic flow optimization")
print("+--------------------------------------------------------+")
start_city = int(input(" Enter the start or your current city (1-26): "))
end_city = int(input(" Enter the end or destination city (1-26): "))


shortest_distance = shortest_distance(start_city, end_city)  #find shortest distance
if shortest_distance is None:
    print(" No route available")
else:
    print(f" The fastest route from City {start_city} to City {end_city} is {shortest_distance} minutes.")
print("+--------------------------------------------------------+")