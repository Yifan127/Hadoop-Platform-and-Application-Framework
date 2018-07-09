### Spark - Advanced Join
We will reuse the Map/reduce advanced join example. But the task is to find out the total number of viewers across all 
shows for the channel BAT.

#### Mapper
split_genchan.py emits <show, views> as the <key, value>
split_gennum.py emits <show, channel> as the <key, value>

#### Join
Join the two data sets by show name. The output in this step should look like this:
<show, (views, channel)>

#### Extract channel as key
extract_channel_views.py transforms <show, (views, channel)> to <channel, views> (channel as key)

#### Sum across all channels
Reduce by key and output the final result.