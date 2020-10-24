#!/bin/python3

import math
import os
import random
import re
import sys


#
# The function is expected to return an INTEGER.
# The function accepts INTEGER year as parameter.
#

import calendar

def ada(year):
    # Get October week days.
    oct_weeks = calendar.monthcalendar(year, 10)
    
    ada_first_week = oct_weeks[0]
    ada_second_week = oct_weeks[1]
    ada_third_week = oct_weeks[2]
    
    # If a Tuesday falls in the first week, the second Tuesday is in the second week
    # else the second Tuesday must be in the third week.
    
    if ada_first_week[calendar.TUESDAY]:
        ada_day = ada_second_week[calendar.TUESDAY]
    else:
        ada_day = ada_third_week[calendar.TUESDAY]

    # print("Ada Day is on {} .".format(ada_day))
    return ada_day
        
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = ada(year)

    fptr.write(str(result) + '\n')

    fptr.close()
