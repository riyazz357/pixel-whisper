import numpy as np
from PIL import Image

def message_to_binary(message):
    '''conver the string to its binary representation'''
    if type(message) == str:
        # Convert string to binary: 'A' -> 01000001
        return ''.join([format(ord(i), "08b") for i in message])
    elif type(message) == bytes or type(message) == np.ndarray:
        return [format(i, "08b") for i in message]
    elif type(message) == int or type(message) == np.uint8:
        return format(message, "08b")
    else:
        raise TypeError("Input type not supported")
    
def encode_image(image_path,secret_message,output_path):
    '''hides a secret message inside a image'''

    image=Image.open(image_path,'r')
    width,height=image.size
    img_data=np.array(list(image.getdata()))

    # add a delimiter to the message to indicate the end
    secret_message += "#####"
    binary_message=message_to_binary(secret_message)
    data_len=len(binary_message)
    total_pixels=img_data.size // 3

    if data_len > total_pixels:
        raise ValueError("message is to large for this message")
    
    idx=0
    for i in range(len(img_data)):
        for j in range(3):
            if idx < data_len :
                pixel_bin=list(message_to_binary(img_data[i][j]))
                pixel_bin[-1]=binary_message[idx]

                img_data[i][j]=int(''.join(pixel_bin),2)
                idx+=1
    # reshape the array back to image dim and save it 
    img_data=img_data.reshape((height,width,3))
    encode_image=Image.fromarray(img_data.astype('uint8'),image.mode)
    encode_image.save(output_path)
    print(f"saved encoed image to:{output_path}")

