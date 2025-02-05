import pytest
from pyscipopt.scip import Model, is_memory_freed, print_memory_in_use
from util import is_optimized_mode

def test_not_freed():
    if is_optimized_mode():
       pytest.skip()
    m = Model()
    assert not is_memory_freed()

def test_freed():
    if is_optimized_mode():
       pytest.skip()
    m = Model()
    del m
    assert is_memory_freed()

def test_print_memory_in_use():
    print_memory_in_use()

if __name__ == "__main__":
    test_not_freed()
    test_freed()