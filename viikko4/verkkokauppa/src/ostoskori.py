class Ostoskori:
    def __init__(self):
        self._tuotteet = []
    
    def lisaa(self, tuote):
        self._tuotteet.append(tuote)
    
    def poista(self, tuote):
        if tuote in self._tuotteet:
            self._tuotteet.remove(tuote)

    def hinta(self):
        hinnat = map(lambda t: t.hinta, self._tuotteet)

        return sum(hinnat)
