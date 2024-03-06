def write_file(file_name, file_content):
    #To open the file for writing
    with open(str(file_name) + '.txt', 'w', encoding='utf-8') as f: 
       #Write
        f.write(file_content)
        pass

def append_file(file_name, append_content):
     # Open the file for appending
     #File converted to string,opens in writing mode and encoding for reading
     with open(str(file_name) + '.txt', 'a', encoding='utf-8') as f:
       #Append the content
        f.write(append_content)
        pass

def read_file(file_name):
    #Open the file for reading
     with open(str(file_name) + '.txt', 'r', encoding='utf-8') as f:
        #Read
        file_content = f.read()
     return file_content
pass
