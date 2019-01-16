# https://github.com/kylemcdonald/SmileCNN

import os
import cx_Oracle

oh="D:/tools/Oracle/instantclient_12_2_x8664"
os.environ["ORACLE_HOME"]=oh
os.environ["PATH"]=oh+os.pathsep+os.environ["PATH"]
os.environ["NLS_LANG"]="AMERICAN_AMERICA.AL32UTF8"

def connectToOracle(url, username, password, mode=None):
    if mode is not None:
        connection = cx_Oracle.Connection (user=username, password=password, dsn=url, mode=mode)
    else:
        connection = cx_Oracle.Connection (user=username, password=password, dsn=url)
    return connection

def executeStmt(conn, stmt, parameters):
    if conn is not None and isinstance (conn, cx_Oracle.Connection):
        cur = conn.cursor()
        if parameters is None:
            cur.execute (stmt)
        else:
            cur.execute(stmt,parameters)
    return cur

def insertFile(conn, status, data_file ):
    if conn is not None and isinstance (conn, cx_Oracle.Connection):
        cur = conn.cursor()
        binvar=cur.var(cx_Oracle.BLOB)
        binvar.setvalue(0,data_file)
        stmt= 'INSERT INTO BIN_FILE VALUES(:1,:2)'
        cur.execute(stmt,[status,binvar])
        cur.close()

# main
if __name__ == '__main__':
    root_dir = 'D:/JetBrains_projects/PycharmProjects/work/'
    os.chdir (root_dir)

    c = cx_Oracle.Connection
# create table bin_file(status number, b blob);
# alter table bin_file add constraint check_status check (status in (0,1));
    try:
        c=connectToOracle("192.168.99.2:1521/orcl","laurent","laurent")
        for file in [ pos for pos in os.listdir ('SMILEsmileD-master/SMILEs/negatives/negatives7/')
            if pos.endswith (".jpg") ]:
            f=open('SMILEsmileD-master/SMILEs/negatives/negatives7/'+file,'rb')
            insertFile(conn=c, status=0, data_file=f.read())
            f.close()
        for file in [ pos for pos in os.listdir ('SMILEsmileD-master/SMILEs/positives/positives7/')
            if pos.endswith (".jpg") ]:
            f=open('SMILEsmileD-master/SMILEs/positives/positives7/'+file,'rb')
            insertFile(conn=c, status=1, data_file=f.read())
            f.close()
        c.commit()
    except cx_Oracle.DatabaseError as ex:
        err, =ex.args
        print("Error code    = ",err.code)
        print("Error Message = ",err.message)
        c.close()
        os._exit(1)
    c.close()