class RemoveSite:
    def __init__(self):
        pass

    def remover_site(self, treeview):
        item_selecionado = treeview.selection()[0]
        treeview.delete(item_selecionado)
