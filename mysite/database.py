import psycopg2

def db_read_single_value( sql ) :
    conn = psycopg2.connect(host="db",database="postgres", user="postgres", password="postgres")
    cur = conn.cursor()
    cur.execute(sql)
    row = cur.fetchone()
    conn.close()
    return row
