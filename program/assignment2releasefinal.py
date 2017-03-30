
"""
This script cleans the data presented in the raw data csv and turns it into the format that
would easily be imported into a relational database. This is done by opening each file, and
parsing through line-by-line.

author: Caleb Dowdy , Charlie Edelson
created: 09/04/2016
"""


def extract_data(aline):
        """
        This function will extract  the release date, release code,and
        SOID from the input aline.

        Arguments
        ----------
        `aline`: a string that contains sub-strings(not always).

        """
        RE_DATE = None
        RE_CODE	= None
        SOID = None
        # Normalize the input by making the input lowercase
	lower_line = aline
	# check the input string for "release date"
        if "release date".upper() in lower_line:
		# Split the string into a list with n elements
                # where n = number of commas pressent in string
                # the first line containing 'release date' looks like this:
                # RELEASE DATE: 06/08/2000 ,RELEASE CODE: TIME SERVED , SOID: 
		line_list = lower_line.strip().split(',')
		# The first element in our new list looks like:
                # RELEASE DATE: 06/08/2000
                # So we need to seperate it further using .split() and then
                # store the 2nd element in this list.
		RE_DATE = line_list[0].strip().split(':')[1].strip()
		# Repeat the process above for release code
		RE_CODE = line_list[1].strip().split(':')[1].strip()
		# Repeat the process above for SOID
		SOID = line_list[2].strip().split(':')[1].strip()
	return RE_DATE, RE_CODE, SOID
				
if __name__ == "__main__":

# create the new file to write our results to
	write_file = open('release.clean', 'w')
# write in our header info
	write_file.write("releaseDate,releaseCode,SOID\n")
	
	for i in range(1,10):
	
		data_raw = "%i LAYOUT B CSV.csv" % i
	
		with open(data_raw, 'r') as f:
			read_data = f.readlines()
			for line in read_data:
				date, code, soid = extract_data(line)
				if date == None:
					pass
				else:
					write_file.write("%s,%s,%s\n" % (date, code, soid))
		
	write_file.close()
	
	
