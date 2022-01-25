import board
import usteno
from micropython import const


ROWS = (board.SCL, board.AREF, board.D6, board.A4)
COLS = (board.MOSI, board.SCK, board.A0, board.MISO, board.A3, board.A5,
        board.TX, board.A2, board.A6, board.A1)


_FN = const(0)
_N1 = const(1)
_N2 = const(2)
_N3 = const(3)
_N4 = const(4)
_N5 = const(5)
_N6 = const(6)

_S1 = const(7)
_S2 = const(8)
_TX = const(9)
_KX = const(10)
_PX = const(11)
_WX = const(12)
_HX = const(13)

_RX = const(14)
_AX = const(15)
_OX = const(16)
_X1 = const(17)
_X2 = const(18)
_R1 = const(19)
_R2 = const(20)

_PW = const(21)
_X3 = const(22)
_X4 = const(23)
_XE = const(24)
_XU = const(25)
_XF = const(26)
_XR = const(27)

_XP = const(28)
_XB = const(29)
_XL = const(30)
_XG = const(31)
_XT = const(32)
_XS = const(33)
_XD = const(34)

_N7 = const(35)
_N8 = const(36)
_N9 = const(37)
_NA = const(38)
_NB = const(39)
_NC = const(40)
_XZ = const(41)


MATRIX = (
    (_N1, _N2,   0, _N3,     0,   _N4,   0, _N8, _N9, _NA),
    (_S1, _TX, _PX, _HX,   _X1,   _XF, _XP, _XL, _XT, _XD),
    (_S2, _KX, _WX, _RX,   _X2,   _XR, _XB, _XG, _XS, _XZ),
    (  0,   0, _AX, _OX,     0,   _XE, _XU,   0,   0,   0),
)


usteno.Steno(MATRIX, COLS, ROWS).run()
