import tensorboard
import tensorflow as tf
from tensorflow.keras import Sequential, layers, losses, optimizers, datasets
import datetime

# 通过Sequnentia容器创建LeNet-5
network = Sequential([
    layers.Conv2D(6, kernel_size=3, strides=1),  # 第一个卷积核，6个3X3的卷积核，
    layers.MaxPooling2D(pool_size=2, strides=2),  # 高宽各减半的池化层
    layers.ReLU(),  # 激活函数
    layers.Conv2D(16, kernel_size=3, strides=1),  # 第二个卷积核，16个3X3的卷积核，
    layers.MaxPooling2D(pool_size=2, strides=2),  # 高宽各减半的池化层
    layers.ReLU(),  # 激活函数
    layers.Flatten(),  # 打平层，方便全连接层处理
    layers.Dense(120, activation='relu'),  # 全连接层，120个结点
    layers.Dense(84, activation='relu'),  # 全连接层，84个结点
    layers.Dense(10, activation='relu')  # 全连接层，10个结点
])
# build 一次网络模型，给输入X的形状
network.build(input_shape=(1000, 28, 28, 1))
# 统计网络信息
network.summary()
