#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
print enron_data.keys()
print len(enron_data)
print enron_data['METTS MARK'].keys()
print len(enron_data['METTS MARK'].keys())
print sum([v['poi'] for k,v in enron_data.iteritems()])
print enron_data['PRENTICE JAMES']['total_stock_value']
print enron_data['COLWELL WESLEY']['from_this_person_to_poi']
print enron_data['SKILLING JEFFREY K']['total_payments']
print enron_data['LAY KENNETH L']['total_payments']
print enron_data['FASTOW ANDREW S']['total_payments']
print enron_data['THE TRAVEL AGENCY IN THE PARK']
print sum([v['salary']!='NaN' for k,v in enron_data.iteritems()])
print sum([v['email_address']!='NaN' for k,v in enron_data.iteritems()])
print sum([v['total_payments']=='NaN' for k,v in enron_data.iteritems()])#/(len(enron_data)+0.0)

