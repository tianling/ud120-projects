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

nameLay = "LAY"
nameSkilling = "SKILLING"
nameFastow = "FASTOW"

dataFrameEn = pd.DataFrame(enron_data)
dataSeries = []
print(dataSeries)

dataLay = dataFrameEn[[name for name in dataFrameEn.columns if nameLay in name or nameSkilling in name or nameFastow in name]]
print(dataLay)
for name in dataLay:
    # print(dataLay[name]["total_payments"])
    # print(pd.Series([dataLay[name]["total_payments"]]))
    dataSeries.append(dataLay[name]["total_payments"])

dataSeries = pd.Series(dataSeries)

print(dataSeries.max())
# dataSkilling = dataFrameEn[[name for name in dataFrameEn.columns if nameSkilling in name]]['total_payments']
# dataFastow = dataFrameEn[[name for name in dataFrameEn.columns if nameFastow in name]]['total_payments']
#
# dataSeries = pd.Series[np.array(dataLay,dataSkilling,dataFastow)]
#
# print(dataSeries)








