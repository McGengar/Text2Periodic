#Returns dictionary of abbreviations and full names of elements from file
def read_elements(path):
    file = open(path)
    file_content = file.readlines()
    e_dict = dict()
    for line in file_content:
        a = line.split()[0]
        e = line.split()[1]
        e_dict[a] = e
    return e_dict

#Checks if it is possible to recreate text from abbreviations from periodic table, returs logical value
#if its possible and list of abbreviations in order. 
def text2periodic(e_dict,text,output=[]):
    N = len(text)
    if N==0:
        return True,output
    if text[0].capitalize() in e_dict.keys():
        output.append(text[0].capitalize())
        temp_bool,output =  text2periodic(e_dict, text[1:],output)
        if temp_bool:
            return True, output
        else:    
            output = output[:-1]
    if N>1 and text[0:2].capitalize() in e_dict.keys():
        output.append(text[0:2].capitalize())
        temp_bool,output = text2periodic(e_dict, text[2:],output)
        if temp_bool:
            return True, output
        else:    
            output = output[:-2]
    return False,output

#main program   
if __name__ == "__main__":
    e_dict = read_elements("elements.txt")

    text = input("Enter text: ").strip(" ")
    possible,output = text2periodic(e_dict,text)

    #Build output
    if possible:
        print("Are you made of ", end="")
        for e in output:
            print(e_dict[e], end=" ")
        print("? Because you are ")
        for e in output:
            print(e,end="")
    else:
        print("Sorry, no can do")