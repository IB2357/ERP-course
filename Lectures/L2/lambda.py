"""
 . Lambda function (anonymous function) 
 is just a nameless function.

 . Its one of the Important principles in 
 the functional programming paradigm

. Often used for simple operations or 
transformations and are typically defined 
in a single line of code.

. its the perfect argument 
for higher-order functions like:
 map(), filter(),sorted()

"""

# Regular expression:
def add(x,y):
    return x + y;

Regular_add = add #functions name

# lambda expression:
simple_add = lambda x,y: x + y; #nameless function

print(add(4,3))
print(Regular_add(4,3))
print(simple_add(4,3))

#########################################
print("___________________________")
# using lambda with map(), filter(),sorted()
ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# map()
add_10 = list(map(lambda x: x+10, ls))
print(add_10) 


#filter()
even_nums = list(filter(lambda x: x%2==0, ls))
print(even_nums) 

#sorted()      -from chatGPT
points = [(3, 5), (1, 9), (2, 7), (4, 2)]
sorted_points = sorted(points, key=lambda x: x[1])
print(sorted_points)
