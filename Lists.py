#Create empty list and append elements

my_list=[]

for item in [10,20,30,40]:
    my_list.append(item)

#insert 15 at second position
my_list[1]=15

#extend list with another
new_list=[50,60,70]

my_list.extend(new_list)

#remove the last element
my_list.pop()

#sort list in ascending order
my_list.sort

#index of value 30
value_index= my_list.index(30)
print(value_index) 