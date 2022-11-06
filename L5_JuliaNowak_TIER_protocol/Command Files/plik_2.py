import pandas as pd
import numpy as np

df1 = pd.read_excel("Command Files/New_clear_recznie_poprawiony.xlsx", 'r')
print(df1)
########################
# Tabela końcowa I

tmax_final = []
tmin_final = []
date = []


for i in range(len(df1.index)):
    for d in range(31):
        if df1.at[i, 'element'] == 'TMAX':
            if df1.at[i, 'month'] in ['04', '06', '09', '11']:
                if d >= 30:
                    continue
            elif df1.at[i, 'month'] == '02':
                if int(df1.at[i, 'year']) % 4 == 0:
                    if d >= 29:
                        continue
                else:
                    if d >= 28:
                        continue
            tmax_final.append(df1.at[i, f'd{d+1}'])
        elif df1.at[i, 'element'] == 'TMIN':
            if df1.at[i, 'month'] in ['04', '06', '09', '11']:
                if d >= 30:
                    continue
            elif df1.at[i, 'month'] == '02':
                if int(df1.at[i, 'year']) % 4 == 0:
                    if d >= 29:
                        continue
                else:
                    if d >= 28:
                        continue
            tmin_final.append(df1.at[i, f'd{d+1}'])


        txt = df1.at[i, 'year'] + '-' + df1.at[i, 'month'] + '-' + f'{d+1}'
        if txt not in date:
            date.append(txt)

print(len(date))
print(len(tmax_final))
print(len(tmin_final))

print(tmin_final)
data = dict()
#data['id'] =
data['date'] = date
data['tmax'] = tmax_final
data['tmin'] = tmin_final

df_final = pd.DataFrame(data)
print(df_final)

