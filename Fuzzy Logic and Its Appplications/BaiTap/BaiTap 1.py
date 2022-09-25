import numpy as np
import matplotlib.pyplot as plt

X = np.array( [30,50,75,90,100,125,150,200] )
A = np.array( [0,0,0,0.1,0.5,0.8,1,1] )
B = np.array( [1,1,0.9,0.8,0.7,0.3,0.1,0] )
C = np.array( [0,0.3,0.9,1,1,0.9,0.5,0] )

plt.figure( figsize=(12,6) )
plt.title( "ĐỒ THỊ BIỂU DIỄN HÀM THUỘC CỦA TẬP MỜ" )
plt.plot( X,A,label="Tập mờ A = " + r"$\{\frac{0}{30},\frac{0}{50},\frac{0}{75},\frac{0.1}{90},\frac{0.5}{100},\frac{0.8}{125},\frac{1}{150},\frac{1}{200},\}$",color="blue",marker="+" )
plt.plot( X,B,label="Tập mờ B = " + r"$\{\frac{1}{30},\frac{1}{50},\frac{0.9}{75},\frac{0.8}{90},\frac{0.7}{100},\frac{0.3}{125},\frac{0.1}{150},\frac{0}{200},\}$",color="red",marker="*")
plt.plot( X,C,label="Tập mờ C = " + r"$\{\frac{0}{30},\frac{0.3}{50},\frac{0.9}{75},\frac{1}{90},\frac{1}{100},\frac{0.9}{125},\frac{0.5}{150},\frac{0}{200},\}$",color="green",marker="o" )
plt.xlabel( "Không gian nền X = " + str(X) )
plt.ylabel( "Mức độ phụ thuộc: " + r"$\mu_A(x)$" )
plt.legend( loc="best" )
plt.show()





