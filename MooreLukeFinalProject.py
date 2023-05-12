"""
Author: Luke Moore
Date written: 05/4/23
Assignment: Final Project Peer Review 
Short Desc: A program that determines the users age by their DOB and then determines their ideal weight from their height and gender. 
"""

import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Ideal Weight Calculator") # The title is ideal weight calculator, although the formula has been out of date and the output can be subjective. 
root.geometry("500x400")  # Size of window in pixels 


# Label for the age to be input
age_label = tk.Label(root, text="Enter your age (years): ") # Place to enter age. The age doesn't factor into the weight. It was originally the plan to have it do so but I couldn't figure out how to get them to work. 
age_label.pack()

# Entry box for the age input
age_entry = tk.Entry(root) 
age_entry.pack()

# Label for the height input
height_label = tk.Label(root, text="Enter your height (feet, inches): ")
height_label.pack()

# Boxes for the feet and inches 
height_frame = tk.Frame(root)
height_frame.pack()

feet_entry = tk.Entry(height_frame, width=5)
feet_entry.pack(side=tk.LEFT)

inches_entry = tk.Entry(height_frame, width=5) 
inches_entry.pack(side=tk.LEFT)

# Text label for the gender input
gender_label = tk.Label(root, text="Select your gender: ")
gender_label.pack()

# Creates buttons for gender
gender_frame = tk.Frame(root)
gender_frame.pack()

gender_var = tk.StringVar()
male_radio = tk.Radiobutton(gender_frame, text="Male", variable=gender_var, value="male") # Male button 
male_radio.pack(side=tk.LEFT) # Button is to the left 

female_radio = tk.Radiobutton(gender_frame, text="Female", variable=gender_var, value="female") # Female button
female_radio.pack(side=tk.RIGHT) # Button is to the right 

# Function to calculate ideal weight
def calculate_ideal_weight():
    # Takes users' inputs 
    try:
        feet = int(feet_entry.get())
        inches = int(inches_entry.get())
        gender = gender_var.get()

        # Calculates weight
        height_inches = feet * 12 + inches
        if gender == "male":
            ideal_weight = 106 + 6 * (height_inches - 60) # Equation for male weight
        else:
            ideal_weight = 100 + 5 * (height_inches - 60) # Equation for female weight

        # Creates separate result window
        result_window = tk.Toplevel(root)
        result_window.title("Ideal Weight Results")
        result_window.geometry("400x300") # Size

        # Weight results
        result_label = tk.Label(result_window, text="Your ideal weight is {:.1f} lbs.".format(ideal_weight)) # Result text 
        result_label.pack()

    except ValueError:
        # Tells you if there is an error because of invalid input on the original screen. Doesn't let you on the next screen until you provide valid input. 
        error_label = tk.Label(root, text="Invalid input. Please enter valid values.") 
        error_label.pack()

# Create a button to calculate the ideal weight
calculate_button = tk.Button(root, text="Calculate", command=calculate_ideal_weight)
calculate_button.pack()

def clear_input(): # Deletes all of the input in the boxes. 
    age_entry.delete(0, tk.END)
    feet_entry.delete(0, tk.END)
    inches_entry.delete(0, tk.END)

def close_app(): # Closes application
    root.destroy() # Closes main window

# Clear buttom 
clear_button = tk.Button(root, text="Clear", command=clear_input)
clear_button.pack()

# Makes button to close the GUI
close_button = tk.Button(root, text="Close", command=close_app)
close_button.pack()

root.mainloop() # Used to run GUI 
