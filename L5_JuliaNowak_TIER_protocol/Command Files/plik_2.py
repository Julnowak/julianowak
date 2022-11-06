import pandas as pd
import numpy as np

df1 = pd.read_excel("../Command Files/Data_edited.xlsx")
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

        if len(str(df1.at[i, 'month'])) == 1:
            t = '0' + str(df1.at[i, 'month'])
        else:
            t = str(df1.at[i, 'month'])

        if len(str(df1.at[i, 'month'])) == 1:
            y = '0' + str(df1.at[i, 'year'])
        else:
            y = str(df1.at[i, 'year'])

        txt = y + '-' + t + '-' + f'{d+1}'
        if txt not in date:
            date.append(txt)


aku = pd.read_excel("../Command Files/Data_edited.xlsx", usecols="A", skiprows=list(range(1, len(df1.index) + 1, 2)))
data = dict()
data['id'] = 'MX000017004'
data['date'] = date
data['tmax'] = tmax_final
data['tmin'] = tmin_final

df_final = pd.DataFrame(data)
print(df_final)
df_final = df_final.dropna()
df_final.to_excel("../Analysis Data/Final_data.xlsx", sheet_name='One_one')