# This python file converts morse code into english text

#importing the file which contains english character to morse code values as a python dictionary , as morse

import morsedictionary as morse 

#saving the python dictionary variable morsecode from morsedictionary file to morsecode variable in this file 

morsecode = morse.morsecode



class decoder:

    """this function reads a text file whose location is passed in parameters and 
       saves the whole content of that text file into a variable . if the user chooses 
       to read the morse code from a text file"""

    def FromFileToText(self , filelocation):

        #variable which stores the content of the file for decoding

        self.FileMorseToConvert = ""

        

        try:
            #opening the file and storing the file contents into a variable .

            f=open(filelocation  , "r")
            self.FileMorseToConvert = f.read()
            f.close()   


        except:

            raise Exception("Error File : File Not Found")

        """in case the location passed in parameters is not found , try catches that exception
           and statements in except are executed """


    """This Function saves the value of morse code to be converted
       passed as parameters into a string which is inputed by the user if he chooses to 
       input the morse code as string"""

    def FromStringToText(self,StringValue):
        self.StringMorseToConvert = StringValue

    """ This function converts the morsecode passed in as parameters into English text
        and saves the resulting text into a file Named "MorseCodeTotext.txt" located in 
        the same folder in which the file that run this program is saved """

    """ the alogorithm is simple , the function selects one character from
        the morse file compares it to space , if space is found then concates
        between that space to previous one and stores them into a variable
        and finds for a match in the morsecode dictionary if found appends that character 
        into the file and moves on to next character , again to find space """

    def MorseToTextConverterinFile(self , MorseToConvert):

        #variable to keep track of the index number of MorseToConvert String Variable

        currentposition = 0

        """variable to know the index number of previous number space so to concate the morcecode 
           between the spaces"""

        startPosition = 0    

        for x in MorseToConvert:

            """this variable tells whether the character is found
               or not , this is very helpful when a morse is concanted and
               searchs for but not found and the for loop moves on to next
               space ignoring the previous morse code , this variable would
               help us futher for checking for any exceptions"""

            CharacterFound = False

            if(x != ' '):
                #if the character is not a space the current position moves ahead and the loop goes on

                currentposition +=1
                continue

            else:

                """if a space is found the character is concated between the startposition
                   which will be the index of ( index of previous space +1) and currentposition """

                codeOfCharacter = MorseToConvert[startPosition:currentposition]

                """This for loop searches for the concated string from above in the 
                   dictionary variable morce code and then writes the character into 
                a text file and changes CharacterFund to true"""

                for y,z in morsecode.items():
                    if(codeOfCharacter == z):
                        f= open("MorseCodeToText.txt" , "a")
                   
                        f.write(y)
                        f.close()
                        CharacterFound = True

                """if the character is found then we should move the startposition
                   to the next character in the loop so that when the space is found next 
                   time the startposition becomes the previous space position index + 1 """

                """There could be exceptions like \n in the textfile or
                   a character which doesnot have morse code or 
                   wrongly entered morse code , below else 
                   else statement writes those exception as it is
                   in the file , and increase the startposition value """

                if(CharacterFound):
                    startPosition = currentposition+1
                
                else:

                    if(MorseToConvert[currentposition-1] != " "):

                        if(MorseToConvert[currentposition-2] != " "):

                            f=open("MorseCodeToText.txt" , "a")
                            f.write(MorseToConvert[startPosition:currentposition])
                            f.close()
                            startPosition = currentposition+1
                    
                        else:

                            f=open("MorseCodeToText.txt" , "a")
                            f.write(MorseToConvert[currentposition-1])
                            f.close()
                            startPosition = currentposition+1
               
                
            currentposition +=1

        print("File saved as MorseCodeToText.txt")

    
    """ This function converts the morsecode passed in as parameters into English text
        and saves the resulting text into a Variable and returns the variable which
        can be stored in a variable when this class is called . """

    """Algorithm is same as above function , instead of writing the result
       in a file this is store it as a text"""

    def MorseToTextConverterinString(self , MorseToConvert):

        currentposition = 0
        startPosition = 0    
        self.TextAsString =""

        for x in MorseToConvert:

            CharacterFound = False

            if(x != ' '):

                currentposition +=1
                continue

            else:
            
                codeOfCharacter = MorseToConvert[startPosition:currentposition]
                
                for y,z in morsecode.items():

                    if(codeOfCharacter == z):
                        
                        self.TextAsString = self.TextAsString + y
                        
                        CharacterFound = True

                if(CharacterFound):

                    startPosition = currentposition+1
                
                else:

                    if(MorseToConvert[currentposition-1] != " "):

                        if(MorseToConvert[currentposition-2] != " "):

                            self.TextAsString = self.TextAsString + MorseToConvert[startPosition:currentposition]
                            
                            startPosition = currentposition+1
                    
                        else:

                            self.TextAsString = self.TextAsString + MorseToConvert[currentposition-1]
                            
                            startPosition = currentposition+1
               
                
            currentposition +=1
        
        return self.TextAsString
              
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

            self.FromFileToText(self.fileLocationOrString)
            self.MorseToConvertAsParameter = self.FileMorseToConvert.lower()

        elif(self.FileOrString.lower == "string"):

            self.FromStringToText(self.fileLocationOrString)
            self.MorseToConvertAsParameter = self.StringMorseToConvert.lower()

        else:

            raise Exception("Error Parameters : Please Check Your Parameters in decoder()")

        if(self.outputAsFileOrString.lower() == "file"):

            self.MorseToTextConverterinFile(self.MorseToConvertAsParameter)
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

            TextInString = self.MorseToTextConverterinString(self.MorseToConvertAsParameter)
            return TextInString

        elif(self.outputAsFileOrString.lower() == "file"):

            return "file has been created"

        else:

            raise Exception("Error Parameters : Please Check Your Parameters in encoder()")
      

