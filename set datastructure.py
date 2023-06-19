#create set
#1set creation by using curly braces
sets={1,2,3,4,5}
print(sets)
#2 set creation by using set keyword
#sets=set(1,2,3,4,5)
#print(sets)         TypeError: set expected at most 1 argument, got 5
sets=set([1,2,3,4,5])
print(sets)
# set does not allows duplicates
sets={1,2,3,4,5,1,2,3}
print(sets)       #{1, 2, 3, 4, 5}
# set does not have index numbers so set indexing and slicing is not possible .
#set elements order is not fixed
#set also does not support concatenation and repetation
#set supports both packing and unpacking
#set is a mutable object means we add,remove,update elements possible
#set is also used for delete duplicate elements in string,list,tuple.
#delete duplicate elements in list
lst=[1,2,3,4,1,2,3,]
print(list(set(lst)))       #[1, 2, 3, 4]
#delete duplicate elements in tuple
t=1,2,3,4,1,2,3
print(tuple(set(t)))        #(1, 2, 3, 4)
#delete duplicate elements in string
st='koteswara rao'
print(str(set(st)))          #{'k', ' ', 't', 's', 'e', 'a', 'r', 'o', 'w'}
print(''.join(set(st)))      #esw atkor
#set functions
#1.union  it will return all elements in both sets except matching elements
s1={1,2,3,4}
s2={1,2,5,6}
print(s1.union(s2))
#2 intersection it will return only matching elements in both sets
print(s1.intersection(s2))
#3 difference it will return all un matching elements in first set
print(s1.difference(s2))
#4 symmetric_difference it will return all un matching elements from both sets
print(s1.symmetric_difference(s2))
#5



















