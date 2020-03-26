class A(object):
    def __init__(self):
        super().__init__()
        self._x = None
    
    @property
    def hah(self):
        return self._x

a = A()
a.hah = 1
print(a.hah)