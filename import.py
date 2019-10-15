import geometri2D
def main():
  p = 9
  l = 4
  
  luas = geometri2D.LuasPersegiPanjang(p, l)
  kel  = geometri2D.KelilingPersegiPanjang(p, l)
  
  print("PERSEGI PANJANG")
  print("Panjang\t  : ",p)
  print("Lebar\t    : ",l)
  print("Luas\t     : ", luas)
  print("Keliling\t : ", kel)
  
  jarijari= 3
  
  luas = geometri2D.LuasLingkaran(jarijari)
  kel  = geometri2D.KelilingLingkaran(jarijari)
  
  print("\nLINGKARAN")
  print("Jari-Jari\t  : ",jarijari)
  print("Luas\t       : ", luas)
  print("Keliling\t   : ", kel)
  
if __name__ == "__main__":
  main()
