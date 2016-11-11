
#!/usr/bin/env python
# // example of program that detects suspicious transactions
# // fraud detection algorithm
# //python ./src/antifraud.py ./paymo_input/batch_payment.txt ./paymo_input/stream_payment.txt ./paymo_output/output1.txt ./paymo_output/output2.txt ./paymo_output/output3.txt

import time
import sys
from graph import Graph
from graph import Vertex

# string to be entered into the output files
str_unverified = "unverified"
str_trusted = "trusted"

batch_file = sys.argv[1] 
stream_file = sys.argv[2]

feature1_file = sys.argv[3]
feature2_file = sys.argv[4]
feature3_file = sys.argv[5]

header = None

#initiate graph
gr = Graph()

try:
    
    t1 = time.time()

    with open(batch_file, 'rb') as f:

        #skipping the header
        if not header:
            header = f.readline()

        for line in f:

            record = line.split(",")

            #skip records that are not comma delimited
            if len(record)<=1:
                continue
            
            #obtain user ids    
            vertex1 = int(record[1])
            vertex2 = int(record[2])
             
            gr.add_edge(vertex1,vertex2)
        
        t2 = time.time()
        print "=========finish reading batch:"+str(t2-t1)+"=========="
    

    #Finish reading batch file and constructing initial graph
    #Start reading the stream file.

    outputfile_feature1 = open(feature1_file, 'w')
    outputfile_feature2 = open(feature2_file, 'w')
    outputfile_feature3 = open(feature3_file, 'w')

    header = None
    
    with open(stream_file, 'rb') as f2:

        #skipping the header
        if not header:
            header = f2.readline()

        for line in f2:

            record = line.split(",")

            if len(record)<=1:
                continue

            stream_vertex1 = int(record[1])
            stream_vertex2 = int(record[2])


            degree = gr.bibfs_degree_between(stream_vertex1,stream_vertex2,4)


            if degree==1:
                # if the two users are first degree connections
                outputfile_feature1.write(str_trusted+"\n")
                outputfile_feature2.write(str_trusted+"\n")
                outputfile_feature3.write(str_trusted+"\n")
            elif degree==2:
                # if the two users are second degree connections
                outputfile_feature1.write(str_unverified+"\n")
                outputfile_feature2.write(str_trusted+"\n")
                outputfile_feature3.write(str_trusted+"\n")
            elif degree==4 or degree==3:
                # if the two users are third/fourth degree connections
                outputfile_feature1.write(str_unverified+"\n")
                outputfile_feature2.write(str_unverified+"\n")
                outputfile_feature3.write(str_trusted+"\n")
            else:
                outputfile_feature1.write(str_unverified+"\n")
                outputfile_feature2.write(str_unverified+"\n")
                outputfile_feature3.write(str_unverified+"\n")


            #update graph with streaming record
            gr.add_edge(stream_vertex1,stream_vertex2)



        t3 = time.time()
        print "=========finish reading stream:"+str(t3-t2)+"=========="

        f2.close()


except EnvironmentError:
    print("Oops!  No such file!")
finally:
    f.close()
    f2.close()
    outputfile_feature1.close()
    outputfile_feature2.close()
    outputfile_feature3.close()
    


#v = gr.get_vertex(6989)
#for w in v.getConnections():
#    print("( %d)" % (w))


