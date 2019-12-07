from ATM import *

class User:

    def __init__(self,nama,alamat,notelp,norekening):
        self.nama = nama
        self.alamat = alamat
        self.notelp = notelp
        self.norekening = norekening
     
    def tampil(self):
        return "Nama      : %s\nAlamat    : %s\nNo.Telp   : %s\nNo.Rek    : %s" %(self.nama,self.alamat,self.notelp,self.norekening)
        
    def cek_saldo(self):
        return ATM.lihat_saldo()
        
    def cek_mutasi(self):
        return ATM.daftar_mutasi()
        
    def input_pin(self):
        pin=''
        while pin != '123123':
            pin=input('masukan pin anda : ')
            print("Pin yang anda masukkan salah")
        print(self.tampil())
        self.cek_mutasi()
        self.cek_saldo()
                
                #while pin != 123123:
        
                #self.input_pin()
                #break

a=User('ANDI','Jl. Raya','08123123123','09741111')
a.input_pin()