def bits_to_bytes(bits):
    return bits / 8

def bytes_to_mb(bytes):
    return bytes / (1024 ** 2)

def bytes_to_gb(bytes):
    return bytes / (1024 ** 3)

def bytes_to_tb(bytes):
    return bytes / (1024 ** 4)

def main():
    bits = int(input("Enter the number of bits: "))
    bytes = bits_to_bytes(bits)
    
    print("In Megabytes (MB):", bytes_to_mb(bytes))
    print("In Gigabytes (GB):", bytes_to_gb(bytes))
    print("In Terabytes (TB):", bytes_to_tb(bytes))

if __name__ == "__main__":
    main()
