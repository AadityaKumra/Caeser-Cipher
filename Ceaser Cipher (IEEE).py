n=input("Type code to be decrypted:")
s=int(input("Shift:"))

def CC(n,s):
    result=""
    for i in range(len(n)):
               ch=n[i]
               if (ch.isupper()):
                   result+=chr((ord(ch)+(26-s-65))%26+65)
               else:
                   result+=chr((ord(ch)+(26-s-97))%26+97)
    return result
print(CC(n,s))

                

