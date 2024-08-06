a={}
print(type(a))
b={"Good":"Something is pleasant","Fetch":"To bring something","Set":"Collection of similar objects"}    #Mutable
print(b["Good"])  #Its a key value pair
b["Syntax"]="Rules or Pattern"
print(b)
print(b.get("Pleasant"))   #.get function protects you from errors
print(b.keys())
print(b.values())
print(b.items())  #Returns key values tuples