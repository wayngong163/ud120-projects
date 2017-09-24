#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    data_len = len(ages)
    for i in range(0, data_len):
        error = net_worths[i] - predictions[i]
        error = error*error
        item = [ages[i], net_worths[i], error]
        cleaned_data.append([ages[i], net_worths[i], error])

    # for item in cleaned_data:
    #    print item


    cleaned_data.sort(key = lambda x : x[2])
    # for item in cleaned_data:
    #    print item

    cleaned_data = cleaned_data[:int(0.9*len(cleaned_data))]
    
    return cleaned_data

