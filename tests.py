# # # def encode_to_binary(data): 
 
# # #     binary_msg=""     
# # #     for letter in data:  
# # #         ascii_val=ord(letter) 
# # #         bin=""  
# # #         while ascii_val>0: 
# # #             remainder=ascii_val%2 
# # #             bin=str(remainder)+bin 
# # #             ascii_val=ascii_val//2 
# # #         binary_msg+=bin.zfill(8)    
# # #     return binary_msg

# # # def test_encode_to_binary():

# # #     assert encode_to_binary("A") == "01000001"  
# # #     assert encode_to_binary("AB") == "0100000101000010" 
# # #     assert encode_to_binary("") == "" 
# # #     assert encode_to_binary("###") == "001000110010001100100011"

# # # test_encode_to_binary()
# # # print("All tests for encode_to_binary passed!")

# # # #####################
# # # #####################

# # # def decode_from_binary(binary_data): 

# # #     msg="" 
# # #     for i in range(0,len(binary_data),8): 
# # #         byte=binary_data[i:i+8] 
# # #         ascii_val=int(byte,2) 
# # #         msg=msg+chr(ascii_val) 
# # #     return msg

# # # def test_decode_from_binary():

# # #     assert decode_from_binary("01000001") == "A"  
# # #     assert decode_from_binary("0100000101000010") == "AB"  
# # #     assert decode_from_binary("") == ""  
# # #     assert decode_from_binary("001000110010001100100011") == "###"  

# # # test_decode_from_binary()
# # # print("All tests for decode_from_binary passed!")

# # # ######################
# # # ######################

# # # def hide_message(image_path, output_path, message):

# # #     with open(image_path, 'rb') as image_file:  
# # #         image_data = bytearray(image_file.read()) 

# # #     header = image_data[:54]   

# # #     pixel_data = image_data[54:] 

# # #     binary_message = encode_to_binary(message) + encode_to_binary("###")

# # #     if len(binary_message) > len(pixel_data):
# # #         raise ValueError("The message is too large to fit in this image.") 

# # #     for i in range(len(binary_message)):  
# # #         pixel_data[i] = (pixel_data[i] & 0xFE) | int(binary_message[i])

# # #     with open(output_path, 'wb') as output_file: 
# # #         output_file.write(header + pixel_data) 

# # # def test_hide_message():

# # #     input_image_path = "input.bmp"  
# # #     output_image_path = "output.bmp"
# # #     secret_message = "Testing message 101"

# # #     try:
# # #         hide_message(input_image_path, output_image_path, secret_message)
# # #         print(f"Message successfully hidden in {output_image_path}. Test successful.")
# # #     except Exception as e:
# # #         print(f"Test failed: {e}")

# # # test_hide_message()

# # # ######################
# # # ######################

# # # def reveal_secret_message(image_path): #This function extracts the secret message from the output image.

# # #     with open(image_path, 'rb') as image_file:  #It Opens the BMP image file in RB and loads it into a bytearray.
# # #         image_data = bytearray(image_file.read())
# # #     pixel_data = image_data[54:]
# # #     binary_message = ''.join(str(byte & 1) for byte in pixel_data)#It Extracts the(LSBs) from the pixel data and joins them to reform the binary message.
# # #     message = decode_from_binary(binary_message)  #It Converts the binary string into text.
# # #     delimiter_position = message.find("###") #It Looks for the delimiter ("###") to determine where the hidden message ends.
# # #     if delimiter_position != -1: #If the delimiter is found it returns the message up to the delimiter.
# # #         return message[:delimiter_position]
# # #     return "No hidden message found."

# # # def test_reveal_secret_message():
# # #     input_image_path = "output.bmp"  
# # #     expected_message = "Testing message 101"

# # #     try:
# # #         hidden_message = reveal_secret_message(input_image_path)
# # #         assert hidden_message == expected_message, f"Expected '{expected_message}', got '{hidden_message}'"
# # #         print("Test for reveal_secret_message passed!")
# # #     except Exception as e:
# # #         print(f"Test failed: {e}")

# # # test_reveal_secret_message()

