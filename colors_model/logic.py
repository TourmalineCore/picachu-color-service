import numpy as np
import cv2
import io
import PIL.Image as Image
from datetime import datetime
from sklearn.cluster import KMeans
from collections import Counter
import imageio

def get_modified_img(image):
    modified_img = cv2.resize(image, 
                              (600, 400), 
                              interpolation = cv2.INTER_AREA)
    modified_img = modified_img.reshape(modified_img.shape[0] * modified_img.shape[1], 3)
    return modified_img


def get_base_colors(image_path, number_of_colours):
    image = image_path
    image=get_modified_img(image)

    clf = KMeans(n_clusters = number_of_colours)
    labels = clf.fit_predict(image)

    counts = Counter(labels)
    counts = dict(sorted(counts.items()))

    center_colours = clf.cluster_centers_
    ordered_colours = [center_colours[i] for i in counts.keys()]

    rgb_colors = [ordered_colours[i].astype(int) for i in counts.keys()]

    return rgb_colors,list(counts.values())



class ModelLogic:
    def __init__(self):
        pass

    def model_specific_logic(self, image_bytes):
        started_time = datetime.now()
        #image = cv2.imread(io.BytesIO(image_bytes))
        image = imageio.imread(io.BytesIO(image_bytes), as_gray=False, pilmode="RGB")

        colors, values = get_base_colors(image, 4)

        ended_time = datetime.now()
        print(f'TIME:{ended_time - started_time}')

        return [{'red': str(color[0]),'green': str(color[1]),'blue': str(color[2])} for color in colors]
