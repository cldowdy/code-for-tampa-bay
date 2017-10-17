# Code for Tampa Bay 

Data was collected as part of the Code for Tampa Bay initiative, an international network of people committed to using tech skills to improve the local community. The overall goal of this project was to gauge the impact of chronic homelessness has on the Criminal Justice System. We took part in this project and built a relational database of incarceration and release data.

## Data 
The raw data came to us in the form of a web scrape of the online offender based transaction system. The files included in this repository are intended to showcase the preprocessing necessary to go from a messy web scrape to something that can be easily migrated to a database.

## Repo Contents

- `2016 hack poster Code for Tampa Bay.pdf`: Promotional flier associated with the Tampa Bay initiative
- `Homelessness_Tampa_Bay.pdf`: A preliminary analysis of the cleaned database
- **cleaned-data**
	* `booking_add.clean.example`: The head of the cleaned charges dataset
	* `release.clean.example`: The head of the cleaned release dataset
- **input-data**
	* `[1-9] LAYOUT CSV.csv`: Raw web scrape data to be used in preprocessing
- **preprocessing**
	* `add_charges.py`: Python program responsible for extracting the charges data from the raw web scrape
	* `releasefinal.py`: Python program responsible for extracting the release data from the raw web scrape
	


