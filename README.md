String Program and Unit Testing

This project includes two Python programs:

stringProgram.py - Main program that contains the functions
stringProgramTest.py - Unit test program that runs the tests

!!!The program is designed to work with English characters utf8 format!!!

Before running these programs, you need to have:

1. Latest version of windows
2. Latest version of python
3. The basic knowledge of file navigation system in terminal and in windows and how to use GitHub to get the files.

How to Run the Programs:

Step 1: Download the programs and save them in same folder so they can work together.

Step 2: Open a command prompt and navigate to the folder where you saved the programs. 

Step 3: Type this - "python stringProgram.py" and hit enter to run the program. (copy it without quotes)

	The program will ask you to enter a string. You can type in text, and it will show you:
	The number of characters.
	The number of vowels.
	The number of digits.

Step 4: Run the Unit Tests	
	In the same command prompt(meaning in the same directory)
	Type this "python -m unittest stringProgramTest.py" and hit enter. (copy it without quotes)

	If the functions count the characters, vowels, and digits correctly.
	If they handle special cases like empty strings, strings with spaces, and strings with mixed characters.
	The program will output a result:

	"OK" means all tests passed.
	If something is wrong it will tell you.
