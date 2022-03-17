def info():
  name = input("Enter Your Name : ")
  fname = input("Enter Your Father Name : ")
  mname = input("Enter Your Mother Name : ")

	
  while True:
    try:
      age = int(input("\033[0m Enter your age: "))
      break
    except Exception as e:
      print("\033[31m invalid age\nplease try again ")
      continue
    
  if age >18:
		
    x = len(fname)
    y = x // 2
    print ("Your father middle character: ", fname[y])
    print ("Your Mother middle character: ", mname[y])
  else:
		
    fx = fname [-1]
    mx = mname [-1]
    print ("You are not 18")
    print ("Your father last character: ", fx)
    print ("Your Mother last character: ", mx)
    rep = input('\n[+] press restart for restart......')
info()    
	  
info()