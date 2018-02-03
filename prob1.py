import numpy as np
import matplotlib.pyplot as plt


# For this problem, we use data generator instead of real dataset
def data_generator(size,noise_scale=0.05):
    xs = np.random.uniform(low=0,high=3,size=size)

    # for function y = 0.5x - 0.3 + sin(x) + epsilon, where epsilon is a gaussian noise with std dev= 0.05
    ys = xs * 0.5 - 0.3 + np.sin(3*xs) + np.random.normal(loc=0,scale=noise_scale,size=size)
    return xs, ys


def main():
    noise_scales = [0.05,0.2]

    # for example, choose the first kind of noise scale
    noise_scale = noise_scales[0]

    # generate the data form generator given noise scale
    X_train, y_train = data_generator((100,1),noise_scale=noise_scale)
    X_test, y_test = data_generator((30,1),noise_scale=noise_scale)

    # bandwidth parameters
    sigma_paras = [0.1,0.2,0.4,0.8,1.6]
    
    return X_train, y_train, X_test, y_test

X_train, y_train, X_test, y_test = main()


def normalize(x, y):
    x = (x - np.mean(y))/np.std(y)
    return x

# print(X_train)
X_train = normalize(X_train, X_train)
X_test = normalize(X_test, X_train)

X_train = np.hstack((np.ones((len(X_train),1)),X_train))
X_test = np.hstack((np.ones((len(X_test),1)),X_test))


def mse(x, y):
    a = np.dot(x.T, x)
    w_hat = np.linalg.pinv(a).dot(x.T).dot(y)
    mse_ = 1/len(x) * sum((np.dot(w_hat, x[i,:]) - y[i])**2 for i in range(len(x)))
    return mse_
  
print(mse(X_train, y_train))
#
## report learned weight vector & the bias term
#print("The weight vector in closed form solution: " + str(w_hat[1:]))
#print("The bias term in closed form solution: " + str(w_hat[0]))
#print("They agree with learned paremeters in two ways of gradient descent methods.")
#
## Theoretical train/test errors.
#
#def mse(x):

#y_pred = np.dot(w_hat, np.transpose(x_test))
#mse_test = 1/Nsplit * sum((y_test - y_pred) ** 2)
#print("The theoretical train/test errors: " + str(mse_train) + "/" + str(mse_test))
#




