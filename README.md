DESCRIPTION
This repository contains the different stages in building a clone of the Airbnb website.
The concept of AirBnB revolves around a peer-to-peer online marketplace that connects inndividuals who want to rent out their properties or spare rooms with travelers seeking accomodations. instead of traditional hotels or resorts, AirBnB offers a platform where hosts can list their properties, including apartments, houses, villas, or even unique spaces like tree houses or yurls.
The first stage of this project, we wrote a command interpreter to manage the AirBnB obejects which;
-put in place a parent class called the BaseModel  which take care of the intialization, serialization and deserialization of all future instances
-create a simple flow of serialization/deserialization. Insatnce <-> Dictionary <-> JSON string <-> file
-create all classes used  for AirBnB (user, state, city, place..) that inherit from BaseModel
create the first abstracted storage engine of the projects file storage
create all unittests to validate all our classes and storage engine

DESCRIPTION OF THE COMMAND INTERPRETER
A command interpreter also known as a command line interpreter or shell, facilitates the interaction between a user to enter commands and executes various operations.
THE CONSOLE
Run the console using ./console.py
Quit the console using (hbnb) quit
TESTING
Unit test for this project are defined in the test folder to run the test simultaneously the following command should be executed $python3 unittest -m dicover tests

AUTHOR
This foleder contains the perons that carried the work in this repository:
Okwori Patience
Damian Oguche


