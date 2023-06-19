# Parent-Child Relationship

This is a Python solution to the problem of finding the ultimate parent of a given child in a parent-child relationship.

## Requirements

* Python 3.6 or higher

## How to Use

1. Download the zip file to your local machine and unzip
2. Navigate to the directory containing the `assignment.py` file
3. Make sure that the `data_parent.txt` exist in the same directory.
4. Open a terminal, navigate to the directory where the files are located.
5. Run the command `python3 assignment.py` to execute the program 
6. The program will output the ultimate parent of each child in the input file.

## Input Format

The input file contains one parent-child relationship per line, with each line formatted as follows:

`child_id parent_id`

For example:

````
 Child                  Parent           
 --------------------------------------- 
 NO0000000071225394 | NO0000000974685019 
 NO0000000974685019 | NO0000000917019215 
 NO0000000810033622 |                  
 NO0000000810034882 |                  
 NO0000000810037342 |                  
 NO0000000810059672 |                  
 NO0000000810093382 |                  
 NO0000000810985852 | NO0000000991442588 
 NO0000000810094532 |                  

````

## Output Format

The program will output the ultimate parent of each child in the input file, with each line formatted as follows:

`child_id ultimate_parent_id`

For example:
````
Child                   Parent
---------------------------------------
NO0000000071225394 | NO0000000917019215
NO0000000810985852 | NO0000000991442588

