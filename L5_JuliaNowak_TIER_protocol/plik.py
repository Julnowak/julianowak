import pandas as pd


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
                        addon[index] = 'NaN'
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
        data[f'd{i + 1}'].append(ll_new[u][i])

df = pd.DataFrame(data)
print(df)

df.to_excel("Command Files/Data_after_processing.xlsx", sheet_name='One_one')