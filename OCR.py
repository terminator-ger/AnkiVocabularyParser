import json
import torch
import os
torch.backends.nnpack.enabled = False
os.environ["USE_NNPACK"] = "0"
import easyocr

class OCR():
    def __init__(self):

        self.reader = easyocr.Reader(['it','de'],gpu=False) # this needs to run only once to load the model into memory

    def read(self, file):
        result = self.reader.readtext(file)
        output = {"rec_poly": [box for box, _, _ in result],
                  "rec_texts": [txt for _, txt, _ in result]
                  }
        with open(f"output/{file.strip(".jpg")}.json", "w+") as fout:
            json.dump(output, fout)

if __name__ == '__main__':
    ocr = OCR()
    ocr.read('img.jpg')