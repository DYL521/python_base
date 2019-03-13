"""
常用的魔法方法：
"""


class A():
    name = 234

    def __iadd__(self, other):
        print('123')

if __name__ == '__main__':
       a  = A()
       a.__iadd__(11)
