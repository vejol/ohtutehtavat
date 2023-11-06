import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )
    
    def test_search_loytaa_pelaajan(self):
        pelaaja = self.stats.search('Semenko')

        self.assertEqual(pelaaja.name, 'Semenko')
    
    def test_search_palauttaa_tyhjan_jos_pelaajaa_ei_ole(self):
        pelaaja = self.stats.search('Sauli Niinistö')

        self.assertEqual(pelaaja, None)

    def test_team_palauttaa_listan_joukkueen_pelaajista(self):
        pelaajat = self.stats.team('EDM')
        nimet = list(map(lambda p: p.name, pelaajat))

        self.assertTrue(len(nimet), 3)
        self.assertTrue('Semenko' in nimet)
        self.assertTrue('Kurri' in nimet)
        self.assertTrue('Gretzky' in nimet)

    def test_top_palauttaa_oikeat_pelaajat_pisteiden_perusteella(self):
        top2 = self.stats.top(1)
        top2_nimet = list(map(lambda p: p.name, top2))

        self.assertTrue(len(top2_nimet) == 2)
        self.assertTrue('Gretzky' in top2_nimet)
        self.assertTrue('Lemieux' in top2_nimet)

    def test_top_palauttaa_oikeat_pelaajat_maalien_perusteella(self):
        top2 = self.stats.top(1, SortBy.GOALS)
        top2_nimet = list(map(lambda p: p.name, top2))

        self.assertTrue(len(top2_nimet) == 2)
        self.assertTrue('Lemieux' in top2_nimet)
        self.assertTrue('Yzerman' in top2_nimet)

    def test_top_palauttaa_oikeat_pelaajat_syottojen_perusteella(self):
        top2 = self.stats.top(1, SortBy.ASSISTS)
        top2_nimet = list(map(lambda p: p.name, top2))

        self.assertTrue(len(top2_nimet) == 2)
        self.assertTrue('Gretzky' in top2_nimet)
        self.assertTrue('Yzerman' in top2_nimet)