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
def test00():
    """-5 -> Kart No: """
    check50.run("./odev3").stdin("-5").stdout("Kart No: ").stdin("9").stdout("GECERSIZ\n").stdout(check50.EOF).exit(0)
