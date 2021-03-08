#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Paul Multi Cipher
# Version 1
# Unpublished work © 2018 Paul Cooper
import os

#-------------------------------------------ENCRYPT CAESAR-------------------------------------------
def encryptCaesar(plain, key):
    lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    realkey = 3
    numofchar = 26
    if str(key).isdigit():
        realkey = key
    else:
        realkey = lower.index(key)


    cipher = []
    for ch in plain:
        if ch.islower():
            cipher.append(lower[(lower.index(ch) + realkey) % numofchar])
        elif ch.isupper():
            cipher.append(upper[(upper.index(ch) + realkey) % numofchar])
        elif ch == " ":
            cipher.append(" ")
            
    return "".join(cipher)


#-------------------------------------------DECRYPT CAESAR-------------------------------------------
def decryptCaesar(cipher, key):
    lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    realkey = 3
    numofchar = 26
    if str(key).isdigit():
        realkey = key
    else:
        realkey = lower.index(key)
    

    plain = []
    for ch in cipher:
        if ch.islower():
            plain.append(lower[(lower.index(ch) - realkey) % numofchar])
        if ch.isupper():
            plain.append(upper[(upper.index(ch) - realkey) % numofchar])
        if ch == " ":
            plain.append(" ")

    return "".join(plain)


#-------------------------------------------ENCRYPT SIMTRAN-------------------------------------------
def encryptSimtran(plain, key):
    blocksize = len(key)
    msglen = len(plain)
    if msglen % blocksize != 0:
        print("bad key!")
        return
    
    numblocks = msglen // blocksize
    cipher = []
    for b in range(numblocks):
        for i in range(blocksize):
            cipher.append(plain[b*blocksize + int(key[i])-1])

    return "".join(cipher)   



#-------------------------------------------DECRYPT SIMTRAN-------------------------------------------
def decryptSimtran(cipher, key):
    blocksize = len(key)
    msglen = len(cipher)
    if msglen % blocksize != 0:
        print("bad key!")
        return
    
    numblocks = msglen // blocksize
    pblk = ['0']*blocksize
    plain=[]
    for b in range(numblocks):
        for i in range(blocksize):
            pblk[int(key[i])-1]=cipher[b*blocksize + i]
        plain.extend(pblk)

    return "".join(plain)  




if __name__ == '__main__':

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#-------------------------------------------GETTING ALL TEXT FILES IN FOLDER-------------------------------------------    
    cwd = os.getcwd()
    for file in os.listdir(cwd):
        if file.endswith(".txt"):
            print(file[:-4] + "")
#------------------------------------------------------------------------------------------------------------------------------------------


#-------------------------------------------CHOOSING A FILE-------------------------------------------

#USER INPUT FOR FILE CHOISE-------------------------------------------
    selectedFile = input("\nChoose a file to encrypt or decrypt: ")

#EXCEPTION PREVENTER-------------------------------------------
    while True:
        if os.path.exists(selectedFile + ".txt"):
            f = open(selectedFile + ".txt", "r")
            strplain = f.read()
            f.close()
            break
        else:
            print("\nFile does not exist or the name was mistyped (do not forget the extention). Please try again: \n\n")
            selectedFile = input()
#-------------------------------------------------------------------------------

            
    print("\n\n" + strplain)
#---------------------------------------------------------------------------------------------------------------

    

#-------------------------------------------CHOOSING ENCRYPT/DECRYPT-------------------------------------------    

#ENCRYPT OR DECRYPT?-------------------------------------------
    encDec = input("\n\nDo you plan to (1) encrypt or (2) decrypt this file?: ")
    while True:
        if encDec != '1' and encDec != '2':
            print("Selection invalid. Please choose 1 or 2")
            encDec = input()
        else:
            break
#--------------------------------------------------------------------------------
        
#CAESAR OR SIMTRAN?-------------------------------------------
    cOrS = input("\n\nAnd do you plan to use (1) Caesar Cipher, or (2) Simtran Cipher?: ")
    while True:
        if cOrS != '1' and cOrS != '2':
            print("Selection invalid. Please choose 1 or 2")
            cOrS = input()
        else:
            break
#----------------------------------------------------------------------------
        
