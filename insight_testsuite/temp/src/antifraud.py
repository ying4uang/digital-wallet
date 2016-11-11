
# // example of program that detects suspicious transactions
# // fraud detection algorithm

# //python ./src/antifraud.py ./paymo_input/batch_payment.txt ./paymo_input/stream_payment.txt ./paymo_output/output1.txt ./paymo_output/output2.txt ./paymo_output/output3.txt
import time
import sys
from graph import Graph
from graph import Vertex

str_unverified = "unverified"
str_trusted = "trusted"

batch_file = sys.argv[1] 
stream_file = sys.argv[2]

feature1_file = sys.argv[3]
feature2_file = sys.argv[4]
feature3_file = sys.argv[5]


gr = Graph()

try:
    
    t1 = time.time()
    with open(batch_file, 'rb') as f:

        for line in f:

            if line == '\n':
                print "Skipping an empty line."
                continue
                
            if "time" in line :
                continue

            record = line.split(",")

            if len(record)<=1:
                continue
                
            vertex1 = int(record[1])
            vertex2 = int(record[2])
             
            gr.add_edge(vertex1,vertex2)
        t2 = time.time()
        print "=========finish reading batch:"+str(t2-t1)+"=========="
    
    f.close()
    
    #for i in gr.get_vertex(46702).get_first_connections():
    #    print i
    #print gr.bibfs_degree_between(46702,3289,4)

    outputfile_feature1 = open(feature1_file, 'w')
    outputfile_feature2 = open(feature2_file, 'w')
    outputfile_feature3 = open(feature3_file, 'w')

    header = None
    
    with open(stream_file, 'rb') as f2:

        if not header:
            header = f2.readline()

        for line in f2:

            if line == '\n':
                print "Skipping an empty line."
                continue

            record = line.split(",")

            if len(record)<=1:
                continue

            stream_vertex1 = int(record[1])
            stream_vertex2 = int(record[2])


            degree = gr.bibfs_degree_between(stream_vertex1,stream_vertex2,4)


            if degree==1:
                outputfile_feature1.write(str_trusted+"\n")
                outputfile_feature2.write(str_trusted+"\n")
                outputfile_feature3.write(str_trusted+"\n")
            elif degree==2:
                outputfile_feature1.write(str_unverified+"\n")
                outputfile_feature2.write(str_trusted+"\n")
                outputfile_feature3.write(str_trusted+"\n")
            elif degree<=4:
                outputfile_feature1.write(str_unverified+"\n")
                outputfile_feature2.write(str_unverified+"\n")
                outputfile_feature3.write(str_trusted+"\n")
            else:
                outputfile_feature1.write(str_unverified+"\n")
                outputfile_feature2.write(str_unverified+"\n")
                outputfile_feature3.write(str_unverified+"\n")

            gr.add_edge(stream_vertex1,stream_vertex2)



        t3 = time.time()
        print "=========finish reading stream:"+str(t3-t2)+"=========="

        f2.close()


except EnvironmentError:
    print("Oops!  No such file!")


#v = gr.get_vertex(6989)
#for w in v.getConnections():
#    print("( %d)" % (w))


