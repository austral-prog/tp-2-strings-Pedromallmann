def check_vowels():
    """Lee un nombre y verifica si contiene cada una de las vocales (a, e, i, o, u),
    sin distinguir mayúsculas de minúsculas.
    """
    pass

    nombre = input("Ingrese la nombre: ")

    vocal_a = "a" in nombre.lower()
    vocal_e = "e" in nombre.lower()
    vocal_i = "i" in nombre.lower()
    vocal_o = "o" in nombre.lower()
    vocal_u = "u" in nombre.lower()

    print (f"Contiene a: {vocal_a}")
    print (f"Contiene e: {vocal_e}")
    print (f"Contiene i: {vocal_i}")
    print (f"Contiene o: {vocal_o}")
    print (f"Contiene u: {vocal_u}")
check_vowels()
