import pytest
from CountUniqueNames import count_unique_names

def test_basic_name():
	assert count_unique_names("Deborah","Egli","Deborah","Egli","Deborah Egli") == 1

def test_nickname():
	assert count_unique_names("Deborah","Egli","Debbie","Egli","Debbie Egli") == 1

def test_typo():
	assert count_unique_names("Deborah","Egni","Deborah","Egli","Deborah Egli") == 1

@pytest.mark.xfail
def test_two_letter_typo():
	assert count_unique_names("Deborah","Engi","Deborah","Egli","Deborah Egli") == 1

@pytest.mark.xfail
def test_letter_swap_typo():
	assert count_unique_names("Deobrah","Egli","Deborah","Egli","Deborah Egli") == 1

@pytest.mark.xfail
def test_typo_nickname():
	assert count_unique_names("Debarah","Egli","Debbie","Egli","Debarah Egli") == 1

def test_typo_nickname_and_no_nickname():
	assert count_unique_names("Debarah","Egli","Debbie","Egli","Deborah Egli") == 1

def test_unused_middle_name():
	assert count_unique_names("Deborah S","Egli","Deborah","Egli","Egli Deborah") == 1

def test_reorder():
	assert count_unique_names("Deborah","Egli","Egli","Deborah","Deborah Egli") == 1

@pytest.mark.xfail
def test_reorder_used_middle_name():
	assert count_unique_names("Deborah","Egli","Michelle","Egli"," Egli Deborah Michelle") == 1

def test_reorder_typo():
	assert count_unique_names("Debarah","Elli","Egli","Deborah","Deborah Egli") == 1

def test_used_middle_name(): 
	assert count_unique_names("Michele","Egli","Deborah","Egli","Deborah Michele Egli") == 1

def test_different_ship_to_others():
	assert count_unique_names("Michele","Egli","Deborah","Egli","Michele Egli") == 2

def test_different_bill_to_others():
	assert count_unique_names("Deborah","Egli","Michele","Egli","Michele Egli") == 2

def test_different_card_to_others():
	assert count_unique_names("Michele","Egli","Michele","Egli","Deborah Egli") == 2

def test_all_different():
	assert count_unique_names("Michele","Egli","dave","Egli","Deborah Egli") == 3