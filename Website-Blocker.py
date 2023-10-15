import tkinter as tk
from tkinter import messagebox

# Define the function to block websites
def block_websites():
    host_path = r'C:\Windows\System32\drivers\etc\hosts'
    ip_address = '127.0.0.1'

    websites = websites_entry.get("1.0", "end-1c").split(",")

    try:
        with open(host_path, 'r+') as host_file:
            content = host_file.read()
            for website in websites:
                if website.strip() not in content:
                    host_file.write(ip_address + " " + website.strip() + '\n')
            messagebox.showinfo("Success", "Websites blocked successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create the main GUI window
root = tk.Tk()
root.geometry('500x300')
root.title("Website Blocker")

# Create labels and entry
tk.Label(root, text='Website Blocker', font='arial 20 bold').pack(pady=10)
tk.Label(root, text='Enter Websites (comma-separated):', font='arial 12').pack()
websites_entry = tk.Text(root, font='arial 12', height=2, width=40, wrap=tk.WORD)
websites_entry.pack()

# Create the Block button
block_button = tk.Button(root, text='Block', font='arial 12 bold', command=block_websites)
block_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
