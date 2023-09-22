# Problem Set - Python Skills (30 points)

You will be performing several Python exercises in this assignment to build and/or reinforce skills that will be used later in the semester.

You will be doing all the exercises in SageMaker. Follow the procedures from the lab to clone your Git repo to SageMaker.

## Requirements:

* You may only use **core** Python libraries (including `re`, `os`, `argparse`, `sys`, etc.)  

## Submission

You will follow the two part submission process for all labs and assignments:

1. Add all your requested files to the GitHub assignment repo for the appropriate deliverable.
2. Submit the URL for your repo to Canvas indicating that you have completed your deliverable. **Do not change your GitHub repo after submitting your URL on Canvas**

Make sure you commit **only the files requested**.

The files to be committed and pushed to your repository for this assignment are:

* `missing.py`
* `words.py`
* `babynames.py`
* `babynames.bash`
* `result.txt`

## Instructions

1. Clone this repository in SageMaker
2. Change directory into the repository
3. Do the work. Remember, all files must be within the repository directory otherwise git will not see them.
4. Remember to commit and push often (this is important when working in the cloud.)

## Problem 1 (5 points)

Write a program `missing.py` that takes two arguments as a command line argument: an integer `N`, and a set of distinct integers `N - 1` separated by a space as a string. The program should print out the missing number in the set.

```
$ python missing.py 5 "1 3 2 5"
The missing number is 4.
```

The program should produce an error for any of the following conditions:

* a non-integer value is provided in the first or as part of the second argument
* the number of items provided in the second argument does not match `N-1`
* there are duplicate values in the second argument

For example:

```
$ python missing.py 5 "1 3 3 5"
Error: the second argument has duplicate values.
```

Start off by developing your code as either a Jupyter notebook or a python script in SageMaker. You can convert a jupyter notebook to a python script using the Linux command `jupyter nbconvert --to script [YOUR_NOTEBOOK].ipynb`. You should simulate the system arguments so that you can develop iteratively and quickly. Once the program is in good shape then add capability of running from the ocommand line.

Open a Terminal in Jupyter Lab by going to `File` in the menu bar, then going to `New` then choosing `Terminal`. Use the Terminal for SageMaker Studio and not the Terminal specific to the EC2 instance you spun up.

## Problem 2 (5 points)

Write a program `words.py` that reads **either** a text file **or** text from [`stdin`](https://en.wikipedia.org/wiki/Standard_streams) and writes to [`stdout`](https://en.wikipedia.org/wiki/Standard_streams) all the unique words in the input in alphabetical order (one per line.)

The program should be setup in such a way that if the program gets a command line argument, it expects it to be a file name, and if not it reads `stdin`.

You can use the following command to make sure it works right: `$ cat filename | python words.py`. This should produce the same result as `$ python words.py filename`.

The `filename` file to be used for this problem is on the internet at this location:

`http://www.gutenberg.org/files/11/11-0.txt`

**You need to download the file into your repository directory, but you must not commit it.**

## Problem 3 (12.5 points)

For this problem, the source data files are in the babynames/ directory within this repository.

* In the `babynames.py` file, implement the *extract_names(filename)* function which takes the filename of a baby\<year\>.html file and returns the data from the file as a single list -- the year string at the start of the list followed by the name-rank strings in alphabetical order. ['2006', 'Aaliyah 91', 'Aaron 57', 'Abagail 895', ...]. 
* Modify *main()* so it calls your *extract_names()* function and prints what it returns (main already has the code for the command line argument parsing). You will be using regular expressions to parse the html. Note that for parsing webpages in general, regular expressions don't do a good job, but these webpages have a simple and consistent format.

Rather than treat the boy and girl names separately, just lump them all together. In some years, a name appears more than once in the html, but just use one number per name. Optional: make the algorithm smart about this case and choose whichever number is smaller.

Build the program as a series of small milestones, getting each step to run/print something before trying the next step. This is the pattern used by experienced programmers -- build a series of incremental milestones, each with some output to check, rather than building the whole program in one huge step.

Printing the data you have at the end of one milestone helps you think about how to re-structure that data for the next milestone. Python is well suited to this style of incremental development. For example, first get it to the point where it extracts and prints the year and calls `sys.exit(0)`. Here are some suggested milestones:

* Extract all the text from the file and print it
* Find and extract the year and print it
* Extract the names and rank numbers and print them
* Get the names data into a dict and print it
* Build the [year, 'name rank', ... ] list and print it
* Fix `main()` to use the ExtractNames list

Rather than have functions just print to standard out, it is more re-usable to have the function *return* the extracted data, so then the caller has the choice to print it or do something else with it. (You can still print directly from inside your functions for your little experiments during development.)

Have `main()` call `extract_names()` for each command line arg and print a text summary. To make the list into a reasonable looking summary text, here's a clever use of join: `text = '\n'.join(mylist) + '\n'`

The summary text should look like this for each file:

```
2006
Aaliyah 91
Aaron 57
Abagail 895
Abbey 695
Abbie 650
...
```

## Problem 4 (7.5 points)

Add an additional argument in the `extract_names()` function from problem 3 that accepts an S3 file path that, if used with the `summary` argument, will push the summary file to the specified S3 bucket location using an AWS CLI related python library. This is the only non-core Python library you can use.

Save the command that sends the summary file to S3 to a bash script called `babynames.bash`. Use a linux command and the AWS CLI to print the contents of your S3 bucket showing the summary file and save to a file called `results.txt`. Include both files in your Git repo.

## Grading Rubric

If your the submission meets or exceeds the requirements, is creative, is well thought-out, has proper presentation and grammar, and is at the graduate student level, then the submission will get full credit. Otherwise, partial credit will be given and deductions may be made for any of the following reasons:

Points will be deducted for any of the following reasons:

* The instructions are not followed
* There are missing sections of the deliverable
* The overall presentation and/or writing is sloppy
* There are no comments in your code
* There are files in the repository other than those requested
* There are absolute filename links in your code
* The repository structure is altered in any way
* Files are named incorrectly (wrong extensions, wrong case, etc.)
