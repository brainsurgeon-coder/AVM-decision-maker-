print("*".center(80, '*'))
print("Hi! Welcome to Decision making tool for management of Cerebral Arteriovenous Malformation - Copyright Dr Hrishikesh Sarkar")
print()
print("You will need to have Digital subtraction images of cerebral angiogram and MRI images")
print()
print("*".center(80, '*'))
print("Enter maximum size of AVM in cms")

inputSize = int(input())
    

def sizeAvm(inputSize):
    if inputSize <= 3:
        return 1
    elif inputSize > 3 and inputSize <6 :
        return 2
    elif inputSize >= 6:
        return 3
    
#sizeAvm(inputSize)

sizescore = sizeAvm(inputSize)

print("Enter 0 if located in non eloquent and 1 if in eloquent")
inputRegion = int(input())
regionscore = inputRegion

print("Enter 0 if superficial drainage or 1 if deep")
inputDrain =int(input())
drainscore = inputDrain

print()

print("The Speztler Martin Grade of this AVM is ", sizescore + regionscore + drainscore)

SMscore = sizescore + regionscore + drainscore

print()

if SMscore <= 2:
    print("This AVM is suitable for surgery")
elif SMscore ==3:
    print("Multimodality treatment is recommended")
elif SMscore ==4:
    print("Endovascular treatment followed by surgery/SRS/observation needed")
elif SMscore ==5:
     print("Observation is highly recommended")
    
print("*".center(80, '*'))
