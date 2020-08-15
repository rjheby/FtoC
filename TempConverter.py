#Simple Fahrenheit to Celcius converter
#Quit prompt and Title
end = False
print("Fahrenheit to Celcius Converter")
#So abiding by the quit prompt, we'll ask you the temperature
while end == False:
  Temp = input("So...how many degrees Fahrenheit is it? ")
  if Temp == "end":
     print("End of Report")
     break
#Formula for Fahrenheit to Celcius
  else:
      print(("                         Great, so it's " + str(round(float(Temp) - 32 * (5/9), 1)) + "° " + "Celcius."))
