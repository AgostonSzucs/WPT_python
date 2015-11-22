import sys
import glob
pullData = [[]]
i = 0;
for name in glob.glob('/Users/agoston_developer/Anaconda_projects/Dynamic_graph/dynamic/*'):
    data = open(name,"r").read();
    print data
    pullData[[data]] 
    print pullData
    i += 1
print pullData