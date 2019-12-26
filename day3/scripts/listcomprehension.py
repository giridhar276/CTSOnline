

#syntax : [ output_expression() for(set of values to iterate) if(conditional filtering) ]
print([x**2 for x in range(0,10)])

multiplied = [item*3 for item in [3,4,5] ] 
print(multiplied)

print([x for x in range(1,20) if x%2==0 ])

print([x for x in 'MATHEMATICS' if x in ['A','E','I','O','U']])

print(["Even" if i%2==0 else "Odd" for i in range(8)])


print([(x,y,z) for x in range(1,30) for y in range(x,30) for z in range(y,30) if x**2 + y**2 == z**2])
#[(3, 4, 5), (5, 12, 13), (6, 8, 10), (7, 24, 25), (8, 15, 17), (9, 12, 15), (10, 24, 26), (12, 16, 20), (15, 20, 25), (20, 21, 29)]


colours = [ "red", "green", "yellow", "blue" ]
things = [ "house", "car", "tree" ]
coloured_things = [ (x,y) for x in colours for y in things ]


a = 5
table = [[a, b, a * b] for b in range(1, 11)]
print(table)


string = "my phone number is : 9550712233"
numbers = [x for x in string if x.isdigit()] 
print(numbers) 

print([x.lower() for x in ["A","B","C"]])

print([x.upper() for x in ["a","b","c"]])


matrix = [[j for j in range(5)] for i in range(5)]
print(matrix) #[[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]


matrix = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
flatten_matrix = [val for sublist in matrix for val in sublist]
print(flatten_matrix)


planets = [['Mercury', 'Venus', 'Earth'], ['Mars', 'Jupiter', 'Saturn'], ['Uranus', 'Neptune', 'Pluto']]
#flatten a given 2-D list and only include those strings whose lengths are less than 6:
#Expected Output: flatten_planets = [‘Venus’, ‘Earth’, ‘Mars’, ‘Pluto’]

# 2-D List of planets 
planets = [['Mercury', 'Venus', 'Earth'], ['Mars', 'Jupiter', 'Saturn'], ['Uranus', 'Neptune', 'Pluto']] 
  
flatten_planets = [] 
  
for sublist in planets: 
    for planet in sublist: 
          
        if len(planet) < 6: 
            flatten_planets.append(planet) 
          
print(flatten_planets)


# Nested List comprehension with an if condition 
flatten_planets = [planet for sublist in planets for planet in sublist if len(planet) < 6] 
          
print(flatten_planets)






