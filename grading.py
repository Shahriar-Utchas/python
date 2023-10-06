a = float(input('Enter Your Grade '))

if a>=0 and a<=100:
  if a>=0 and a<50:
    print('Your Grade is: F')
  elif(a>=50 and a<60):
     print('Your grade is: D')
  elif(a>=60 and a<65):
     print('Your grade is: D+')
  elif(a>=65 and a<70):
     print('Your grade is: C')
  elif(a>=70 and a<75):
     print('Your grade is: C+')
  elif(a>=75 and a<80):
     print('Your grade is: B')
  elif(a>=80 and a<85):
     print('Your grade is: B+')
  elif(a>=85 and a<90):
     print('Your grade is: A')
  elif(a>=90 and a<=100):
     print('Your grade is: A+')
else:
  print('Wrong Input')