from expand import expand
from heapq import heappop, heappush
# TODO Put your code here.
# be sure to call the imported function expand to get the next list of nodes

#def a_star_search (dis_map, time_map, start, end):
#    path = []
#    path.append(end)
#    closedset = dict()
#    openset = dict()
#    g_score = {start: 0}
#    h_score = {start:dis_map[start][end]}
#    f_score = {start:dis_map[start][end]}
#    time_map_current = time_map[start]
#    came_from = {}
#    for i in time_map_current:
#        if time_map_current[i] == None:
#            pass
#        else:
#            g_score.update({i:time_map_current[i]})
#            h_score.update({i:dis_map[end][i]})
#            f_score.update({i:(h_score[i]+g_score[i])})
#            openset.update({i: f_score[i]})
#    closedset.update({start:f_score[start]})
#
#    while openset:
#        print(openset)
#        print(closedset)
#        x = min(openset, key=openset.get)
#        g_score[x] = time_map[start][x]
#        if x == end:
#            return reconstruct_path(came_from,end,path)
#        closedset[x] = openset[x]
#        openset.pop(x)
#        for y in time_map[x]:
#            if time_map[x][y] == None:
#                continue
#            if y in closedset:
#                continue
#            print("gscore"+str(g_score[x])+"timemap"+str(time_map[x][y]))
#            candidate_g_score = g_score[x] + time_map[x][y]
#            candidate_h_score = dis_map[end][y]
#            candidate_f_score = candidate_g_score+candidate_h_score
#            if y not in openset:
#                openset.update({y:candidate_f_score})
#            else:
#                if candidate_f_score<openset[y]:
#                    openset.update({y:candidate_f_score})
#                    came_from.update({x:y})
#    return False

def a_star_search(dis_map, time_map, start, end):
    path = []
    open_set = []
    closed_set = []
    heappush(open_set, Node(start))
    while open_set:
        q = heappop(open_set)
        if q.name == end:
            while q is not None:
                path.insert(0, q.name)
                q = q.parent
            return path
        for x in expand(q.name, time_map):
            if time_map[q.name][x] is not None:
                g_score = time_map[q.name][x] + q.g_score
                h_score = dis_map[x][end]
                y = Node(x, q, g_score, h_score)
                if y in closed_set:
                    continue
                if y in open_set:
                    if y < open_set[open_set.index(y)]:
                        open_set[open_set.index(y)] = y
                        continue
                    else:
                        continue
                heappush(open_set, y)
        heappush(closed_set, q)
    return path

class Node:
    def __init__(self, name, parent=None, g_score=0, h_score=0):
        self.name = name
        self.parent = parent
        self.g_score = g_score
        self.h_score = h_score
        self.f_score = g_score + h_score

    def __lt__(self, other):
        if self.f_score == other.f_score:
            return self.name < other.name
        return self.f_score < other.f_score

    def __eq__(self, other):
        return self.name == other.name

def reconstruct_path(came_from, current_node, path):
    for i in came_from.keys():
        if came_from[i]==current_node:
            path.append(i)
            print(path.reverse())
            reconstruct_path(came_from, i, path)
            return path.reverse()
    return current_node