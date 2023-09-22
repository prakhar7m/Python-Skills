# Python-Skills

Description:

In this mini project, I engaged in various Python exercises aimed at building and reinforcing fundamental Python skills. The tasks were performed within the SageMaker environment, and the project involved multiple problem-solving tasks:

Task 1 - Missing Number Finder:

File Created: missing.py

Description:
I created a Python program, missing.py, that takes two command-line arguments: an integer N and a set of distinct integers (N-1) separated by spaces. The program's purpose is to find and print the missing number in the set. The program performs error checks for non-integer values, mismatched argument lengths, and duplicate values.

Task 2 - Unique Words Extractor:

File Created: words.py

Description:
I developed a Python program, words.py, that reads either a text file or text from standard input (stdin) and prints all unique words in alphabetical order, one per line. The program is designed to accept a filename as a command-line argument or read from stdin. It uses a sample text file hosted on the internet for testing and avoids committing the file to the repository.

Task 3 - Baby Names Data Extractor:

File Created: babynames.py

Description:
In babynames.py, I implemented the extract_names(filename) function. This function extracts data from a baby<year>.html file and returns it as a single list, including the year string at the start, followed by name-rank strings in alphabetical order. The program uses regular expressions to parse the HTML data. It combines boy and girl names and handles cases where a name appears more than once. I developed this program incrementally, achieving various milestones before the final implementation.

Task 4 - AWS S3 Integration:

File Created: babynames.bash

Description:
I extended the extract_names() function from problem 3 to accept an S3 file path and, when used with a summary argument, pushes the summary file to the specified S3 bucket location using the AWS CLI Python library. I created a bash script called babynames.bash to save the command that sends the summary file to S3. Additionally, I used a Linux command and the AWS CLI to print the contents of the S3 bucket, capturing the output in a file named results.txt.


This project demonstrates my ability to solve Python programming challenges, handle command-line arguments, work with external data sources, and integrate with cloud services like AWS S3 for data storage
