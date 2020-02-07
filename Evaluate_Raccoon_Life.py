#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 13:47:18 2020
ABE 651 - Environmental Informatics; Think Python - Chapter 8-14
Assignment 03 - Using Files and Simple Data Structures with Python
This program uses the data file(comma separated) available in text format (2008Male00006.txt)in GitHub repository from a simulated Raccoon behavior model which
describes th emovement of a racoon named George pver the entire course of day.
The purpose is to open data file, store data from file in a Dictionary and develops function to compute mean of th elist, cumulative sum of the list and distance 
between two points. It produces a new output file "Georges_life.txt"
@author: tiwari13 (Alka Tiwari)
"""
# Import necessary library
import math

# 1. Open data file in text format obtained from a Raccoon behavior model

racoon_data = open( "2008Male00006.txt", "r" )                                # open and read the data file in github repository
rlines = racoon_data.readlines()                                              # read all lines from file
headers = rlines[0].strip().split(',')                                        # headers of the file
George_status = rlines[15].strip()                                            # status(movement over the course of day) of the racoon named George  
racoon_data.close()                                                           # close the file

# 2. Store the data in a dictionary; key terms are headers of each column 
# 3. Convert column of numbers into lists of the correct number type

data = [0]*(len(rlines)-2)                                                    # create empty list excluding header and george'status line
for i in range(len(rlines[1:15])):                                            # Stores values in empty list with different data type
    data[i] = rlines[1:15][i].strip().split(",")
    data[i][3] = int(data[i][3])
    data[i][4:6] = map(float,data[i][4:6])
    data[i][8:15] = map(float,data[i][8:15])
transpose_data = list(map(list,zip(*data)))                                   # Transpose list   
dic = dict()                                                                  # Create Dictionary 
dic ['Status'] = George_status                                                # Add note for George's status                                                                             
for j in range(len(headers)):                                                 # Adds values from data to key from header 
    for j in range (len(transpose_data)):
        dic[headers[j]] = transpose_data[j]
                                                 
# 4. Writing funtions

def com_avg(lst): 
    ''' 
     Compute the mean/average of a list
    '''                                                            
    average = sum(lst)/len(lst)
    return average
     
def com_sum(lst):  
    ''' 
     Compute the cumulative sum of a list
    '''                                                            
    cum_sum = sum(lst)
    return round(cum_sum, 2)

def way(X1,Y1,X2,Y2):   
     ''' 
      Compute the distance between two points (x1,y1) and (x2,y2)
     '''                                              
     dist = sqrt((X2-X1)**2+(Y2-Y1)**2)
     return round(dist, 2)

def com_dist(X, Y, dic):
    ''' Computes the distance between subsequent set of coordinates from two lists, X and Y 
        returns list of distances added to dictionary
        initial distance = 0 and
        dic = Dictionary to add list of distances '''
            
    e_lst = []                                 
    distance = 0                               
    e_lst.append(distance)
    
    for i in range(len(X)-1):                                                 # Uses way function to calculate distances
        distance = way(X[i], Y[i], X[i+1], Y[i+1])
        e_lst.append(distance)
    
    dic['Distance'] = e_lst                                                   # Adds list of distances to Dictionary

#5. Use the function to:

# (i) Add George's movement to the data dictionary.
com_dist(dic[' X'], dic[' Y'], dic)        
# (ii) Compute George's average energy level and location(average X and Y)                   
energy_level = com_avg(dic['Energy Level'])                                   # computing energy level.
loc_X = com_avg(dic[' X'])                                                    # computing average location.
loc_Y = com_avg(dic[' Y'])
# (iii) Compute the total distance George moved in his life.
total_dist = com_sum(dic['Distance'])          

# 6. Finally, the Program should

# (i) Create a new output file called "Georges_life.txt"
output = open("Georges_life.txt", 'w')                            

# (ii) The file should have a new header block that is formatted as (replace terms in <> with values you got from the file):                                          
output.write ('Raccoon name: %s \n' %dic['Status'][:6] )              
output.write ('Average location: X %f, Y %f \n' %(loc_X, loc_Y))
output.write ('Distance traveled: %.2f \n' %total_dist)
output.write ('Average energy level: %.2f  \n' % energy_level)
output.write ('Raccoon end state: %s \n\n' % dic['Status'])                   # a blank line in between the header block and the next section of the file.  

# Write select contents of data dictionary to a new TAB delimited section of the file. This section should include the columns 
# Date, Time, X and Y coordinates, the Asleep flag, the behavior mode, and the distance traveled (in that order).
# The columns names should be labeled in the first row.
# Data from each hour of the raccoon's life should be printed on each subsequent row.

# write heading from dictionary
output.write('Date'+'\t'+'Time'+'\t'+'X'+'\t'+'Y'+'\t'+'Asleep'+'\t'+'Behavior Mode'+'\t'+'Distance traveled'+'\n')
for i in range(len(dic['Year'])):
    output.write(str(dic['Day'][i])+'\t'+str(dic['Time'][i])+'\t'+str(dic[' X'][i])+'\t'
            +str(dic[' Y'][i])+'\t'+str(dic[' Asleep'][i])+'\t'+str(dic['Behavior Mode'][i])
            +'\t'+str(dic['Distance'][i])+'\n')
# close the output
output.close()
