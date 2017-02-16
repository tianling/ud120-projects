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
from __future__ import division

import pickle
import pandas as pd,numpy as np


enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

type(enron_data)


# poinum

# poiNum = 0
# for name in enron_data:
#     print(name)
#     if(enron_data[name]['poi'] == True):
#         poiNum += 1
#
#
# print(poiNum)

# columns = pd.DataFrame(enron_data).columns
#
# Lay = columns.str.contains("LAY")
#
# print(Lay)

#nameLay = "LAY"
#nameSkilling = "SKILLING"
#nameFastow = "FASTOW"

dataFrameEn = pd.DataFrame(enron_data)
#dataSeries = []
#print(dataSeries)

#dataLay = dataFrameEn[[name for name in dataFrameEn.columns if nameLay in name or nameSkilling in name or nameFastow in name]]
#print(dataLay)
#for name in dataLay:
 #   dataSeries.append(dataLay[name]["total_payments"])

#dataSeries = pd.Series(dataSeries)

#print(dataSeries.max())




dataSalary = dataFrameEn[[name for name in dataFrameEn.columns if dataFrameEn[name]["poi"] == True and dataFrameEn[name]["total_payments"] == "NaN"]]
total = 0;
for salaryName in dataSalary:
    total += 1
    
count = 0
for name in dataFrameEn:
    count += 1
    
print(count)
print(total+10)

percent = total/count

print(percent)









