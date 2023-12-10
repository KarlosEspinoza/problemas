import check50

@check50.check()
def exists():
    """hola.py existe"""
    check50.exists("hola.py")

@check50.check(exists)
def emma():
    """responde correctamente"""
    check50.run("python3 hola.py").stdout("Hola, mundo!\nMinombre es Karlos\nNos vemos!").exit()

@check50.check(compiles)