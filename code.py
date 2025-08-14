import tkinter as tk


root = tk.Tk()
root.title("GROCERIES LIST")
root.geometry("300x400")
g_entry = tk.Entry(root, font=("Arial", 12))
g_entry.pack(pady=5)

add_btn = tk.Button(root, text = "Add")
add_btn.pack(pady=5)

g_list = tk.Listbox(root, width=40, height=10)
g_list.pack(pady=5)


delete_btn = tk.Button(root, text = "Delete Grocery")
delete_btn.pack(pady=5)


def add_g():
    g = g_entry.get().strip()
    if g == "":
        print("Please enter a Grocery!")
    elif len(g)<3:
        print("Grocery name too short!")
    elif g in g_list.get(0, tk.END):
        print("Grocery already exists!")
    else:
        g_list.insert(tk.END, g)
        g_entry.delete(0, tk.END)

add_btn.config(command=add_g)

def delete_g():
    selected = g_list.curselection()
    if selected:
        g_list.delete(selected)

delete_btn.config(command=delete_g)

root.mainloop()
