import check50
import re

@check50.check()
def exists():
    check50.exists("fibonacci.py")

@check50.check()
def test1():
    """Fibonacci function correctly calculates number on 5th place"""
    check50.run("python3 fibonacci.py").stdin("5").stdout("3").exit(0)

@check50.check()
def test2():
    """Fibonacci function correctly calculates number on 5th place"""
    check50.run("python3 fibonacci.py").stdin("2").stdout("1").exit(0)

@check50.check()
def test3():
    """Fibonacci funtion accepts only numbers"""
    actual = check50.run("python3 fibonacci.py").stdin("abc").stdout()
    if not re.match(r"[A-Za-z]+", actual):
        raise check50.Failure("Your function does't provide message in case of alphabetic input")
