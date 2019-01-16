import os
import cx_Oracle
import sys

if sys.platform=='darwin':
    root_dir = '/Users/leturgezl/PycharmProjects/work'
    os.chdir (root_dir)
    oh="/Users/leturgezl/Applications/instantclient_12_2"

os.environ["ORACLE_HOME"]=oh
os.environ["PATH"]=oh+os.pathsep+os.environ["PATH"]
os.environ["NLS_LANG"]="AMERICAN_AMERICA.AL32UTF8"


if __name__ == '__main__':
    c = cx_Oracle.Connection
    try:

        c = cx_Oracle.Connection (user="laurent", password="laurent", dsn="192.168.99.3:1521/orcl")

        cur = c.cursor()
        cur.execute('select status,b from bin_file where rownum=1')
        r=cur.fetchall()
        cur.close()
    except cx_Oracle.DatabaseError as ex:
        err, =ex.args
        print("Error code    = ",err.code)
        print("Error Message = ",err.message)
        c.close()
    c.close()

    print("r",r)
