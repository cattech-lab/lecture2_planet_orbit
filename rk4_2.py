import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# parameter
r = np.array([0.0, 1.0]) 
v = np.array([-1.0, 0.0])
t = 0.0

dt = 0.001
nt = 10000
nout = 20

# graph data array
gx = []
gy = []
ims = []
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# function
def fr(v):
    return v

def fv(r):
    rnorm = np.linalg.norm(r)
    return -r / rnorm**3  

# time loop
for i in range(nt):
    rp = r
    vp = v
    kr1 = fr(vp)
    kv1 = fv(rp)

    rp = r + 0.5 * dt * kr1
    vp = v + 0.5 * dt * kv1
    kr2 = fr(vp)
    kv2 = fv(rp)

    rp = r + 0.5 * dt * kr2
    vp = v + 0.5 * dt * kv2
    kr3 = fr(vp)
    kv3 = fv(rp)

    rp = r + dt * kr3
    vp = v + dt * kv3
    kr4 = fr(vp)
    kv4 = fv(rp)

    r += dt * (kr1 + 2.0 * kr2 + 2.0 * kr3 + kr4) / 6.0
    v += dt * (kv1 + 2.0 * kv2 + 2.0 * kv3 + kv4) / 6.0
    t += dt

    if i % nout == 0:    
        print('i: {0:4d}, t: {1:6.2f}, x: {2:9.6f}, y: {3:9.6f} , vx: {4:9.6f}, vy: {5:9.6f}'.format(i, t, r[0], r[1], v[0], v[1]))   
        gx.append(r[0])
        gy.append(r[1])
        im_line = ax.plot(gx, gy, 'b')
        im_point = ax.plot(r[0], r[1], marker='.', color='b', markersize=10 )
        im_time = ax.text(0.0, 0.1, 'time = {0:5.2f}'.format(t))
        ims.append(im_line + im_point + [im_time])

# graph plot
ax.plot(0.0, 0.0, marker='.', color='r', markersize=10 )
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_aspect('equal', 'datalim')
anm = animation.ArtistAnimation(fig, ims, interval=50)
anm.save('animation.gif', writer='pillow')
plt.show()
