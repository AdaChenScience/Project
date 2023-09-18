# 9.18 作业

## ex01

对于本题，定义n对应的正整数列的乘积为product[n]，使用动态规划，将每个正整数拆解为两个正整数i,j之和，记录product[i]*product[j]的最大值以及这种拆解对应的正整数列（即i,j对应序列的拼接），再特判不进行拆解的情形，实现递推

![ex01](./imgs/ex_01.png)

## ex02

![ex02](./imgs/ex_02.png)

## ex03

对于本题，将题目中十个状态点从左上至右下依次编号为0~9，建立矩阵表示连接关系，采用dfs算法遍历求得所有可行的状态转移路径，对应四种渡河方案

![ex03](./imgs/ex_03_figure.png)

![ex03](./imgs/ex_03.png)

## ex04

![ex04](./imgs/ex_04.png)

## ex05

![ex05](./imgs/ex_05_1.png)

![ex05](./imgs/ex_05_2.png)

## ex06

由下图可知，所除系数的选取对最终结果无明显影响，只影响迭代次数

![ex06](./imgs/ex_06_1.png)

![ex06](./imgs/ex_06_2.png)

![ex06](./imgs/ex_06_3.png)

## ex07

c的三次方根的牛顿迭代式为 $x_{n+1}=x_{n}-{x_{n}^3-c \over 3x_{n}^2}$，c=10时迭代过程如下：

![ex07](./imgs/ex_07.png)

## ex08

对于本题，分别采用arctan级数、进行欧拉变换后的arctan级数、BBP公式逼近$\pi$的值，由结果可知BBP公式效率最高

![ex08](./imgs/ex_08.png)

## ex09

![ex09](./imgs/ex_09.png)

