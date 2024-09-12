"""
Name: Adam Stafford
Date: 2/05/24
Gymnastics Scoring
This program reads a CSV text file and outputs the average gymnastics score of each competitor after removing the highest and lowest value score of the competitors.
"""
#subroutine for calculating average score of each competitor after sorting and removal of highest and lowest score.
def gymnastics_average(scores):
    
    #sorting each list first to easily remove lowest and highest values.
    #https://www.geeksforgeeks.org/python-sorted-function/
    sort_scores = sorted(scores)
    
    #source for how to remove lowest and highest value in list:
    # https://stackoverflow.com/questions/5656670/remove-max-and-min-values-from-python-list-of-integers
    trim_scores = sort_scores[1:-1]
  
    #calculates sum of the remaining 8 values and divides by 8 as well to obtain average.
    average = sum(trim_scores) / len(trim_scores)

    return average

###MAIN PROGRAM###

file = open("scores.csv", "r")

# will read every line in file until there is not a line to be read.
for line in file:
    # will read every line in file until there is not a line to be read.
    values = line.strip().split(",")
   
    #name of the competitor, given that the name is the first element in each line, it is attributed index 0.
    competitor = values[0]

    #interprets the list and converts into float for easy calculation. Will ignore the first index as that is the name of the competitor.
    #https://stackoverflow.com/a/48481713
    numbers = [float(value) for value in values[1:]]
  
    #call upon my subroutine to calculate the average for each competitor.
    competitor_score = gymnastics_average(numbers)
    
    #prints name and competitor score after removing lowest and highest value. prints to 4 decimal places.
    print(f"{competitor} earned {competitor_score:.4f} points")

#close file as to not corrupt anything  
file.close()
    