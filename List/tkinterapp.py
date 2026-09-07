# import tkinter as tk

# # 1. Window banao
# app = tk.Tk()

# # 2. Window par bas ek text dikhao
# text = tk.Label(app, text="Hello World!")
# text.pack()

# # 3. Window ko khula rakho
# app.mainloop()



#====================================================================


# import tkinter as tk

# app = tk.Tk()

# # 1. Text dikhane ke liye Label
# label = tk.Label(app, text="Apna Naam Likho:")
# label.pack()

# # 2. Input lene ke liye Entry Box (Yahan user type karega)
# input_box = tk.Entry(app)
# input_box.pack()

# app.mainloop()





#====================================================================

import tkinter as tk

# Function jo button dabane par chalega
def button_clicked():
    print("Button daba diya!")

app = tk.Tk()

# 1. Label
label = tk.Label(app, text="Button dabao niche:")
label.pack()

# 2. Button (command=button_clicked se function connect hota hai)
my_button = tk.Button(app, text="Click Me", command=button_clicked)
my_button.pack()

app.mainloop()