
def FizzBuzz():
	inp = input("Enter number ")
	if(inp.isdigit() == True):
		fiz = ""
		buz = ""
		if(int(inp) % 3 == 0):
			fiz = "Fizz"
		if(int(inp) % 5 == 0):
			buz = "Buzz"
		else:
			if(int(inp) % 3 != 0):
				fiz = inp
		print(fiz+buz)
	else:
		print("Type in a digit next time")
		




def main():
	FizzBuzz()
    
if __name__ == "__main__":
    main()
	
