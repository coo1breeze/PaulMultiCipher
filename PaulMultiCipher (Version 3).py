#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Paul's Multi-Cipher
# Version 3
# Unpublished work © 2018 Paul Cooper
import os
import re
import collections

#-------------------------------------------ENCRYPT CAESAR-------------------------------------------
def encryptCaesar(plain, key):
    lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numeric = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    realkey = 3
    numofchar = 26
    numofnum = 10
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
        elif ch.isdigit():
            cipher.append(numeric[(numeric.index(ch) + realkey) % numofnum])    
        elif ch == " ":
            cipher.append(" ")
            
    return "".join(cipher)


#-------------------------------------------DECRYPT CAESAR-------------------------------------------
def decryptCaesar(cipher, key):
    lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numeric = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    realkey = 3
    numofchar = 26
    numofnum = 10
    if str(key).isdigit():
        realkey = key
    else:
        realkey = lower.index(key)
    

    plain = []
    for ch in cipher:
        if ch.islower():
            plain.append(lower[(lower.index(ch) - realkey) % numofchar])
        elif ch.isupper():
            plain.append(upper[(upper.index(ch) - realkey) % numofchar])
        elif ch.isdigit():
            plain.append(numeric[(numeric.index(ch) - realkey) % numofnum])    
        elif ch == " ":
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


#-------------------------------------------ENCRYPT MODB-------------------------------------------
def encryptModb(plain, key):
    xlen = len(plain)
    if(xlen !=  len(key)):
        print("message length should equal key length")
        print("message length: ", str(len(plain)))
        print("key length: ", str(len(key)))
        return
    cipher = bytearray(b'0'*xlen)
    i=0
    pairs = zip(plain, key)
    for p,k in pairs:
        cipher[i] = int((p+k) % 256) #.to_bytes(1,byteorder='little')
        i = i+1
    return bytes(cipher)  


#-------------------------------------------DECRYPT MODB-------------------------------------------
def decryptModb(cipher, key):
    xlen = len(cipher)
    if(xlen !=  len(key)):
        print("ciphertext length should equal key length")
        print("message length: ", str(len(cipher)))
        print("key length: ", str(len(key)))
        return
    
    plain = bytearray(b'0'*xlen)
    i=0
    pairs = zip(cipher, key)
    for c,k in pairs:
        plain[i] = int((c-k) % 256) #.to_bytes(1,byteorder='little')
        i = i+1
    return bytes(plain) 


#-------------------------------------------ENCRYPT XORB-------------------------------------------
def encryptXorb(plain, key):
    xlen = len(plain)
    if(xlen !=  len(key)):
        print("message length should equal key length")
        print("message length: ", str(len(plain)))
        print("key length: ", str(len(key)))
        return
        
    cipher = bytearray(b'0'*xlen)
    i=0
    pairs = zip(plain, key)
    for p,k in pairs:
        cipher[i] = int(p ^ k) #.to_bytes(1,byteorder='little')
        i = i+1
    return bytes(cipher)


#-------------------------------------------DECRYPT XORB-------------------------------------------
def decryptXorb(cipher, key):
    xlen = len(cipher)
    if(xlen !=  len(key)):
        print("ciphertext length should equal key length")
        print("message length: ", str(len(cipher)))
        print("key length: ", str(len(key)))
        return
    
    plain = bytearray(b'0'*xlen)
    i=0
    pairs = zip(cipher, key)
    for c,k in pairs:
        plain[i] = int(c ^ k) #.to_bytes(1,byteorder='little')
        i = i+1
    return bytes(plain)



