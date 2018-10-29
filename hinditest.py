import codecs as cd

import timeit
import operator
#####################################################
class Node:
   
   def __init__(self):
      self.next = {}
      self.word_marker = False


      
   def add_item(self, string):
      if len(string) == 0:
         self.word_marker = True
         return 		
      key = string[0] #Extract first character
      string = string[1:] #Create a string by removing first character
      if key in self.next:
         self.next[key].add_item(string)
      else:
         node = Node()
         self.next[key]=node
         node.add_item(string)


         
   def dfs(self, sofar=None):
      if self.word_marker == True:
         matchfreq[sofar]=hindi.get(sofar)
         print("Match:",sofar)
      for key in self.next.keys():
         self.next[key].dfs(sofar+key)


         
   def search(self, string, sofar=""):
      if (len(string) > 0):
         key = string[0]
         string= string[1:]
         if key in self.next:
            sofar = sofar + key
            self.next[key].search(string,sofar)
         else:
##            print("No match")
            return
      else:
         for key in self.next.keys():
            self.next[key].dfs(sofar+key)
###################################################


def cleanData(n):
    f=(".","!",")","|",",","-","।","(","'")
    if sabd.endswith(f):
        n=n[:len(n)-1]
##        print(n)
    if sabd.startswith(f):
        n=n[1:]
    return n

wordfreq={}
matchfreq={}
l1=[]
l=[]
hindi={}
root=Node()
f=cd.open("hindi.txt",encoding='utf-8',mode='r')
k=f.read().splitlines()
s=input()
for i in k:
    l1=i.split(" ")
    l.append(l1)
for i in range(0,len(l)):
    for j in range(0,len(l[i])):
        sabd=l[i][j]
        sabd=cleanData(sabd)
        if sabd not in hindi.keys():
            hindi[sabd]=1
            root.add_item(sabd)
        else:
            hindi[sabd]=hindi.get(sabd)+1
root.search(s)
matchfreq=sorted(matchfreq.items(), key=operator.itemgetter(1))
##print(matchfreq)
num=len(matchfreq)
for i in range(num-1,num-6,-1):
    try:
      print(matchfreq[i][0].rstrip())
      if(i)<=0:
         break
    except:
        print("No match")
        break

