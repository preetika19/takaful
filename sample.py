# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 12:06:42 2021

@author: Preetika Lakshmanan
"""
import requests
import pandas as pd
df = pd.DataFrame()

pload1 = {'gender': 1}
pload2 = {'gender': 2}
r1 = requests.post('https://55fc5c69dac1.ngrok.io/GetFullName',json = pload1)
r2 = requests.post('https://55fc5c69dac1.ngrok.io/GetFullName',json = pload2)
print(r1.status_code)
#print(r1.text)

people = r1.json()
person1_f= people["firstName"]
person1_l=people["lastName"]

people = r2.json()
person2_f= people["firstName"]
person2_l=people["lastName"]

data = [[person1_f,person1_l],[person2_f,person2_l]]

#print(data)

df = pd.DataFrame(data,columns=['firstname','lastname'])
print (df)

df.to_excel (r'export_dataframe.xlsx', index = False, header=True)

