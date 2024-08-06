S={5,"Usama",6,5,"Usama",98,"5"} #In sets single element considered as once
print(S)  #Set is a mutabable
a1={0,1,2,3,5,9}
a2={0,3,5,4,8,6,9}
print(S.pop()) #Remove any random element
print(a1.union(a2))            #Returns new string
print(a1.intersection(a2))
print(a1.add(23))
print(a1)
c =set() #Empty SET
print(type(c))