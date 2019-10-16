import nurrahmi
def main():
  #persamaan kuadrat
  a = 6
  b = 4
  c = 2
  
  PK = nurrahmi.PersamaanKuadrat(a,b,c)
  print("PERSAMAAN KUADRAT")
  print("a\t : ", a)
  print("b\t : ", b)
  print("c\t : ", c)
  print("Persamaan Kuadrat\t = ", PK)
  
  #Barisan Aritmatika
  a = 9
  b = 7
  n = 5
  
  BA = nurrahmi.BarisanAritmatika (a, b, n)
  print("BARISAN ARITMATIKA")
  print("a\t : ", a)
  print("b\t : ", b)
  print("n\t : ", n)
  print("Barisan Aritmatika\t = ", BA)
  
  #Basis Induksi
  n = 9
  
  basis = nurrahmi.BasisInduksi(n)
  print("BASIS INDUKSI")
  print("n\t : ", n)
  print("Basis Induksi\t = ", basis)
if __name__ == "__main__":
  main()
