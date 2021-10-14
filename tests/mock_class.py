from src.ecgai_overload.metaclass import OverloadMeta, overload

int_overload = f'int overload'
str_overload = f'str overload'
int_str_overload = f'int, str overload'
int_int_overload = f'int, int overload'
str_str_overload = f'str, str overload'
flt_flt_overload = f'float, float overload from sub class'


# noinspection PyUnusedLocal
class RootClass(metaclass=OverloadMeta):

    @overload
    def run(self, num1: int = 2):
        return int_overload

    @overload
    def run(self, str1: str):
        return str_overload

    @overload
    def run(self, num1: int, str1: str):
        return int_str_overload

    @overload
    def run(self, num1: int, num2: int):
        return int_int_overload

    @overload
    def run(self, str1: str, str2: str):
        return str_str_overload

    @overload
    def run(self, str1: str, str2: str, num1: int = 7):
        return str_str_overload


class SubClass(RootClass):

    @overload
    def run(self, flt1: float, flt2: float):
        return flt_flt_overload
