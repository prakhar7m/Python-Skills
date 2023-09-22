#!/usr/bin/python
import sys
import re
import boto3
"""
Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
    
    
    
    
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  names = []

  # Open and read the file.
  f = open(filename, 'rU')
  text = f.read()


  # Get the year.
  year_search = re.search(r'Popularity\sin\s(\d\d\d\d)', text)
  if not year_search:
    # year not found, exit.
    sys.stderr.write('Couldn\'t find the year!\n')
    sys.exit(1)
  year = year_search.group(1)
  names.append(year)

  
  #tuple is: (rank, boy-name, girl-name). Could be extracted using findall
  tuples = re.findall(r'<td>(\d+)</td><td>(\w+)</td>\<td>(\w+)</td>', text)
  #print tuples

  # Store data in a dictionary where name is a key and rank is the corresponding value.
 # not adding the already added number.
  names_to_rank =  {}
  for rank_tuple in tuples:
    (rank, boyname, girlname) = rank_tuple  # unpacking tuple
    if boyname not in names_to_rank:
      names_to_rank[boyname] = rank
    if girlname not in names_to_rank:
      names_to_rank[girlname] = rank


  # Get the names, sorted in the right order
  sorted_names = sorted(names_to_rank.keys())

  # Build up result list, one element per line
  for name in sorted_names:
    names.append(name + " " + names_to_rank[name])
    
  

    ## Adding the summry text to my s3 bucket
  s3 = boto3.resource('s3')
  object = s3.Object('pm1178-labdata', 'summary.txt')
  object.put(Body=text)
    
     ## writing summary in results.txt
  my_bucket = s3.Bucket('pm1178-labdata')
    
    
   
    
  for my_bucket_object in my_bucket.objects.all():
    file1 = open("results.txt","a+")
    file1.writelines(my_bucket_object.key+"\n")
    file1.close()
  print(my_bucket_object.key)
  
  return names  

    
    


def main():

  # keeping the arguements in list and omitting the 0th arg i.e. a script name
 

  if len(sys.argv) == 2:
        args = sys.argv[1:]
  else:
       print("usage: ", sys.argv[0], "filename")
       sys.exit(1)

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  
  for filename in args:
    names = extract_names(filename)

    # Make text out of the whole list
    text = '\n'.join(names)
  print(text)
  print('\nYes, you are running the script correctly!')
    
     
    
   

   
if __name__ == '__main__':
  main()