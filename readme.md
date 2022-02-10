# University of Guelph Speed Dating Match Maker

This is a match making algorithm that creates matches from a csv file for the 2022 
CCC (Caribbean Culture Club) Valentine's Day event. It compares people using information
pertaining to their: gender, preference, age, past dates (doesn't match two people twice).
It can be configured to generate as many rounds as needed, altough the more rounds and more 
past dates, the more likely it is for people not to get matched. 

## Running Script: 

To run script, the there must be a csv called "candidatesReal.csv" in the root directory.

``` python3 matching.py > matches.txt ```

Outputs the console logs to file matches.txt


