ip_address = input("Please enter an IP address: ")

octets = [int(octet) for octet in ip_address.split(".")]

for i, oct in enumerate(octets):
    print("---------------Octet " + str(i+1) + "-------------------")
    print("Decimal: " + str(oct))
    print("Hex: " + str(hex(oct)))
    print("Binary: " + str(bin(oct)))
print("-----------------------------------------") 