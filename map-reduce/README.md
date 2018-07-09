### Map/Reduce

The Map/Reduce framework moves computation to data, rather than moving data to computation.

It requires two functions: mapper and reducer, where the mapper reads in the data and outputs <key, value> pairs. 
Hadoop then shuffles and sorts the <key, value> pairs so that all pairs with the same key are grouped together 
and distributed to the reducer. The reducer then reads and processes the intermediary <key, value> pairs and 
outputs the results. 

