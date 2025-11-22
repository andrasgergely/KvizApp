import random


def AA_betolt_kerdesek():
    return [
        {"kerdes": "Melyik ország nyerte az első labdarúgó-világbajnokságot 1930-ban?",
         "valaszok": ["Brazília", "Uruguay", "Olaszország"], "jo": 1},
        {"kerdes": "Melyik klubhoz kötődik leginkább Lionel Messi?",
         "valaszok": ["Real Madrid", "Barcelona", "Manchester City"], "jo": 1},
        {"kerdes": "Melyik csapat nyerte a 2016-os Európa-bajnokságot?",
         "valaszok": ["Portugália", "Franciaország", "Németország"], "jo": 0},
        {"kerdes": "Melyik ország rendezte a 2018-as világbajnokságot?",
         "valaszok": ["Oroszország", "Németország", "Brazília"], "jo": 0},
        {"kerdes": "Melyik csapat nyerte a BL-t 2005-ben Isztambulban?",
         "valaszok": ["Liverpool", "AC Milan", "Barcelona"], "jo": 0},
        {"kerdes": "Melyik válogatott beceneve az 'Azzurri'?",
         "valaszok": ["Olaszország", "Argentína", "Franciaország"], "jo": 0},
        {"kerdes": "Cristiano Ronaldo melyik PL csapatban játszott?",
         "valaszok": ["Manchester United", "Liverpool", "Arsenal"], "jo": 0},
        {"kerdes": "Milyen poszton játszik Manuel Neuer?",
         "valaszok": ["Csatár", "Kapus", "Védő"], "jo": 1},
        {"kerdes": "Ki nyerte a 2014-es VB-t?",
         "valaszok": ["Argentína", "Németország", "Spanyolország"], "jo": 1},
        {"kerdes": "Hol játszik a Barcelona hazai pályán?",
         "valaszok": ["Camp Nou", "Bernabéu", "Wanda"], "jo": 0},
        {"kerdes": "Ki volt az Aranycsapat csatára?",
         "valaszok": ["Puskás Ferenc", "Dzsudzsák Balázs", "Albert Flórián"], "jo": 0},
        {"kerdes": "Melyik válogatott beceneve a 'Seleção'?",
         "valaszok": ["Brazília", "Spanyolország", "Portugália"], "jo": 0},
        {"kerdes": "Ki nyerte a BL-t 2021-ben?",
         "valaszok": ["Chelsea", "Manchester City", "PSG"], "jo": 0},
        {"kerdes": "Sergio Ramos posztja:",
         "valaszok": ["Középpályás", "Védő", "Csatár"], "jo": 1},
        {"kerdes": "Hol rendezték a 2006-os VB-t?",
         "valaszok": ["Németország", "Dél-Afrika", "Japán"], "jo": 0},
        {"kerdes": "Melyik csapat a 'Vörös Ördögök'?",
         "valaszok": ["Liverpool", "Manchester United", "Bayern"], "jo": 1},
        {"kerdes": "Haaland melyik csapatnál robbant be?",
         "valaszok": ["Dortmund", "Ajax", "Napoli"], "jo": 0},
        {"kerdes": "Hány perc a rendes játékidő?",
         "valaszok": ["80", "90", "100"], "jo": 1},
        {"kerdes": "Hány perc egy félidő?",
         "valaszok": ["45", "40", "50"], "jo": 0},
        {"kerdes": "Mikor van tizenegyespárbaj?",
         "valaszok": ["Sok gól után", "Döntetlennél", "Barátságoson"], "jo": 1},
        {"kerdes": "Melyik ország meze narancssárga?",
         "valaszok": ["Hollandia", "Belgium", "Horvátország"], "jo": 0},
        {"kerdes": "Melyik lap jelzi a kiállítást?",
         "valaszok": ["Sárga", "Piros", "Zöld"], "jo": 1},
        {"kerdes": "Ki kapta az Aranylabdát 2009-ben?",
         "valaszok": ["Messi", "Ronaldo", "Kaká"], "jo": 0},
        {"kerdes": "Zidane melyik csapatban játszott?",
         "valaszok": ["Juventus", "PSG", "Milan"], "jo": 0},
        {"kerdes": "Ki nyerte a 2010-es VB-t?",
         "valaszok": ["Spanyolország", "Hollandia", "Brazília"], "jo": 0},
        {"kerdes": "Hol játszik a Liverpool?",
         "valaszok": ["Anfield", "Etihad", "Old Trafford"], "jo": 0},
        {"kerdes": "Maracanã stadion melyik országban?",
         "valaszok": ["Argentina", "Brazília", "Chile"], "jo": 1},
        {"kerdes": "Ki volt kapitány 2016-ban?",
         "valaszok": ["Dárdai", "Storck", "Rossi"], "jo": 1},
        {"kerdes": "Bayern München városa:",
         "valaszok": ["Berlin", "München", "Frankfurt"], "jo": 1},
        {"kerdes": "Melyik klub nyert 3 BL-t zsinórban (2016–18)?",
         "valaszok": ["Real Madrid", "Barcelona", "Juve"], "jo": 0},
        {"kerdes": "Ki 'El Fenómeno'?",
         "valaszok": ["Cristiano Ronaldo", "Ronaldo Nazário", "Ronaldinho"], "jo": 1},
        {"kerdes": "La Albiceleste melyik válogatott?",
         "valaszok": ["Argentína", "Spanyolország", "Chile"], "jo": 0},
        {"kerdes": "Parc des Princes stadion kié?",
         "valaszok": ["PSG", "Barca", "Atléti"], "jo": 0},
        {"kerdes": "Ki nyerte a 2021-ben rendezett Eb-t?",
         "valaszok": ["Olaszország", "Anglia", "Portugália"], "jo": 0},
        {"kerdes": "Totti melyik csapat legendája?",
         "valaszok": ["Inter", "Roma", "Lazio"], "jo": 1},
        {"kerdes": "Atlético melyik város?",
         "valaszok": ["Madrid", "Sevilla", "Valencia"], "jo": 0},
        {"kerdes": "Modrić melyik országból jön?",
         "valaszok": ["Horvátország", "Szerbia", "Szlovénia"], "jo": 0},
        {"kerdes": "Hány pont jár egy győzelemért?",
         "valaszok": ["2", "3", "4"], "jo": 1},
        {"kerdes": "Wolves melyik csapat beceneve?",
         "valaszok": ["Wolverhampton", "Leicester", "Leeds"], "jo": 0},
        {"kerdes": "CR melyik csapatban kezdte?",
         "valaszok": ["Sporting CP", "Porto", "Benfica"], "jo": 0},
        {"kerdes": "U21 Eb-t melyik évben rendezte Magyarország?",
         "valaszok": ["2021", "2016", "2012"], "jo": 0},
        {"kerdes": "Maldini melyik csapat ikonja?",
         "valaszok": ["AC Milan", "Inter", "Juve"], "jo": 0},
        {"kerdes": "Ki nyerte a legtöbb VB-t?",
         "valaszok": ["Brazília", "Németország", "Olaszország"], "jo": 0},
        {"kerdes": "Rossoneri melyik klub?",
         "valaszok": ["AC Milan", "Bologna", "Roma"], "jo": 0},
        {"kerdes": "Signal Iduna Park kié?",
         "valaszok": ["Dortmund", "Bayern", "Leipzig"], "jo": 0},
        {"kerdes": "Pirlo melyik csapatban játszott a Juve előtt?",
         "valaszok": ["AC Milan", "Roma", "Inter"], "jo": 0},
        {"kerdes": "Mi az El Clásico?",
         "valaszok": ["Real–Barca", "Milan–Inter", "PSG–Lyon"], "jo": 0},
        {"kerdes": "Serie A melyik ország?",
         "valaszok": ["Olaszország", "Spanyolország", "Franciaország"], "jo": 0},
        {"kerdes": "Melyik klub angol?",
         "valaszok": ["Tottenham", "Real Sociedad", "Fiorentina"], "jo": 0},
    ]


class AA_Kviz:
    def __init__(self, kerdesek, kerdes_db=10):
        self.minden = kerdesek
        self.db = kerdes_db
        self.uj()

    def uj(self):
        self.kivalasztott = random.sample(self.minden, self.db)
        self.index = 0
        self.helyesek = 0

    def aktualis(self):
        if self.index >= self.db:
            return None
        q = self.kivalasztott[self.index]
        return q["kerdes"], q["valaszok"]

    def valasz(self, idx):
        q = self.kivalasztott[self.index]
        helyes = (idx == q["jo"])
        if helyes:
            self.helyesek += 1
        self.index += 1
        return helyes

    def vege(self):
        return self.index >= self.db

    def eredmeny(self):
        szaz = round(self.helyesek / self.db * 100)
        if szaz == 100:
            txt = "Tökéletes!"
        elif szaz >= 80:
            txt = "Nagyon jó!"
        elif szaz >= 50:
            txt = "Közepes teljesítmény."
        else:
            txt = "Gyenge eredmény."
        return self.helyesek, self.db, szaz, txt
