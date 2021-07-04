from tkinter import *
from tkinter import ttk

window = Tk()

width = 500
height = 500

width_screen = window.winfo_screenwidth()
height_screen = window.winfo_screenheight()

position_x = int(width_screen/2) - int(width/2)
position_y = int(height_screen/2) - int(height/2)

window.geometry(f'{width}x{height}+{position_x}+{position_y}')
window.resizable(False, False)

block_site_lists = ttk.Treeview(window)

block_site_lists['columns'] = (
    'ID',
    'Site'
)

block_site_lists.column('#1')
block_site_lists.column('ID', anchor=W)
block_site_lists.column('Site', anchor=CENTER)

block_site_lists.heading('#1', text='ID', anchor=W)
block_site_lists.heading('Site', text='Site', anchor=W)

block_site_lists.pack(pady=20)

window.mainloop()
