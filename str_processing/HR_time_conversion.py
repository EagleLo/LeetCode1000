#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    """
    Convert 12-hour time format to 24-hour military time format.
    
    Rules:
    - 12:00:00AM -> 00:00:00 (midnight)
    - 12:00:00PM -> 12:00:00 (noon)
    - For AM times (1-11): keep same hour
    - For PM times (1-11): add 12 to hour
    
    Args:
        s: Time string in format "HH:MM:SSAM" or "HH:MM:SSPM"
    
    Returns:
        Time string in 24-hour format "HH:MM:SS"
    """
    # Extract AM/PM indicator
    period = s[-2:]  # Get last 2 characters (AM or PM)
    time_part = s[:-2]  # Get time part without AM/PM
    
    # Split time into hours, minutes, seconds
    hours, minutes, seconds = time_part.split(':')
    hours = int(hours)
    
    # Handle special cases for 12:xx:xx
    if period == 'AM':
        if hours == 12:
            # 12:xx:xx AM becomes 00:xx:xx
            hours = 0
    else:  # period == 'PM'
        if hours != 12:
            # 1:xx:xx PM to 11:xx:xx PM becomes 13:xx:xx to 23:xx:xx
            hours += 12
    
    # Format the result with leading zeros
    return f"{hours:02d}:{minutes}:{seconds}"


def test_timeConversion():
    """Test the timeConversion function with various examples."""
    print("Testing timeConversion function:")
    print("=" * 50)
    
    test_cases = [
        ("12:00:00AM", "00:00:00", "Midnight"),
        ("12:00:00PM", "12:00:00", "Noon"),
        ("07:05:45PM", "19:05:45", "Sample input"),
        ("12:01:00AM", "00:01:00", "Just after midnight"),
        ("12:01:00PM", "12:01:00", "Just after noon"),
        ("01:00:00AM", "01:00:00", "1 AM"),
        ("01:00:00PM", "13:00:00", "1 PM"),
        ("11:59:59AM", "11:59:59", "Just before noon"),
        ("11:59:59PM", "23:59:59", "Just before midnight"),
        ("06:30:00AM", "06:30:00", "Morning time"),
        ("06:30:00PM", "18:30:00", "Evening time"),
    ]
    
    for input_time, expected, description in test_cases:
        result = timeConversion(input_time)
        status = "✓" if result == expected else "✗"
        print(f"{status} {description}:")
        print(f"  Input: {input_time}")
        print(f"  Expected: {expected}")
        print(f"  Got: {result}")
        if result != expected:
            print(f"  ERROR: Expected {expected}, got {result}")
        print()


if __name__ == '__main__':
    # Check if running in test mode
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        test_timeConversion()
    else:
        # Normal execution for HackerRank
        s = input()
        result = timeConversion(s)
        print(result)
