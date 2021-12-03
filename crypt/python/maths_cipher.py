def Encrypt(ATM_Pin, K):
    
    digit_pin =[]

    # add k to each digit of pin 
    for i in ATM_Pin:
        pin = int(i)+K
        digit_pin.append(pin)
    
    # swap first and third digit
    temp = digit_pin[0]
    digit_pin[0] = digit_pin[2]
    digit_pin[2] = temp

    # swap second and fourth digit
    temp = digit_pin[1]
    digit_pin[1] = digit_pin[3]
    digit_pin[3] = temp

    # return encrypted ATM pin
    return digit_pin

    
# function of decryption of encrypted ATM pin

def Decrypt(Enc_Pin,K):
    
    # Swap first and third digit
    temp = Enc_Pin[0] 
    Enc_Pin[0] = Enc_Pin[2]
    Enc_Pin[2] = temp

    #swap second and fourth digit
    temp = Enc_Pin[1]
    Enc_Pin[1] = Enc_Pin[3]
    Enc_Pin[3] = temp

    Decrypted_pin = []
    # Minus k from each digit
    for i in Enc_Pin:
        n = int(i)-K
        Decrypted_pin.append(n)

    # return decrypted ATM oin
    return Decrypted_pin



ATM_Pin = input("enter 4 digit ATM Pin:")
Key = int(input("enter key:"))

# Encryption of ATM pin
Encrypted_pin = Encrypt(ATM_Pin,Key)

print("ATM pin after Encryption:",*Encrypted_pin, sep="")

# Decryption of Encrypted ATM pin
Decrypted_pin = Decrypt(Encrypted_pin, Key)

print("ATM pin after decryption:",*Decrypted_pin, sep="")