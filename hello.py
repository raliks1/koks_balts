# prasa lietotājam vārdu
# name = input("Kā tevi sauc? ")

# saka Sveiks lietotājiem
# print("sveiks, ")
# print(name)

# print("Sveiki, \"labie skolēni\"")
# print(*objects, sep=' ', ends'\n', file=sys.stdout, flush=False)
# print("Ralfs", "Aliks-Romāns", sep='?????')
# print("Sveiks, ", end="")
name = input("Kā tevi sauc? ")

name = name.strip().title()


print("Sveiks,", name)
print(f"Sveiks, {name}")
