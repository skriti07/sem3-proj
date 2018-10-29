class Node:
   
   def __init__(self):
      self.next = {}
      self.word_marker = False


      
   def add_item(self, string):
##      print(string)       
      if len(string) == 0:
         self.word_marker = True
##         print("***",self.next,self.word_marker)
         return 		
      key = string[0] #Extract first character
      string = string[1:] #Create a string by removing first character
      if key in self.next:
##          print("*",self.next,self.word_marker)
          self.next[key].add_item(string)
          
      else:
         node = Node()
         self.next[key]=node
##         print("**",self.next,self.word_marker)
         node.add_item(string)


         
   def dfs(self, sofar=None):
      if self.word_marker == True:
         print("Match:",sofar)
      for key in self.next.keys():
         self.next[key].dfs(sofar+key)


   def findKeys(self):
##      print("inside")
      for key in self.next.keys():
         print(key)
         self.next[key].findKeys()

         
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
##root.add_item("am")
##root.add_item("amazon")
root.add_item("a")
print("##")
root.add_item("amazed")
print("##")
root.add_item("amaz")
print("##")
root.add_item("amaze")
root.add_item("b")
root.add_item("cat")
root.add_item("boy")
root.add_item("boys")
##root.add_item("amazing")
root.findKeys()
##print(root)
##print("##",root.next,root.word_marker)
            
            
