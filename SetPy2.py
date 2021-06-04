# l = (1,22,22,33,44)
# print(l)
#
# lst = ["chinmay","chinmay"]
# print(lst)
#
#
# person = {
#
#     'name':'chinmay',
#     'name':"poorva"
#
#
# }
#
# print(person)


setA = {1,2,3,333,444,444,4,3}
# print(setA)




# setA.add(9)
# print(setA)
#
# setA.remove(9)
# print(setA)
#
# setA.pop()
# print(setA)
#
# tupleA = (1,2)
# tupleA = (5,7)
#
# string and tuple are immutable
# setA
# setA.clear()
# print(setA)
#
# b = set([44,55,44,66,55])
# print(b)



# tuple and list -- stored the value by index

# set and dict they basically hold same value


# listA = []

# dict = {

    #'name':'chinmay'
#
# }

#tupleA = ()

# tupleB = 1,2


setA = {1,2,2,3,4}
print(setA)

for item in setA:
    print(item)

#Methods
# add function to add the element
setA.add(7)
print(setA)

#

setA = {1,2,3}
setB = {3,4,5}

# setA.update(setB)
# print(setA)

listA =[5,6,7]
tupleA = (12,22,33,44)

setB.update(setA)
print(setB) #
print(setA)


# setB.update(listA)
# print(setB)
#
#
# name = "chinmay"
# setB.update(name)
# print(setB)

setA = {1,23,24}
# setB = {}


setC = setA.copy()

print(setA)
print(setC)

setC.remove(24)
print(setA)
print(setC)


# setA.copy(setB)
# print(setA)
# print(setB)







#
# setC= setA
#
# setC.remove(23)
#
# print(setC)
# print(setA)

#------------------------
# setC.copy(setA)
# setB.remove(23)

# print(setB)
# print(setA)







#
# setA.pop()  # removes random element
# print(setA)
#
# setA.remove(23) # removes by value
#
# # setA.clear()
# # print(setA)
# print(setA)


# setA = {1,22,33}
# setB = {1,22}
#
# b = setA.union(setB)
# print(b)
# print(setA)
#
#
#
# print(setB.issubset(setA))
# print(setA.issubset(setB))
#
#
# print(setB.issuperset(setA)) # false
# print(setA.issuperset(setB)) # true


setA = {1,22,33}
setB = {1,22,4,5,6}


print(setA.symmetric_difference(setB))
print(setB.symmetric_difference(setA))

setA.symmetric_difference_update(setB)
setB.symmetric_difference_update(setA)
print(setA)
print(setB)


setA = {1,22,33}
setB = {1,22,4,5,6}


g = setA.intersection(setB)
print(g)

setA.intersection_update(setB)
setB.intersection_update(setA)
print(setA)
print(setB)


setA = {1,22,33}
setB = {1,22,4,5,6}

# print(setA.difference(setB)) # 33
# print(setB.difference(setA)) # 4,5,6
#
# print(setA)
# print(setB)


#setA.difference_update(setB)
# setB.difference_update(setA)
# print(setB) #  33

setA = {1,22,33}
setB = {4,5,6}


print(setA.isdisjoint(setB))
print(setB.isdisjoint(setA))
print(5,6,7)
setA.discard(22)
print(setA)

# discard and remove : return