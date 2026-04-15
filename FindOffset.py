from pwn import *

# Valore preso con GDB usando: x/gx $rsp dopo che il programma crasha
rip_value = 0x6161616161616166

offset = cyclic_find(rip_value, n = 8)

print("Offset:", offset)