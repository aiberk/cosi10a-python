# Write the function diffs(vals) which takes a list vals of n integers and returns a 
# list of the successive differences.
# e.g.
# diffs([3,5,8,20]) --> [2,3,12]  as 5-3=2,  8-5=3, and 20-8=12
# diffs([1,3,5,7,9]) --> [2,2,2,2]
# diffs([0,1,4,9,16,25]) --> [1,3,5,7,9]

def diffs(list):
    ''' Takes a list vals of n integers and returns a list of the successive differences.'''
    final_array = [list[i + 1] - list[i] for i in range(len(list)-1)]
    return final_array

list = [3,5,8,20,1,22,100]
print(diffs(list))


# def diffs(list):
#     ''' Takes a list vals of n integers and returns a list of the successive differences.'''
#     final_array = [list[i + 1] - list[i] for i in range(len(list)-1)]
#     # final_array=[]
#     # temp_list = list
#     # i=0
#     # while i<=(len(list)):
#     #     temp_index = i + 1
#     #     temp = temp_list[temp_index] - list[i]
#     #     final_array.append(temp) 
#     #     i = i + 1
#     return res
# list = [3,5,8,20]
# print(diffs(list))