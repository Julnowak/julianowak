import pandas as pd


with open("Original Data/weather.txt") as f:
    first_col = []
    lines = f.readlines()
    n = len('MX000017004195504TMAX')
    for line in lines:
        first_col.append(line[:n])
        print(line[n:].split('\tI\t'))

    print(lines)