import json
f = open('C:\\Users\\SThangaraj\\Downloads\\flash-2018-04-30T09-07.json','r')
outF = open("C:\\Users\\SThangaraj\\Downloads\\myoutfile.json", "w")
for line in f:
    decoded = json.loads(line)
    if decoded['timeStamp'][17:19] in ('05','06','07','08','09','10','11','12','13','14'):
        outF.write(line)

outF.close()
