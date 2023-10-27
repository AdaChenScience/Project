from keras.models import Model
from keras.layers import Input, Conv2D, MaxPooling2D, Flatten, Dense
from keras.layers import Dropout
 
def VGG19(input_shape=(224, 224, 3), num_classes=1000, dropout_rate=0.5):
    # 定义输入层
    inputs = Input(shape=input_shape)
 
    # 第1段卷积-池化层
    x = Conv2D(filters=64, kernel_size=(3, 3), padding="same", activation="relu")(inputs)
    x = Conv2D(filters=64, kernel_size=(3, 3), padding="same", activation="relu")(x)
    x = MaxPooling2D(pool_size=(2, 2), strides=(2, 2))(x)
 
    # 第2段卷积-池化层
    x = Conv2D(filters=128, kernel_size=(3, 3), padding="same", activation="relu")(x)
    x = Conv2D(filters=128, kernel_size=(3, 3), padding="same", activation="relu")(x)
    x = MaxPooling2D(pool_size=(2, 2), strides=(2, 2))(x)
 
    # 第3段卷积-池化层
    x = Conv2D(filters=256, kernel_size=(3, 3), padding="same", activation="relu")(x)
    x = Conv2D(filters=256, kernel_size=(3, 3), padding="same", activation="relu")(x)
    x = Conv2D(filters=256, kernel_size=(3, 3), padding="same", activation="relu")(x)
    x = Conv2D(filters=256, kernel_size=(3, 3), padding="same", activation="relu")(x)
    x = MaxPooling2D(pool_size=(2, 2), strides=(2, 2))(x)
 
    # 第4段卷积-池化层
    x = Conv2D(filters=512, kernel_size=(3, 3), padding="same", activation="relu")(x)
    x = Conv2D(filters=512, kernel_size=(3, 3), padding="same", activation="relu")(x)
    x = Conv2D(filters=512, kernel_size=(3, 3), padding="same", activation="relu")(x)
    x = Conv2D(filters=512, kernel_size=(3, 3), padding="same", activation="relu")(x)
    x = MaxPooling2D(pool_size=(2, 2), strides=(2, 2))(x)
 
    # 第5段卷积-池化层
    x = Conv2D(filters=512, kernel_size=(3, 3), padding="same", activation="relu")(x)
    x = Conv2D(filters=512, kernel_size=(3, 3), padding="same", activation="relu")(x)
    x = Conv2D(filters=512, kernel_size=(3, 3), padding="same", activation="relu")(x)
    x = Conv2D(filters=512, kernel_size=(3, 3), padding="same", activation="relu")(x)
    x = MaxPooling2D(pool_size=(2, 2), strides=(2, 2))(x)
 
    # 全连接层
    x = Flatten()(x)
    x = Dense(units=4096, activation="relu")(x)
    x = Dropout(rate=dropout_rate)(x)
    x = Dense(units=4096, activation="relu")(x)
    x = Dropout(rate=dropout_rate)(x)
    outputs = Dense(units=num_classes, activation="softmax")(x)
 
    # 定义模型
    model = Model(inputs=inputs, outputs=outputs, name="VGG19")
 
    return model

if __name__ == "__main__":
    VGG19().summary()