# Table of Contents

1. [Challenge Summary] (README.md#challenge-summary)
2. [Details of Implementation] (README.md#details-of-implementation)
3. [Test Cases] (README.md#test-cases)
4. [Writing clean, scalable and well-tested code](README.md#writing-clean-scalable-and-well-tested-code)
5. [Repo directory structure] (README.md#repo-directory-structure)
6. [Testing your directory structure and output format] (README.md#testing-your-directory-structure-and-output-format)
7. [FAQ] (README.md#faq)

##Challenge Summary 

Imagine you're a data engineer at a "digital wallet" company called PayMo that allows users to easily request and make payments to other PayMo users. The team at PayMo has decided they want to implement features to prevent fraudulent payment requests from untrusted users. 

[Back to Table of Contents] (README.md#table-of-contents)

##Detail of Implementation 

This submitted solution is mainly based on Graph and Graph Search. I have utilized bidirectional breadth search to speed up the traditional bfs because the degree of connections can grow exponentially. 

###Language and Libraries
This challenge was completed in Python and no external libraries were used.

###Future Improvements:
1.File Input Output can be improved to read and write in chunk.
2.With a high-performance machine, we could precalculate second degree connections in the batch process to speed up the process in streadming.


##Test Cases

In addition to the test case 1 provided. Two addition test cases were provided.


###Test Case 2
This test case is to validate the graph is being updated by the latest streaming data.

Batch File:
*time, id1, id2, amount, message
*2016-11-01 17:38:25, 49466, 6989, 23.74, 🦄

Stream File:
*time, id1, id2, amount, message
*2016-11-01 17:38:25, 49466, 6990, 23.74, 🦄
*2016-11-01 17:38:25, 49466, 6991, 23.75, 🦄
*2016-11-01 17:38:25, 6990, 6991, 23.75, 🦄

Expected Result: The first two records have no connections, the third one was a second degree connection.


###Test Case 3
This test case is to test out 3rd degree connection is included in feature 3. 

Batch File:
*time, id1, id2, amount, message
*2016-11-01 17:38:25, 49466, 6989, 23.74, 🦄
*2016-11-01 17:38:25, 1123, 6989, 23.74, 🦄
*2016-11-01 17:38:25, 1123, 2255, 23.74, 🦄

Stream File:
time, id1, id2, amount, message
2016-11-01 17:38:25, 49466, 2255, 23.74, 🦄

Expected Result: The two users are within fourth degree connections.

### Batch and Stream File Downloaded

I have only spot checked the results. Took about 17s for the batch file and 1200s for the stream file to load. A rough timer was also added in the code.


##Repo directory structure
[Back to Table of Contents] (README.md#table-of-contents)

Example Repo Structure

	├── README.md 
	├── run.sh
	├── src
	│  	└── antifraud.java
	├── paymo_input
	│   └── batch_payment.txt
	|   └── stream_payment.txt
	├── paymo_output
	│   └── output1.txt
	|   └── output2.txt
	|   └── output3.txt
	└── insight_testsuite
	 	   ├── run_tests.sh
		   └── tests
	        	└── test-1-paymo-trans
        		│   ├── paymo_input
        		│   │   └── batch_payment.txt
        		│   │   └── stream_payment.txt
        		│   └── paymo_output
        		│       └── output1.txt
        		│       └── output2.txt
        		│       └── output3.txt
        		└── your-own-test
            		 ├── paymo_input
        		     │   └── batch_payment.txt
        		     │   └── stream_payment.txt
        		     └── paymo_output
        		         └── output1.txt
        		         └── output2.txt
        		         └── output3.txt

The contents of `src` do not have to contain the single file called `"antifraud.java"`, you are free to include one or more files and name them as required by your implementation.

##Testing your directory structure and output format
[Back to Table of Contents] (README.md#table-of-contents)
