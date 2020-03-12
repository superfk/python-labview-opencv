import cv2
import numpy as np

# Display barcode and QR code location
def display(im, bbox):
    n = len(bbox)
    for j in range(n):
        cv2.line(im, tuple(bbox[j][0]), tuple(bbox[ (j+1) % n][0]), (255,0,0), 3)

    # Display results
    return im

def detect_qr_code(source_path, output_path):
    # read source image
    inputImage = cv2.imread(source_path)
    # Create a qrCodeDetector Object
    qrDecoder = cv2.QRCodeDetector()

    # Detect and decode the qrcode
    data,bbox,rectifiedImage = qrDecoder.detectAndDecode(inputImage)
   
    if len(data)>0:
        print("Decoded Data : {}".format(data))
        decode_data = data
        found = 1
        im = display(inputImage,bbox)
        cv2.imwrite(output_path,im)
    else:
        print("QR Code not detected")
        found = 0
        decode_data = ""
    return (found, decode_data)