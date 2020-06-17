#def insertion_sort(list_a):
#	for i in range(1,len(list_a)) :
#     value_to_sort = list_a[i]
#    	
#    	while list_a[i-1] > value_to_sort and i > 0 :
#    		list_a[i-1] ,list_a[i] = list_a[i] , list_a[i-1]
#    		i = i-1 
#    return list_a 

def insertion_sort(list_a):
    indexing_length = range(1, len(list_a))
    for i in indexing_length:
        value_to_sort = list_a[i]

        while list_a[i-1] > value_to_sort and i > 0:
            list_a[i], list_a[i-1] = list_a[i-1], list_a[i]
            i = i -1
 	 
list_a = [1,4,2,3,67,9]
insertion_sort(list_a)




print(list_a)
