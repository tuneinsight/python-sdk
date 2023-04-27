from math import erf,sqrt
import numpy as np

def phi(x):
    #'Cumulative distribution function for the standard normal distribution'
    return (1.0 + erf(x / sqrt(2.0))) / 2.0

def GWASLinReg(V, X, Y):
    """
        p: the number of patients
        v: the number of variants
        f: the number of covariates

        input:

            V: the (v * p) matrix of variants
            X: the (p * (f+1)) matrix of covariates (with intercept)
            Y: the (1 * p) vector of phenotypes/labels/conditions

        output:

            P: the (v * 1) vector of p-values
    """

    v = V.shape[0]
    p = V.shape[1]
    f = X.shape[1]-1

    assert f > -1 # X must include intercept
    assert X.shape[0] == p
    assert Y.shape[0] == p

    P = [0 for i in range(v)]

    #Iterates over all the variants
    for i in range(v):
        # S = 1 || X || V
        S = np.c_[X, V[i].T]

        # (S^T x S)^-1
        STSInv = np.linalg.inv(S.T @ S)

        # err
        err = pow(STSInv[f+1][f+1], 0.5)

        # w = Y x S x (S^T x S)^-1
        w = (Y @ S) @ STSInv

        #yhat = Y x S x (S^T x S)^-1 x S^T
        Yhat = w @ S.T

        # mse = sqrt(sum((y[i] - yhat[i])^2) / p)
        mse = Y - Yhat
        mse = pow(np.inner(mse, mse)/p, 0.5)

        # p-value = 2 * cdf(-|beta/(mse*err)|(
        P[i] = 2 * phi(-abs(w[f+1] / (mse * err)))


    return np.array(P)
