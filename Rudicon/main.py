version = '0.1'


class TokenTypes():
    def MathTypes(text) -> dict:
        TToken =\
            {
                '-': 'MINUS',
                '+': 'PLUS',
                '*': 'MULTI',
                '/': 'DIV',
                '.': 'SEP',
                '_': 'FLOOR',
                '(': 'LPARENT',
                ')': 'RPARENT',
            }
        return TToken


class Token():
    def __init__(self, _type, value=None) -> None:
        self.type = _type
        self.value = value

    def __repr__(self) -> str:
        return f'Token [{self.type}]: {self.value}'\
            if self.value is not None else f'Token [{self.type}]'


class Parser():
    def __init__(self) -> None:
        self._text = ''
        self._pos = -1
        self._currentChar = self.advance()

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        self._text = text
        self._pos = -1
        self._currentChar = None
        self.advance()

    def advance(self) -> None:
        self._pos += 1
        self._currentChar = self._text[self._pos] if self._pos < len(self._text) else None

    def __repr__(self) -> str:
        return f'Rudicon Parser Version: {version}. Let Hynek be with you'

    def Parse(self):
        ttype = TokenTypes()
        mtypes = ttype.MathTypes()
        tokens = []
        while self._currentChar is not None:
            if self._currentChar in ' \t':
                self.advance()
                continue
            elif self._currentChar in mtypes.keys():
                tokens.append(Token(mtypes[self._currentChar]))
            self.advance()
        return tokens


if __name__ == '__main__':
    lex = Parser()
    while True:
        # text = input("Rudicon> ")
        text = 'wtf ( abs ] * - 2'
        lex.text = text
        print(lex.Parse())
