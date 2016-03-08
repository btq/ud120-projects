#!/usr/bin/python

import numpy

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []
    error = [x-y for x,y in zip(predictions,net_worths)]
    data = zip(list(ages),list(net_worths),list(error))
    cleaned_data = sorted(data, key= lambda x: numpy.fabs(x[2]))[0:80]
    #cleaned_data = sorted(data, key= lambda x: numpy.fabs(x[2]))[0:80]
    #print 'hi'
    #print data[0]
    #clean_data = sorted(data, key= lambda x: x[2]**2)
    #print clean_data
    ### your code goes here
    #for n in range(len(predictions)):
    #    print error[n]
        #error = predictions[n]-net_worths[n]

    
    return cleaned_data

