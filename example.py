#this is example of work with graphs
graph = {'C': ['A', 'B'],

         'D': ['C'],

         'E': ['C'],

         'F': ['D'],

         'G': ['E'],

         'H': ['G'],

         'I': ['H']}

#first-enter the number of queries
questions = list()
for q in range(int(input())):
    questions.append(list(input().replace(" ","")))#enter Child(end) and Parent(start)

def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not graph.__contains__(start):
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
    return None

for qi in questions:
    if find_path(graph,qi[1],qi[0]) == None:
        print('No')
    else:
        print('Yes')





