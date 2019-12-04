class ATM:
    
    def lihat_saldo():
        saldo='Rp 200.000,-'
        print('saldo anda adalah', saldo)
        
    def daftar_mutasi():
        print('daftar mutasi anda :')
        mutasi=['debit  200.000','kerdit 50.000','kredit 100.000','debit  75.000']
        for i in mutasi:
            print(i)