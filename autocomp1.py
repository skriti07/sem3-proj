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
         matchfreq[sofar]=wordfreq.get(sofar)
##         print("Match:",sofar)
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
def cleanData(k):
   if k.endswith(".") or k.endswith(","):
      k=k[:len(k)-1]
   return(k)


start = timeit.default_timer()            
wordfreq={}
matchfreq={}
root = Node()
f=open("dict.txt",'r')
lines=f.read().splitlines()#reading file and removing \n
s=input("Enter ")
s=s.lower()
for i in lines: 
      i=i.lower().strip()
      j=i.split(" ")
      for k in j:
         k=cleanData(k)
         if k not in wordfreq.keys():
            wordfreq[k]=1
            root.add_item(k)
         else:
            wordfreq[k]=wordfreq.get(k)+1
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
stop = timeit.default_timer()
##print(stop-start)
         

            
            
