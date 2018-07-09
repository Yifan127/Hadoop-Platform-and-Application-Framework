### Map/Reduce Advanced Join

#### Data Generation

Run the following command to generate six files
```commandline
sh make_data_join2.txt
```

#### Data Description
- join2_gennum*.txt consists of <TV show, count> (A TV show title and the number of viewers)
- join2_genchan*.txt consists of <TV show title, channel> (A TV show title and the channel it was on)

#### Task

Implement the following join request in Map/Reduce:

What is the total number of viewers for shows on ABC?

In pseudo-SQL it might be something like:

select sum( viewer count) from File A, File B where FileA.TV show = FileB.TV show and FileB.Channel='ABC' grouped by 
TV show

#### Solution

- mapper: The mapper emits <TV show, count> as <key, value> for join2_gennum*.txt files, 
and emits <TV show, 'ABC'> for join2_genchan*.txt files, selecting rows related to 'ABC'
- reducer: The reducer receives the shuffled-and-sorted <key, value> pairs, aggregates the viewer_count values for 
all the same keys, and emits <TV show, viewer_total> for shows related to ABC.