import psycopg2
from config import config,config2

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()
        params2 = config2()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
        conn2 = psycopg2.connect(**params2)

        # create a cursor
        cur = conn.cursor()
        cur2 = conn2.cursor()
        
	# execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')
        cur2.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        db_version2 = cur2.fetchone()
        print(db_version)
        print(db_version2)
       
	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            # print('Database connection closed.')

def checkdata():
    conn = None
    try:
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        ENDC = '\033[0m'

        match = 0
        notmatch = 0

        # read connection parameters
        params = config()

	    #read connection production
        params2 = config2()

        # connect to the PostgreSQL server
        #print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
        conn2 = psycopg2.connect(**params2)

        # create a cursor
        cur = conn.cursor()

        # execute a statement
        print('Listing Table Name')
        cur.execute("SELECT table_schema,table_name FROM information_schema.tables WHERE table_schema = 'public' ORDER BY table_schema,table_name")

        # display the PostgreSQL database server version
        #db_version = cur.fetchone()
        #print(db_version)
        for row in cur:
           #do something with every single row here
           #optionally print the row
           cur2 = conn.cursor()
           cur3 = conn2.cursor()
           cur2.execute("SELECT COUNT(*) FROM "+row[1])
           cur3.execute("SELECT COUNT(*) FROM "+row[1])
           res = cur2.fetchone()
           res2 = cur3.fetchone()
           print("===========================================")
           print("Table name : "+str(row[1]))
           print("Backup Count : "+str(res[0]))
           print("Production Count : "+str(res2[0]))
           if res[0] == res2[0]:
              match = match + 1
              print(OKGREEN + "Status : Match"+ENDC)
           else:
              notmatch = notmatch + 1
              print(WARNING + "Status : Not Match"+ENDC)
           print("===========================================")

        print("================Summary====================")
        print("Match : "+str(match))
        print("Not Match : "+str(notmatch))
        print("===========================================")
        # close the communication with the PostgreSQL
        cur.close()
        cur2.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            conn2.close()
            print('Database connection closed.')


if __name__ == '__main__':
    print("===========================================")
    print("Checking Database")
    print("===========================================")
    connect()
    checkdata()
