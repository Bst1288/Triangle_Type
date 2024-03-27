import tkinter as tk

# Triangle Type
def triangle_type(side_1, side_2, side_3):
      if side_1 + side_2 > side_3 and side_1 + side_3 > side_2 and side_2 + side_3 > side_1:
        if side_1 == side_2 == side_3:
          triangle_type = " Equilateral triangle"
        elif side_1 == side_2 or side_1 == side_3 or side_2 == side_3:
          triangle_type = " Isosceles triangle"
        elif pow(side_1,2) + pow(side_2,2) == pow(side_3,2) or pow(side_1,2) + pow(side_3,2) == pow(side_2,2) or pow(side_3,2) + pow(side_2,2) == pow(side_1,2):
          triangle_type = " Right Triangle"
        else:
          triangle_type = " Scalene triangle"
      else:
        triangle_type = " Invalid triangle"
      return triangle_type

def triangle_type_output():
  try:
    side_1 = int(entry_side1.get())
    side_2 = int(entry_side2.get())
    side_3 = int(entry_side3.get())

    # check input side is between 0 - 999999
    if 0 < side_1 <= 999999 and 0 < side_2 <= 999999 and 0 < side_3 <= 999999:
      # show result in Entry widget
      entry_result.delete(0, tk.END)
      entry_result.insert(40, triangle_type(side_1, side_2, side_3))
    else:
      if side_1 == 0 or side_2 == 0 or side_3 == 0:
        error_message = " Error, input value is zero" # error if input 0
      
      elif side_1 < 0 or side_2 < 0 or side_3 < 0:
        error_message = " Error, input is negative integers" # error if input is negative integer
      
      if side_1 > 999999 or side_2 > 999999 or side_3 > 999999:
        error_message = " Error, input value exceeds 999999" # error if input value exceeds 999999
      
      entry_result.delete(0, tk.END)
      entry_result.insert(40, error_message)
  except:
    error_message = " Error, input is non-numeric value" # error if input isn't integer or no input or space
    entry_result.delete(0, tk.END)
    entry_result.insert(40, error_message)

# -------------------- Interface -------------------- #
root = tk.Tk()
root.geometry("490x320")
root.configure(bg='#D6D7EC')
root.title("Triangle Type")

# "Enter the length of sides" Label
label_title = tk.Label(text="Enter the length of sides", font=("Arial", 20), bg='#D6D7EC')
label_title.pack(pady=20)
label_title.place(x=20,y=20)

# "Side 1" Label
label_side1 = tk.Label(text="Side 1", font=("Arial", 20), bg='#D6D7EC')
label_side1.place(x=20, y=60)
# "Side 1" Entry widget
entry_side1 = tk.Entry(width=28, font=18, bg='#CDCC03')
entry_side1.place(x=160, y=65)

# "Side 2" Label
label_side2 = tk.Label(text="Side 2", font=("Arial", 20), bg='#D6D7EC')
label_side2.place(x=20, y=100)
# "Side 2" Entry widget
entry_side2 = tk.Entry(width=28, font=18, bg='#CDCC03')
entry_side2.place(x=160, y=105)

# Side 3" Label
label_side3 = tk.Label(text="Side 3", font=("Arial", 20), bg='#D6D7EC')
label_side3.place(x=20, y=140)
# "Side 3" Entry widget
entry_side3 = tk.Entry(width=28, font=18, bg='#CDCC03')
entry_side3.place(x=160, y=145)

# Label "Result"
label_result = tk.Label(text="Result", font=("Arial", 20), bg='#D6D7EC')
label_result.place(x=265, y=200)

# Enter butt
button_calculate = tk.Button(text="Enter", font=("Arial", 17), bg='#CDCC03', command = triangle_type_output)
button_calculate.place(x=20, y=250)

# Entry widget "Result"
entry_result = tk.Entry(width=28, font=18, bg='#CDCC03')
entry_result.place(x=160, y=260)

root.mainloop()
