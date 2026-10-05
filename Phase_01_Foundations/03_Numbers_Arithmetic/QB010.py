# Q10. Write a Python program to convert pressure in kilopascals to pounds per square inch, a millimeter
# of mercury (mmHg) and atmosphere pressure.

# Conversion Factors - FORMULA's

# 1 kilopascal (kPa) = 0.145038 psi
# 1 kilopascal (kPa) = 7.50062 mmHg
# 1 kilopascal (kPa) = 0.00986923 atm

kpa = float(input("Enter pressure in kilopascals (kPa): "))

psi = kpa * 0.145038
mmhg = kpa * 7.50062
atm = kpa * 0.00986923

print("Pressure in PSI  :", psi)
print("Pressure in mmHg :", mmhg)
print("Pressure in atm  :", atm)

# Formatted Version

kpa = float(input("Enter pressure in kPa: "))

psi = kpa * 0.145038
mmhg = kpa * 7.50062
atm = kpa * 0.00986923

print(f"PSI  : {psi:.4f}")
print(f"mmHg : {mmhg:.4f}")
print(f"atm  : {atm:.6f}")