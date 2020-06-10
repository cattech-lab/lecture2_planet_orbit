import matplotlib.pyplot as plt
import csv

# parameter
x = 0.1
v = 0.0
t = 0.0

k = 0.2
c = 0.1
m = 1.0

dt = 0.1

# graph data array
gt = []
gx = []
gv = []

# function
def fx(v):
    return v

def fv(x, v, k, c, m):
    return (-k * x - c * v) / m

# csv file
outfile = open('output.csv','w', newline='')
writer = csv.writer(outfile)
writer.writerow(['i', 't', 'x', 'v'])

# time loop
for i in range(1000):
    xp = x
    vp = v
    kx1 = fx(vp)
    kv1 = fv(xp, vp, k, c, m)

    xp = x + 0.5 * dt * kx1
    vp = v + 0.5 * dt * kv1
    kx2 = fx(vp)
    kv2 = fv(xp, vp, k, c, m)

    xp = x + 0.5 * dt * kx2
    vp = v + 0.5 * dt * kv2
    kx3 = fx(vp)
    kv3 = fv(xp, vp, k, c, m)

    xp = x + dt * kx3
    vp = v + dt * kv3
    kx4 = fx(vp)
    kv4 = fv(xp, vp, k, c, m)

    x = x + dt * (kx1 + 2.0 * kx2 + 2.0 * kx3 + kx4) / 6.0
    v = v + dt * (kv1 + 2.0 * kv2 + 2.0 * kv3 + kv4) / 6.0
    t = t + dt

    print('i: {0:4d}, t: {1:6.2f}, x: {2:9.6f}, v: {3:9.6f}'.format(i, t, x, v))

    gt.append(t)
    gx.append(x)
    gv.append(v)

    writer.writerow([i, t, x, v])

outfile.close()

# graph plot
plt.subplot(2,1,1)
plt.plot(gt, gx)
plt.ylabel('x')
plt.legend(['x'])
plt.grid()

plt.subplot(2,1,2)
plt.plot(gt, gv)
plt.xlabel('Time')
plt.ylabel('v')
plt.legend(['v'])
plt.grid()

plt.show()
