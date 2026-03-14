import oracledb

connection = oracledb.connect(
    user="your_username",
    password="your_password",
    dsn="localhost:1521/orcl"
)
cursor = connection.cursor()
cursor.execute('SELECT d.d_id, d.d_ad, i.ad, i.soyad, i.maas FROM departmentt d INNER JOIN iscilerr i ON i.d_id = d.d_id')

rows=cursor.fetchall()
maks={}
for row in rows:
    d_id = row[0]
    d_ad = row[1]
    ad = row[2]
    soyad = row[3]
    maas = row[4]
    if d_id not in maks:
        maks[d_id] = row
    else:
        if maas > maks[d_id][4]:
            maks[d_id] = row

print("Departament uzre maksimum maas:")
for d in maks.values():
    print(f"Departament: {d[1]} | Isci: {d[2]} {d[3]} | Maas: {d[4]}")

cursor.close()
connection.close()
