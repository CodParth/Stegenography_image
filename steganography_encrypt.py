import cv2
import os

def encrypt_image(image_path, output_path, message, password):
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError("Error: Unable to load the image. Check the file path.")

    height, width, _ = img.shape
    max_length = height * width * 3  # Maximum characters that can be stored

    if len(message) > max_length:
        raise ValueError("Error: Message is too long to fit in the image.")

    # Store password and message length
    with open("encryption_data.txt", "w") as f:
        f.write(f"{password}\n{len(message)}\n")

    n, m, z = 0, 0, 0
    for char in message:
        img[n, m, z] = ord(char)  # Convert character to ASCII and store
        z += 1
        if z == 3:  # Move to next pixel after modifying all 3 RGB channels
            z = 0
            m += 1
            if m >= width:  # Move to next row if column limit is reached
                m = 0
                n += 1

    cv2.imwrite(output_path, img)  # Save as PNG to prevent compression
    print(f"Encryption successful! Encrypted image saved as {output_path}")
    os.system(f"start {output_path}")  # Opens the image on Windows

# Example usage
if __name__ == "__main__":
    img_path = "mypic.png"  # Replace with correct image path
    output_img = "encryptedImage.png"
    secret_msg = input("Enter secret message: ")
    passcode = input("Enter a passcode: ")

    encrypt_image(img_path, output_img, secret_msg, passcode)
