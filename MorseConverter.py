#importing english text to morse code dictionary file & encoder and decode python files

import morsedictionary as morse
import encoder as encoder
import decoder as decoder

morsecode = morse.morsecode

print(type(morsecode["b"]))

# A Function for converting text to morse code

def ToMorse():
    """ A while loop so the program keeps asking the user input 
        in case user enters values other than 'T/t' or 'S/s' """

    while True:

        TypeOfFormat = input("Enter T for program to fetch data from a text file Or Enter S for Typing text : ")

        if(TypeOfFormat.lower() == "t" or TypeOfFormat.lower() == "s"):

            break

        else:

            print("Enter a valid response either T or S")


    while True:

        TypeOfFormatToSave = input("Enter T for program to save data to a text file Or Enter S to return a String : ")

        if(TypeOfFormat.lower() == "t" or TypeOfFormat.lower() == "s"):

            break
        
        else:

            print("Enter a valid response either T or S")
    
    #If the user selects T meaning from text file this if executes otherwise the next one

    if(TypeOfFormat.lower() == "t"):
        
        #input asking for the location of file where text is saved To convert

        filelocation = input("Enter the Location of the file end the input with filename.txt : ")

        if(TypeOfFormatToSave.lower() == "t"):

            #calling the encoder file and creating an object of encoder class with parameters 

            encoder.encoder("file",filelocation,"file" )

        elif(TypeOfFormatToSave.lower() == "s"):

            """calling the encoder file and creating an object of encoder class with parameters 
               inside a variable because the last parameter is Passed as String which means the
               object will return the morse code which can be saved in a variable"""

            MorseCodeValue = encoder.encoder("file",filelocation,"String" )
            print(MorseCodeValue)

     
    elif(TypeOfFormat.lower() == 's'):
        
        #input asking for the String value To convert

        txtToConvert = input("Enter the string to Convert to Morse Code: ")
        
        if(TypeOfFormatToSave.lower() == "t"):

            encoder.encoder("string",txtToConvert,"file" )

        elif(TypeOfFormatToSave.lower() == "s"):

            MorseCodeValue = encoder.encoder("string",txtToConvert,"String" )
            print(MorseCodeValue)
    


    

def ToText():

    """ A while loop so the program keeps asking the user input 
        in case user enters values other than 'T/t' or 'S/s' """

    while True:

        TypeOfFormat = input("Enter T for program to fetch data from a text file Or Enter S for Typing text : ")
        
        if(TypeOfFormat.lower() == "t" or TypeOfFormat.lower() == "s"):

            break

        else:

            print("Enter a valid response either T or S")
    
    while True:

        TypeOfFormatToSave = input("Enter T for program to save data to a text file Or Enter S to return a String : ")
        
        if(TypeOfFormat.lower() == "t" or TypeOfFormat.lower() == "s"):

            break

        else:

            print("Enter a valid response either T or S")
    
    #If the user selects T meaning from text file this if executes otherwise the next one

    if(TypeOfFormat.lower() == "t"):

        #input asking for the location of file where text is saved To convert

        filelocation = input("Enter the Location of the file end the input with filename.txt : ")

        if(TypeOfFormatToSave.lower() == "t"):

            #calling the decoder file and creating an object of decoder class with parameters 

            decoder.decoder("file",filelocation,"file" )

        elif(TypeOfFormatToSave.lower() == "s"):

            """calling the decoder file and creating an object of decoder class with parameters 
               inside a variable because the last parameter is Passed as String which means the
               object will return the English Text which can be saved in a variable"""

            MorseCodeValue = decoder.decoder("file",filelocation,"String" )
            print(MorseCodeValue)

    elif(TypeOfFormat.lower() == 's'):

        #input asking for the String value To convert
        
        MorseToConvert = input("Enter the Morse code to Convert to Text: ")
        
        if(TypeOfFormatToSave.lower() == "t"):

            decoder.decoder("String",MorseToConvert,"file" )

        elif(TypeOfFormatToSave.lower() == "s"):

            MorseCodeValue = decoder.decoder("String",MorseToConvert,"String" )
            print(MorseCodeValue)

    

    
    

            






""" A while loop so the program keeps asking the user input 
    in case user enters values other than 'E/e' or 'D/d' """

while True :
    EncodeOrDecode =input("Enter E to convert text to morse code Or D to convert morse code to text :")
    if(EncodeOrDecode.lower() == 'e' or EncodeOrDecode.lower() == 'd' ):
        break
    
    else:
        print("Enter a valid response either E or D")


if(EncodeOrDecode.lower() == "e"):
    ToMorse()

elif(EncodeOrDecode.lower() == "d"):
    ToText()
