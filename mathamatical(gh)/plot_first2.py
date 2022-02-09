import matplotlib.pyplot as plt
# import pandas as pd
print("enter coordinate")
x=input()
y=input()
e=list(x.split(" "))
f=list(y.split(" "))
# print(e,f)
plt.plot(e,f)
plt.xlabel("time")
plt.ylabel("efficiance")
plt.title("life lonogavity")
plt.show()