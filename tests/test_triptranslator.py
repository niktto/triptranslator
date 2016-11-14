#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_triptranslator
----------------------------------

Tests for `triptranslator` module.
"""

import unittest

from triptranslator import triptranslator



class TestTriptranslator(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_bad_start(self):
        def create_bad_bc():
            triptranslator.BoardingCard(
                start=None,
                end=u"Szczecin Glowny",
                transport_type='train',
                transport_seat='225',
                transport_number=u'Kopernik',
            )

        self.assertRaises(ValueError, create_bad_bc)

    def test_bad_end(self):
        def create_bad_bc():
            triptranslator.BoardingCard(
                start=u"Szczecin Glowny",
                end='',
                transport_type='train',
                transport_seat='225',
                transport_number=u'Kopernik',
            )

        self.assertRaises(ValueError, create_bad_bc)

    def test_simple_trip(self):
        random_boarding_passes = [
            triptranslator.BoardingCard(
                start=u"Warszawa Wschodnia",
                end=u"Szczecin Glowny",
                transport_type='train',
                transport_seat='225',
                transport_number=u'Kopernik',
            ),
            triptranslator.BoardingCard(
                start=u"Otwock",
                end=u"Warszawa Dworzec Gdanski",
                transport_type='train',
                transport_seat='16',
                transport_number='S1',
            ),
            triptranslator.BoardingCard(
                start=u"Warszawa Dworzec Wilenski",
                end=u"Warszawa Wschodnia",
                transport_type='metro',
                transport_number='M1',
            ),
            triptranslator.BoardingCard(
                start=u"Warszawa Dworzec Gdanski",
                end=u"Warszawa Dworzec Wilenski",
                transport_type='bus',
                transport_number='145',
            ),
        ]

        valid_messages = [
            u'Take train S1 from Otwock to Warszawa Dworzec Gdanski. Sit in seat 16.',
            u'Take the 145 bus from Warszawa Dworzec Gdanski to Warszawa Dworzec Wilenski. No seat assignment.',
            u'Get from Warszawa Dworzec Wilenski to Warszawa Wschodnia.',
            u'Take train Kopernik from Warszawa Wschodnia to Szczecin Glowny. Sit in seat 225.',
            u'You have arrived at your final destination.'
        ]
        assert triptranslator.translate_boarding_cards(random_boarding_passes) == valid_messages

    def test_split_trip(self):
        random_boarding_passes = [
            triptranslator.BoardingCard(
                start=u"Warszawa Wschodnia",
                end=u"Szczecin Glowny",
                transport_type='train',
                transport_seat='225',
                transport_number=u'Kopernik',
            ),
            triptranslator.BoardingCard(
                start=u"Otwock",
                end=u"Warszawa Dworzec Gdanski",
                transport_type='train',
                transport_seat='16',
                transport_number='S1',
            ),
            triptranslator.BoardingCard(
                start=u"Warszawa Dworzec Wilenski",
                end=u"Warszawa Wschodnia",
                transport_type='metro',
                transport_number='M1',
            ),
            triptranslator.BoardingCard(
                start=u"Warszawa Dworzec Pocztowy",
                end=u"Warszawa Dworzec Wilenski",
                transport_type='bus',
                transport_number='145',
            ),
        ]


        def generate_trip():
            return triptranslator.translate_boarding_cards(random_boarding_passes)

        self.assertRaises(ValueError, generate_trip)

    def test_split_end_trip(self):
        random_boarding_passes = [
            triptranslator.BoardingCard(
                start=u"Warszawa Wschodnia",
                end=u"Szczecin Glowny",
                transport_type='train',
                transport_seat='225',
                transport_number=u'Kopernik',
            ),
            triptranslator.BoardingCard(
                start=u"Warszawa Dworzec Wilenski",
                end=u"Warszawa Dworzec Gdanski",
                transport_type='train',
                transport_seat='16',
                transport_number='S1',
            ),
            triptranslator.BoardingCard(
                start=u"Warszawa Dworzec Wilenski",
                end=u"Warszawa Wschodnia",
                transport_type='metro',
                transport_number='M1',
            ),
            triptranslator.BoardingCard(
                start=u"Warszawa Dworzec Pocztowy",
                end=u"Warszawa Dworzec Wilenski",
                transport_type='bus',
                transport_number='145',
            ),
        ]


        def generate_trip():
            return triptranslator.translate_boarding_cards(random_boarding_passes)

        self.assertRaises(ValueError, generate_trip)

    def test_complex_trip(self):
        random_boarding_passes = [
            triptranslator.BoardingCard(
                start=u"Warszawa Wschodnia",
                end=u"Szczecin Glowny",
                transport_type='train',
                transport_seat='225',
                transport_number=u'Kopernik',
            ),
            triptranslator.BoardingCard(
                start=u"Otwock",
                end=u"Warszawa Dworzec Gdanski",
                transport_type='train',
                transport_seat='16',
                transport_number='S1',
            ),
            triptranslator.BoardingCard(
                start=u"Warszawa Dworzec Wilenski",
                end=u"Warszawa Wschodnia",
                transport_type='metro',
                transport_number='M1',
            ),
            triptranslator.BoardingCard(
                start=u"Warszawa Dworzec Gdanski",
                end=u"Warszawa Dworzec Wilenski",
                transport_type='bus',
                transport_number='145',
            ),
            triptranslator.BoardingCard(
                start=u"Szczecin Goleniow",
                end=u"Berlin",
                transport_type='plane',
                transport_seat='3112',
                transport_number='PF3455',
                transport_gate='H3L'
            ),
            triptranslator.BoardingCard(
                start=u"Szczecin Glowny",
                end=u"Szczecin Goleniow",
                transport_type='bus',
                transport_number=u'airport',
            ),
            triptranslator.BoardingCard(
                start=u"Berlin",
                end=u"Maroko",
                transport_type='plane',
                transport_seat='112',
                transport_number='K332',
                transport_gate='H3L',
                transport_baggage_number='18',
            ),
        ]

        valid_messages = [
            u'Take train S1 from Otwock to Warszawa Dworzec Gdanski. Sit in seat 16.',
            u'Take the 145 bus from Warszawa Dworzec Gdanski to Warszawa Dworzec Wilenski. No seat assignment.',
            u'Get from Warszawa Dworzec Wilenski to Warszawa Wschodnia.',
            u'Take train Kopernik from Warszawa Wschodnia to Szczecin Glowny. Sit in seat 225.',
            u'Take the airport bus from Szczecin Glowny to Szczecin Goleniow. No seat assignment.',
            u'From Szczecin Goleniow, take flight PF3455 to Berlin. Gate H3L, seat 3112. Baggage will we automatically transferred from your last leg.',
            u'From Berlin, take flight K332 to Maroko. Gate H3L, seat 112. Baggage drop at ticket counter 18.',
            u'You have arrived at your final destination.',
        ]
        self.assertEqual(triptranslator.translate_boarding_cards(random_boarding_passes), valid_messages)
