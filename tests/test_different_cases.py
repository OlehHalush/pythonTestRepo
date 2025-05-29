import pytest
from assertpy import assert_that


class TestTesting:
    value = 0

    def test_one(self):
        self.value = 1
        assert self.value == TestTesting.value

    # assertion with description on fail
    def test_assertion(self):
        assert 3 == 4, "should be 3"

    # assertion of exception being raised
    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            1 / 0

    # assertion of exception being raised
    def test_zero_division_with_exception_details_access(self):
        with pytest.raises(ZeroDivisionError) as exception_info:
            1 / 0
        print("\nprinting exception_info")
        print(exception_info.traceback)

    # check specific exception
    def test_specific_exception_being_raised(self):
        def foo():
            raise NotImplementedError

        with pytest.raises(RuntimeError) as exception_info:
            foo()
        assert exception_info.type is RuntimeError

    content = "content"

    def test_create_file(self, tmp_path):
        d = tmp_path / "sub"
        d.mkdir()
        p = d / "hello.txt"
        p.write_text(TestTesting.content)
        assert p.read_text(encoding="utf-8") == TestTesting.content
        assert len(list(tmp_path.iterdir())) == 1
        assert 0