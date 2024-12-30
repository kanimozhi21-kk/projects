
""" 
#pandas
import pandas as pd
a=[1,2,3]
my=pd.Series(a)
print(my)
##
import pandas as pd
a=[1,2,3]
myvar=pd.Series(a,index=["x","y","z"])
print(myvar)
##
import pandas as pd
mydataset={
    'cars':['bmw','volvo','ford'],
    'passin':[3,7,2] 
    }

print(mydataset)
myvar=pd.DataFrame(mydataset)
print(myvar)
##
#numpy
import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9,10])
print(arr)
print(arr[1])
print(arr[6]+arr[3])
print(arr[1:5])
print(arr[4:])
print(arr[:5])
print(arr[-3:-1])
print(arr[1:10:3])
##
import numpy 
arr=numpy.array([1,2,3,4,5])
print(arr)
a=[]
print(type(a))
print(type(arr))
##
import numpy as np
#print(np.__version__)
arr=np.array([[[2,5,6,7],[7,9,0,2],[1,0,1,8]],[[3,4,9,7],[5,7,2,4],[8,9,2,1]],[[2,4,5,8],[7,5,8,0],[9,0,4,2]]])
#print(arr)
print("2nd element on 1st row:",arr[1,2])
print('element:',arr[1,1])
print('element:',arr[0,1])
print('element:',arr[1,2])
print('element:',arr[0,2])
print('element:',arr[1,0]) 
print(arr[1,1,1])
print(arr[0,2,1])
print(arr[2,2,1])
print(arr[0,1,1])
print(arr[1,1,2])
print(arr[2,1,3])
print(arr[1,1])
##
#matplotlib
import matplotlib.pyplot as plt
import numpy as np
xpoints=np.array([1,4,8,12,16,20])
ypoints=np.array([150,200,175,125,25,180])
plt.plot(xpoints,ypoints)
plt.show()
##
import matplotlib.pyplot as plt
import numpy as np
xpoints=np.array([1,2,3,4,5])
ypoints=np.array([23,45,67,89,90])
font1={'family':'serif','color':'green','size':20}
font2={'family':'serif','color':'blue','size':10}
plt.plot(xpoints,ypoints)
plt.title("main",fontdict=font1)
plt.xlabel("number",fontdict=font2)
plt.ylabel("mark",fontdict=font2)
plt.show()
##
import matplotlib.pyplot as plt
import numpy as np
ypoints=np.array([23,95,100,89,90])
plt.plot(ypoints)
plt.show()
##
import matplotlib.pyplot as plt
import numpy as np
ypoints=np.array([23,95,100,89,90])
plt.plot(ypoints,marker="o")
plt.plot(ypoints,marker="*")
plt.show()
##
import matplotlib.pyplot as plt
import numpy as np
ypoints=np.array([23,95,100,89,90])
plt.plot(ypoints,marker="o",ms=20,mfc="g")
plt.plot(ypoints,marker="*",ms=10,mec="y")
plt.show()
##
import matplotlib.pyplot as plt
import numpy as np
ypoints=np.array([23,95,100,89,90])
plt.plot(ypoints,c='hotpink',marker="o")
plt.show()
plt.plot(ypoints,color='cyan',marker="o")
plt.show()
plt.plot(ypoints,c="green",linewidth="20")
plt.show()
##
import matplotlib.pyplot as plt
import numpy as np
y1points=np.array([1,4,8,12,16,20])
ypoints=np.array([150,200,175,125,25,180])
ypoi=np.array([45,78,98,23,90,100])
ypo=np.array([67,89,21,34,56,60])
plt.plot(ypoints)
plt.plot(y1points)
plt.plot(ypoi)
plt.plot(ypo)
plt.show()
##
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
np.random.seed(42)
x=np.random.rand(50)*10
y=2*x+1+np.random.randn(50)*10
slope,intercept,r_value,p_value,std_err=linregress(x,y)
yy=slope* x + intercept
plt.scatter(x, y, label='Data')
plt.plot(x,yy,color='red',label=f'regression line:y={slope:.2f}x + {intercept:.2f}')
plt.xlabel('x')
plt.ylabel("y")
plt.legend()
plt.show()"""

