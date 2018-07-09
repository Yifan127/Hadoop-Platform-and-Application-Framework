### Map/Reduce - Simple Join

#### Data Description
- join1_FileA.txt consists of <word, total_count> 
- join1_FileB.txt consists of <date word, day-count> (2 values in the key)

#### Task

Combine the data sets by word

In pseudo-SQL:

Select * from table A, table B, where A.key=B.key

#### Solution

- mapper: The mapper emits <word, total_count> as <key, value> for join1_FileA.txt files, 
and emits <word, date day-count> for join1_FileB.txt files (put date into value field)
- reducer: The reducer receives the shuffled-and-sorted <key, value> pairs, joins the data and puts date back into key.