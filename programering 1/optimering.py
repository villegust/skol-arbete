#Författare Vilhelm
#Optimering

import numpy as np
import matplotlib.pyplot as plt  

n = 250   # antal punkter  
r_längd = 20
r_bredd = 20 
s_bredd = 5  

x_list = np.linspace(0, r_längd, n) # avstånd från skärmväggen
xopt = [0]*n
ymax = [0]*n   
pos_bredd = np.linspace(s_bredd/2, r_bredd/2, n) # rumsbredd 
for i in range(n): 
    v1_list = np.arctan((pos_bredd[i] - s_bredd/2) / x_list)
    v2_list = np.arctan((pos_bredd[i] + s_bredd/2) / x_list)
    y_list = (v2_list - v1_list) * 180 / np.pi  # grader
    ymax[i] = max(y_list)
    xopt[i] = x_list[ np.argmax(y_list) ]

plt.figure(1)
plt.title('Bästa position för en linje parallell med rummets långvägg')
plt.plot(pos_bredd, xopt, 'b-', label = 'Bästa position') 
plt.plot(-pos_bredd, xopt, 'b-')
plt.plot([-r_bredd/2, r_bredd/2], [0, 0], 'k--', lw = 1)
plt.text(-10, -1, ' Kortvägg', color = 'k') 
plt.plot([-s_bredd/2, s_bredd/2], [0, 0], 'g-', lw = 3)
plt.text(-1, -1, ' Skärm', color = 'g') 
plt.grid()  
plt.axis('equal') 
plt.legend() 
plt.show()
plt.savefig('position.png') 

plt.figure(2)
plt.title('Optimal vinkel för en linje parallell med rummets långvägg')
plt.plot(pos_bredd, ymax, 'r-', label = 'Vinkel')
plt.ylim(0, 90)
plt.xlim(0, 10) 
plt.xlabel('Sidoavstånd från skärmens centrum (m)')
plt.ylabel('Optimal vinkel mot skärmen (°)')
plt.grid()
plt.legend()
plt.show()
plt.savefig('vinkel.png')