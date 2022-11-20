alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(len(alphabet))

should_end = False
while not should_end:
    text = input("enter your message: ").lower()
    text = list(text)
    shift = int(input("enter the shift: "))

    if shift > len(alphabet):
        shift = shift % len(alphabet)
    elif shift < -len(alphabet):
        shift = shift % -len(alphabet)










































