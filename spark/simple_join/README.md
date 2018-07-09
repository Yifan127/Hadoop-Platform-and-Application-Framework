### Spark - Simple Join
We will repeat the Map/reduce simple join exercise using spark. 

#### Mapper
Instead of having 1 mapper, we define 2 mapper functions for fileA and fileB, respectively.

split_fileA.py emits (word, total-count) as the (key, value)
split_fileB.py emits (word, date day-count) as the (key, value)

#### Join
We run the command in spark_join.txt to call the mappers and join the two outputs by word.

#### Result
The result is in spark_join1_output.txt.