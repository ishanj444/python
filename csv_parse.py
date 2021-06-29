# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 03:50:59 2020

@author: jain
"""

import csv

def read_csv_fieldnames(file_name):
    """
    Given a CSV file, read the data into a nested list
    Input: String corresponding to comma-separated  CSV file
    Output: Nested list consisting of the fields in the CSV file
    """ 
       
    with open(file_name, newline='') as csv_file:       # don't need to explicitly close the file now
        csv_table = []
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            csv_table.append(row)
    return csv_table

def write_csv_file1(csv_table, file_name):
    """
    Input: Nested list csv_table and a string file_name
    Action: Write fields in csv_table into a comma-separated CSV file with the name file_name
    """
    
    with open(file_name, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        for row in csv_table:
            csv_writer.writerow(row)


def read_csv_as_list_dict(csvfilename, keyfield, arg3):
    """
    Reads CSV file named csvfilename, parses
    it's content and returns the data within
    the file as a dictionary of dictionaries.
    """
    table = {}
    with open(csvfilename, "rt", newline='') as csvfile:
        csvreader = csv.DictReader(csvfile,
                                   skipinitialspace=True)
        for row in csvreader:
            table[row[keyfield]] = row
    return table

def read_csv_as_nested_dict (csvfilename, keyfield, separator, quote, quotestrategy):
    """
    Reads CSV file named csvfilename, parses
    it's content and returns the data within
    the file as a dictionary of dictionaries.
    """
    table = {}
    with open(csvfilename, "rt", newline='') as csvfile:
        csvreader = csv.DictReader(csvfile,
                                   skipinitialspace=True,
                                   delimiter=separator,
                                   quotechar=quote,
                                   quoting=quotestrategy)
        for row in csvreader:
            table[row[keyfield]] = row
    return table, csvreader.fieldnames

def read_csv_file1(file_name, file_delimeter):
    """
    Given a CSV file path and a delimiter as strings,
    read the data into a 2D table and return the table
    """
       
    with open(file_name, newline='') as csv_file:       # don't need to explicitly close the file now
        csv_table = []
        csv_reader = csv.reader(csv_file, delimiter=file_delimeter)
        for row in csv_reader:
            csv_table.append(row)
    return csv_table


def parse(csvfilename):
    """
    Reads CSV file named csvfilename, parses
    it's content and returns the data within
    the file as a list of lists.
    """
    table = []
    with open(csvfilename, "r") as csvfile:
        for line in csvfile:
            line = line.rstrip()
            columns = line.split(',')
            table.append(columns)
    return table

