import keypad
import usb_cdc


class Steno:
    def __init__(self, matrix, cols, rows):
        self.matrix = matrix
        self.keypad = keypad.KeyMatrix(rows, cols)
        self.width = len(cols)

    def run(self):
        report = bytearray(6)
        report[:] = b"\x80\x00\x00\x00\x00\x00"
        pressed_count = 0
        event = keypad.Event()
        while True:
            while self.keypad.events.get_into(event):
                y, x = divmod(event.key_number, self.width)
                key = self.matrix[y][x]
                if event.pressed:
                    byte, bit = divmod(key, 7)
                    report[byte] |= 1 << (6 - bit)
                    pressed_count += 1
                else:
                    pressed_count -= 1
                    if pressed_count == 0:
                        usb_cdc.data.write(report))
                        report[:] = b"\x80\x00\x00\x00\x00\x00"
