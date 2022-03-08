

#Prompt the user to enter

#the name of the input file.

first_file = input("Enter the name of the input file: ")

    #Prompt the user to enter

    #the name of the second file.

second_file = input("Enter the name of the output file: ")

    #Open the input file.

in_file = open(first_file, 'r')

    #Open the output file.

out_file = open(second_file, 'w')

    #Define a variable to

   #store the line count.

line_count = 1

    #Run the loop to access

    #the line in the file.

for line in in_file:

        #Use the rjust() function to

        #specify the line number.

    number_in_str = (str(line_count)).rjust(4, ' ')

        #Add the line number to the line.

    new_line = number_in_str + "> " +line

        #Write the output to the file.

    out_file.write(new_line)

        #Increase the line count.

    line_count += 1



in_file.close()

out_file.close()

