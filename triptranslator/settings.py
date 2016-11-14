TRANSPORT_REQUIRED_DATA = {
    'plane': ['transport_seat', 'transport_gate', 'transport_number'],
    'bus': ['transport_number'],
    'train': ['transport_seat', 'transport_number'],
}

TRANSPORT_OPTIONAL_DATA = {
    'plane': ['transport_baggage_number']
}

PLACE_BAGGAGE_DROP_MESSAGE = u'Baggage drop at ticket counter {}.'
PLACE_BAGGAGE_AUTO_MESSAGE = u'Baggage will we automatically transferred from your last leg.'

TRANSPORT_BAGGAGE_MESSAGES = {
    'plane': lambda bc: PLACE_BAGGAGE_DROP_MESSAGE.format(bc.transport_baggage_number) if bc.transport_baggage_number else PLACE_BAGGAGE_AUTO_MESSAGE
}

TRANSPORT_READABLE_MESSAGES = {
    'plane': u'From {bc.start}, take flight {bc.transport_number} to {bc.end}. Gate {bc.transport_gate}, seat {bc.transport_seat}. {bc.baggage_optional_message}',
    'bus': u'Take the {bc.transport_number} bus from {bc.start} to {bc.end}. No seat assignment.',
    'train': u'Take train {bc.transport_number} from {bc.start} to {bc.end}. Sit in seat {bc.transport_seat}.',
    'unknown': u'Get from {bc.start} to {bc.end}.'
}

TRIP_FINISH_MESSAGE = u'You have arrived at your final destination.'
