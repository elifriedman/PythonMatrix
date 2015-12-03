def ones(m,n):
  return Mat(m,n,1.0)
def zeros(m,n):
  return Mat(m,n)
def eye(m):
  mat = Mat(m,m)
  for i in range(m):
    mat[i,i] = 1.0
  return mat

class Mat:
  def __init__(self,m,n,fill=0.0):
    self.m = m
    self.n = n
    self.x = [[fill for i in range(n)] for j in range(m)]

  def size(self,dim=None):
    if dim==None:
      return (self.m,self.n)
    if dim==0:
      return self.m
    if dim==1:
      return self.n
    return -1
  def numel(self):
    return self.m*self.n

  def __getitem__(self,k):
    if hasattr(k, "__len__") and len(k)>=2:
      if type(k[0])==int and type(k[1])==int:
        return self.x[k[0]][k[1]]
      else:
        k0,k1 = k
        if type(k0)==int: k0 = slice(k0,k0+1)
        if type(k1)==int: k1 = slice(k1,k1+1)
        a0,b0,a1,b1 = k0.start,k0.stop,k1.start,k1.stop
        if a0==None: a0=0
        if a1==None: a1=0
        if b0==None: b0=self.m
        if b1==None: b1=self.n
        l0 = b0-a0
        l1 = b1-a1
        C = Mat(l0,l1)
        x = self.x[k0]
        C.x = [x[i][k1] for i in range(l0)]
        return C
    C = Mat(1,self.n)
    C.x = [self.x[k]]
    return C
  def __setitem__(self,k,v):
    if hasattr(k, "__len__") and len(k)>=2:
      self.x[k[0]][k[1]] = v

  def __iter__(self):
    arr = self.x[0]
    for i in range(1,self.m):
      arr.extend(self.x[i])
    return iter(arr)

  def T(self):
    C = Mat(self.n,self.m)
    C.x = [[self[i,j] for i in range(self.m)] for j in range(self.n)]
    return C

  def concat(self,other):
    assert self.m == other.m
    C = Mat(self.m,self.n+other.n)
    for i in range(self.m):
      for j in range(self.n):
        C[i,j] = self[i,j]
    for i in range(other.m):
      for j in range(other.n):
        C[i,j+self.n] = other[i,j]
    return C


  def dot(self,other):
    if type(self) == type(other):
      assert self.n == other.m
      C = Mat(self.m,other.n)
      for i in range(self.m):
        for j in range(other.n):
          C[i,j] = sum([self[i,k]*other[k,j] for k in range(self.n)])
      return C
    else: # scalar
      return self*other

  def elemwiseopp(self,other,opp):
    if type(self)==type(other):
      assert self.m == self.m and self.n == self.n
      C = Mat(self.m,self.n)
      C.x = [[(opp(self[j,i],other[j,i])) for i in range(self.n)] for j in range(self.m)]
      return C
    else:
      C = Mat(self.m,self.n)
      C.x = [[opp(self[j,i],other) for i in range(self.n)] for j in range(self.m)]
      return C

  def __gt__(self,other):
    return self.elemwiseopp(other,lambda a,b: (a>b)*1)
  def __ge__(self,other):
    return self.elemwiseopp(other,lambda a,b: (a>=b)*1)
  def __lt__(self,other):
    return self.elemwiseopp(other,lambda a,b: (a<b)*1)
  def __le__(self,other):
    return self.elemwiseopp(other,lambda a,b: (a<=b)*1)
  def __eq__(self,other):
    return self.elemwiseopp(other,lambda a,b: (a==b)*1)
  def __ne__(self,other):
    return self.elemwiseopp(other,lambda a,b: (a!=b)*1)

  def __mul__(self,other):
    """
      A*B : elementwise multiplication
    """
    return self.elemwiseopp(other,lambda a,b: a*b)
  def __rmul__(self,other):
    return self*other

  def __div__(self,other):
    """
      A*B : elementwise division
    """
    return self.elemwiseopp(other,lambda a,b: 1.0*a/b)

  def __neg__(self):
    return self*-1

  def __add__(self,other):
    return self.elemwiseopp(other,lambda a,b: a+b)
  def __radd__(self,other):
    return self+other

  def __sub__(a,b):
    return a+(-b)
  def __rsub__(a,b):
    return b+(-a)

  def applyfn(self,fn):
    C = Mat(self.m,self.n)
    C.x = [[fn(self[j,i]) for i in range(self.n)] for j in range(self.m)]
    return C

  def __str__(self):
    s = ''
    for m in range(self.m):
      for n in range(self.n):
        s += str(self[m,n]) + '\t'
      s += '\n'
    return s

  def copy(self):
    return self[:,:]

  def __repr__(self):
      "evaluatable representation"
      return self.__str__()

