import json
import random as r
import math
import heapq as hq
import re

def nombre():
  with open("file 0502a.txt") as f:
    G = []
    for line in f:
      nums = [int(x) for x in line.split()]
      G.append([])
      for i in range(0, len(nums), 3):
       G[-1].append((nums[i], r.randint(1, 345353)))
  return G

def pasarLoc():
  with open("loc.txt",) as f:
    G = []
    a = []
    b = 0
    for line in f:
      if line[1].isdigit():
        b = b+1
        line = re.sub("\,|\\n", "", line)
        nums = [float(x) for x in line.split()]
        for i in range(0, len(nums), 2):
          G.append((nums[i], nums[i+1]))
      else:
        a.append(b)
        b = 0
  a.pop(0)
  return G, a

def transformGraph():
    #n, m = 8, 56
    #Loc = [(i * 100 - r.randint(145, 155), j * 100 - r.randint(145, 155))
    #       for i in range(1, n + 1) for j in range(1, m + 1)]
    Loc, x =pasarLoc()
    suma = 0
    for fila in x:
      suma += fila
    n=len(x)
    #G = [[] for _ in range(suma +1-19)]
    G= nombre()
    """for i in range(n):
        m=x[i]
        for j in range(m):
            adjs = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
            for u, v in adjs:
                if u >= 0 and u < n and v >= 0 and v < m:
                    G[i * m + j].append((u * m + v, r.randint(1, 345353)))"""
    return G, Loc


def bfs(G, s):
  n = len(G)
  visited = [False]*n
  path = [-1]*n  # parent
  queue = [s]
  visited[s] = True

  while queue:
    u = queue.pop(0)
    for v, _  in G[u]:
      if not visited[v]:
        visited[v] = True
        path[v] = u
        queue.append(v)

  return path


def dfs(G, s):
  n = len(G)
  path = [-1]*n
  visited = [False]*n

  def _dfs(u):
    visited[u] = True
    for v, _ in G[u]:
      if not visited[v]:
        path[v] = u
        _dfs(v)

  _dfs(s)
  return path




def dijkstra(G, s):
    n= len(G)
    visited= [False]*n
    path= [-1]*n
    cost= [math.inf]*n

    cost[s]= 0
    pqueue= [(0, s)]
    while pqueue:
        g, u= hq.heappop(pqueue)
        if not visited[u]:
            visited[u]= True
            for v, w in G[u]:
                if not visited[v]:
                    f= g + w
                    if f < cost[v]:
                        cost[v]= f
                        path[v]= u
                        hq.heappush(pqueue, (f, v))

    return path, cost


G, Loc = transformGraph()


def graph():

    response = {"loc": Loc, "g": G}

    return json.dumps(response)


def paths(s, t):
    bestpath, _ = dijkstra(G, s)
    #path1 = bfs(G, s)
    #path2 = dfs(G, s)
    response = {"bestpath": bestpath }
    #response = {"bestpath": bestpath, "path1": path1 }
    #response = {"bestpath": bestpath, "path1": path1, "path2": path2}

    return json.dumps(response)

