import numpy as np

#inputs
x_0 = np.arange(-1.0, 1.0, 0.1)
x_1 = np.arange(-1.0, 1.0, 0.1)

#Results
Z = np.zeros((400, 2))

w_im  = np.array([[1.0, 2.0], [2.0, 3.0]])
w_mo  = np.array([[-1.0, 1.0], [1.0, -1.0]])

#偏值 
b_im = np.array([0.3, -0.3])
b_mo = np.array([0.4, 0.1])

def middle_layer(x, w, b):
    u = np.dot(x,w) + b
    return 1/(1+np.exp(-u))

def output_layer(x, w, b):
    u = np.dot(x,w) + b
    return np.exp(u)/np.sum((np.exp(u)))

for i in range(20):
    for j in range(20):
        inp =np.array([x_0[i], x_1[j]])
        mid = middle_layer(inp, w_im, b_im)
        out = output_layer(mid, w_mo, b_mo)
        Z[i*20 + j] = out

print(Z)