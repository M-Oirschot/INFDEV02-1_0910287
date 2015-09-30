print ("Specify a number please.")
end = 0
try:
   number = int(raw_input())
   numberStart = number
except ValueError:
   print("That's not an int!")
else:
    while number != -1:
        print ("*" + "*" * number + " " * end + "*")
        end = end + 1
        number = number -1
    print("*" * numberStart +"**")