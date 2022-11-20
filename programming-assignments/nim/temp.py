import re

# txt = input('Wrtie')

# x = txt.replace(" ", ",")
# y = [x]

# print(txt,x,y)

# test = 10 ^ 4 
# test3 = 10 and 7
# test2 = 3 or 4 or 5
# print(test, test2, test3)
# test4 = 10 ^ 4
# test5 = 10 | 4

# print(bin(4))
# print(bin(5))

# print(2^3)
# print(3^2)
# print(2^3^4)

# print(1^4)
# # print(15^15)
# print(10^10^10)

# # for x in range(11):
# #     print(x,bin(x))
# #     x = x+1



# Python program to show
# bitwise operators
 
# a = 10
# b = 9
# c = 3
# # d = 1
 
# # Print bitwise AND operation
# print("a & b =", a & b)
 
# # Print bitwise OR operation
# print("a | b =", a | b)
 
# # Print bitwise NOT operation
# print("~a =", ~a)
 
# # print bitwise XOR operation
# print("a ^ b =", a ^ b)

# print("a ^ b ^ c =", a ^ b ^ c )


# x ^ y ^ z

nim_zero_array=[]
nim_not_zero_array =[]
# for x in range(11):
#     for y in range(11):
#         for z in range(11):
#             if(x^y^z==0):
#                 nim_zero_array.append([x,y,z])
#             elif(x^y^z>0):
#                 nim_not_zero_array.append([x,y,z])


def find_strategy(x,y,z):
        for item in nim_zero_array:
            if((item[0]==x and item[1]==y and item[2]<=z)):
                difference = z - item[2]
                return ['c',difference]
            elif((item[0]==x and item[2]==z and item[1]<=y)):
                difference = y - item[1]
                return ['b',difference]
            elif((item[1]==y and item[2]==z and item[0]<=x)):
                difference = x - item[0]
                return ['a',difference]

def precomputed_nim():
        for x in range(11):
            for y in range(11):
                for z in range(11):
                    if(x^y^z==0):
                        nim_zero_array.append([x,y,z])
                    elif(x^y^z>0):
                        nim_not_zero_array.append([x,y,z])


precomputed_nim()
test = find_strategy(9,8,10)
print(test[0],test[1])

nim_state={'a':10, 'b':10, 'c':10}
print(nim_state['a'])


### after finding target, if multiple - use the one that adds up to the least amount. 
### after defining final target, subtract og peg minus desired peg and return that.