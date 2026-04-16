# ret2win - Buffer Overflow Exploit
Soluzione per l'esercizio ret2win di [ROPEmporium](https://ropemporium.com/)

## Obbiettivo
Sfruttare un buffer overflow per reindirizzare l'esecuzione dle programma verso la funzione "ret2win" ch stampa la flag

---

## 1. Calcolo offset
Per trovare il numero di byte necessari per raggiungere il return address sullo stack:
- Generato cyclic paattern di 100 byte con pwntools
- Mandato in input tramite GDB
- Quando il programma crasha il valore di RSP viene letto con "x/gx $rsp"
- Viene passato alla funzione "cyclic_find()" per calcolare l'offset preciso.

```bash
gdb ./ret2win
run <<< $(python3 -c "from pwn import *; import sys; sys.stdout.buffer.write(cyclic(100, =8))")
x/gx $rsp
```

Il risultato è un offset di 40 byte (32 byte del buffer e 8 byte RBP)

## 2. Allineamento staack
Su x86-64 lo stack, prima di chiamare funzioni come "printf" o "fopen", vaa allineaato a 16 byte. Per fare cio ho aggiunto un gadgeet "ret" prima dell'indirizzo di "ret2win"

---

## Esecuzione

###
```bash
pip install pwntools
```

## Calcola l'offset
```bash
python3 FindOffset.py
```

## Esecuzione exploit
```bash
python3 Exploit.py
```

