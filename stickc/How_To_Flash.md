Flash the M5StickC
==================

Create simplified firmware
--------------------------
The default firmware is very bloated, as it is made for programming
using the online tools at flow.m5stack.com. We therefore need to
create a version of the MicroPython firmware without all the bloat.
   
1. Install a fresh UIFlow image using M5Burner on the M5StickC
2. Terminate the running program (picocom)
3. Use AMPY to delete all files on the M5StickC
4. Transfer the simplified boot.py (from this dir) using AMPY
5. Transfer whatever other necessary libraries
6. Run the following command to read the entire memory to the
   file "appmod_all.bin":

esptool.py --chip esp32 --port /dev/tty.usbserial-5D52F19645 --baud 750000 --before default_reset --after hard_reset read_flash 0x0000 4194304 appmod_all.bin


Flash image to other devices
----------------------------
The appmod_all.bin image created above, now just needs to be flashed
to any other devices needing that firmware:

esptool.py --chip esp32 --port /dev/tty.usbserial-* --baud 750000 --before default_reset --after hard_reset write_flash --flash_mode dio --flash_freq 80m --flash_size detect 0x0000 appmod_all.bin
