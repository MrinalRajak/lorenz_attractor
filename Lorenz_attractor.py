

# Lorenz system using Euler's method

import numpy as np
import matplotlib.pyplot as plt
dt=0.01
num_steps=10000
xs=np.empty(num_steps+1)
ys=np.empty(num_steps+1)
zs=np.empty(num_steps+1)

# set initial values

xs[0],ys[0],zs[0]=(0.1,1,1.05)

sig=10
rho=28
beta=8/3
for i in range(num_steps):
    xs[i+1]=xs[i]+(sig*(ys[i]-xs[i])*dt)
    ys[i+1]=ys[i]+((xs[i]*(rho-zs[i])-ys[i])*dt)
    zs[i+1]=zs[i]+((xs[i]*ys[i]-beta*zs[i])*dt)

# For plotting
fig=plt.figure()
ax=fig.add_subplot(projection='3d')
ax.plot(xs,ys,zs,lw=0.5)
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('Lorenz Attractor')
plt.show()
                   


