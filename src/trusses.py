#@author:ValCh

import argparse


parser = argparse.ArgumentParser()

parser.add_argument("filename", help="inputfile")

parser.add_argument("truss", help="truss",
                    type=int, default=2)

args = parser.parse_args()

dict1 = {}

LIST = []



with open(args.filename) as f:
        
        for line in f:
            
            LIST.append(line.rstrip().split(" "))



k = args.truss #save k-truss input for later as k

for i in LIST:

    List2 = [] #make a second list

    for j in LIST:

        if( i[ 0 ] == j[ 0 ] ):

            List2.append(int(j[ 1 ] ))

        elif(i[ 0 ] == j[ 1 ] ):

            List2.append(int(j[ 0 ] ))

    List2.sort()

    dict1[int(i[ 0 ] )] = List2

#dict1 saved in List2

for i in LIST:

    List3 = []

    for j in LIST:

        if(i[ 1 ] == j[ 1 ]):

            List3.append(int(j[0]))

        elif(i[ 1 ] == j[ 0 ]):

            List3.append(int(j[ 1 ]))

        List3.sort()

        dict1[int(i[ 1 ])] = List3

#dict1 saved in List3

counter = 0

while counter < len(LIST):

    for i in LIST:

        if(len(set(dict1[int(i[ 0 ])]).intersection(dict1[int(i[ 1 ])])) < k - 2 ):

            dict1[int(i[ 0 ])].remove(int(i[ 1 ]))

            dict1[int(i[ 1 ])].remove(int(i[ 0 ]))

            LIST.remove(i)

    counter += 1 #count each time the loop

results = []

for i in LIST:

    List3 = []

    inter = set(dict1[int(i[ 0 ])]).intersection(dict1[int(i[ 1 ] ) ] )
    
    for to in inter:

    	List3.append(int( to ))

    List3.append(int(i[ 0 ] ))

    List3.append(int(i[ 1 ] ))

    List3.sort()

    results.append(List3)

for final in results:

    while(results.count(final) > 1):
        
        results.remove(final)
        
        results.sort()

for output in results:

	print(("({})".format(output))) 
	