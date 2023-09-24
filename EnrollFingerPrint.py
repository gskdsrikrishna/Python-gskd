from pyfingerprint.pyfingerprint import PyFingerprint

def enroll_fingerprint():
    try:
        fingerprint_sensor = PyFingerprint('COM1', 57600, 0xFFFFFFFF, 0x00000000)

        if not fingerprint_sensor.verifyPassword():
            raise ValueError("The fingerprint sensor password is incorrect.")

        print("Place your finger on the sensor for enrollment...")
        while not fingerprint_sensor.readImage():
            pass

        fingerprint_sensor.convertImage(0x01)
        fingerprint_sensor.createTemplate()

        position = fingerprint_sensor.storeTemplate()
        print(f"Fingerprint enrolled successfully. Position: {position}")

    except Exception as e:
        print("Fingerprint enrollment failed:", str(e))

# Example usage
enroll_fingerprint()