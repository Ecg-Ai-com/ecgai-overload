import pytest

from src.ecgai_overload.metaclass import NoMatchingOverload
from tests.mock_class import RootClass, int_overload, str_overload, int_str_overload, int_int_overload, \
    str_str_overload, SubClass, flt_flt_overload


class TestMetaClass:
    def test_int_overload_with_named_and_default_parameters(self):
        expected = int_overload
        sut = RootClass()
        result = sut.run()
        assert expected == result

    def test_str_overload_with_named_parameters(self):
        expected = str_overload
        sut = RootClass()
        result = sut.run(str1='number two')
        assert expected == result

    def test_int_and_str_overload_with_named_parameters(self):
        expected = int_str_overload
        sut = RootClass()
        result = sut.run(num1=2, str1='number two')
        assert expected == result

    def test_int_and_int_overload_with_named_parameters(self):
        expected = int_int_overload
        sut = RootClass()
        result = sut.run(num1=2, num2=6)
        assert expected == result

    def test_str_and_str_overload_with_named_parameters(self):
        expected = str_str_overload
        sut = RootClass()
        result = sut.run(str1='number two', str2='number three')
        assert expected == result

    def test_int_overload_without_named_parameters(self):
        expected = int_overload
        sut = RootClass()
        result = sut.run(2)
        assert expected == result

    def test_str_overload_without_named_parameters(self):
        expected = str_overload
        sut = RootClass()
        result = sut.run('number two')
        assert expected == result

    def test_int_and_str_overload_without_named_parameters(self):
        expected = int_str_overload
        sut = RootClass()
        result = sut.run(2, 'number two')
        assert expected == result

    def test_int_and_int_overload_without_named_parameters(self):
        expected = int_int_overload
        sut = RootClass()
        result = sut.run(2, 6)
        assert expected == result

    def test_str_and_str_overload_without_named_parameters(self):
        expected = str_str_overload
        sut = RootClass()
        result = sut.run('number two', 'number three')
        assert expected == result

    def test_flt_and_flt_overload_from_subclass_with_named_parameters(self):
        expected = flt_flt_overload
        sut = SubClass()
        result = sut.run(flt1=1.0, flt2=2.42343)
        assert expected == result

    def test_int_and_int_overload_from_subclass_with_named_parameters(self):
        expected = int_int_overload
        sut = SubClass()
        result = sut.run(num1=2, num2=6)
        assert expected == result

    def test_flt_and_flt_overload_from_subclass_without_named_parameters(self):
        expected = flt_flt_overload
        sut = SubClass()
        result = sut.run(1.0, 2.42343)
        assert expected == result

    def test_int_and_int_overload_from_subclass_without_named_parameters(self):
        expected = int_int_overload
        sut = SubClass()
        result = sut.run(2, 6)
        assert expected == result

    def test_no_overload_function_found_throw_exception(self):
        sut = SubClass()
        with pytest.raises(NoMatchingOverload):
            # noinspection PyArgumentList
            sut.run(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 'test', 'method', 'does', 'not', 'exist')
