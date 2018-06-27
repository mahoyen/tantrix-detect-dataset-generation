import numpy as np
def toString(*args):
    
    i = 0
    for arg in args:
        if type(arg)==list:
            for a in arg:
                if i == 0:
                    string = str(a)
                else:
                    string += ";"+str(a)
        elif i == 0:
            string = str(arg)
        else:
            string += ";"+str(arg)
        i += 1
    return string

def translatePosition(plasseringer):

    result = [-1,-1,-1,-1,-1,-1]
    if plasseringer[0] == 0:
        return result
    positions = [(60,8);(110,30);(110,85); (60, 110); (20,85); (20,30)]
    for i in range(len(plasseringer)):
        result[i] = positions.pop(int(plasseringer[i]))
    result[4] = positions[0]
    result[5] = positions[1]
    return result



f = open("labels.csv", 'w')

f.write("Name;left;mid;right")

brikkeInt = 2


variableNames = ["Cleft", "Cmid", "Cright", "Sleft", "Eleft", "Smid", "Emid"] #"Sright", "Eright"
variables = np.zeros(len(variableNames), dtype=str)


for i in range(brikkeInt):
    name = "p"+str(i)
    for j in range(len(variableNames)):
        variables[j] = str(input(variableNames[j]+": "))
    
    positions = translatePosition(variables[-4:])
    string = toString(name, variables[:3], positions)
    print(string)

    f.write(string)

f.close()
    
    