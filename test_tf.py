import tensorflow as tf
import numpy as np

if __name__ == '__main__':
    t = np.random.rand(2000,2500)
    # print(t)

    # hello: object = tf.constant('Hello, TensorFlow!')
    # Declaraion des tensors
    x=tf.constant(t)
    resultat=tf.transpose(t)

    # Execution
    # Pour plus de détail sur le placement du GPU
    # sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))
    sess = tf.Session()

    r=sess.run(resultat)
    print(r)