class WebBlocker:
    def __init__(self, sites_to_block):
        self.windows_host = 'C:\Windows\System32\drivers\etc\hosts'
        self.redirect = '127.0.0.1'
        self.sites_to_block = sites_to_block

    def block_websites(self):
        with open(self.windows_host, 'r+') as hostfile:
            hosts = hostfile.read()

            for site in self.sites_to_block:
                if site not in hosts:
                    hostfile.write(f'{self.redirect} {site}\n')
    
    def unblock_websites(self):
        with open(self.windows_host, 'r+') as hostfile:
            hosts = hostfile.readlines()
            hostfile.seek(0)

            for host in hosts:
                if not any(site in host for site in self.sites_to_block):
                    hostfile.write(host)
            
            hostfile.truncate()
