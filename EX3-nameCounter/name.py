from word import Word

class Name(object):
	"""docstring for Name"""
	def __init__(self, first_name, middle_name, last_name, nickname_finder):
		super(Name, self).__init__()
		self.first_name = Word(first_name, nickname_finder)
		self.middle_name = Word(middle_name, nickname_finder)
		self.last_name = Word(last_name, nickname_finder)

	@classmethod
	def from_first_and_last(cls, first_and_middle, last, nickname_finder):
		try:
			first, middle = first_and_middle.split(" ", 1)
		except ValueError:
			first = first_and_middle
			middle = ""
		return cls(first, middle, last, nickname_finder)

	@classmethod
	def from_str(cls, name_str, nickname_finder):
		first_and_middle, last = name_str.rsplit(" ", 1)
		return cls.from_first_and_last(first_and_middle, last, nickname_finder)
		
	def _compare_first(self, other):
		return self.first_name == other.first_name or self.first_name == other.middle_name or self.middle_name == other.first_name

	def _compare_last(self, other):
		return self.last_name == other.last_name

	def _standart_compare(self, other):
		 return self._compare_first(other) and self._compare_last(other)

	def _shuffled_compare(self, other):
		if self.last_name in (other.first_name, other.middle_name) and \
		other.last_name in (self.first_name, self.middle_name):
			return True
		return False

	def __eq__(self, other):
		return self._standart_compare(other) or self._shuffled_compare(other)