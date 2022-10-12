# Course: CIS 117 PythonProgramming
# Name:   Chamith Gamage
# Description:  Programming with Namespaces, Exception Control Flow
# Application:  Data Analysis and Handling Input Errors
# Development Environment:  macOSX 12.4
# Version:  Python 3.10.4
# Date:  10/11/22


# Program Source Statements

'''function to request input'''
def require_input():

	# holds the input file
	file_in =""

	# user instructions
	input_request = "please enter the file name :"


	# repeat user input request while getting a correct input
	while file_in =="":
		try:
			file_name = input(input_request);
			file_in = open(file_name,"r", encoding="utf-8")
		except IOError:
			print("Error: file not found!")
	return file_in


	
'''function to process file'''
def process_file(file):

	# holds the line count value given in the input file (line 0)
	line_count = 0

	# holds the actual line count value
	actual_line_count = 0

	# holds the value of sum (line 1 to line n)
	line_sum = 0


	# iterate over lines of file.
	for line in file:
		

		# remove next line character from line strings.
		line_str = line.replace("\n","")

		
		
		if(line_count == 0):

			# check if integer value is given in line 0
			# returns error message if not.
			try:
				line_count = int(line_str)
			except Exception as e:
				print (e , "\n : first line of the file is not an integer")
			
				return


		else:

			# holds integer value of each line 
			line_int = 0


			# check if integer valueues are given in line 1 to line n.
			# returns error message if not.
			try:
				line_int = int(line_str)
			except Exception as e:
				print ( e ,"\n : file contents invalid")
				return 

			# updates line count and line sum
			actual_line_count += 1;
			line_sum += line_int




	# return the sum value if given line count equals to actual count.
	# else returns error msg.
	if line_count == actual_line_count:
		print ("The sum is :" , line_sum)
	else:
		print( "given line count does not matches with actual line count")



# calls the program func. in order.
def main():
	file =require_input()
	process_file(file)



# calls the main function.
if __name__ == '__main__':
	main()

'''
### output 1(failed)

chamithgamage@Chamiths-Air lab6 % python3 chamithLab6.py
please enter the file name :bad1.dat
given line count does not matches with actual line count

### output 2(failed)

chamithgamage@Chamiths-Air lab6 % python3 chamithLab6.py
please enter the file name :bad2.dat
invalid literal for int() with base 10: 'ten' 
 : first line of the file is not an integer

### output 3(failed)

chamithgamage@Chamiths-Air lab6 % python3 chamithLab6.py
please enter the file name :bad3.dat
invalid literal for int() with base 10: 'one' 
 : file contents invalid

 ### output 4(failed)

chamithgamage@Chamiths-Air lab6 % python3 chamithLab6.py
please enter the file name :bad4.dat
given line count does not matches with actual line count

### output 5(success)

chamithgamage@Chamiths-Air lab6 % python3 chamithLab6.py
please enter the file name :good.dat
The sum is : 55

chamithgamage@Chamiths-Air lab6 % 

'''