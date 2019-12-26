
import json
with open("example_2.json") as fr:
    # converting file object -------> json object
    data = json.load(fr)
    for key,value in data.items():
        for subkey,subvalue in value.items():
            for sskey,ssvalue in subvalue.items():
                print(ssvalue['question'])
                
'''
# hardcoding                
print(data['quiz']['sport']['q1']['question'])                
print(data['quiz']['maths']['q1']['question'])
print(data['quiz']['maths']['q2']['question'])
'''            
    