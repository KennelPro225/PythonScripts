import tkinter as tk

root= tk.Tk()
root.minsize(1000,500)
root.maxsize(1000,500)

# My first Frame for the Logo

Logo_frame= tk.Frame(root, width=800, height=100, bg="red")
Logo_frame.pack(fill="y")

# frame for entry permit to enter the Youtube Url for downloading
frame_entry = tk.Frame(root, width=600, height=100, bg="gray")
frame_entry.pack(fill="y", pady=20)
url_entry = tk.Entry(frame_entry, width=50, borderwidth=4)
url_entry.pack()

# Frame for controle

frame_control= tk.Frame(root, width=800, height=300,bg="blue")
frame_control.pack(fill="both",pady=20)




root.mainloop()
                      