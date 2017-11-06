# tkinter_test


This python file reads and plots data stored in .csv files using the pandas module in combination with the tkinter UI module.  Data and files are structured such that the working directory accesses a subfoler (e.g. 'BAC') containing additional subfolders (Date), contining the .csv files.  This structure is used so that several different subfolders can be access through the GUI interface.  The interface provides a dropdown menu to select the first subfolder (here it cooresponds to a stock name, e.g. 'BAC' for Bank of America Corporation).  Upon selecting the first subfolder, the program reads the subfolder contents using the OS module and producing a second dropdown menu contining a list of the expiration dates which are the titles of the .csv files.  Upon selecting the .csv file, the program reads the file using the Pandas module producing a thrid dropdown menu containing a list of the contracts contained in the .csv file.  Upon selecting a contract, the program executes a ploting function that itterates over the number of 'download dates' to find each instance of the contract and plot the return value over the number of dates.  


REQUIREMENTS
Import: pandas, os, patplotlib, tkinter

File archetecture: Described above Working Directory/'stock ticker(s)'/'download date(s)'/'.csv file(s)'
e.g. WD/'BAC'/'Oct_23_2017'/'BAC_April 20,2018.csv'

