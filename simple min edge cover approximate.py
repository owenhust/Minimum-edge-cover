def min_edge_cover(tokens):
  min_edge_cover = 0
  tokens_split_all = tokens.split(" ")
  #print(tokens_split_all)
  k = int(float(tokens_split_all[0]))
  #find the indeces of brackets
  min_edge_cover = min_edge_cover_pathwidth(k,tokens_split_all)
  return min_edge_cover


def min_edge_cover_pathwidth(k,tokens_split):
  (tokens_split)
  points = []
  edges = []
  minedgecover = []
  labels = []
  #initiate the k-parse size
  j = k
  for i in range(k + 1):
   points.append(str(i))
   labels.append(str(i))
   #print(labels)
  #start reading the k-parses, do one first
  for i in range(1,len(tokens_split)): 
    #set up labels
    if tokens_split[i] != "(" and tokens_split[i] != ")":
      if len(tokens_split[i]) == 1:
        points.append(tokens_split[i])
        j = j + 1
        labels.append(str(j))
      #print(labels)
      #update edges per labels 
      if len(tokens_split[i]) == 2:
        #newpoints.last
        edge = tokens_split[i]
        if len(labels) != 0:
        #replace the number 
          revpoints = points[::-1]
          revlabels = labels[::-1]
          #print(labels)
          #print(points)
          #print(revpoints)
          replind1 = revpoints.index(edge[0])
          #print(replind1)
          replind2 = revpoints.index(edge[1])
          #print(replind2)
          edgelabel1 = str(max(int(float(revlabels[replind1])),int(float(revlabels[replind2]))))
          #print(edgelabel1)
          edgelabel2 = str(min(int(float(revlabels[replind1])),int(float(revlabels[replind2]))))
          edgelabel = edgelabel1+"_"+edgelabel2
          edges.append(edgelabel)  
    #print(edges)  
		  
  #after relabeling all edges now do the min. cover edge
  #find both vertices in edge first
  for edge in edges:
    find_label(edge,minedgecover,edges,labels)
  if len(labels) != 0:
    #print(labels)
    #print(minedgecover)
    min_edge_cover = len(minedgecover) + int(len(labels)/2) 
  return(min_edge_cover)      


def find_label(edge,minedgecover,edges,labels):
  if len(minedgecover) >= 0:
        if edge.split("_")[0] in labels and edge.split("_")[1] in labels:
          minedgecover.append(edge)
          labels.remove(edge.split("_")[0])
          labels.remove(edge.split("_")[1])
  return None

tokens = input()
#print(tokens)
while tokens[0] != "0":
  min_cover = min_edge_cover(tokens)
  print(min_cover)
  tokens = input()
#print(min_edge_cover("7 ( 10 20 30 32 42 21 41 51 62 70 71 73 4 43 41 42 64 54 40 3 32 43 53 63 30 31 73 5 51 50 52 53 65 75 54 4 42 40 41 64 74 43 1 31 41 51 21 71 61 4 41 42 43 64 1 51 41 31 1 10 21 51 61 1 21 41 31 61 10 71 2 21 20 52 42 32 62 72 6 62 63 61 64 60 4 41 42 43 54 64 74 40 )"))
#print(min_edge_cover("4 ( 10 20 30 21 41 32 43 3 32 43 2 21 32 42 0 40 20 30 10 2 21 3 32 43 32 2 20 32 42 2 21 32 3 32 43 4 41 42 1 41 31 21 1 10 21 1 21 10 2 21 3 32 31 4 41 42 0 40 30 0 30 20 10 2 20 2 20 32 3 31 3 31 32 4 43 4 41 1 10 21 1 31 0 20 30 40 2 21 3 32 31 30 4 41 43 1 21 31 10 0 40 20 3 43 32 2 20 32 1 10 31 4 41 42 43 )"))