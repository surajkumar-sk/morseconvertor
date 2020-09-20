# Morse Code TO English Text And Vice Versa (Python) .

This repository can be used as a morse code convertor .

# Cloning This repository 

1 . Open cmd and change its directory to the folder where you want to clone this repository

2. type `git clone https://github.com/fun-with-codes/morseconverote.git`

now this repository is cloned in that folder .

# Usage Of This Repository 

You can convert Morse code to English text and vise versa by 

**running the morseconverter.py**

or

**importing decoder.py and encoder.py
into your python file making it as a functionality in your code by calling its 
class .**

Read futher on Who To do those .

# Converting by running morseconverter.py 

Open cmd in the folder in which this repository is cloned

Then type  `python morseconvertor.py `

Python files starts running .

You can input morse code or english text directly in the command prompt or select a file in which it is typed .

first the program will ask you to enter 'e' or 'd' 

1.'e' means encode - converts morse code to english text .

2."d" means decode - converts english text to morse code .

This input will not terminate until you type either 'e' or 'd' , if anything other that those are inputed it asks for input again

Then the program will ask you to type 't' Or 's'

1.'t' means text file - to select morse code or English Text from a text file

2.'s' means String - to type String as an input when asked For.

This input will not terminate until you type either 't' or 's' , if anything other that those are inputed it asks for input again

Then the program will ask you to type 't' Or 's'

1.'t' means text file - to save the morse code or English Text into a text file saved in the same folder as the python file is saved

2.'s' means String - to print a string value in the console .

This input will not terminate until you type either 't' or 's' , if anything other that those are inputed it asks for input again

Then the program will ask You For File location of Text to convert if You choose 't' in second one or else to input string if 's' is choosen

Then the result is saved in text file if 't' is choosen in third input or else it prints the result string .

# Adding Conversion Functionality to Other Python code

You would need decoder.py to Convert Morse Code to English Text and encoder.py to convert English Text to Morse Code

To add it in you code import those files as modules in your code 

make sure you have that file in the same folder as of the python file you are importing it in .

## For Converting from Morse Code To English

**import decoder as decoder**

then call its class as an object like 

**decoder.decoder("FileOrString" , "FileLocationOrStringValue" , "FileOrStringToOutput")**

the class take three parameters as Strings 

1.FileOrString - pass "file" if You want to input Morse Code From a File
                 
                 pass "string" if you want to input the string as parameter
                 
2.FileLocationOrStringValue - pass "FileLocation" if the First Parameter Was File , make sure you end the locaton with filname.txt
                              
                              pass "String to be converted" if the first parameter was String .
                              
3.FileOrStringToOutput - pass "file" if you want to save the output as a text file . the text file will be saved in the same folder as of this python file .

                         pass "String" if you want the output to be returned as a string which can be saved in a variable .
                         this will return a string so make sure you create object inside a variable like TextValue = decoder.decoder("string",".- -...","string")
                         
                 
## For Converting from English To Morse Code

**import encoder as encoder**

then call its class as an object like 

**encoder.encoder("FileOrString" , "FileLocationOrStringValue" , "FileOrStringToOutput")**

the class take three parameters as Strings 

1.FileOrString - pass "file" if You want to input English Text From a File
                 
                 pass "string" if you want to input the string as parameter
                 
2.FileLocationOrStringValue - pass "FileLocation" if the First Parameter Was File , make sure you end the locaton with filname.txt
                              
                              pass "String to be converted" if the first parameter was String .
                              
3.FileOrStringToOutput - pass "file" if you want to save the output as a text file . the text file will be saved in the same folder as of this python file .

                         pass "String" if you want the output to be returned as a string which can be saved in a variable .
                         this will return a string so make sure you create object inside a variable like TextValue = encoder.encoder("string","Funwithcodes","string")




