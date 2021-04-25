def h(start,end):#эвристика - расстояние 
    return ((end[0]-start[0])**2 + (end[1]-start[1])**2)**0.5 
def w(start,end): # вес ребра между соседними вершинами - в данном случае совпадает с h (здесь можно использовать матрицу весов)
    return ((end[0]-start[0])**2 + (end[1]-start[1])**2)**0.5 
def a(start,end,graph):
    n = len(graph)
    closed=[]#рассмотренные вершины
    openl = [start]#текущие вершины
    froml = {x:n for x in graph.keys()}
    g = {x:10**4 for x in graph.keys()}
    f = {x:10**4 for x in graph.keys()}
    g[start]=0
    for v in graph[start]:
        g[v] = w(start,v)
    f[start] = h(start,end)
    while openl!=[]:
        curr = minf(openl,f)
        if curr == end:
            return decode(froml,start,end)
        openl.remove(curr)
        closed.append(curr)
        for neig in graph[curr]:
            if not(neig in closed):
                temp_g = g[curr] + w(curr,neig)
                if not(neig in openl) or temp_g < g[neig]:
                    froml[neig] =curr
                    g[neig] = temp_g
                    f[neig] = g[neig] + h(neig,end)
                if not(neig in openl):
                    openl.append(neig)
    return False
                                                                                                                          
    

    
def minf(openl,f):#минимальный элемент из текущих по f
    minel = openl[0]
    for i in openl:
        if f[i]<= f[minel]:
            minel = i
    return minel
def decode(froml,start,end):
    res =[]
    i=end
    while i!=start:
        res.insert(0,i)
        i = froml[i]
    return(res)
