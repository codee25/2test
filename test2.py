raw = "   !!!SuPer     MEGA--Phone!!!  5000   BLACK!!!   "

raw1 = raw.strip()
print(raw1)
raw2 = raw1.replace("!", "")
print(raw2)
raw3 = raw2.replace("  ", "")
print(raw3)
raw4 = raw3.lower().title()
print(raw4)
rawindex = raw4.startswith("Super")
print(rawindex)
before, sep, after = raw4.partition("5000")
Original: f"Початковий рядок : {raw}"
Clean: f"Очищений рядок : {raw4}"
Starts_with_super: f"Починається з 'Super': {raw4.startswith('Super')}"
Before_number: f"До числа : {before}"
After_number: f"Після числа : {after}"
