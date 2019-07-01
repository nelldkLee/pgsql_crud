import psycopg2

try:
    conn = psycopg2.connect(
            user='webdb',
            password='webdb',
            host='192.168.1.222',
            port='5432',
            database='webdb')

    corsor = conn.cursor()
    corsor.execute('select version()')
    record = corsor.fetchone()
    print('connected to -', record)

except Exception as e:
    print(f'error: {e}')
finally:
    'conn' in locals() and \
    conn and \
    conn.close()
    'corsor' in locals()