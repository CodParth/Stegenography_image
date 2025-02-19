import cv2

def decrypt_image(image_path):
    try:
        # Load stored encryption data
        try:
            with open("encryption_data.txt", "r") as f:
                stored_password = f.readline().strip()
                msg_length = int(f.readline().strip())
        except FileNotFoundError:
            raise ValueError("Error: Encryption data not found. Run encryption first.")

        img = cv2.imread(image_path)
        if img is None:
            raise ValueError("Error: Unable to load the image. Check the file path.")

        height, width, _ = img.shape
        if msg_length > height * width * 3:
            raise ValueError("Error: Message length is larger than image capacity.")

        input_password = input("Enter passcode for decryption: ")
        if input_password != stored_password:
            print("Incorrect password. Access denied!")
            return

        message = ""
        n, m, z = 0, 0, 0

        for _ in range(msg_length):
            message += chr(img[n, m, z])  # Retrieve ASCII character
            z += 1
            if z == 3:  # Move to next pixel after reading all 3 RGB channels
                z = 0
                m += 1
                if m >= width:
                    m = 0
                    n += 1

        print("Decrypted message:", message)

    except Exception as e:
        print(e)

# Example usage
if __name__ == "__main__":
    img_path = "encryptedImage.png"  # Use PNG to prevent data loss
    decrypt_image(img_path)
