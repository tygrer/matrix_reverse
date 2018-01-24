import numpy as np
import unittest
class Matrix:
    def __init__(self,a):
        self.a=a
        m,n=a.shape
        if m!=n:
            raise ValueError('This is not a matrix.')
    def __eq__(self, other):
        # Overrides the default implementation
        if isinstance(self, other.__class__):
            return self.__dict__ == other.__dict__
        return False

    def triangleFun(self):
        a=self.a
        a=a.astype(np.float64)
        m, n = a.shape
        b = np.eye(m)
        b = b.astype(np.float64)
        row=a.shape[0]
        col=a.shape[1]
        n=row-1
        for i in range(0,n):#clean the lower left corner
            for j in range(i+1,n+1):
                if a[i,i]==0:
                    continue
                lam =float(a[j,i])/a[i,i]
                a[j,0:n+1]=a[j,0:n+1]-lam*a[i,0:n+1]
                b[j,0:n+1]=b[j,0:n+1]-lam*b[i,0:n+1]
        for p in range(n,-1,-1):#clean the upper right corner
            for q in range(p-1,-1,-1):
                if a[p,p]==0:
                    continue
                lam=float(a[q,p])/a[p,p]
                a[q,0:n+1]=a[q,0:n+1]-lam*a[p,0:n+1]
                b[q,0:n+1]=b[q,0:n+1]-lam*b[p,0:n+1]
        for l in range(0,n+1):#change to E matrix
            lam=a[l,l]
            if lam==0:
                raise ValueError('The matrix has no reverse matrix.')
            a[l,l]=a[l,l]/lam
            b[l,:]=b[l,:]/lam
        #print(b)
        return b.round()
class TestMatrixFunc(unittest.TestCase):
    def test_matrix_reverse(self):
        self.assertEqual(np.mat([[1,2],[-1,-3]]).astype(np.float64).tolist(),Matrix(np.mat([[3,2],[-1,-1]])).triangleFun().tolist())

if __name__=='__main__':
    try:
        unittest.main()
    except Exception as e:
        print(e)