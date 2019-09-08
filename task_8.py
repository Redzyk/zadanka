weight = int(input("Weight: "))
while True:
  unit = input("(K)g or (L)bs? ")
  if unit.upper() == "K":
    kg_to_lb = int(weight // 0.45)
    print(f"It's {kg_to_lb} pounds.")
    break
  elif unit.upper() == "L":
    lb_to_kg = int(weight * 0.45)
    print(f"It's {lb_to_kg} kilos.")
    break
  else:
    print("""Please use "K" or "L". """)