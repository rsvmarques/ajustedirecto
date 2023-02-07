# Ajuste Directo

`ajustedirecto.py` is a command line program that retrieves information about contracts from the Base 4 database in Portugal: https://www.base.gov.pt/Base4/pt/

## ajustedirecto.py - Contract Information Retriever

### What is it?

`ajustedirecto.py` is a command line program that retrieves information about contracts from the Base 4 database in Portugal. It takes in input such as contract type, period, and district, and retrieves a CSV file that contains the relevant information.

### How does it work?

The program begins by showing a menu with the following options:

- **Create Report** - to input the start and end dates, type and district, and retrieve the report
- **Reports** - to list the existing reports in the local directory, with the option to remove one if desired
- **Exit** - to quit the program

The user can input the information, and the program will create a URL to access the report, using the `wget` command to download the file and save it to a local directory. The file name will be in the format `num_start_date`, where `num` is an incremental id.

### Libraries required

The following libraries are required to run the `ajustedirecto.py` program:

- `wget`

### Installation 

To install the required libraries on Kali Linux, run the following command in the terminal:

pip3 install -r requirements.txt

### Usage 

To run the program, simply enter the following command in the terminal:

python3 ajustedirecto.py

