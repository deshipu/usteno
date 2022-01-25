import usb_cdc
import usb_hid
import storage
import board
import digitalio


row = digitalio.DigitalInOut(board.SCL)
col = digitalio.DigitalInOut(board.MOSI)
col.switch_to_output(value=1)
row.switch_to_input(pull=digitalio.Pull.DOWN)

if not row.value:
    storage.disable_usb_drive()
    usb_cdc.enable(console=False, data=True)
    pass
else:
    usb_cdc.enable(console=True, data=True)
    pass
usb_hid.disable()

row.deinit()
col.deinit()
