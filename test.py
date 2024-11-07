import numpy as np
from arr import integrate


def test1():
  '''Test case 1'''
  arr = np.array([1, 2, 3, 4, 5])
  assert integrate(arr, 1) == 15

def test2():
  '''Test case 2'''
  arr = np.array([])
  assert integrate(arr, 2) == 0

if __name__ == '__main__':
  test1()
  test2() 
