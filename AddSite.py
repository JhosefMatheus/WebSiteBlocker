from tkinter import messagebox

class AddSite:
    def __init__(self):
        pass

    def adiciona_site(self, site, treeview):
        if site.get().replace(' ', '') == '':
            messagebox.showwarning('Erro', 'Por favor, preencha o campo acima para poder cadastrar um site')
        else:
            treeview.insert('', 'end', values=(site.get()))
        
        site.delete(0, 'end')

