from PIL import Image
import os
import numpy as np
import matplotlib.pyplot as plt



def summary():
    for entry in os.scandir("images\Claude Monet"):
        if (entry.path.endswith(".jpg") and entry.is_file()):
            print(entry.path)
            image = Image.open(entry.path)
            print(f"Format ---> {image.format}")
            print(f"Mode ---> {image.mode}")
            print(f"SIZE ---> {image.size}")

            pixels = np.asarray(image)
            print(f'Data Type: {pixels.dtype}')
            print('Min: %.2f, Max: %.2f' % (pixels.min(), pixels.max()))
            print('MEAN: %.2f' % (pixels.mean()))
            
            print("AFTER NORMALIZATION")
            pixels = pixels.astype('float32')
            pixels /= 255.0
            print('Min: %.2f, Max: %.2f' % (pixels.min(), pixels.max()))
            print('MEAN: %.2f' % (pixels.mean()))

            # global centering of data (set mean at 0)
            print("AFTER CENTERING")
            pixels.mean()
            pixels -= pixels.mean()
            print('Min: %.2f, Max: %.2f' % (pixels.min(), pixels.max()))
            print('MEAN: %.2f' % (pixels.mean()))

def resize():
    for entry in os.scandir("images\Claude Monet"):
        if (entry.path.endswith(".jpg") and entry.is_file()):
            print(entry.path)
            image = Image.open(entry.path)
            image= image.resize((128,128))
            image.save(entry.path, format="JPEG")

