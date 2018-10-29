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
            print("No match")
      else:
         for key in self.next.keys():
            self.next[key].dfs(sofar+key)

            
      
root = Node()
f=open("dict.txt",'r')
lines=f.read().splitlines()#reading file and removing \n
s=input("Enter ")
s=s.lower()
for i in lines: #1st word
      i=i.lower().strip()
      j=i.split(" ")
      for k in j:
         if k.endswith(".") or k.endswith(","):
            k=k[:len(k)-1]
         root.add_item(k)
root.search(s)

            
            
