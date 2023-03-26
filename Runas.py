class RUNA_ALA_RESISTENCIA_AGUA():
    def __init__(self, resto):
        self.CANT = 1
        self.SIGNO = True
        self.NAME = "ALA_RESISTENCIA_AGUA"
        self.STAT_IMG = "img/ala_resis_agua.png"
        self.RESTO = resto


class RUNA_ALA_RESISTENCIA_FUEGO():
    def __init__(self, resto):
        self.CANT = 1
        self.SIGNO = True
        self.NAME = "ALA_RESISTENCIA_FUEGO"
        self.STAT_IMG = "img/ala_resis_fuego.png"
        self.RESTO = resto


class RUNA_ALA_RESISTENCIA_NEUTRAL():
    def __init__(self, resto):
        self.CANT = 1
        self.SIGNO = True
        self.NAME = "ALA_RESISTENCIA_NEUTRAL"
        self.STAT_IMG = "img/ala_resis_fuego.png"  # Tiene imagen erronea
        self.RESTO = resto


class RUNA_ALA_RESISTENCIA_TIERRA():
    def __init__(self, resto):
        self.CANT = 1
        self.SIGNO = True
        self.NAME = "ALA_RESISTENCIA_TIERRA"
        self.STAT_IMG = "img/ala_resis_tierra.png"
        self.RESTO = resto


class RUNA_ALCANCE():
    def __init__(self, resto):
        self.CANT = 1
        self.SIGNO = True
        self.NAME = "ALCANCE"
        self.STAT_IMG = "img/alcance.png"
        self.RESTO = resto


class RUNA_AUMENTO_DANIO():
    def __init__(self, resto):
        self.CANT = 1
        self.SIGNO = False
        self.NAME = "AUMENTO_DANIO"
        self.STAT_IMG = "img/aumento_danio.png"
        self.RESTO = resto


class RUNA_CRITICO():
    def __init__(self, resto):
        self.CANT = 1
        self.SIGNO = True
        self.NAME = "CRITICO"
        self.STAT_IMG = "img/critico.png"
        self.RESTO = resto


class RUNA_CURA():
    def __init__(self, resto):
        self.CANT = 1
        self.SIGNO = True
        self.NAME = "CURA"
        self.STAT_IMG = "img/cura.png"
        self.RESTO = resto


class RUNA_DANIO():
    def __init__(self, resto):
        self.CANT = 1
        self.SIGNO = True
        self.NAME = "DANIO"
        self.STAT_IMG = "img/danio.png"
        self.RESTO = resto


class RUNA_FUERZA():
    def __init__(self, resto):
        self.CANT = 3
        self.SIGNO = True
        self.NAME = "FUERZA"
        self.STAT_IMG = "img/fuerza.png"
        self.RESTO = resto


class RUNA_INICIATIVA():
    def __init__(self, resto):
        self.CANT = 30
        self.SIGNO = True
        self.NAME = "INICIATIVA"
        self.STAT_IMG = "img/iniciativa.png"
        self.RESTO = resto


class RUNA_INTELIGENCIA():
    def __init__(self, resto):
        self.CANT = 3
        self.SIGNO = True
        self.NAME = "INTELIGENCIA"
        self.STAT_IMG = "img/inte.png"
        self.RESTO = resto


class RUNA_INVOCACION():
    def __init__(self, resto):
        self.CANT = 1
        self.SIGNO = True
        self.NAME = "INVOCACION"
        self.STAT_IMG = "img/invo.png"
        self.RESTO = resto


class RUNA_PM():
    def __init__(self, resto):
        self.CANT = 1
        self.SIGNO = True
        self.NAME = "PM"
        self.STAT_IMG = "img/pm.png"
        self.RESTO = resto


class RUNA_PP_ROJA():
    def __init__(self, resto):
        self.CANT = 3
        self.SIGNO = True
        self.NAME = "PP_ROJA"
        self.STAT_IMG = "img/pp_roja.png"
        self.RESTO = resto


class RUNA_PP():
    def __init__(self, resto):
        self.CANT = 1
        self.SIGNO = True
        self.NAME = "PP"
        self.STAT_IMG = "img/pp.png"
        self.RESTO = resto


class RUNA_RESIS_NEUTRAL():
    def __init__(self, resto):
        self.CANT = 1
        self.SIGNO = False
        self.NAME = "RESIS_NEUTRAL"
        self.STAT_IMG = "img/resis_neutral.png"
        self.RESTO = resto


class RUNA_RESIS_TIERRA():
    def __init__(self, resto):
        self.CANT = 1
        self.SIGNO = False
        self.NAME = "RESIS_TIERRA"
        self.STAT_IMG = "img/resis_tierra.png"
        self.RESTO = resto


class RUNA_SABIDURIA():
    def __init__(self, resto):
        self.CANT = 3
        self.SIGNO = True
        self.NAME = "SABIDURIA"
        self.STAT_IMG = "img/sabi.png"
        self.RESTO = resto


class RUNA_SUERTE():
    def __init__(self, resto):
        self.CANT = 3
        self.SIGNO = True
        self.NAME = "SUERTE"
        self.STAT_IMG = "img/suerte.png"
        self.RESTO = resto


class RUNA_VITALIDAD():
    def __init__(self, resto):
        self.CANT = 10
        self.SIGNO = True
        self.NAME = "VITALIDAD"
        self.STAT_IMG = "img/vita.png"
        self.RESTO = resto