#-------------------------------------------------------------------------------------------------------------------------------------

        
    
#-------------------------------------------DECRYPTION OPTIONS-------------------------------------------
    if encDec == '2':
#DECRYPT SIMTRAN-------------------------------------------        
        if cOrS == '2':
            response = input("\nPlease enter the key: ")
            print("\nAttained inceptive missive: ", strplain)
            decplain = decryptSimtran(strplain, response)
            print("\n\nDecrypted text using " + response + " : ", decplain)
#-----------------------------------------------------------------------


#DECRYPT CAESAR-------------------------------------------
        if cOrS == '1':
            response = input("\nIf you know the key, enter it now, otherwise, say 'no': ")
            if response == 'No' or response == 'no':
                for x in alphabet:
                    print("\n\nDecrypted text using " + x + " : ", decryptCaesar(strplain, x))
                decplain = decryptCaesar(strplain, input("Please choose the correct decryption key: "))
                print("\n\n", decplain)
            else:
                decplain = decryptCaesar(strplain, response)
                print("\n\n", decplain)
#-----------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------------------



#-------------------------------------------ENCRYPTION OPTIONS-------------------------------------------
    if encDec == '1':
#ENCRYPT CAESAR-------------------------------------------
        if cOrS == '1':
            print("\nAttained inceptive missive: ", strplain)
            ciphertext = encryptCaesar(strplain, input("Please choose a key to encrypt with: "))
            print("\n\nProcured cryptogram: ", ciphertext)
#----------------------------------------------------------------------

#ENCRYPT SIMTRAN-------------------------------------------
        if cOrS == '2':
            print("\nAttained inceptive missive: ", strplain)
            ciphertext = encryptSimtran(strplain, input("Please choose a key to encrypt with: "))
            print("\n\nProcured cryptogram: ", ciphertext)
#----------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------



            

#-------------------------------------------SAVE/APPEND/EXIT OPTIONS-------------------------------------------
            
#SELECT OPTION-------------------------------------------
    fileMaker = input("""\n\nWould you like to...\n(1) Commit the encryption or decryption to a new file\n(2) Append the original file with the encryption or decryption\n(3) Just exit the program\n\n""")
#EXCEPTION PREVENTER
    while True:
        if fileMaker != '1' and fileMaker != '2' and fileMaker != '3':
            print("Selection invalid. Please choose 1, 2, or 3")
            fileMaker = input()
        else:
            break
#-------------------------------------------------------------------

#CREATE NEW FILE-------------------------------------------
        
#IF ENCRYPTOR USED
    if fileMaker == '1':
        if encDec == '1':
            fileWrite = open(input("Choose a file name: ") + ".txt", "w")
            print("\n\nData accessed for inscription")
            fileWrite.write(ciphertext)
            print("\nCryptogram inscribed")
            fileWrite.close()
            input("Press any key to exit . . .")
            exit()
#IF DECRYPTOR USED
        elif encDec == '2':
            fileWrite = open(input("Choose a file name: ") + ".txt", "w")
            print("\n\nData accessed for deciphering")
            fileWrite.write(decplain)
            print("\nDeciphered missive inscribed")
            fileWrite.close()
            input("Press any key to exit . . .")
            exit()
#----------------------------------------------------------------------


#APPEND CURRENT FILE-------------------------------------------

#IF ENCRYPTOR USED
    elif fileMaker == '2':
        if encDec == '1':
            fileWrite = open(selectedFile, "a")
            print("\n\nData accessed for inscription")
            fileWrite.write("\n\n" + ciphertext)
            print("\nCryptogram inscribed")
            fileWrite.close()
            input("Press any key to exit . . .")
            exit()
#IF DECRYPTOR USED
        elif encDec == '2':
            fileWrite = open(selectedFile, "a")
            print("\n\nData accessed for deciphering")
            fileWrite.write("\n\n" + decplain)
            print("\nDeciphered missive inscribed")
            fileWrite.close()
            input("Press any key to exit . . .")
            exit()
#------------------------------------------------------------------------------


#EXIT PROGRAM-------------------------------------------
    elif fileMaker == '3':
        exit()
#-----------------------------------------------------------------
