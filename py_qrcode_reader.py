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
    try:
        # read source image
        inputImage = cv2.imread(source_path)
        # Create a qrCodeDetector Object
        qrDecoder = cv2.QRCodeDetector()

        # Detect and decode the qrcode
        data,bbox,rectifiedImage = qrDecoder.detectAndDecode(inputImage)
    
        if len(data)>0:
            message = "Decoded Data : {}".format(data)
            print(message)
            decode_data = data
            found = 1
            im = display(inputImage,bbox)
            cv2.imwrite(output_path,im)
        else:
            message = "QR Code not detected"
            print(message)
            found = 0
            decode_data = message
    except Exception as e:
        message = "Internal Error: {}".format(e)
        print(message)
        found = 0
        decode_data = message
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
        message = "Internal Error: {}".format(e)
        print(message)
        found = 0
        barcodeData = message
    return (found,barcodeData)

def detect_zbar_numpy(source_img_list, output_path):
    try:
        # load the input image 2d array to numpy array
        image = np.asarray(source_img_list, dtype=np.uint8)
        # convert gray array to BGR
        image = cv2.cvtColor(image,cv2.COLOR_GRAY2BGR)
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
    except Exception as e:
        message = "Internal Error: {}".format(e)
        print(message)
        found = 0
        barcodeData = message
    return (found,barcodeData)

def debug(source_img_list, output_path):
    image = np.asarray(source_img_list)
    image = np.reshape(image,(200,200,4))
    msg = "{}".format(image.shape)
    return msg

if __name__ == "__main__":
    ret = detect_zbar_numpy("t3.png", "decode.png")
    print(ret)