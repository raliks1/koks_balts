import os
os.system('cls') #attira terminala logu pasa sakuma
print("\n") # ieliek tuksu rindinu pirms izdrukas

#1. Perfekti skaitļi

# for sk in range(1, 10000):
#     summa = 0
#     for i  in range(1, sk):
#         if sk % i == 0:
#             summa = summa + i
#     if summa == sk:
#         print(f"{sk} ir perfekts skaitlis")

#2.Skaitļu piramīda

n = int(input("ievadi rindu skaitu: "))
rinda = 1
while rinda <  n:
    for i in  range(1, rinda):
        print(i)
    rinda += 15
# for i in range(n):
#     for j in range(i+1):
#         print(j+1, end=" ")
#     print()


#3. Fibonači virkne



#4.Pirmskaitļi


