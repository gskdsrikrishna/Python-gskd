import datetime
import time

def binary_clock():
    while True:
        current_time = datetime.datetime.now().time()
        binary_time = current_time.strftime("%H:%M:%S")
        binary_digits = [bin(int(digit))[2:].zfill(4) for digit in binary_time.replace(":", "")]
        
        print("Binary Clock:")
        for digit in binary_digits:
            for bit in digit:
                if bit == "0":
                    print("O", end=" ")
                else:
                    print("X", end=" ")
            print()
        
        print("------------------------")
        time.sleep(1)

binary_clock()