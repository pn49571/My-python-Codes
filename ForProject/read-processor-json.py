import json

f1 = open('C:\\Users\\SThangaraj\\Downloads\\myoutfile.json','w')
with open('C:\\Users\\SThangaraj\\Downloads\\flash-2018-04-30T09-07.json') as f:
    for line in f:
        list_json = (json.loads(line))
        if list_json['timeStamp'][17:19] in ('05', '06', '07', '08', '09', '10', '11', '12', '13', '14'):
            #print(list_json['timeStamp'])
            f1.write(line)

print('completed')
