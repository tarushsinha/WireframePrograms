## program to request the user's input on temperature and unit, and will spit back converted temp & units
def weatherConverter():
    ## Capture temperature values & unit (F or C)
    while True:
        try:
            num = float(input("What is the temperature outside?: \ "))
            break
        except ValueError as error:
            print(f"Error Caught: {error}\n")
    while(True):
        mode = input("Is that Fahrenheit or Celsius? Enter `F` for Fahrenheit or `C` for Celsius! \ ")
        if mode == 'F' or mode == 'C':
            break

    ## Proces conversion for each
    if mode == 'C':
        num = (num * 9/5) + 32
        mode = "Fahrenheit"
    else:
        num =(num - 32) * 5/9
        mode = "Celsius"

    retMsg = "The temperature outside is {0} degrees {1}".format(num, mode)
    print(retMsg)

weatherConverter()