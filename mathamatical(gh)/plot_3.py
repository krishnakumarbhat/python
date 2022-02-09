# from cv2 import split
# from cProfile import label
# from distutils.fancy_getopt import fancy_getopt
# from turtle import color, width
from matplotlib import colors
import matplotlib.pyplot as plt
import numpy as np
import random

# from webob import year
# import panda as pd
# import math
x= np.linspace(0,10,20)
y =[1/i for i in x]
y1= x**3
# print(x,y)
plt.subplot(3,3,1)
plt.plot(x,y,x,y1,marker='*',ms ='5',mec="r",mfc = "y",ls="solid",lw="3")
plt.legend(["cube",'hyperbolic'],loc = 'upper right',framealpha=1,facecolor="yellow",edgecolor="black",fancybox=True,shadow=True,fontsize=8.5)
plt.grid(axis="both",ls="dashdot",lw=1,c="r")
f1 ={'family':'cambria','color':'red','size':15}
plt.xlabel("xaxis",fontdict= f1)
plt.ylabel("yaxis",fontdict= f1)
plt.title("hyberbolic")
plt.title("1nd one")
plt.subplot(3,3,2)
plt.plot(x,y,y1,marker='*',ms ='5',mec="r",mfc = "y",ls="dotted",c='g',lw="3")
plt.title("2nd one")
plt.subplot(3,3,3)
x=[1,3,4,5,7,89,64,45,8,7,26,99,0,7,5,3,2,23]
y=[8,7,26,99,0,7,5,3,2,23,1,3,4,5,7,89,64,45]
random.shuffle(y)
plt.scatter(x,y)
plt.colorbar()
plt.subplot(3,3,4)
x1=[1,3,4,5,7,89,64,45,8,7,26,99,0,7,5,3,2,23]
y1=[53,74,53,33,28,23,1,3,4,8,7,26,99,5,7,89,64,45]
random.shuffle(y1)
plt.scatter(x1,y1,color = "green",marker="^",s=140,linewidths=3,alpha=0.7)
plt.subplot(3,3,5)
x=[1,3,45,7,89]
y=[8,7,26,99,23]
colors= [12,22,12,35,33]
sizes = [100,50,300,250,150]
plt.scatter(x,y,c=colors,s=sizes,cmap="rainbow")
plt.colorbar()
plt.subplot(3,3,6)
x3=[1,3,45,7,89]
y3=[8,7,26,99,23]
c3=["red","green","blue","yellow","brown"]
plt.barh(x3,color = c3,height=0.2,width=0.6)
plt.subplot(3,3,7)
years = ["2017","2018","2019","2020"]
placement = [150,275,324,295]
cse = [75,35,45,40,]
it=[32,23,43,22]
ece=[45,43,46,32]
w=0.4

cse_bar= np.arange(len(years))
it_bar = [i+w for i in cse_bar]
ese_bar = [i+w for i in it_bar]
ece_start=[cse[i]+it[i] for i in range(len(cse))]
plt.bar(it_bar,it,width=w,label="IT")
plt.bar(ese_bar,it,width=w,label="ese")

plt.bar(years,cse,width=0.4,color = "yellow")
plt.bar(years,it,bottom=cse,width=0.4,color = "red")
plt.bar(years,ece,bottom=ece_start,width=0.4,color = "green")
plt.legend()
plt.ylim(0,300)


# plt.figure(figsize(10,5))

plt.subplot(3,3,8)
pefor = ["excclent","good","average","poor"]
ist=[32,23,43,22]

plt.pie(ist,labels = ist,startangle = 0,explode=[0.2,0,0,0],shadow=True,colors=["black","blue","green","red"],autopct ="%2.1f%%")
plt.legend(title="pefor")
plt.figure(figsize =(7,10))





plt.show()


