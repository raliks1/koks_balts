class Kvadrats:

  def info(self):
    return "Kvadrāts", 4


class Taisnsturis:

  def info(self):
    return "Taisnstūris", 4


class Trijsturis:

  def info(self):
    return "Trijsturis", 3


def izdrukat(objekts):
  nosaukums, malas = objekts.info()
  print(f"{nosaukums} — {malas} malas")


for d in [Kvadrats(), Taisnsturis(), Trijsturis()]:
  izdrukat(d)