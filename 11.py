import math

sine={
    0 : 0,
    30: 1/2,
    45:math.sqrt(2)/2,
    60:math.sqrt(3)/2,
    90:1

}

cosine={
    0 : 1,
    30: math.sqrt(3)/2,
    45:math.sqrt(2)/2,
    60:1/2,
    90:0


}

tangent={
    0 : 0,
    30: math.sqrt(3)/3,
    45: 1,
    60: math.sqrt(3),
    90: "Not Define"


}

userInput = input("Enter the angle of degrees:")

print(userInput)