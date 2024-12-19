
def outputHeader(dataFieldName,dataFieldType,className):
    
    # Setup formatting
    with open(className + "Gen.h","w") as file:
        file.write("#ifndef " + className.upper() + "_H\n")
        file.write("#define "+ className.upper() + "_H\n")
        file.write("#include <iostream>\n")
        file.write("using namespace std;\n\n")
        file.write("class " + className + "\n")
        file.write("{\n")
        file.write("public:\n")

        
    ## write datafields to the private section.

        if len(dataFieldName) != len(dataFieldType):
            print("Error, lists not of the same length data types or names may be lost")
            

        for i in range(len(dataFieldName)):
            
            # Line for commenting 
            file.write("    //\n")
            
            # write a string of the form "    <type> <name>;"
            file.write("    " + dataFieldType[i] + " " + dataFieldName[i] + ";\n")

    ## write getters and setters to the public section
        file.write("public:\n\n")


        # Write getters
        for i in range(len(dataFieldName)):
            file.write("    // Returns "+ dataFieldName[i] + " (" + dataFieldType[i] + ")\n")
            # Used underscore instead of camelCase to avoid changing the case of chars
            file.write("    " + dataFieldType[i] + " get_" + dataFieldName[i] + "();\n\n")

        # Write setters
        for i in range(len(dataFieldName)):
            file.write("    // Reassigns the value of " + dataFieldName[i] + "\n")
            file.write("    void " + "set_" + dataFieldName[i] + "(" + dataFieldType[i] + " new_" + dataFieldName[i] + ");\n\n")
        
        # Close formatting
        file.write("};\n\n")
        file.write("#endif")

def outputImplementation(dataFieldName,dataFieldType,className):

# Set formatting
    with open(className +"Gen.cpp", "w") as file:
        file.write("#include <iostream>\n")
        file.write('#include "' + className + 'Gen.h"\n')
        file.write("using namespace std;\n\n")

        if len(dataFieldName) != len(dataFieldType):
            print("Error, lists not of the same length data types or names may be lost")

    
# Write getters
        for i in range(len(dataFieldName)):
            file.write("\n\n// Returns " + dataFieldName[i] + " (" + dataFieldType[i] + ")\n")
            
            # Used underscore instead of camelCase to avoid changing the case of chars
            file.write(dataFieldType[i] + " "+ className + ":: get_" + dataFieldName[i] + "()\n")
            file.write("{\n")
            file.write("    return " + dataFieldName[i] + ";")
            file.write("\n}")

# Write setters
        for i in range(len(dataFieldName)):
            file.write("\n\n// Reassigns the value of " + dataFieldName[i] + "\n")
            file.write("void " + className + ":: set_" + dataFieldName[i] + "(" + dataFieldType[i] + " new_" + dataFieldName[i] + ")\n")
            file.write("{\n")
            file.write("    " + dataFieldName[i] + " = " + "new_" + dataFieldName[i] + ";\n")
            file.write("}\n")

# Close formatting
        
    
        

    

print("Welcome to the class designer.")
print ("Enter each of your data fields in the format <Type> <name>. Input 'exit' to exit")

dataType = ""
dataName = ""
# Stores each data fields type as a string
dataTypes = []

# Stores each data field's name as a string
dataNames = []


# This while loop gets the type and then the name of each datafield in the class
while dataType != "exit":
    
    dataType = input("Input data type ")

    # Ensure the user is not trying to exit
    if dataType != "exit":
        
        dataTypes.append(dataType)

        # Add name
        dataName = input("Input data field name (your data is of type " + dataType + ") ")
        dataNames.append(dataName)

className = input("Enter class name")
##### Add the ability to edit here #####

# Output header file

outputHeader(dataNames,dataTypes,className)

outputImplementation(dataNames,dataTypes,className)
# Open a file
