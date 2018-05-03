import sys

usage = "pyhton imput_qemu.py <string>"

if len(sys.argv) < 2:
	print(usage)
	sys.exit(1)

output = open('command_qemu', 'w')
commandline = sys.argv[1]

characters = "0123456789abcdefghijklmnopqrstuvwxyz \\\n"
qemu_value = [ "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", \
				"c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", \
				"o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", \
				"space", "backslash", "kp_enter" ]

#Sortie standard rediriger dans fichier
sys.stdout = output
for c in commandline:
	try:
		characters.index(c)
	except Exception as e:
		sys.stdout = sys.__stdout__
		print("characteres non valide:" + c)
		sys.exit(1)
	else:
		print("sendkey " + qemu_value[characters.index(c)] + "\n")
#Retablir la sortie standard par default
sys.stdout = sys.__stdout__