T = float(input("Enter a temperature : "))
C = input("Convert to Fahrenheit or Celsius? ")
Tf = float()
Tc = float()
if C.upper() == 'F':
    tc = (9/5)*T+32
    print("온도는 : {}C".format(tc))
elif C.upper() == 'C':
    tf = (5/9)*T-32
    print("온도는 : {}F ".format(tf))
