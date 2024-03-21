import re
a='From ismaailkhan@gmail.com rollno 2528'
#This is the way to find @ first and then start will be next element to @ and end will be non-chacter space means empty space
# b=re.findall('@([^ ]*) ',a)
# print(b)

#Now this is the second way to devide the given String into words so we can easily index these words
# word=a.split()
# email=word[1]
# piece= email.split('@')
# print(piece[1])


# In this we are reading the text file in which we have names of student and their data like numbers we want to check
# who got max numbers to perform further calculation on his numbers
#
# hand=open('index.txt')
# numlist=list()
# for line in hand:
#     line=line.rstrip()
#     stuff=re.findall('From-this-document: ([0-9.]+)', line)
#     print(type(stuff))
#     if len(stuff) !=1:continue
#     num=float(stuff[0])
#     numlist.append(num)
# print('Maximum:',max(numlist,default=0) )


a='From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
stuff = re.findall('@\S+', a)
print(stuff)