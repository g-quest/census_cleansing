# census_cleansing

This is a rigorous manual data cleansing program that works with census data between 1900 and 1990 without the aid of external libraries. The original file is in plain text and includes an excessive amount of unwanted characters. 

<br>After cleansing, the program asks the user for a census year, in which the states that had the minimum and maximum populations are then retrieved.

#### Example output:
```
$ python census.py
Enter census year between 1900 to 1990: 1910
Minimum: (64356, 'Alaska')
Maximum: (9113614, 'New York')
```
