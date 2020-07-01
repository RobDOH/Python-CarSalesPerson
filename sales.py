#Student Robert Doult
#Date 09022019
#Class CSCI 1511 - Lab 2-4
#4. Write a Car Salesman program where the user enters the base price of a car.
#The program should add on a bunch of extra fees such as tax, license, dealer prep, and destination charge.
#Make tax and license a percent of the base price.#
#The other fees should be set values.
#Display the actual price of the car once all the extras are applied.


base_price = input ("Please enter the Base price of the car.$")
base_price = float (base_price)
tax = base_price * 0.075
license = base_price * 0.10
dealer = 500
destination = 900
total = base_price + tax + license + dealer + destination
print ("The tax rate in Ohio is 7.5% of the base price of the car which is $""{0:.2f}".format(tax))
print ("The license rate in Ohio is 10% of the base price of the car which is $""{0:.2f}".format(license))
print ("The dealer prep is a flat fee of $500")
print ("The dealer destination charge is a flat fee of $900")
print("\nThe actual price of the car once all the extras are applied:$ ""{0:.2f}".format(total))

input("\n\nPress the enter key to exit.")


