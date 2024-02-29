#Personal Property of Owais Ali
# Create a script that accepts the file name and puts its extension to output. If there is no extension - an exception should be raised.

import os

def get_file_extension(file_name):
    _, file_extension = os.path.splitext(file_name)
    if file_extension:
        return file_extension
    else:
        raise ValueError("File has no extension.")

if __name__ == "__main__":
    file_name = input("Enter the file name: ")
    try:
        extension = get_file_extension(file_name)
        print("File extension:", extension)
    except ValueError as e:
        print(e)

