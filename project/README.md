# Swimming Academy Manager
#### Video Demo: <https://youtu.be/QFpvlZ7P88Y>
#### Description:

I built a small system for the administrative employee of the academy to help him with:

1. Registering swimmers and creating an ID for each one, so operations are done using the ID instead of dealing with all the data.
2. A table with all the data of the swimmers in the academy, such as the name, the ID, and the age.
3. A table of the swimmers who are subscribed but have not paid the subscription.
4. Updating the status of a swimmer after paying the subscription.
5. Handling errors when the employee does something wrong, instead of the whole program crashing.
6. After dealing with a swimmer, the information is saved in a file called swimmers.json, so the data is permanent and not just a program working on temporary data.

## Project files

- project.py: explained in detail below.
- test_project.py: I used the pytest tool to test my three functions: add_swimmer, mark_paid and unpaid_swimmers. I used different kinds of data, including wrong data, to check whether the function raises a ValueError or not.
- requirements.txt: contains the libraries I used in the project that need to be installed.
- swimmers.json: I used it as a database file.

### project.py

The program is written in Python and divided into several functions.

- **main**: responsible for organizing the program and the flow between the functions. It reaches each function through one big loop, based on what the user chooses to do.
- **load_swimmers**: deals with the data file, which is a JSON file. It reads the file and converts it into a list so Python can work with it.
- **save_swimmers**: also deals with the JSON file, but unlike load_swimmers, it is the one that writes to the file. It takes the list of swimmers after it changes and saves it in the file in an organized way.
- **add_swimmer**: deals with new swimmers. It receives the name, age, training day and training time, creates a four-digit ID for the swimmer, and adds the swimmer to the list (main then saves it in the data file). It also checks for errors, and if something is wrong it raises a suitable error message.
- **table_swimmers**: responsible for creating the nice-looking tables using the rich library, made of columns and rows. It is used by the other parts of the program to display any list of swimmers. If the list is empty, it shows a message that there are no swimmers.
- **mark_paid**: lets the admin change the status of a swimmer from not paid to paid, using the swimmer's ID. The admin first sees a table with all the swimmers (shown by main) so he can choose the ID.
- **unpaid_swimmers**: returns the swimmers who have not paid the subscription until now, and main shows them in a table.


## Design decisions

I chose a JSON file instead of CSV because JSON is easier for me to work with, since it is similar to a dictionary.

The ID is made of four digits so there are a lot of possibilities (around 9,000 different IDs), which is enough for the expected number of swimmers in the academy, and the program makes sure the ID is not used before.

I used the rich library to design tables that look nice and fit the design of the system, and the questionary library to make the choices like multiple choice questions. This reduces extra code, instead of making options from 1 to 4 and then finding the user entered a third number or sent a string.