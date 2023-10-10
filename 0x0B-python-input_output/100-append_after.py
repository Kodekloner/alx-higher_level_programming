#!/usr/bin/python3
"""Defines a text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
	"""Insert text after each line containing a given string in a file.

        Args:
            filename (str): The name of the file.
            search_string (str): The string to search for within the file.
            new_string (str): The string to insert.
        """
	read = []
	with open(filename, "r", encoding="utf-8") as f:
		read = f.readlines()
		index = 0

		while index < len(read):
			if search_string in read[index]:
				read[index:index + 1] = [read[index], new_string]
				index += 1
			index += 1

	with open(filename, "w", encoding="utf-8") as file:
		file.writelines(read)
