while True:
    print("Input celcius")
    celcius = int(raw_input(""))

    if(celcius < -273):
        print ("Value cannot be lower then -273")
    else:
        kelvin = round(celcius + 273.15,0)
        print (kelvin)
        break
