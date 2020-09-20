# This python file converts English Text into Morse Code

#importing the file which contains english character to morse code values as a python dictionary , as morse

import morsedictionary as morse 

#saving the python dictionary variable morsecode from morsedictionary file to morsecode variable in this file 

morsecode = morse.morsecode

class encoder:

    """this function reads a text file whose location is passed in parameters and 
       saves the whole content of that text file into a variable . if the user chooses 
       to read the English Text from a text file"""

    def FromFileToMorse(self , filelocation):
        #variable which stores the content of the file for encoding

        self.FileTxtToConvert = ""

        try:
            #opening the file and storing the file contents into a variable .

            f=open(filelocation  , "r")
            self.FileTxtToConvert = f.read()
            f.close() 

        except:

            print("File not found ! Please Check The location of the file")

        """in case the location passed in parameters is not found , try catches that exception
           and statements in except are executed """

    """This Function saves the value of English Text to be converted
       passed as parameters into a string which is inputed by the user if he chooses to 
       input the English Text as string"""

    def FromStringToMorse(self,StringValue):
        self.StringTxtToConvert = StringValue


    """ This function converts the Text passed in as parameters into Morse Code
        and saves the resulting text into a file Named "TextToMorseCode.txt" located in 
        the same folder in which the file that run this program is saved """

    """The algorithm is pretty simple , the function selects on character of the 
       variable and searches for it in the morsedictionary and appends that into the file"""

    def TextToMorseConverterinFile(self , txtToConvert):

        for x in txtToConvert :

            f = open("TextTOMorseCode.txt" , "a")

            try:

                morseOfCharacter = morsecode[x.lower()]

            except:

                morseOfCharacter = x
            
            """in case the character is not found ,that character doesnt have
               morse code so its directly written in file without encoding ."""

            f.write(morseOfCharacter + " ")
            f.close()

        print("File saved as TextToMorseCode.txt")

    """ This function converts the Text passed in as parameters into Morse Code
        and saves the resulting text into a variable and returns it , in case the
        user wants the string value to be saved in a variable in his program """

    """The algorithm is same as above function"""

    def TextToMorseConverterinString(self , txtToConvert):

        self.MorseAsString = ""
        for x in txtToConvert :
            
            try:
                morseOfCharacter = morsecode[x.lower()]

            except:
                morseOfCharacter = x
        
            self.MorseAsString = self.MorseAsString + morseOfCharacter + " "
        
        return self.MorseAsString
            
    


    """The main Function function which calls the above functions 
       takes the user inputs as parameters and assigns them to
       above functions as parameters and executes all the function as soon as 
       an object of this class is created ."""

    def __init__(self , FileOrString , FileLocationOrString , outputAsFileOrString ):

        self.FileOrString = FileOrString 
        self.fileLocationOrString = FileLocationOrString
        self.outputAsFileOrString = outputAsFileOrString
        self.MorseToConvertAsParameter =""

        if(self.FileOrString.lower() == "file"):

            self.FromFileToMorse(self.fileLocationOrString)
            self.txtToConvertAsParameter = self.FileTxtToConvert.lower()

        elif(self.FileOrString.lower == "string"):

            self.FromStringToMorse(self.fileLocationOrString)
            self.txtToConvertAsParameter = self.StringTxtToConvert.lower()

        else:

            raise Exception("Error Parameters : Please Check Your Parameters in encoder()")

        if(self.outputAsFileOrString.lower() == "file"):

            self.TextToMorseConverterinFile(self.txtToConvertAsParameter)
            print("File Has Been Created")

        elif(self.outputAsFileOrString.lower() == "string"):

            pass

        else:

            raise Exception("Error Parameters : Please Check Your Parameters in encoder()")


    """The __repr__ function gets executed as the class is called but unlike __init__
       it returns a string i need this in case the user wants to get the final text to
       be returned and saved into a variable in which the class is called ."""
          
    def __repr__(self):
        
            
        if(self.outputAsFileOrString.lower() == "string"):

            MorseInString = self.TextToMorseConverterinString(self.txtToConvertAsParameter)
            return MorseInString

        elif(self.outputAsFileOrString.lower() == "file"):

            return "file has been created"

        else:
            raise Exception("Error Parameters : Please Check Your Parameters in encoder()")
      




        

        
            


    

    

