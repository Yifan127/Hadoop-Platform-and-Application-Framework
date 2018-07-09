#!/usr/bin/env python
import sys

my_channel = 'ABC'

for line in sys.stdin:
    line       = line.strip()   #strip out carriage return
    key_value  = line.split(",")   #split line, into key and value, returns a list
    key_in     = key_value[0].strip()   #key is first item in list
    value_in   = key_value[1].strip()   #value is 2nd item

    if(value_in.isdigit() or value_in == my_channel):
        print( '%s\t%s' % (key_in, value_in) )  #print a string tab and string
