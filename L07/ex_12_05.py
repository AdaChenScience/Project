import tensorflow as tf
import matplotlib.pyplot as plt

# 加载图像
image_raw_data = tf.io.read_file('./data/img28.jpg')
image = tf.image.decode_jpeg(image_raw_data)

# 将图像转换为灰度图像
gray_image = tf.image.rgb_to_grayscale(image)

# 显示图像
plt.imshow(gray_image.numpy().squeeze(), cmap='gray')
plt.show()

# 缩放灰度图像并显示
resize_image = tf.image.resize(images=gray_image, size=(56,56))
plt.imshow(resize_image.numpy().squeeze(), cmap='gray')
plt.show()