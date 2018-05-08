import tensorflow as tf
# TensorFlow 实现简单的 hello world

# 创建一个常量操作
# 这个常量操作会在默认的图中添加一个节点
#
# 构造函数返回的值表示常量op的输出。
hello = tf.constant('Hello, TensorFlow!')
# 启动 tf session
sess = tf.Session()
# 运行图
print(sess.run(hello))
