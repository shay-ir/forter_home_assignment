from pythonParser import NameDenormalizer
from name import Name

def count_unique_names(bill_first_name, bill_last_name, ship_first_name, 
	ship_last_name, bill_name_on_card):
	nickname_finder = NameDenormalizer(r"D:\developnemt\UniqueNameCounter\names.csv")

	bill_name = Name.from_first_and_last(bill_first_name, bill_last_name, nickname_finder)
	ship_name = Name.from_first_and_last(ship_first_name, ship_last_name, nickname_finder)
	card_name = Name.from_str(bill_name_on_card, nickname_finder)
	
	bill_to_ship = bill_name == ship_name
	ship_to_card = ship_name == card_name
	bill_to_card = bill_name == card_name

	if bill_to_ship:
		if ship_to_card or bill_to_card:
			return 1
		else:
			return 2
	if ship_to_card:
		if bill_to_card:
			return 1
		else:
			return 2
	if bill_to_card:
		return 2
	return 3