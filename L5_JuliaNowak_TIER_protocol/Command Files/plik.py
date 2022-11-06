import pandas as pd
import numpy as np

######################
# Wstępne czyszczenie błędnych odczytów, odpowiedni podział wartości, szkielet tabeli i utworzenie DF
with open("Original Data/weather.txt") as f:
    id = []
    year = []
    month = []
    element = []
    ll_new =[]
    lines = f.readlines()
    n = len('MX000017004195504TMAX')
    for line in lines:
        if 'S' in line:
            continue
        elif 'PRCP' in line:
            continue
        else:
            id.append(line[:11])
            year.append(line[11:15])
            month.append(line[15:17])
            element.append(line[17:n])

            helper = line[n:].split('\tI\t')
            new = []
            for h in helper:
                torm_id = []
                addon = [x for x in h.split('\t') if x != '' and x != '\n' and x != 'I\n' ]
                for index in range(len(addon)):
                    if addon[index] == 'I-9999' or addon[index] == '-9999':
                        addon[index] = np.NaN
                    if addon[index] == 'OI':
                        addon[index] = ''
                new += addon
                new = list(filter(lambda g: g != '', new))
            ll_new.append(new)


data = dict()
data['id'] = id
data['year'] = year
data['month'] = month
data['element'] = element

for i in range(31):
    data[f'd{i + 1}'] = []
    for u in range(len(ll_new)):
        data[f'd{i + 1}'].append(float((ll_new[u][i])))

df = pd.DataFrame(data)
print(df)

df.to_excel("../Command Files/Data_after_processing.xlsx", sheet_name='One_one')

###########################
# Czyszczenie pustych miejsc, zgodnie z latami i ilością dni w miesiącu

ok = df.isnull().sum(axis=1)
to_del = []
for u in range(len(ll_new)):
    if df.at[u, 'month'] in ['04', '06', '09', '11']:
        if ok[u] == 1:
            continue
    elif df.at[u, 'month'] == '02':
        if int(df.at[u, 'year']) % 4 == 0:
            if ok[u] == 2:
                continue
        else:
            if ok[u] == 3:
                continue
    else:
        if ok[u] == 0:
            continue
    to_del.append(u)

df1 = df.drop(labels=to_del, axis=0)
df1 = df1.reset_index()
print(df1)
print(df.loc[:, ['year','month', 'element']])

war = []
c1 = 0
c2 = 0
flaga = True
for i in range(len(df1.index)):
    if flaga:
        if df1.at[i, 'element'] == 'TMAX':
            c1 += 1
        if df1.at[i, 'element'] == 'TMIN':
            c2 += 1

        if c1+c2 == 2:
            if i != len(df1.index)-1 and df1.at[i+1, 'element'] != 'TMAX':
                war.append(i)
                flaga = False
            c1 = 0
            c2 = 0
    else:
        flaga = True

print(war)  # Do usunięcia
df1.to_excel("../Command Files/New_clear.xlsx", sheet_name='One_one')

