# -*- coding: utf-8 -*-

from .settings import (
    TRANSPORT_REQUIRED_DATA,
    TRANSPORT_OPTIONAL_DATA,
    TRANSPORT_READABLE_MESSAGES,
    TRANSPORT_BAGGAGE_MESSAGES,
    TRIP_FINISH_MESSAGE,
)


class BoardingCard(object):

    """Simple class representing boarding card"""

    #: Start location name (eg: 'Berlin Train Station')
    start = None

    #: End location name (eg: 'Chopin Airport')
    end = None

    #: Name of transport type (eg: 'plane', 'bus' etc.)
    transport_type = None

    def __init__(self, start, end, transport_type, **kwargs):
        """Create boarding pass.

        :param start: Start location name (eg: 'Berlin Train Station')
        :param end: End location name (eg: 'Chopin Airport')
        :param transport_type: Name of transport type. Not defined types are
            handled as unknowns.

        Accepts optional keyword arguments that depend on transport type.

        """

        # Required values validation
        if not start:
            raise ValueError(u'Boarding Card starting point must be defined!')
        self.start = start

        if not end:
            raise ValueError(u'Boarding Card ending point must be defined!')
        self.end = end

        if not transport_type:
            raise ValueError(u'Boarding Card transport type must be defined!')
        self.transport_type = transport_type

        # Assigning dynamic, required data that depends on transport_type
        for additional_arg_name in TRANSPORT_REQUIRED_DATA.get(self.transport_type, []):
            if additional_arg_name not in kwargs:
                raise ValueError(
                    (
                        u'For "{}" transport type '
                        u'{} must be additionally defined'
                    ).format(self.transport_type, additional_arg_name)
                )
            setattr(self, additional_arg_name, kwargs[additional_arg_name])

        # Assigning dynamic, optional data that depends on transport_type
        for additional_arg_name in TRANSPORT_OPTIONAL_DATA.get(self.transport_type, []):
            setattr(self, additional_arg_name, kwargs.get(additional_arg_name))

    @staticmethod
    def create_key_from_string(input_string):
        """Create standardized, lowercase key from string.

        :param input_string: string that need to be standardized.

        :return: standardized string.

        """
        return input_string.lower().replace(' ', '')

    @property
    def start_key(self):
        """Get standardized start location name.

        :return: standardized string.

        """
        return self.create_key_from_string(self.start)

    @property
    def end_key(self):
        """Get standardized end location name.

        :return: standardized string.

        """
        return self.create_key_from_string(self.end)

    @property
    def transport_key(self):
        """Get standardized transport type or key for unknown type.

        :return: standardized string.

        """
        return self.transport_type if self.transport_type in TRANSPORT_READABLE_MESSAGES else 'unknown'

    @property
    def human_readable_message(self):
        """Get human readable message based on boarding card.

        :return: readable string.

        """
        return TRANSPORT_READABLE_MESSAGES[self.transport_key].format(bc=self)

    @property
    def baggage_optional_message(self):
        """Get human readable message based only on baggage related actions.

        :return: readable string.

        """
        return TRANSPORT_BAGGAGE_MESSAGES[self.transport_key](bc=self)


def translate_boarding_cards(boarding_cards):
    """Translate list of BoardingCards to readable travel instructions.

    This function sorts list of random BoardingCard objects connecting starts
    with ends of every stage of the trip then returns readable instructions
    that include seat numbers, location names and additional data.

    :param boarding_cards: list of :class:`BoardingCard` objects.
    :return: list of human readable string that describe the whole trip.

    """

    # Creating helper maps, one is keyed based on start locations, second one
    # is keyed on end locations
    starts_map = {
        boarding_card.start_key: boarding_card for boarding_card
        in boarding_cards
    }
    ends_map = {
        boarding_card.end_key: boarding_card for boarding_card
        in boarding_cards
    }

    # Guessing start and end of the trip
    trip_start_keys = [
        start_key for start_key in starts_map
        if start_key not in ends_map
    ]
    trip_end_keys = [
        end_key for end_key in ends_map
        if end_key not in starts_map
    ]

    # Validating our guess of start and end of the trip
    if len(trip_start_keys) > 1:
        raise ValueError(u'More than 1 starting point in the trip!')

    if not trip_start_keys:
        raise ValueError(u'No starting point in the trip!')

    if len(trip_end_keys) > 1:
        raise ValueError(u'More than 1 ending point in the trip!')

    if not trip_end_keys:
        raise ValueError(u'No ending point in the trip!')

    trip_start_key = trip_start_keys[0]
    trip_end_key = trip_end_keys[0]

    # Connecting boarding cards into ordered trip list
    trip = [starts_map[trip_start_key]]
    current_stop_index = 0
    trip_reached_end = False

    while not trip_reached_end:
        last_stop = trip[current_stop_index]

        if last_stop.end_key == trip_end_key:
            trip_reached_end = True
        else:
            trip.append(starts_map[last_stop.end_key])
            current_stop_index += 1

    # building human readable messages from every stop of the trip
    directions = [
        boarding_card.human_readable_message for boarding_card in trip
    ]

    if TRIP_FINISH_MESSAGE:
        directions.append(TRIP_FINISH_MESSAGE)

    return directions
