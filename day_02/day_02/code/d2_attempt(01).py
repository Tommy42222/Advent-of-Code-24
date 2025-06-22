with open("../input/data2.txt", "r") as file: # opens file
    content = file.read()

safeCountList = 0 #total number of safe tests
formatedList = [] #list the formated content goes in
differnce = 0 

splitConent = content.splitlines() # 
for numbs in splitConent:
    formatedList.append(numbs.split(" "))

intList = [list( map(int,i) ) for i in formatedList] 

for row in range(0,len(intList)):
    print(intList[row])
    print(safeCountList)
    valueChange = 0



    for digit in range(1,len(intList[row])): # loops for each row in data set

        a,b = intList[row][digit-1], intList[row][digit] # store the N and N-1 digits in 'a' and 'b'
        differnce = abs(a - b) # get the differnce between them
        
        if differnce == 0 or differnce > 3: # if differnce is not between 1 and 3, test is unsafe and break to next test
            print(f"{intList[row]} is UNSAFE as it has a diffence of {differnce}")
            break

        if valueChange == 0: # tells the program if this row is ment to assend or desend in value
            if a > b:
                valueChange = -1 # -1 = desending
            else:
                valueChange = 1 # 1 = assending

    else:
        if valueChange == 1:
            if intList[row] == sorted(intList[row]):
                print("SAFE_A")
                safeCountList += 1
            
            else:
                print(f'{intList[row]} IS UNSAFE as it fails to ASECSEND')
                
        else:
            if intList[row] == sorted(intList[row],reverse=True):
                print("SAFE_D")
                safeCountList += 1 

            else:
                print(f'{intList[row]} IS UNSAFE as it fails to DECSEND')
                

print(f"The final number is >>> {safeCountList}")
