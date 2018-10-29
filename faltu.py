n=input()
f=(".","!",")","|")
if n.endswith(f):
    print(n[:len(n)-1])
else:
    print(n)
