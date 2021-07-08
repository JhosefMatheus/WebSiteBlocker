from tkinter import *
from tkinter import ttk
import ListaSites

listaSites = ListaSites.ListaSites()

window = Tk()

width = 400
height = 435

width_screen = window.winfo_screenwidth()
height_screen = window.winfo_screenheight()

position_x = int(width_screen/2) - int(width/2)
position_y = int(height_screen/2) - int(height/2)

window.geometry(f'{width}x{height}+{position_x}+{position_y}')
window.resizable(False, False)

block_site_lists = ttk.Treeview(
    window,
    columns=('site',),
    show='headings',
)

block_site_lists.column('site', minwidth=0, width=250)

block_site_lists.heading('site', text='SITE')

block_site_lists.pack(pady=15)

novo_site = Entry(
    window
)

novo_site.pack(pady=5)

button_add_site = Button(
    window,
    text='Adicionar site',
    command=lambda:listaSites.adiciona_site(novo_site, block_site_lists)
).pack(pady=5)

button_remover_site = Button(
    window,
    text='Remover site',
    command=lambda:listaSites.remove_site(block_site_lists)
).pack(pady=5)

button_bloquear_sites = Button(
    window,
    text='Bloquear sites',
    command=lambda:listaSites.bloquear_sites()
).pack(pady=5)

button_desbloquear_sites = Button(
    window,
    text='Desbloquear sites',
    command=lambda:listaSites.desbloquear_sites()
).pack(pady=5)

window.mainloop()
