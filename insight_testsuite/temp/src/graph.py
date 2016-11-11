#!/usr/bin/env python

from collections import deque

class Vertex:
    """
    Stores vertices in a Graph. Vertex encapsulates first_connections and node_id.
    """
    def __init__(self,node_id):
        """
        Construct a new 'Vertex' object.
        :param node_id: The id of the vertex, in our case userid.
        :return: returns nothing
        """
        self.id = node_id
        self.first_connections = set()

    def add_first_connections(self,node_id):
        """
        Add node_id to the first degree connection of the current vertex.

        :param node_id: current vertex's neighbor, in our case a user's first degree connection.
        :return: returns nothing
        """
        self.first_connections.add(node_id)

    def __str__(self):
        return str(self.id) 

    def get_first_connections(self):
        """
        Retrieve all first degree connections of the current vertex.

        :return: returns first degree connections, stored in a set.
        """
        return self.first_connections

    def get_id(self):
        """
        Return node_id of the current vertex.

        :return: returns nothing
        """
        return self.id
    


class Graph:
    """
    Graph structure, consisted of zero to many vertices.
    """
    def __init__(self):
        """
        Construct a new Graph object.

        :return: returns nothing
        """
        self.vert_list = {}
        self.numVertices = 0

    def add_vertex(self,node_id):
        """
        Add a vertex to the graph

        :param node_id: int, id of the vertex, userid.
        :return: returns nothing
        """
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(node_id)
        self.vert_list[node_id] = newVertex
        return newVertex

    def get_vertex(self,node_id):
        """
        Obtain a vertex object by its id

        :param node_id: int, id of the vertex, userid.
        :return: returns nothing
        """
        if node_id in self.vert_list:
            return self.vert_list[node_id]
        else:
            return None

    def add_edge(self,source_id,target_id):
        """
        Add an edge to the graph.

        :param source_id: int, id of source node.
        :param target_id: int, id of target node.
        :return: returns degree between the two
        """
        if source_id not in self.vert_list:
            nv = self.add_vertex(source_id)
        if target_id not in self.vert_list:
            nv = self.add_vertex(target_id)
        self.vert_list[source_id].add_first_connections(target_id)
        self.vert_list[target_id].add_first_connections(source_id)
    
    
    def bibfs_degree_between(self,source_id,target_id,level_limit):
        """
        Bidirectional breadth first search on the graph to retrieve the degree between users. It goes through
        neighbors of source users and see if it is in connections of target users as the first level. And then
        goes through neighbors of target users to see if they contain source user. And then continue to the
        second degree connections.

        :param source_id: int, id of source node.
        :param target_id: int, id of target node.
        :param level_limit: int, the limit to the degree of connections we are searching
        :return: int, returns degree between the two users.
        """

        

        #stores the current level of target/source users, visited users will be removed from the queue
        source_queue = deque()
        source_queue.append(source_id)

        target_queue = deque()
        target_queue.append(target_id)

        #whether we have visited the source or target node
        source_visited = set()
        source_visited.add(source_id)

        target_visited = set()
        target_visited.add(target_id)

        #stores the connections of source/target users. As we goes thru each level, all the connections
        #of source/target users will be added.
        source_connections = set()
        source_connections.add(source_id)

        target_connections = set()
        target_connections.add(target_id)

        #level helps to limit how much further we look into the common connections between the source
        #and target users. Since we are searching bidirectionally from both source and target. If we are
        #looking for 4th degree connection we only need to go down 2 levels from each side
        current_level = 1

        #helps determines whether we finish the current degree of connection search for sourcce/target
        dist_source = dist_target = 0

        while current_level <= level_limit/2: 
        
            while (source_queue):

                source_vert_id = source_queue.popleft()
                source_vert = self.get_vertex(source_vert_id) 

                if(source_vert is not None):

                    for source_node in source_vert.get_first_connections():
                        if source_node not in source_visited:
                            if source_node in target_connections:
                                return dist_source + dist_target + 1
        
                            source_queue.append(source_node)
                            source_visited.add(source_node)
                            source_connections.add(source_node)
                    
                    dist_source = dist_source + 1

                #switching to target loop
                if current_level == dist_source:
                        
                        break

            while (target_queue):

                target_vert_id = target_queue.popleft()
                target_vert = self.get_vertex(target_vert_id) 

                if(target_vert is not None):
                    for target_node in target_vert.get_first_connections():
                        if target_node not in target_visited:
                            if target_node in source_connections:
                                return dist_source + dist_target + 1
                            target_queue.append(target_node)
                            target_visited.add(target_node)
                            target_connections.add(target_node)
                    dist_target = dist_target+1
                else:
                    return 0

                if current_level == dist_target:
                    break

            current_level = current_level + 1

        return 0


