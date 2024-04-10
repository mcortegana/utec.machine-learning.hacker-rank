received_n1 = input()
received_n2 = input()

n1 = int(received_n1)
n2 = int(received_n2)

if 0 <= n1 <= 20 and 0 <= n2 <= 20:
    missingNote = 45 - (n1 + n2)
    print(missingNote)
