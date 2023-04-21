show_version = "*0 CISCO3750-SEC-K9 FTX0003877X "

show_version = show_version.strip()

print("Cleaned version — " + show_version)

model, s_num = show_version.split()[1:3]

if "cisco" in model.lower():
    print("Model:", model)
else:
    print("Model name is absent")

if "3750" in model:
    print("Serial number:", s_num)
else:
    print("Serial number is absent")
