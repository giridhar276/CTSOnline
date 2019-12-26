#dictionary comprehension

values = {str(i):i for i in [1,2,3,4,5]}
print(values)


lang = ['spark','spark','java','hadoop','oracle']
langdict = {f:len(f) for f in lang}
print(langdict)


lang = ['spark','spark','java','hadoop','oracle']
langdict = {f:i for i,f in enumerate(lang)}
print(langdict)



keys = ['a', 'b', 'c']
values = [1, 2, 3]
valuedict = {i:j for (i,j) in zip(keys, values)}
print(valuedict)


dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# Double each value in the dictionary
double_dict1 = {k:v*2 for (k,v) in dict1.items()}
print(double_dict1)
