import sys

#checking the CLI arguement
print(sys.argv)

#check the length of input if greater than 1 it search the file in directory
if len(sys.argv) > 1:
    input = open(sys.argv[1])
else:
    input = sys.stdin
#initialize empty dict   
D = {}
for line in input:
    for word in line.split():
        D[word] = None 
input.close()
words = D.keys()
words = list(words)                           
words.sort() 
for word in words:
    print (word)