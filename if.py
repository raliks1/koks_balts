import os
os.system('cls') #attira terminala logu pasa sakuma
print("\n") # ieliek tuksu rindinu pirms izdrukas

#x = int(input("Kāda ir x vērtība? "))
#y = int(input("Kāda ir y vērtība? "))

#if x != y:
    #print("x nav vienāds y")
#else:                                 # or    elif x == y:
    #print("x ir vienāds ar y")
punkti = int(input("punkti:"))

if punkti >= 90 and punkti <= 100:
    print("Vērtējums: 10")
elif punkti >=80 and punkti < 90:
    print("Vērtējums: 9")
elif punkti >=70 and punkti < 80:
    print("Vērtējums: 8")
elif punkti >=60 and punkti < 70:
    print("Vērtējums: 7")
else:
    print("Vērtējums: n/v")