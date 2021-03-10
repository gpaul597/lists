#items in python
thislist=["apple","banana","cherry"]
print (thislist)
#lists allows duplicate values
thislist=["apple","banana","cherry","apple","cherry"]
print (thislist)
#list items can be of any datatypes eg strings,int and boolean
list1=["abc",34,True,"paul"]
print (list1)
mylist=["apple","banana","cherry"]
print (type(mylist))
#using list constructor to create a new list
thislist=list(("apple","banana","cherry"))
print (thislist)
#accessing items in a list
thislist=["paul","jane","joy"]
print (thislist[1])
print (thislist[-1])
print (thislist[0])
#ranging the index
thislist=["paul","jane","joy","mark","john","mary","james"]
print (thislist[2:5])
print (thislist[:4])
print (thislist[2:])
print (thislist[-4:-1])
#checking if items exist in a list using 'in' keyword
thislist=["apple","banana","cherry"]
if "apple" in thislist:
  print ("yes, is in the list")