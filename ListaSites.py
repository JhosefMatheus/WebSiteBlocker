from tkinter import messagebox
import WebBLocker

class ListaSites:
    def __init__(self):
        self.sites = []
        pass

    def adiciona_site(self, site, treeview):
        if site.get().replace(' ', '') == '':
            messagebox.showwarning('Erro', 'Por favor, preencha o campo do site, para poder cadastrar um site')
        else:
            treeview.insert('', 'end', values=(site.get()))
            self.sites.append(site.get())
        
        print(self.sites)
        
        site.delete(0, 'end')
    
    def remove_site(self, treeview):
        site_selecionado = treeview.selection()[0]

        self.sites.remove(treeview.item(site_selecionado)['values'][0])

        treeview.delete(site_selecionado)

        print(self.sites)
    
    def bloquear_sites(self):
        webBlocker = WebBLocker.WebBlocker(self.sites)

        webBlocker.block_websites()
    
    def desbloquear_sites(self):
        webBlocker = WebBLocker.WebBlocker(self.sites)

        webBlocker.unblock_websites()
