Program Description:
This Python program interacts with the EOSIO WaxP blockchain using the AtomicAssets API to retrieve and save information related to NFT (Non-Fungible Token) collections. The program performs the following tasks:

Tasks:
- Save Collection Information: Retrieves and saves information about a specific NFT collection, including its name, author, and other details. The information is saved as a JSON file.

- Save Schema Names: Retrieves and saves the schema names associated with the specified NFT collection. Schema names represent different categories or types of NFTs within the collection.

- Save Template IDs: Retrieves and saves the template IDs associated with the specified NFT collection. Template IDs are unique identifiers for individual NFT templates within a schema.

- Save Template Structure: Retrieves and saves the structure of each template within the collection. This includes information about the fields, data types, and constraints defined for each template.

- Save All Templates: Retrieves and saves detailed information about all templates within the collection, including attributes, properties, and metadata. This data is stored as a JSON file.

- Display Possible Keys: Lists all possible keys found in the saved data from the 'All Templates' step. This can help users identify available data fields.

- Search and Save Variables: Allows users to search for specific variables or keys within the saved data and save the results in separate JSON files. This feature can be useful for extracting specific information of interest.

- Check Schema Structure: Retrieves and displays the structure of each schema within the collection, including field names, data types, and constraints.

How to Use the Program:
1. Prerequisites: Ensure you have Python installed on your system.

2. Installation: There are no specific installation requirements for this program. Simply download the Python script and ensure you have the necessary libraries installed.

3. Running the Program:
   - Run the script using Python by executing it in your terminal or IDE.
   - You will be prompted to enter the name of the NFT collection you want to work with.

4. Follow the On-Screen Instructions: The program will guide you through the steps to perform various operations on the specified NFT collection.

5. Results: The program will save the retrieved data in separate folders within the program directory. Each operation generates a corresponding JSON file or folder containing the data.

Libraries Used:
- json: Used for reading and writing JSON data.
- os: Used for working with the file system, including creating directories.
- requests: Used to send HTTP requests to the AtomicAssets API for data retrieval.

Important Notes:
- Ensure that you have a stable internet connection to access the AtomicAssets API.
- Be cautious when using the 'Search and Save Variables' feature, as it can generate multiple JSON files depending on the search results.

Disclaimer:
This program is provided as-is and does not guarantee the accuracy or completeness of the data retrieved from the AtomicAssets API. Users are responsible for verifying and using the data appropriately.

Author: elMoNoW alias: BoboCoin
Date: 08/10/2023
Version: 0.0.1
