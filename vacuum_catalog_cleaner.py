__author__ = 'carminecalicchio'

import psycopg2

def vacuum_cleaner():
    dbname = "fms_db"
    dbuser = "carminecalicchio"
    try:
        conn = psycopg2.connect("dbname=%s user=%s" % (dbname,dbuser))
        conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
        cur = conn.cursor()
        cur.execute("""select tablename from pg_tables where schemaname = 'pg_catalog'""")
        pg_tables = cur.fetchall()
        for table in pg_tables:
            print (table[0])
            cur.execute("""vacuum full analyze %s""" % table)
            conn.commit()
        cur.close()
        conn.close()
    except:
        print ("DB ERROR")

vacuum_cleaner()