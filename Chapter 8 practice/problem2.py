# (°C * 9/5) + 32 = °F

def cel_to_farenheit(temp):
    f = (temp * 9/5) + 32
    return f

ctemp = int(input("Enter temprature in celcius: "))

print("Corresponding temprature in farenheit: ", cel_to_farenheit(ctemp))

