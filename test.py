import csv
from sql_test import MySQL

csv_file = open("./pokevalue_insert.csv", "r", encoding="ms932", errors="", newline="")

# csvreader 今回は使用しない
'''
f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
header = next(f)
print(header)

for row in f:
    #rowはList
    #row[0]で必要な項目を取得することができる
    for i in range(8):
        print(row[i])
'''

# csvdictreaderで実装
f = csv.DictReader(csv_file)
for row in f:
    ins_main = 'INSERT INTO pokevalue\
        (id, name, H, A, B, C, D, S, T)\
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)'

    ins_judge = MySQL.ins_query(ins_main, row["id"], row["name"], row["H"], row["A"], row["B"], row["C"], row["D"], row["S"], row["T"])
    if not ins_judge:
        print("insert error. {0} のINSERTが失敗しました。".format(row["name"]))
        break

    sel_main = 'SELECT * FROM pokevalue\
        WHERE id=%s AND name=%s AND H=%s AND A=%s AND B=%s AND C=%s AND D=%s AND S=%s AND T=%s'

    sel_value = MySQL.query(sel_main, row["id"], row["name"], row["H"], row["A"], row["B"], row["C"], row["D"], row["S"], row["T"])
    if len(sel_value) == 0:
        print("retern no record. {0} のレコードが見つかりません。".format(row["name"]))
        break
    else:
        with open('summary.log', mode='a') as log:
            log.write("{0}{1}".format(str(sel_value), "\n"))

