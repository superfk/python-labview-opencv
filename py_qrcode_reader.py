import cv2
import numpy as np
from pyzbar import pyzbar

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

def detect_zbar(source_path, output_path):
    try:
        # load the input image
        image = cv2.imread(source_path)
        # find the barcodes in the image and decode each of the barcodes
        barcodes = pyzbar.decode(image)
        # loop over the detected barcodes
        for barcode in barcodes:
            # extract the bounding box location of the barcode and draw the
            # bounding box surrounding the barcode on the image
            (x, y, w, h) = barcode.rect
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
            # the barcode data is a bytes object so if we want to draw it on
            # our output image we need to convert it to a string first
            barcodeData = barcode.data.decode("utf-8")
            barcodeType = barcode.type
            # draw the barcode data and barcode type on the image
            text = "{} ({})".format(barcodeData, barcodeType)
            cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                0.5, (0, 0, 255), 2)
            # print the barcode type and data to the terminal
            print("[INFO] Found {} barcode: {}".format(barcodeType, barcodeData))
        # show the output image
        cv2.imwrite(output_path,image)
        found = 1
        barcodeData = barcodeData
    except:
        found = 0
        barcodeData = ''
    return (found,barcodeData)

if __name__ == "__main__":
    ret = detect_zbar("meet.png", "decode.png")
    print(ret)