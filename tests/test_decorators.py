import pytest

from src.decorators import log


def test_log_save_file():
    @log(filename="mylog.txt")
    def my_function(x, y):
        return x + y

    my_function(2, 2)
    with open("mylog.txt") as file:
        content = file.read()
        assert "my_function ok" in content


def test_crash_log():
    with pytest.raises(Exception):

        @log(filename="mylog.txt")
        def my_function(x, y):
            return x + y

        my_function(1, "a")
        with open("mylog.txt") as file:
            content = file.read()
            assert (
                "my_function error: unsupported operand type(s) for +: 'int' and 'str'. Inputs: (1, 'a'), {}"
                in content
            )


def test_log_captured(capsys):  # Проверка с capsys
    @log(filename=None)
    def my_function(x, y):
        return x + y

    my_function(2, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n"
