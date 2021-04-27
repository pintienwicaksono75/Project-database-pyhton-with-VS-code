import psycopg2
con = psycopg2.connect(
        host="localhost", 
        user = "postgres",
        database = "db_bengkelmotor57",
        port = 5432,
        password = "pitikbalap57")

cur = con.cursor()
print(" Program Demo Operasi CRUD PostgreSQL Database ")
print("       Pintien Wicaksono (19/447122/SV/16841)     ")
print("================================================\n")
def main() :
    print("Menu operasi database")
    print("1. Create database dan tabel")
    print("2. Insert data")
    print("3. Select/search data")
    print("4. Update data")
    print("5. Delete data")
    menu=input("Silahkan pilih operasi ( 1/2/3/4/5 ) ? ")
    print("Anda memilih : " + menu)
    if menu=='1' :
        print("Create database dan tabel")
        # create a database named bengkel
        con = psycopg2.connect(
        host="localhost", 
        user = "postgres",
        database = "db_bengkelmotor57",
        port = 5432,
        password = "pitikbalap57")
        cur = con.cursor()
        # create a table named user
        cur = con.cursor()
        cur.execute("CREATE TABLE insight (nama VARCHAR(60) NOT NULL, penilaian BOOLEAN NOT NULL)")
        con.commit()
    elif menu=='2' :
        print("Insert data")
    elif menu=='3' :
        print("Select/search data")
    elif menu=='4' :
        print("Update data")
    elif menu=='5' :
        print("Delete data")

    lagi=input("\nUlangi ga (y/n) ? ")
    if lagi.lower() == "y" :
        main ()
    else :
        print("Program selesai")

main() 