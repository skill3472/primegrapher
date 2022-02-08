import  numpy as np
from matplotlib import pyplot as plt

def prime(n): # Function for checking if a number is a prime number
	if n in (0,1):
		return False
	counter=0
	
	for each in range(2, n):
		if n % each == 0:   
			counter += 1
	
	if counter == 0:
		 return True
	else:
		return False

def arange(a): # Arange the primes in the correct places
    primes = []
    for i in range(a):
        if(prime(i)):
            primes.append(i)
    
    print(f"Here are all the primes: {primes}")

    plt.axes(projection = 'polar')

    for i in range(len(primes)):
        x = np.arange(primes[i])
        plt.polar(x, x, 'g.')

    plt.title(f"Primes of a max value of {a} on a polar graph", fontweight="bold") # Title
    plt.show() # Rendering

def main():
    print("""
 ____       _                 ____                 _               
|  _ \ _ __(_)_ __ ___   ___ / ___|_ __ __ _ _ __ | |__   ___ _ __ 
| |_) | '__| | '_ ` _ \ / _ \ |  _| '__/ _` | '_ \| '_ \ / _ \ '__|
|  __/| |  | | | | | | |  __/ |_| | | | (_| | |_) | | | |  __/ |   
|_|   |_|  |_|_| |_| |_|\___|\____|_|  \__,_| .__/|_| |_|\___|_|   
                                            |_|                    
by skill3472

Input the maximum value: 
    """)

    a = input()

    if int(a) <= 0:
        print('Number is invalid!\n')
        main()
    else:
        arange(int(a))

main()