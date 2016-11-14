# trip translator

Python library for translating boarding passes into human readable directions.


* Free software: MIT license


## Installation

Package requires `python2.7` with no additional dependencies.

```
$ git clone https://github.com/niktto/triptranslator.git
$ cd triptranslator
$ python setup.py test
```

## Assumptions

* set of boarding cards represents one trip (has one start and one end)
* trip does no "loop" (for example goes to same station twice)
* not all boarding passes need to be used

## Usage

```
from triptranslator import BoardingCard, translate_boarding_cards


stop_a = triptranslator.BoardingCard(
    start=u"Warszawa Wschodnia",
    end=u"Szczecin Glowny",
    transport_type='train',
    transport_seat='225',
    transport_number=u'Kopernik',
)
stop_b = triptranslator.BoardingCard(
    start=u"Otwock",
    end=u"Warszawa Dworzec Gdanski",
    transport_type='train',
    transport_seat='16',
    transport_number='S1',
)
stop_c = triptranslator.BoardingCard(
    start=u"Warszawa Dworzec Wilenski",
    end=u"Warszawa Wschodnia",
    transport_type='metro',
    transport_number='M1',
)
stop_d = triptranslator.BoardingCard(
    start=u"Warszawa Dworzec Gdanski",
    end=u"Warszawa Dworzec Wilenski",
    transport_type='bus',
    transport_number='145',
)

translate_boarding_cards([stop_a, stop_b, stop_c, stop_d])
```
