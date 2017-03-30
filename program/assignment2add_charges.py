#!/opt/anaconda/bin/python
"""
This script cleans the data presented in the raw data csv and turns it into the format of
that easily can be migrated to a database. This is done by opening each file, and parsing 
through line-by-line. First commas contained within double quotes are turned into periods.
After, substrings are right stripped. This gets the data into a noraml enough format to 
relativly painlessly parse through it and write it to the file booking_add.clean

author: Caleb Dowdy , Charlie Edelson
created: 09/04/2016
"""

def extract_data(aline, data_lines, index, write_file):
        """This function is the main logic of the script. It is used to find the lines where
        additional charged are located. It then goes through these, copying the appropriate
        data and writing it to the write file. This function makes use of the structure seen
        in the data files. However, it requires a few helper function to work.

        Arguments
        --------
        aline -- a single line, in the form of a string
        data_line -- a list containing all of the lines of the file
        index -- the index of the current line
        write_file -- the file for the output to be written to

        Helper Functions
        ----------------
        quote_comma_fix
        substring_rstrip
        """
        line_lower = aline.lower()
        if "release date" in line_lower and ", ,,,,," not in data_lines[i+3]:
                BOOKING = quote_comma_fix(data_lines[i+1].strip()).split(',')[1]

                cur_ind = index + 3
                current_line = quote_comma_fix(data_lines[cur_ind])
                while ", ,,,,," not in current_line:
                        line_list = current_line.strip().split(',')
                        TYPE = line_list[1].strip()
                        CHARGE = substring_rstrip(line_list[2].strip())
                        COURT = line_list[3].strip()
                        CASE = line_list[4].strip()
                        write_file.write("%s,%s,%s,%s,%s\n" % (BOOKING, TYPE, CHARGE, COURT, CASE ))

                        cur_ind += 1
                        current_line = quote_comma_fix(data_lines[cur_ind])

def first_section(data_lines, write_file):
        """Performs the same action as the above extract_data. However, extract_data looks for lines
        containing the string "release data" which missed the very first line of the file. Because
        of this, first_line just catches any additional charges located at the front of the file.

        Arguments
        ---------
        data_lines -- a list where each element is a string corresponding to a line from a textfile
                        (could be produced by readlines() method)
        write_file -- file to write the output to
        """

        if ", ,,,,," not in data_lines[2]:
                BOOKING = quote_comma_fix(data_lines[0].strip()).split(',')[1]

                cur_ind = 2
                current_line = quote_comma_fix(data_lines[cur_ind])
                while ", ,,,,," not in current_line:
                        line_list = current_line.strip().split(',')
                        TYPE = line_list[1].strip()
                        CHARGE = substring_rstrip(line_list[2].strip())
                        #print(CHARGE)
                        COURT = line_list[3].strip()
                        CASE = line_list[4].strip()
                        write_file.write("%s,%s,%s,%s,%s\n" % (BOOKING, TYPE, CHARGE, COURT, CASE ))

                        cur_ind += 1
                        current_line = quote_comma_fix(data_lines[cur_ind])


def quote_comma_fix(aline):
        """The purpose of this function is to go through the a string, and change all commas inside
        of double quotes into periods. The function works by keeping a level parameter, and adding or
        substracting from it every time it encounters a double quote. While inside the first level, if
        a comma is encountered, it is substituded for a period

        Arguments
        --------
        aline -- a string with weird commas
        """

        list_line = list(aline)
        level = 0
        for i, c in enumerate(list_line):
                if c == '"' and level == 0:
                        level += 1
                elif c =='"' and level >= 1:
                        level -= 1
                else:
                        pass

                if c == "," and level >= 1:
                        list_line[i] = "."

        clean_line = "".join(list_line)
        return clean_line


def substring_rstrip(aline):
        """Occasionally, there are strings located within out strings. It is desireable that all of these have
        no trailing whitespace. This function removes trailing whitespace by keeping track of the quote level,
        and creating a new string from the old one by looking through each element. If the element its on is a
        space, and the next one it a double quote, and its in the first quote level, it'll pass over that element

        Arguments
        --------
        aline -- a string containing a substring (or not)
        """
        list_line = list(aline)
        level = 0
        new_line = []
        for i, c in enumerate(list_line):
                try:
                        next_c = list_line[i+1]
                        if c == '"' and level == 0:
                                level += 1
                        elif c == '"' and level >= 1:
                                level -= 1

                        if level == 1 and c == " ":
                                if next_c == '"':
                                        pass
                                else:
                                        new_line.append(c)
                        else:
                                new_line.append(c)
                except IndexError:
                        new_line.append(c)

        return "".join(new_line)


# this is here so that the above functions can be imported into other files without
# running the entire script
if __name__ == "__main__":

        # create a write to file using pythons built ins and give it the correct header
        write_file = open('booking_add.clean', 'w')
        write_file.write("bookingNumber,chargeType,charge,court,caseNumber\n")

        for i in range(1,10):  # allows us to go through all 10 files with ease
                data_raw = "%i LAYOUT B CSV.csv" % i
                with open(data_raw, 'r') as f:
                        read_data = f.readlines()
                        first_section(read_data, write_file)
                        for i, line in enumerate(read_data):
                                try:
                                        extract_data(line, read_data, i, write_file)
                                except IndexError:
                                        pass

        write_file.close()  # so that we get out hard earned file written to correctly
