from colored import fg, bg, attr
from random import randint
import regex as re
from typing import Union


class WrongInputType(Exception):
    def __init__(self, error, message='Incorrect data met') -> None:
        self.error = error
        self.message = message
        super().__init__(self.message)

    def __str__(self) -> str:
        return f'{self.error} : {self.message}'


class Colors():
    """
    Class made to handle simple work with colors.

    Offers:
        converting common names to colors in RGB, HEX.

        converting between HEX and RGB.

        displaying colored text in terminal.

        checking if RGB or HEX color is correct.
    """
    def __init__(self):
        self.__BaseColors = {
            "maroon":  ((128, 0, 0), "#800000"),
            "dark red":  ((139, 0, 0), "#8B0000"),
            "brown":  ((165, 42, 42), "#A52A2A"),
            "firebrick": ((178, 34, 34), "#B22222"),
            "crimson": ((220, 20, 60), "#DC143C"),
            "red": ((255, 0, 0), "#FF0000"),
            "tomato": ((255, 99, 71), "#FF6347"),
            "coral": ((255, 127, 80), "#FF7F50"),
            "indian red": ((205, 92, 92), "#CD5C5C"),
            "light coral": ((240, 128, 128), "#F08080"),
            "dark salmon": ((233, 150, 122), "#E9967A"),
            "salmon": ((250, 128, 114), "#FA8072"),
            "light salmon": ((255, 160, 122), "#FFA07A"),
            "orange red": ((255, 69, 0), "#FF4500"),
            "dark orange": ((255, 140, 0), "#FF8C00"),
            "orange": ((255, 165, 0), "#FFA500"),
            "gold": ((255, 215, 0), "#FFD700"),
            "dark golden rod": ((184, 134, 11), "#B8860B"),
            "golden rod": ((218, 165, 32), "#DAA520"),
            "pale golden rod": ((238, 232, 170), "#EEE8AA"),
            "dark khaki": ((189, 183, 107), "#BDB76B"),
            "khaki": ((240, 230, 140), "#F0E68C"),
            "olive": ((128, 128, 0), "#808000"),
            "yellow": ((255, 255, 0), "#FFFF00"),
            "yellow green": ((154, 205, 50), "#9ACD32"),
            "dark olive green": ((85, 107, 47), "#556B2F"),
            "olive drab": ((107, 142, 35), "#6B8E23"),
            "lawn green": ((124, 252, 0), "#7CFC00"),
            "chart reuse": ((127, 255, 0), "#7FFF00"),
            "green yellow": ((173, 255, 47), "#ADFF2F"),
            "dark green": ((0, 100, 0), "#006400"),
            "green": ((0, 128, 0), "#008000"),
            "forest green": ((34, 139, 34), "#228B22"),
            "lime": ((0, 255, 0), "#00FF00"),
            "lime green": ((50, 205, 50), "#32CD32"),
            "light green": ((144, 238, 144), "#90EE90"),
            "pale green": ((152, 251, 152), "#98FB98"),
            "dark sea green": ((143, 188, 143), "#8FBC8F"),
            "medium spring green": ((0, 250, 154), "#00FA9A"),
            "spring green": ((0, 255, 127), "#00FF7F"),
            "sea green": ((46, 139, 87), "#2E8B57"),
            "medium aqua marine": ((102, 205, 170), "#66CDAA"),
            "medium sea green": ((60, 179, 113), "#3CB371"),
            "light sea green": ((32, 178, 170), "#20B2AA"),
            "dark slate gray": ((47, 79, 79), "#2F4F4F"),
            "teal": ((0, 128, 128), "#008080"),
            "dark cyan": ((0, 139, 139), "#008B8B"),
            "aqua": ((0, 255, 255), "#00FFFF"),
            "cyan": ((0, 255, 255), "#00FFFF"),
            "light cyan": ((224, 255, 255), "#E0FFFF"),
            "dark turquoise": ((0, 206, 209), "#00CED1"),
            "turquoise": ((64, 224, 208), "#40E0D0"),
            "medium turquoise": ((72, 209, 204), "#48D1CC"),
            "pale turquoise": ((175, 238, 238), "#AFEEEE"),
            "aqua marine": ((127, 255, 212), "#7FFFD4"),
            "powder blue": ((176, 224, 230), "#B0E0E6"),
            "cadet blue": ((95, 158, 160), "#5F9EA0"),
            "steel blue": ((70, 130, 180), "#4682B4"),
            "corn flower blue": ((100, 149, 237), "#6495ED"),
            "deep sky blue": ((0, 191, 255), "#00BFFF"),
            "dodger blue": ((30, 144, 255), "#1E90FF"),
            "light blue": ((173, 216, 230), "#ADD8E6"),
            "sky blue": ((135, 206, 235), "#87CEEB"),
            "light sky blue": ((135, 206, 250), "#87CEFA"),
            "midnight blue": ((25, 25, 112), "#191970"),
            "navy": ((0, 0, 128), "#000080"),
            "dark blue": ((0, 0, 139), "#00008B"),
            "medium blue": ((0, 0, 205), "#0000CD"),
            "blue": ((0, 0, 255), "#0000FF"),
            "royal blue": ((65, 105, 225), "#4169E1"),
            "blue violet": ((138, 43, 226), "#8A2BE2"),
            "indigo": ((75, 0, 130), "#4B0082"),
            "dark slate blue": ((72, 61, 139), "#483D8B"),
            "slate blue": ((106, 90, 205), "#6A5ACD"),
            "medium slate blue": ((123, 104, 238), "#7B68EE"),
            "medium purple": ((147, 112, 219), "#9370DB"),
            "dark magenta": ((139, 0, 139), "#8B008B"),
            "dark violet": ((148, 0, 211), "#9400D3"),
            "dark orchid": ((153, 50, 204), "#9932CC"),
            "medium orchid": ((186, 85, 211), "#BA55D3"),
            "purple": ((128, 0, 128), "#800080"),
            "thistle": ((216, 191, 216), "#D8BFD8"),
            "plum": ((221, 160, 221), "#DDA0DD"),
            "violet": ((238, 130, 238), "#EE82EE"),
            "magenta": ((255, 0, 255), "#FF00FF"),
            "orchid": ((218, 112, 214), "#DA70D6"),
            "medium violet red": ((199, 21, 133), "#C71585"),
            "pale violet red": ((219, 112, 147), "#DB7093"),
            "deep pink": ((255, 20, 147), "#FF1493"),
            "hot pink": ((255, 105, 180), "#FF69B4"),
            "light pink": ((255, 182, 193), "#FFB6C1"),
            "pink": ((255, 192, 203), "#FFC0CB"),
            "antique white": ((250, 235, 215), "#FAEBD7"),
            "beige": ((245, 245, 220), "#F5F5DC"),
            "bisque": ((255, 228, 196), "#FFE4C4"),
            "blanched almond": ((255, 235, 205), "#FFEBCD"),
            "wheat": ((245, 222, 179), "#F5DEB3"),
            "corn silk": ((255, 248, 220), "#FFF8DC"),
            "lemon chiffon": ((255, 250, 205), "#FFFACD"),
            "light golden rod yellow": ((250, 250, 210), "#FAFAD2"),
            "light yellow": ((255, 255, 224), "#FFFFE0"),
            "saddle brown": ((139, 69, 19), "#8B4513"),
            "sienna": ((160, 82, 45), "#A0522D"),
            "chocolate": ((210, 105, 30), "#D2691E"),
            "peru": ((205, 133, 63), "#CD853F"),
            "sandy brown": ((244, 164, 96), "#F4A460"),
            "burly wood": ((222, 184, 135), "#DEB887"),
            "tan": ((210, 180, 140), "#D2B48C"),
            "rosy brown": ((188, 143, 143), "#BC8F8F"),
            "moccasin": ((255, 228, 181), "#FFE4B5"),
            "navajo white": ((255, 222, 173), "#FFDEAD"),
            "peach puff": ((255, 218, 185), "#FFDAB9"),
            "misty rose": ((255, 228, 225), "#FFE4E1"),
            "lavender blush": ((255, 240, 245), "#FFF0F5"),
            "linen": ((250, 240, 230), "#FAF0E6"),
            "old lace": ((253, 245, 230), "#FDF5E6"),
            "papaya whip": ((255, 239, 213), "#FFEFD5"),
            "sea shell": ((255, 245, 238), "#FFF5EE"),
            "mint cream": ((245, 255, 250), "#F5FFFA"),
            "slate gray": ((112, 128, 144), "#708090"),
            "light slate gray": ((119, 136, 153), "#778899"),
            "light steel blue": ((176, 196, 222), "#B0C4DE"),
            "lavender": ((230, 230, 250), "#E6E6FA"),
            "floral white": ((255, 250, 240), "#FFFAF0"),
            "alice blue": ((240, 248, 255), "#F0F8FF"),
            "ghost white": ((248, 248, 255), "#F8F8FF"),
            "honeydew": ((240, 255, 240), "#F0FFF0"),
            "ivory": ((255, 255, 240), "#FFFFF0"),
            "azure": ((240, 255, 255), "#F0FFFF"),
            "snow": ((255, 250, 250), "#FFFAFA"),
            "black": ((0, 0, 0), "#000000"),
            "dim gray": ((105, 105, 105), "#696969"),
            "gray": ((128, 128, 128), "#808080"),
            "dark gray": ((169, 169, 169), "#A9A9A9"),
            "silver": ((192, 192, 192), "#C0C0C0"),
            "light gray": ((211, 211, 211), "#D3D3D3"),
            "gainsboro": ((220, 220, 220), "#DCDCDC"),
            "white smoke": ((245, 245, 245), "#F5F5F5"),
            "white": ((255, 255, 255), "#FFFFFF")
        }

    def GetColor(self, name: str, rgb: bool = True) -> Union[str, 'tuple[int, int, int]']:
        """Returns value of color based on `rgb=`.
        If True returns RGB else HEX.

        Args:
            name (str) - Name of color.
            
            rgb (bool) - Defines if color is returned as RGB. Default is True.
        Returns:
            str | None | tuple(int, int, int) : Value of provided color.
        Note:
            Returns `None` if color is not in dictionary.

        Example:
        >>> Class.GetColor('blue', rgb=True)
        (0, 0, 255)
        >>> Class.GetColor('orange', rgb=False)
        '#FFA500'
        """
        ans = self.__BaseColors.get(name)
        if ans is None:
            raise ValueError(f"Color '{name}' is not in list")
        if ans:
            return ans[0] if rgb else ans[1]

    @staticmethod
    def __IsCorrectType(color: Union[str, 'tuple[int, int, int]'], _type: str) -> bool:
        """Checks if provided color is correct type. For RGB `tuple | list` and RGB `str`.

        Args:
            color (str | tuple(int, int, int)): Color to check.
            _type (str): 'RGB' or 'HEX'

        Raises:
            WrongInputType: if _type is other than RGB and HEX.

        Returns:
            bool: True if color matches type
        Note:
            It's simple type check, that doesn't check data validity.
            For this exists `IsFullyCorrect`.
        """
        if _type.upper() == 'RGB':
            if not isinstance(color, (list, tuple)):
                return False
            return True
        elif _type.upper() == 'HEX':
            if not isinstance(color, str):
                return False
            return True
        raise WrongInputType(_type, 'Type could not match to HEX|RGB')

    @staticmethod
    def __IsCorrectFormat(color: Union[str, 'tuple[int, int, int]']) -> bool:
        """
        Checks if provided color is correct format.
        If Color has `len = 3` and `range(0, 255)` and `all(int)` or matches `Regex HEX`.

        Args:
            color (str | tuple(int, int, int)): Color to check.

        Returns:
            bool: True if format of data belongs to HEX or RGB
        Note:
            It only checks if correct format.
        """
        if not isinstance(color, (list, tuple, str)):
            return False
        if color is None or len(color) == 0:
            return False
        if isinstance(color, (list, tuple)):
            if len(color) != 3:
                return False
            if not all(type(var) == int for var in color):
                return False
            if max(color) > 255 or min(color) < 0:
                return False
            return True
        hexa = r'^#[0-9a-fA-F]{6}$'
        if not re.match(hexa, color):
            return False
        return True

    @staticmethod
    def IsFullyCorrect(color: Union[str, 'tuple[int, int, int]'], _type: str) -> bool:
        """Returns True if provided color matches to `_type` and is correct format.

        Args:
            color (str | tuple(int, int, int)): Color to check.
            _type (str): 'RGB' or 'HEX'

        Returns:
            bool: True if it's fully correct.
        Example:
        >>> Class.IsFullyCorrect((220, 18, 127), 'RGB')
        True
        >>> Class.IsFullyCorrect((-12, 260, 12), 'RGB')
        False
        >>> Class.IsFullyCorrect('#aabbcc', 'HEX')
        True
        >>> Class.IsFullyCorrect('#ggaaaa', 'HEX')
        False
        """
        if not Colors.__IsCorrectType(color, _type):
            return False
        if not Colors.__IsCorrectFormat(color):
            return False
        return True

    def ColoredText(self,
                    text: str,
                    text_color: Union[str, 'tuple[int, int, int]'] = 'Random',
                    background_color: Union[str, 'tuple[int, int, int]'] = None,
                    debug: bool = False) -> str:
        """Returns text after color formatting. It's possible to choose text color and text background.

        Args:
            text (str): Text to display.
            text_color (str | tuple(int, int, int): Color to display text. Defaults to 'Random'.
            background_color (str | tuple(int, int, int), optional):Color of text background. Defaults to None.
            debug (bool, optional): Decides if debug display is on. Defaults to False.

        Raises:
            WrongInputType: If `text_color` is wrong format.
            WrongInputType: If `background_color` is wrong format.

        Returns:
            str: Text with color formatting.
        """
        if text_color == 'Random':
            text_color = Colors.RandomColor()

        if not Colors.__IsCorrectFormat(text_color):
            raise WrongInputType(text_color, 'Could not match to any color')
        if not Colors.__IsCorrectFormat(background_color) and background_color is not None:
            raise WrongInputType(background_color, 'Could not match to any color')

        elif Colors.__IsCorrectType(text_color, 'RGB'):
            text_color = Colors.ToHex(text_color)

        if Colors.__IsCorrectType(background_color, 'RGB'):
            background_color = Colors.ToHex(background_color)

        if debug:
            return f'Foreground : {text_color.upper()} | Text : {text} | Background : {str(background_color).upper()}'

        if background_color:
            return fg(text_color) + bg(background_color) + text + attr('reset')
        return fg(text_color) + text + attr('reset')

    @staticmethod
    def ToHex(color: Union['list[int]', 'tuple[int, int, int]']) -> str:
        """Converts Color from list or tuple to HEX format.

        Args:
            color (list[int, int, int] | tuple(int, int, int)): Color to convert.

        Raises:
            WrongInputType: If provided color is not correct type or format.

        Returns:
            str: Color as HEX format
        Example:
        >>> Class.ToHex((255, 0, 0))
        '#FF0000'
        >>> Class.ToHex((255, 255, 255))
        '#FFFFFF'
        """
        if not Colors.IsFullyCorrect(color, 'RGB'):
            raise WrongInputType(color, 'Color not matching HEX standard')
        return '#%02x%02x%02x'.upper() % (color[0], color[1], color[2])

    @staticmethod
    def ToRGB(_hex: str) -> 'tuple[int, int, int]':
        """Converts Color from str to tuple.

        Args:
            _hex (str): Color in HEX format.

        Raises:
            WrongInputType: If provided color is not correct type or format.

        Returns:
            tuple[int, int, int]: Color as RGB format.
        Example:
        >>> Class.ToRGB('#ff0000')
        (255, 0, 0)
        >>> Class.ToRGB('#FFFFFF')
        (255, 255, 255)
        """
        if not Colors.IsFullyCorrect(_hex, 'HEX'):
            raise WrongInputType(
                _hex, message='Field outside of range |0123456789ABCDEF|')
        _hex = _hex.lstrip('#').upper()
        return tuple(int(_hex[i:i + 2], 16) for i in (0, 2, 4))

    @staticmethod
    def RandomColor(rgb: bool = True) -> Union[str, 'tuple[int, int, int]']:
        """Returns random color in RGB or HEX format based on `rgb=`.

        Returns:
            str | tuple(int, int, int): Color in specified format.
        """
        color = (randint(0, 255), randint(0, 255), randint(0, 255))
        return color if rgb else Colors.ToHex(color)

    def __repr__(self) -> str:
        return 'Custom class to return Color values for assigned words'

    def __str__(self) -> str:
        """Returns whole dictionary with background representing colors.

        Returns:
            str: Whole dictionary.
        """
        full_string = ''
        reset = attr('reset')
        for name, value in zip(self.__BaseColors.keys(), self.__BaseColors.values()):
            str_color = fg('#FFFFFF') + bg(value[1])\
                if sum(value[0]) / len(value[0]) < 160 else fg('#000000') + bg(value[1])
            full_string += (
                f'{str_color}{name} : rgb{value[0]}, {value[1]}{reset}\n')
        return full_string

    def __iter__(self):
        """Returns everything as tuples with (key, value).

        Returns:
            tuple(str, tuple(tuple, str)): Tuple with keys and values from dict.
        """
        return ((k, v) for k, v in zip(self.__BaseColors.keys(), self.__BaseColors.values()))

    def __len__(self) -> int:
        return len(self.__BaseColors)


if __name__ == '__main__':
    c = Colors()
    print(c.ColoredText('testujemy',
                        text_color=c.GetColor('powder blue', rgb=False),
                        background_color=c.GetColor('blue violet', rgb=False)))
    print(len(c))
    print(c)
    print(repr(c))
