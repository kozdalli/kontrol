import check50
import check50.c

@check50.check()
def exists():
    """odev3.c exists"""
    check50.exists("odev3.c")

@check50.check(exists)
def compiles():
    """odev3.c compiles"""
    check50.c.compile("odev3.c")
    
@check50.check(compiles)
def test1():
    """378282246310005 AMEX"""
    check50.run("./odev3").stdin("378282246310005").stdout("AMEX\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def test2():
    """371449635398431 AMEX"""
    check50.run("./odev3").stdin("371449635398431").stdout("AMEX\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def test3():
    """5555555555554444 MASTERCARD"""
    check50.run("./odev3").stdin("5555555555554444").stdout("MASTERCARD\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def test4():
    """5105105105105100 MASTERCARD"""
    check50.run("./odev3").stdin("5105105105105100").stdout("MASTERCARD\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def test5():
    """4111111111111111 VISA"""
    check50.run("./odev3").stdin("4111111111111111").stdout("VISA\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def test6():
    """4012888888881881 VISA"""
    check50.run("./odev3").stdin("4012888888881881").stdout("VISA\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def test7():
    """1234567890 GECERSIZ"""
    check50.run("./odev3").stdin("1234567890").stdout("GECERSIZ\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def test8():
    """369421438430814 GECERSIZ"""
    check50.run("./odev3").stdin("369421438430814").stdout("GECERSIZ\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def test9():
    """4062901840 GECERSIZ"""
    check50.run("./odev3").stdin("4062901840").stdout("GECERSIZ\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def test10():
    """5673598276138003 GECERSIZ"""
    check50.run("./odev3").stdin("5673598276138003").stdout("GECERSIZ\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def test11():
    """4111111111111113 GECERSIZ"""
    check50.run("./odev3").stdin("4111111111111113").stdout("GECERSIZ\n").stdout(check50.EOF).exit(0)
    
@check50.check(compiles)
def test00():
    """-5 -> Kart No: """
    check50.run("./odev3").stdin("-5").stdout("Kart No: ")
    

