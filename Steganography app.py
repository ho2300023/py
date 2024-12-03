def encode_to_binary(data): #Changes string to binary.
 
    binary_msg=""     #Creates an empty string to store the binary number of the input data.
    for letter in data:   #Iterates through each character in the string.
        ascii_val=ord(letter) #Converts the character to its ASCII valu.
        bin=""      #I defined bin and created an empty string
        while ascii_val>0:      # While loops on each character until the ASCII value is fully converted to binary.
            remainder=ascii_val%2 #calculates the remainder when dividing the ASCII value by 2(binary).
            bin=str(remainder)+bin #The rest of the binary string we add to it the calculated binary digit
            ascii_val=ascii_val//2 #I divided the integer to move to the next binary number.
        binary_msg+=bin.zfill(8)    #Ensures each byte is exactly 8 bits.
    return binary_msg


def decode_from_binary(binary_data): #Changes binary to string.

    msg="" # It defines msg and creates an empty string to store the message.
    for i in range(0,len(binary_data),8): # It groups every 8 bits together.
        byte=binary_data[i:i+8] # The slicing iterates with steps of 8 starting from a multiple of 8 and ending multiple + 8.
        ascii_val=int(byte,2) # It converted the binary groups to their originl ASCII int(values.
        msg=msg+chr(ascii_val) # It converts the ASCII values tto characters and addsthem msg(decoded message) .
    return msg


def hide_message(image_path, output_path, message):

    with open(image_path, 'rb') as image_file:  # It opens the BMP image file in rb and run it through bytearray.
        image_data = bytearray(image_file.read()) # It read the image in a readable format(Bytearray).

    header = image_data[:54]    # We take out the header (first 54 bytes).

    pixel_data = image_data[54:] # We take the pixel data which starts after 54 bytes after the header to encode the message.

    binary_message = encode_to_binary(message) + encode_to_binary("###")# It Converts the secret message into binary and adds the delimiter at the end

    if len(binary_message) > len(pixel_data): # It the encoded message is too large it will give an error with the following msg.
        raise ValueError("The message is too large to fit in this image.") 

    for i in range(len(binary_message)):  # It Loops through each binary bit and encodes it into the pixel data.
        pixel_data[i] = (pixel_data[i] & 0xFE) | int(binary_message[i])#It sets the LSB to 0, leaving all other bits unchanged.

    # Write the new image data with the hidden message to the output file.
    with open(output_path, 'wb') as output_file: #It opens the output file in RB(read binary mode).
        output_file.write(header + pixel_data) #Rewrittes the image by adding the unchanged header with our modified pixel data.


def reveal_secret_message(image_path): #This function extracts the secret message from the output image.

    with open(image_path, 'rb') as image_file:  #It Opens the BMP image file in RB and loads it into a bytearray.
        image_data = bytearray(image_file.read())
    pixel_data = image_data[54:]
    binary_message = ''.join(str(byte & 1) for byte in pixel_data)#It Extracts the(LSBs) from the pixel data and joins them to reform the binary message.
    message = decode_from_binary(binary_message)  #It Converts the binary string into text.
    delimiter_position = message.find("###") #It Looks for the delimiter ("###") to determine where the hidden message ends.
    if delimiter_position != -1: #If the delimiter is found it returns the message up to the delimiter.
        return message[:delimiter_position]
    return "No hidden message found."


def main():
    print("Welcome to Steganography!")
    print("Choose an option:")
    print("1. Encode (Hide a secret message)")
    print("2. Decode (Extract a hidden message)")
    choice = input("Enter your choice (1 or 2): ").strip()

    if choice == '1':
        image_path = input("Enter your BMP image path: ").strip() 
        output_path = input("Enter the path you'd like to save the output BMP image: ").strip()
        secret_message = input("Enter the secret message you'd like to hide: ").strip()
        try:
            hide_message(image_path, output_path, secret_message)
            print(f"Message successfully hidden, Saved to {output_path}.")
        except Exception as e:
            print(f"Error: {e}")
    elif choice == '2':
        image_path = input("Enter the path to the BMP image to decode: ").strip()
        try:
            hidden_message = reveal_secret_message(image_path)
            print("The secret message is:")
            print(hidden_message)
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("You've entered an invalid option! Please restart the program and enter either 1 or 2.")

if __name__ == "__main__":
    main()
