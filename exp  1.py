import pandas as pd

data = [['Sunny','Warm','Normal','Strong','Warm','Same','Yes'],
        ['Sunny','Warm','High','Strong','Warm','Same','Yes'],
        ['Rainy','Cold','High','Strong','Warm','Change','No']]

h = ['0']*6

for row in data:
    if row[-1] == 'Yes':
        for i in range(6):
            if h[i] == '0':
                h[i] = row[i]
            elif h[i] != row[i]:
                h[i] = '?'

print("Hypothesis:", h)
