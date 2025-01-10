# Make a code that calculates volume of sphere, area of triangle and make changes into the class project 3 in 1 task.

from random import randint
from time import time


MAX = 5
MIN = 1
pi = 3.14159

 
  

  

def calculate_sphere_volume():

      r = randint(MIN, MAX)
      

      volume = (4/3) * pi * (r**3)

      
      
      display_time = time()

      
      print("Calculate volume of the sphere. (up to 2 decimals)")
      print(f"The radius is {r}.")
      
      
      

      answer = float(input("My answer: "))
      input_time = time()

      correct = round(volume, 2) == round(answer, 2)
      print(f"RESULT: {correct}")
      
      print(f"correct answer {volume}")
      elapsed = input_time - display_time

      print(f"Time elapsed: {elapsed:.3} seconds")

def calculate_area_of_triangle():
    
    l = randint(MIN, MAX)
    b = randint(MIN, MAX)


   
   
   
   
    area:.3 = (1/2) * l * b

    
    print("Calculate area of the triangle.(up to 2 decimals)")
    print(f"The length and base are {l} and {b} respectively.")

    display_time = time()

    answer = float(input("My answer: "))
    input_time = time()
    correct = round(area, 2) == round(answer, 2)

    
    elapsed = input_time - display_time

    print(f"RESULT: {correct}")
    print(f"Time elapsed: {elapsed:.3} seconds")
    

calculate_sphere_volume()

calculate_area_of_triangle()



input("Press Enter to exit...")
