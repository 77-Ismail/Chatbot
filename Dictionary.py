#Dictionary are same as list to some extant but in dictionary we have key values in contrast we have simple values in list
a=dict()
a['Name']='Ismail'
a['RollNo']=2528
print(a)

# Both list and dicionaries are same
# Lists
l=list()
l.append('Ismail')
l.append(2528)
print(l)
print(l[0])# This will just print the //Ismail

#Dictionary
d=dict()
d['Name']='Ismail'
d['RollNo']=2528
print(d)
print(d['Name']) # We have to give the key value as we are giving the integer indexes in list
stuff = dict()
print(stuff.get('candy',-1))

print(d.items())