# from src.ecgai_overload.metaclass import overload, OverloadDict, OverloadMeta
#
#
# def overload_dict_usage():
#     print("OVERLOAD DICT USAGE")
#     d = OverloadDict()
#
#     @overload
#     def f(self):
#         pass
#
#     d["a"] = 1
#     d["a"] = 2
#     d["b"] = 3
#     d["f"] = f
#     d["f"] = f
#     print(d)
#
#
# class A(metaclass=OverloadMeta):
#     @overload
#     def f(self, x: int):
#         print('A.f int overload', self, x)
#
#     @overload
#     def f(self, x: str):
#         print('A.f str overload', self, x)
#
#     @overload
#     def f(self, x, y):
#         print('A.f two arg overload', self, x, y)
#
#
# class B(A):
#     def normal_method(self):
#         print('B.f normal method')
#
#     @overload
#     def f(self, x, y, z):
#         print('B.f three arg overload', self, x, y, z)
#
#     # works with inheritance too!
#
#
# class C(B):
#     @overload
#     def f(self, x, y, z, t):
#         print('C.f four arg overload', self, x, y, z, t)
#
#
# def overloaded_class_example():
#     print("OVERLOADED CLASS EXAMPLE")
#
#     a = A()
#     print(f'{a=}')
#     print(f'{type(a)=}')
#     print(f'{type(A)=}')
#     print(f'{A.f=}')
#
#     a.f(0)
#     a.f("hello")
#     # a.f(None) # Error, no matching overload
#     a.f(1, True)
#     print(f'{A.f=}')
#     print(f'{a.f=}')
#
#     b = B()
#     print(f'{b=}')
#     print(f'{type(b)=}')
#     print(f'{type(B)=}')
#     print(f'{B.f=}')
#     b.f(0)
#     b.f("hello")
#     b.f(1, True)
#     b.f(1, True, "hello")
#     # b.f(None)  # no matching overload
#     b.normal_method()
#
#     c = C()
#     c.f(1)
#     c.f(1, 2, 3)
#     c.f(1, 2, 3, 4)
#
#
# def run():
#     overload_dict_usage()
#     overloaded_class_example()
#
#
# if __name__ == '__main__':
#     run()
