try:
  Weight = float(input('Enter the Wieght:'))
  
  Unit = input("Kilogram or gram?(K or G)").lower()
  
  
  if Unit == 'k':
      Weight = Weight * 1000
      Unit = "gram"
  elif Unit == 'g':
      Weight = Weight / 1000
      Unit = "killogram"
  else:
     print("Invalid unit entered.")
     exit()
  
  print(f'Your Weight is: {round(Weight,2)} {Unit}')

except ValueError:
    print("Invalid input! Please enter a numeric value for weight.")