if __name__ == '__main__':
    print("#################")
    print("# Paul's Multi-Cipher")
    print("#################\n")
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#-------------------------------------------GETTING ALL FILES IN FOLDER-------------------------------------------
    print(" _____________________________________")
    print("| Encryptable/Decryptable files in local folder|")
    print(" ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
    cwd = os.getcwd()
    x = 1
    fileList = []
    print(" \n¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
    for file in os.listdir(cwd):
        if file.endswith(".txt") or file.endswith(".bmp"): #or file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png") or file.endswith(".tif") or file.endswith(".gif"):
            print(str(x) + ") " + file + "")
            fileList.append(str(file))
            x += 1
    print("\n ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
#------------------------------------------------------------------------------------------------------------------------------------------


#-------------------------------------------CHOOSING A FILE-------------------------------------------

#USER INPUT FOR FILE CHOICE-------------------------------------------
    preselect = int(input("\nChoose a file to encrypt or decrypt: ")) - 1
    while True:
        if preselect < 0 or preselect > len(fileList):
            preselect = int(input("The number you have chosen does not exist. Try again: ")) - 1
        else:
            break
    selectedFile, fileExtention = os.path.splitext(fileList[preselect])

#EXCEPTION PREVENTER-------------------------------------------
    while True:
        if os.path.exists(selectedFile + fileExtention):

            
            if fileExtention == ".txt":
                try:
                    with open(selectedFile + fileExtention, "r") as f:
                        strplain = f.read()
                        print("\n[Plain] Text '" + selectedFile + "' selected!\n")
                        print("########")
                        print("#              #")
                        print("#     " +  fileExtention[1:] + "     #")
                        print("#              #")
                        print("########")
                except:
                    with open(selectedFile + fileExtention, "rb") as f:
                        strplain = f.read()
                        print("\n[Bytes] Text '" + selectedFile + "' selected!\n")
                        print("########")
                        print("#              #")
                        print("#     " +  fileExtention[1:] + "    #")
                        print("#              #")
                        print("########")
                txtOrImg = '1'
                print("\nSample of file: \n" + str(strplain[:50]) + " . . .")
                break
            
            elif fileExtention == ".bmp":
                txtOrImg = '2'
                break
            else:
                print("\nFile does not exist or the name was mistyped (do not forget the extention). Please try again: \n\n")
                selectedFile, fileExtention = os.path.splitext(input())

                
        else:
            print("\nFile does not exist or the name was mistyped (do not forget the extention). Please try again: \n\n")
            selectedFile, fileExtention = os.path.splitext(input())
#-------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------------

    if txtOrImg == '2':
            theBytes = os.path.getsize(selectedFile + fileExtention)
            with open((selectedFile + fileExtention), "rb") as f:
                strplain = f.read()
            print("\nImage '" + selectedFile + "' selected!\n")
            print("########")
            print("#              #")
            print("#   " +  fileExtention[1:] + "   #")
            print("#              #")
            print("########")
            fileNoHead = strplain[54:]
            headerOfFile = strplain[:54]
            print("\nImage Header Data (size|" + str(len(headerOfFile)) + "):\n", headerOfFile, "\n")
            print("\nSample of Body Data (size|" + str(len(fileNoHead)) + "):\n", fileNoHead[:54], "\n")

#-------------------------------------------CHOOSING ENCRYPT/DECRYPT-------------------------------------------    

#ENCRYPT OR DECRYPT?-------------------------------------------
    encDec = input("\n\nDo you plan to (1) encrypt or (2) decrypt this file?: ")
    while True:
        if encDec != '1' and encDec != '2':
            print("\nSelection invalid. Please choose 1 or 2\n")
            encDec = input()
        else:
            break
#--------------------------------------------------------------------------------
        
#CAESAR, SIMTRAN, MODB, XORB OR ANALYSES?-------------------------------------------
    if encDec == '1':
        csmx = input("\n\nAnd do you plan to use. . .  \n(1) Caesar \n(2) Simtran \n(3) Modb \n(4) Xorb Cipher\n\n")

        while True:
            if csmx != '1' and csmx != '2' and csmx != '3' and csmx != '4':
                print("\nSelection invalid. Please choose again\n")
                csmx = input()
            elif csmx != '3' and csmx != '4' and txtOrImg == '2':
                print("\nThat cannot be used for an image file. Please choose again\n")
                csmx = input()
            else:
                break

            
    elif encDec == '2':
        csmx = input("\n\nAnd do you plan to use. . .  \n(1) Caesar \n(2) Simtran \n(3) Modb \n(4) Xorb Cipher \n(5) Frequency Analysis\n\n")

        while True:
            if csmx != '1' and csmx != '2' and csmx != '3' and csmx != '4' and csmx != '5':
                print("\nSelection invalid. Please choose again\n")
                csmx = input()
            elif csmx != '3' and csmx != '4' and txtOrImg == '2':
                print("\nThat cannot be used for an image file. Please choose again\n")
                csmx = input()
            else:
                break
#----------------------------------------------------------------------------
        
#-------------------------------------------------------------------------------------------------------------------------------------

        
    
#-------------------------------------------DECRYPTION OPTIONS-------------------------------------------
    if encDec == '2':
#DECRYPT SIMTRAN-------------------------------------------        
        if csmx == '2':
            response = input("\nPlease enter the key: ")
            print("\nAttained inceptive missive: ", strplain)
            decplain = decryptSimtran(strplain, response)
            print("\n\nDecrypted text using " + response + " : ", decplain)
#-----------------------------------------------------------------------


#DECRYPT CAESAR-------------------------------------------
        if csmx == '1':
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

#DECRYPT MODB-------------------------------------------
        if csmx == '3':
            cwd = os.getcwd()
            for file in os.listdir(cwd):
                 if file.endswith(".txt"):
                     print(file[:-4] + "")
            theBytes = os.path.getsize(selectedFile + fileExtention)
            
            with open((selectedFile + fileExtention), "rb") as f:
                txtBytesData = f.read()
                txtBytesSize = len(txtBytesData)
                fileNoHead = strplain[54:]
                headerOfFile = strplain[:54]

            keyFile = (input("Choose a text file key to decrypt the image: ") + ".txt")
            
            with open(keyFile, "rb") as key:
                 if txtOrImg == '1':
                     decplain = decryptModb(txtBytesData, key.read())
                     newPic = decplain
                     newFileName = input("Choose a new text file name: ")
                     
                 elif txtOrImg == '2':
                     decplain = decryptModb(fileNoHead, key.read())
                     newPic = headerOfFile+decplain
                     newFileName = input("Choose a new picture name: ")

            if txtOrImg == '1':
                
                while True:
                    if newFileName == selectedFile + fileExtention:
                        print("You cannot choose the same file name as the file you are encrypting")
                        newFileName = input("Please select a new file name: ")
                    else:
                        break
                                    
                                
            if txtOrImg == '1':
                with open(newFileName + fileExtention, "w") as picMaker:
                    picMaker.write(str(newPic))
                    print("\nDecrypted text file created\n")
            elif txtOrImg == '2':
                with open(newFileName + fileExtention, "wb") as picMaker:
                    picMaker.write(newPic)
                    print("\nDecrypted picture created\n")
            
            input("Press any key to exit . . .")
            exit()
#-------------------------------------------

#DECRYPT XORB-------------------------------------------
        if csmx == '4':
            cwd = os.getcwd()
            for file in os.listdir(cwd):
                 if file.endswith(".txt"):
                     print(file[:-4] + "")
            theBytes = os.path.getsize(selectedFile + fileExtention)
            
            with open((selectedFile + fileExtention), "rb") as f:
                txtBytesData = f.read()
                txtBytesSize = len(txtBytesData)
                fileNoHead = strplain[54:]
                headerOfFile = strplain[:54]

            keyFile = (input("Choose a text file key to decrypt the image: ") + ".txt")
            
            with open(keyFile, "rb") as key:
                 if txtOrImg == '1':
                     decplain = decryptXorb(txtBytesData, key.read())
                     newPic = decplain
                     newFileName = input("Choose a new text file name: ")
                     
                 elif txtOrImg == '2':
                     decplain = decryptXorb(fileNoHead, key.read())
                     newPic = headerOfFile+decplain
                     newFileName = input("Choose a new picture name: ")

            if txtOrImg == '1':
                
                while True:
                    if newFileName == selectedFile + fileExtention:
                        print("You cannot choose the same file name as the file you are encrypting")
                        newFileName = input("Please select a new file name: ")
                    else:
                        break
                                    
                                
            if txtOrImg == '1':
                with open(newFileName + fileExtention, "w") as picMaker:
                    picMaker.write(str(newPic))
                    print("\nDecrypted text file created\n")
            elif txtOrImg == '2':
                with open(newFileName + fileExtention, "wb") as picMaker:
                    picMaker.write(newPic)
                    print("\nDecrypted picture created\n")
            
            input("Press any key to exit . . .")
            exit()
#-------------------------------------------

#DECRYPT ANALYSIS-------------------------------------------

        if csmx == '5':
            print(strplain)
            decplain = strplain

            while True:
                feedBack1 = input("Enter letter/s to be replaced in the message for analysis, type 'exit' to exit, or 'lettercount' for a list of letter frequency: ")
                
                if (feedBack1 == 'exit'):
                    
                    break
                
                elif (feedBack1 == 'lettercount'):

                    print("\n Letters used in descending order: \n", collections.Counter(decplain).most_common(), "\n")
                    
                elif feedBack1.isalnum():
                    
                    while True:
                        feedBack2 = input("Which letter would you like to use as a substitution?: ")
                        tempplain = list(decplain)
                        if feedBack2.isalnum():
                            for i, char in enumerate(decplain):
                                if char == feedBack1:
                                    tempplain[i] = feedBack2
                                elif char == feedBack2:
                                    tempplain[i] = feedBack1
                            decplain = ''.join(tempplain)
                            print(decplain)
                            break
                        else:
                            print("Your input is invalid.")
                            break
                    

                else:
                    print("Your input is invalid.")
            
#-------------------------------------------
            
#------------------------------------------------------------------------------------------------------------------------



#-------------------------------------------ENCRYPTION OPTIONS-------------------------------------------
    if encDec == '1':
#ENCRYPT CAESAR-------------------------------------------
        if csmx == '1':
            print("\nAttained inceptive missive: ", strplain)
            ciphertext = encryptCaesar(strplain, input("Please choose a key to encrypt with: "))
            print("\n\nProcured cryptogram: ", ciphertext)
#----------------------------------------------------------------------

#ENCRYPT SIMTRAN-------------------------------------------
        if csmx == '2':
            print("\nAttained inceptive missive: ", strplain)
            ciphertext = encryptSimtran(strplain, input("Please choose a key to encrypt with: "))
            print("\n\nProcured cryptogram: ", ciphertext)
#----------------------------------------------------------------------

#ENCRYPT MODB-------------------------------------------
        if csmx == '3':
            answer = input("Would you like to (1) generate a new key for encryption, or (2) provide your own?")
            while True:
                
                if answer == '1':
                    keyFile = input("Choose a key name: ")
                    
                    with open(keyFile + ".txt", "wb") as keyMaker:
                        if txtOrImg == '1':
                            with open(selectedFile + fileExtention, "rb") as txtBytes:
                                txtBytesData = txtBytes.read()
                                txtBytesSize = len(txtBytesData)
                                keyMaker.write(os.urandom(txtBytesSize))
                        elif txtOrImg == '2':
                            keyMaker.write(os.urandom(len(fileNoHead)))
                        print("\nKey created\n")
                        
                    with open(keyFile + ".txt", "rb") as key:
                        if txtOrImg == '1':
                            ciphertext = encryptModb(txtBytesData, key.read())
                            newPic = ciphertext
                            newFileName = input("Choose a new text file name: ")
                        elif txtOrImg == '2':
                            ciphertext = encryptModb(fileNoHead, key.read())
                            newPic = headerOfFile+ciphertext
                            newFileName = input("Choose a new picture name: ")

                    if txtOrImg == '1':
                        while True:
                            if newFileName == selectedFile + fileExtention:
                                print("You cannot choose the same file name as the file you are encrypting")
                                newFileName = input("Please select a new file name: ")
                            else:
                                    break
                        
                    
                    if txtOrImg == '1':
                        with open(newFileName + fileExtention, "wb") as picMaker:
                            picMaker.write(newPic)
                            print("\nEncrypted text file created\n")
                    elif txtOrImg == '2':
                        with open(newFileName + fileExtention, "wb") as picMaker:
                            picMaker.write(newPic)
                            print("\nEncrypted picture created\n")
                    break
                
                elif answer == '2':
                    cwd = os.getcwd()
                    for file in os.listdir(cwd):
                        if file.endswith(".txt"):
                            print(file[:-4] + "")
                    keyFile = input("Choose a key file to encrypt the image: ") + ".txt"
                    
                    while True:
                        if os.path.exists(keyFile):
                            break
                        else:
                            keyFile = input("Key filename invalid. Try again.") + ".txt"

                    with open(selectedFile + fileExtention, "rb") as txtBytes:
                                txtBytesData = txtBytes.read()
                                txtBytesSize = len(txtBytesData)
                            
                    with open(keyFile, "rb") as key:
                        if txtOrImg == '1':
                            ciphertext = encryptModb(txtBytesData, key.read())
                            newPic = ciphertext
                            newFileName = input("Choose a new text file name: ")

                        elif txtOrImg == '2':
                            ciphertext = encryptModb(fileNoHead, key.read())
                            newPic = headerOfFile+ciphertext
                            newFileName = input("Choose a new picture file name: ")

                    if txtOrImg == '1':

                        while True:
                            if newFileName == selectedFile + fileExtention:
                                print("You cannot choose the same file name as the file you are encrypting")
                                newFileName = input("Please select a new file name: ")
                            else:
                                break

                    with open(newFileName + fileExtention, "wb") as picMaker:
                            picMaker.write(newPic)
                            
                    if txtOrImg == '1':
                        print("\nEncrypted text file created\n")
                    elif txtOrImg == '2':
                        print("\nEncrypted picture created\n")
                    break
                
            print("\nFile encrypted\n")
            input("Press any key to exit . . .")
            exit()
#-------------------------------------------------------------------

#ENCRYPT XORB-------------------------------------------
        if csmx == '4':
            answer = input("Would you like to (1) generate a new key for encryption, or (2) provide your own?")
            while True:
                
                if answer == '1':
                    keyFile = input("Choose a key name: ")
                    
                    with open(keyFile + ".txt", "wb") as keyMaker:
                        if txtOrImg == '1':
                            with open(selectedFile + fileExtention, "rb") as txtBytes:
                                txtBytesData = txtBytes.read()
                                txtBytesSize = len(txtBytesData)
                                keyMaker.write(os.urandom(txtBytesSize))
                        elif txtOrImg == '2':
                            keyMaker.write(os.urandom(len(fileNoHead)))
                        print("\nKey created\n")
                        
                    with open(keyFile + ".txt", "rb") as key:
                        if txtOrImg == '1':
                            ciphertext = encryptXorb(txtBytesData, key.read())
                            newPic = ciphertext
                            newFileName = input("Choose a new text file name: ")
                        elif txtOrImg == '2':
                            ciphertext = encryptXorb(fileNoHead, key.read())
                            newPic = headerOfFile+ciphertext
                            newFileName = input("Choose a new picture name: ")

                    if txtOrImg == '1':
                        while True:
                            if newFileName == selectedFile + fileExtention:
                                print("You cannot choose the same file name as the file you are encrypting")
                                newFileName = input("Please select a new file name: ")
                            else:
                                    break
                        
                    
                    if txtOrImg == '1':
                        with open(newFileName + fileExtention, "wb") as picMaker:
                            picMaker.write(newPic)
                            print("\nEncrypted text file created\n")
                    elif txtOrImg == '2':
                        with open(newFileName + fileExtention, "wb") as picMaker:
                            picMaker.write(newPic)
                            print("\nEncrypted picture created\n")
                    break
                
                elif answer == '2':
                    cwd = os.getcwd()
                    for file in os.listdir(cwd):
                        if file.endswith(".txt"):
                            print(file[:-4] + "")
                    keyFile = input("Choose a key file to encrypt the image: ") + ".txt"
                    
                    while True:
                        if os.path.exists(keyFile):
                            break
                        else:
                            keyFile = input("Key filename invalid. Try again.") + ".txt"

                    with open(selectedFile + fileExtention, "rb") as txtBytes:
                                txtBytesData = txtBytes.read()
                                txtBytesSize = len(txtBytesData)
                            
                    with open(keyFile, "rb") as key:
                        if txtOrImg == '1':
                            ciphertext = encryptXorb(txtBytesData, key.read())
                            newPic = ciphertext
                            newFileName = input("Choose a new text file name: ")

                        elif txtOrImg == '2':
                            ciphertext = encryptXorb(fileNoHead, key.read())
                            newPic = headerOfFile+ciphertext
                            newFileName = input("Choose a new picture file name: ")

                    if txtOrImg == '1':

                        while True:
                            if newFileName == selectedFile + fileExtention:
                                print("You cannot choose the same file name as the file you are encrypting")
                                newFileName = input("Please select a new file name: ")
                            else:
                                break

                    with open(newFileName + fileExtention, "wb") as picMaker:
                            picMaker.write(newPic)
                            
                    if txtOrImg == '1':
                        print("\nEncrypted text file created\n")
                    elif txtOrImg == '2':
                        print("\nEncrypted picture created\n")
                    break
                
            print("\nFile encrypted\n")
            input("Press any key to exit . . .")
            exit()
#------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------



            

#-------------------------------------------SAVE/APPEND/EXIT OPTIONS-------------------------------------------
if txtOrImg == '1':
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
                with open(input("Choose a file name: ") + ".txt", "w") as fileWrite:
                    print("\n\nData accessed for inscription")
                    fileWrite.write(ciphertext)
                print("\nCryptogram inscribed")
                input("Press any key to exit . . .")
                exit()
    #IF DECRYPTOR USED
            elif encDec == '2':
                with open(input("Choose a file name: ") + ".txt", "w") as fileWrite:
                    print("\n\nData accessed for deciphering")
                    fileWrite.write(decplain)
                print("\nDeciphered missive inscribed")
                input("Press any key to exit . . .")
                exit()
    #----------------------------------------------------------------------


    #APPEND CURRENT FILE-------------------------------------------

    #IF ENCRYPTOR USED
        elif fileMaker == '2':
            if encDec == '1':
                with open(selectedFile, "a") as fileWrite:
                    print("\n\nData accessed for inscription")
                    fileWrite.write("\n\n" + ciphertext)
                print("\nCryptogram inscribed")
                input("Press any key to exit . . .")
                exit()
    #IF DECRYPTOR USED
            elif encDec == '2':
                with open(selectedFile, "a") as fileWrite:
                    print("\n\nData accessed for deciphering")
                    fileWrite.write("\n\n" + decplain)
                print("\nDeciphered missive inscribed")
                input("Press any key to exit . . .")
                exit()
    #------------------------------------------------------------------------------


    #EXIT PROGRAM-------------------------------------------
        elif fileMaker == '3':
            exit()
    #-----------------------------------------------------------------
