from pyfingerprint.pyfingerprint import PyFingerprint

def match_fingerprint():
    try:
        fingerprint_sensor = PyFingerprint('COM1', 57600, 0xFFFFFFFF, 0x00000000)

        if not fingerprint_sensor.verifyPassword():
            raise ValueError("The fingerprint sensor password is incorrect.")

        print("Place your finger on the sensor for matching...")
        while not fingerprint_sensor.readImage():
            pass

        fingerprint_sensor.convertImage(0x01)

        result = fingerprint_sensor.searchTemplate()
        position = result[0]
        accuracy = result[1]

        if position >= 0:
            print(f"Fingerprint matched. Position: {position}, Accuracy: {accuracy}")
        else:
            print("Fingerprint not matched.")

    except Exception as e:
        print("Fingerprint matching failed:", str(e))

# Example usage
match_fingerprint()