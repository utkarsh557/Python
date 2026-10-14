# cms = ics * 2.54

def inch_to_cms(inch):
    cms = inch * 2.54
    return cms

inch = float(input("Enter the value in inches: "))
print("Corresponding value in centimeter: ", inch_to_cms(inch))