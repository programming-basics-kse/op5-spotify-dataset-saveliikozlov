import csv
import ast
rows = []
with open('top_50_2023.csv', 'r') as f:
    csv_reader = csv.reader(f, delimiter=',')
    header = next(csv_reader)
    for row in csv_reader:
        rows.append(row)

# # 1
# energy = header.index('energy')
# liveness = header.index('liveness')
# en_list = []
# liv_list = []
# for row in rows:
#     if float(row[energy]) > 0.5:
#         row[liveness] = float(row[liveness])
#         liv_list.append(row[liveness])
#     else:
#         continue
# result = sum(liv_list) / len(liv_list)
# print(result)
# 3
# artist = header.index('artist_name')
# dict_artist = {}
#
# for row in rows:
#     if row[artist] not in dict_artist.keys():
#         dict_artist[row[artist]] = 1
#     else:
#         dict_artist[row[artist]] += 1
# max_val = max(dict_artist.values())
# top = sorted(dict_artist.items(), key=lambda x: x[1], reverse=True)[0]
# print(top)
# # 5
# years = header.index('album_release_date')
# counter = {}
# year_list = []
# for row in rows:
#     year_list.append(row[years][:4])
# for year in year_list:
#     if year not in counter:
#         counter[year] = 1
#     else:
#         counter[year] += 1
# top = sorted(counter.items(), key=lambda x: x[1], reverse=True)[0]
# print(top)