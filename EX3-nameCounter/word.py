class Word(object):
	"""docstring for Word"""
	def __init__(self, word, nickname_finder):
		super(Word, self).__init__()
		self.word = word.lower()
		self.nickname_finder = nickname_finder

	def _check_for_nick(self, other):
		nicks = self.nickname_finder.get(self.word)

		return nicks and other.word in nicks

	def _check_for_typo(self, other):
		if len(self.word) != len(other.word):
			return False
		
		failed = False

		for i in xrange(len(self.word)):
			if self.word[i] != other.word[i]:
				if failed:
					return False
				else:
					failed = True
		return True

	def __eq__(self, other):
		return self.word == other.word or self._check_for_nick(other) or self._check_for_typo(other)
