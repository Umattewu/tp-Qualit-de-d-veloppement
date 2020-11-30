def test_conversion_chiffre():
    import main.main as m
    assert m.convertion("0") == 0
    assert m.convertion("I") == 1
    assert m.convertion("V") == 5
    assert m.convertion("L") == 50
    assert m.convertion("C") == 100
    assert m.convertion("D") == 500
    assert m.convertion("M") == 1000

def test_afficher_nombre():
    import main.main as m
    assert m.afficher_nombre("MMVI") == 2006
    assert m.afficher_nombre("IV") == 4
    assert m.afficher_nombre("MCMXLIV") == 1944
    assert m.afficher_nombre("III") == 3


def test_somme():
    import main.main as m
    assert m.somme('+',"III","MCMXLIV") == 1947

def test_soustraction():
    import main.main as m
    assert m.soustraction('-',"III","MCMXLIV") == 1941
    assert m.soustraction('-',"MCMXLIV","III") == 1941

def test_multiplication():
    import main.main as m
    assert m.multiplication('*',"XII","XIV") == 168

def test_division():
    import main.main as m
    assert m.division('/',"IV","II") == 2
    assert m.division('/', "IV", "0") == "Erreur"
