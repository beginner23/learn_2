a = [1,2,3]
b = [11,12,13]
c = ['a','b','c','d']
#返回的是一个元组一个对象
d = zip(c,a)
#以最短的序列长度
e = zip(a,c)
# print(d)
# for i in d:
#     print(i)
# for i in e:
#     print(i)
class A:
    b = 'B'
    def __init__(self,a,c):
        self.__a = a
        self.c = c
    def run(self):
        print("run")
    def __name(self):
        print("name")
a = A("A","C")
print(hasattr(a,"run"))
print(hasattr(a,"name"))
#私有的属性和方法是找不到的
print(hasattr(a,'a'))
print(hasattr(a,"c"))
#私有的属性和方法是找不到的
print(getattr(a,"run"))
print(getattr(a,"name","没有这个方法"))
print(getattr(a,"b","没有这个属性"))
print(getattr(a,"a","没有这个属性"))
print(a.__dict__)
setattr(a,"b","b")
setattr(a,"a","a")
setattr(a,"c","c")
print(a.__dict__)

