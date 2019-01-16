# https://github.com/kylemcdonald/SmileCNN

import os
import numpy as np
from skimage.measure import block_reduce
from skimage.io import imread
import cx_Oracle

root_dir='D:/JetBrains_projects/PycharmProjects/work/'
os.chdir(root_dir)
oh="D:/tools/Oracle/instantclient_12_2_x8664"
os.environ["ORACLE_HOME"]=oh
os.environ["PATH"]=oh+os.pathsep+os.environ["PATH"]
os.environ["NLS_LANG"]="AMERICAN_AMERICA.AL32UTF8"

def retrieveImageList(url, username, password, mode=None):
    r= ()
    c = cx_Oracle.Connection
    try:
        if mode is not None:
            c = cx_Oracle.Connection (user=username, password=password, dsn=url, mode=mode)
        else:
            c = cx_Oracle.Connection (user=username, password=password, dsn=url)

        cur = c.cursor()
        cur.execute('select status,b from bin_file order by status')
        r=cur.fetchall()
        cur.close()
    except cx_Oracle.DatabaseError as ex:
        err, =ex.args
        print("Error code    = ",err.code)
        print("Error Message = ",err.message)
        c.close()
    c.close()
    return r

# main
if __name__ == '__main__':
    examples = retrieveImageList("192.168.99.2:1521/orcl","laurent","laurent")
    X = []
    y = []

    for label, img in examples:
        # REPRENDRE ICI
        # On passe les images en N/B pour etre conforme au modèle d'apprentissage
        i = imread(path, as_gray=True)
        # Les images étant en 64/64 on les réduit en 32/32
        i = block_reduce(img, block_size=(block_size, block_size), func=np.mean)
        X.append(img)
        y.append(label)
        z.append(path)
    return np.asarray(X), np.asarray(y), np.asarray(z,str)

X, y , z = examples_to_dataset(examples)
X = X.astype(np.float32) / 255.
y = y.astype(np.int32)
print(X.dtype, X.min(), X.max(), X.shape)
print(y.dtype, y.min(), y.max(), y.shape)

X = np.expand_dims(X, axis=-1)
np.save('X.npy', X)
np.save('y.npy', y)
np.save('z.npy',z)