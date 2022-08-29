import keyboard
import pyfiglet

ascii_banner = pyfiglet.figlet_format("Anya \n Nuhaet BEBRU")
print (ascii_banner)

keys = keyboard.record(until = 'ENTER')
keyboard.play(keys)

# need find how output in file