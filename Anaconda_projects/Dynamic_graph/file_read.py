import sys
import glob
pullData = []
i = 0;
validLetters = "ABCDEF0123456789"
for name in glob.glob('dynamic/*'):
    print(name)
    data = open(name,"r").read();
    dataArray_raw = data.split('\n')
    dataArray = []
    for eachLine in dataArray_raw:
        newString=''
        for char in eachLine:
            if char in validLetters:
                newString += char
        dataArray.append(newString)
    pullData.append(dataArray) 
    print pullData
    print "\n\n"
    i += 1
print pullData