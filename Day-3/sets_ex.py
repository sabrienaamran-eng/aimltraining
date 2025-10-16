# # print("Sets in Python")
# # set_one=('laptop','airphone','ipad','mobile','headphone','laptop','ipad')
# # # print('Number of items in set_one are:',len(set_one))
# # # for item in set_one:
# # #     print(item,end=" ")

# # Clear(): remove all the items from set

# # set_one=('laptop','airphone','ipad','mobile','headphone')
# # print('\n After Clear Number of Items in set_one are:',len(set_one))
# # for item in set_one:
# #     print(item,end=" ")
# # #set.remove(item): Updates the set and removes items from set.
# # set_one.remove=('airphone')
# # print('\n After removing one item from set:',len(set_one))
# # for item in set_one:
# #     print(item,end=" ")

# #union,intersection,fifference
# # set_one={100,200,300,500,700,900,150}
# # set_two={100,400,700,1000,1300}

# # #union
# # #s1.union(s2): Returns a new set with all items from both sets s1, s2.
# # print(f'set_one contains:{len(set_one)} items')
# # print(set_one)
# # print(f'set_two contains:{len(set_two)} items')
# # print(set_two)
# # unionset=set_one.union(set_two)
# # print(f'Union of set_one and set_two contains:{len(unionset)} following items')
# # print(unionset)

# # set_one={1,3,5,7}
# # set_two={1,2,4,6,7}

# # #union
# # #s1.union(s2): Returns a new set with all items from both sets s1, s2.
# # print(f'set_one contains:{len(set_one)} items')
# # print(set_one)
# # print(f'set_two contains:{len(set_two)} items')
# # print(set_two)
# # unionset=set_one.union(set_two)
# # print(f'Union of set_one and set_two contains:{len(unionset)} following items')
# # print(unionset)

# set_one={100,200,300,500,700,900,150}
# set_two={100,400,700,1000,1300}
# set_three={200,600,1200,1500,1100}
# #union
# #s1.union(s2): Returns a new set with all items from both sets s1, s2.
# print(f'set_one contains:{len(set_one)} items')
# print(set_one)
# print(f'set_two contains:{len(set_two)} items')
# print(set_two)
# unionset=set_one.union(set_two,set_three)
# print(f'Union of set_one, set_two and set three contains:{len(unionset)} following items')
# print(unionset)

# set_one={100,200,300,500,700,900,150}
# set_two={100,400,700,1000,1300,300}

# #intersection example
# #s1.union(s2): Returns a new set with all items from both sets s1, s2.
# print(f'set_one contains:{len(set_one)} items')
# print(set_one)
# print(f'set_two contains:{len(set_two)} items')
# print(set_two)
# newset=set_one.intersection(set_two)
# print(f'Union of set_one and set_two contains:{len(newset)} following items')
# print(newset)

set_one={100,200,300,500,700,900,150}
set_two={50,150,200,700,550,650}

#intersection example
#s1.difference(s2): Returns set which contains only item those are in s1 but not in s2
print(f'set_one contains:{len(set_one)} items')
print(set_one)
print(f'set_two contains:{len(set_two)} items')
print(set_two)
newset=set_one.difference(set_two)
print(f'differenece of set_one and set_two contains:{len(newset)} following items')
print(newset)