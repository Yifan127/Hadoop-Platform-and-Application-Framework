#!/usr/bin/env python
import sys

# initialize previous word  to blank string
prev_TVShow = "  "
my_channel = 'ABC'
viewer_total = 0  # sum of viewer counts
abc_found = False  # indicates if ABC is found
line_cnt = 0

for line in sys.stdin:
    line = line.strip()  # strip out carriage return
    key_value = line.split('\t')  # split line, into key and value, returns a list
    line_cnt = line_cnt + 1

    # note: for simple debugging use print statements, ie:
    curr_TVShow = key_value[0]  # key is first item in list, indexed by 0
    value_in = key_value[1]  # value is 2nd item

    # -----------------------------------------------------
    # Check if its a new TVShow and not the first line
    #   (b/c for the first line the previous TVShow is not applicable)
    #   if so then print out list of TVShow and counts
    # ----------------------------------------------------
    if curr_TVShow != prev_TVShow:
        # now write out the join result, but not for the first line input
        if line_cnt > 1 and abc_found is True:
            print("{0} {1}".format(prev_TVShow, viewer_total))
        abc_found = False
        viewer_total = 0  # reset values
        prev_TVShow = curr_TVShow

    # ---------------------------------------------------------------
    # whether or not the join result was written out,
    # now process the curr TVShow
    # determine if its from file <TV show, count>  or <TV show, channel>
    # add value to viewer total
    # ---------------------------------------------------------------
    if value_in == my_channel:
        abc_found = True
    else:
        viewer_total += int(value_in)

# ---------------------------------------------------------------
# now write out the LAST join result
# ---------------------------------------------------------------
if curr_TVShow == prev_TVShow and abc_found is True:
    print('{0} {1}'.format(prev_TVShow, viewer_total))
