import cv2 as cv
import numpy as np
import os


def load_images(folder):
    images = []
    for filename in os.listdir(folder):
        filename = "database/train/" + filename
        images.append(filename)
    return images


def get_pixel(img, center, x, y):
    new_value = 0
    try:
        if img[x][y] >= center:
            new_value = 1
    except:
        pass
    return new_value


def lbp_calculated_pixel(img, x, y):
    center = img[x][y]
    val_ar = [get_pixel(img, center, x - 1, y + 1), get_pixel(img, center, x, y + 1),
              get_pixel(img, center, x + 1, y + 1), get_pixel(img, center, x + 1, y),
              get_pixel(img, center, x + 1, y - 1), get_pixel(img, center, x, y - 1),
              get_pixel(img, center, x - 1, y - 1), get_pixel(img, center, x - 1, y)]

    power_val = [1, 2, 4, 8, 16, 32, 64, 128]
    val = 0
    for i in range(len(val_ar)):
        val += val_ar[i] * power_val[i]
    return val


def histogram(image_name):
    image = cv.imread(image_name)
    img_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    r = np.zeros(256, np.float16)
    g = np.zeros(256, np.float16)
    b = np.zeros(256, np.float16)
    lbp = np.zeros(256, np.float16)

    for i in range(0, image.shape[0]):
        for j in range(0, image.shape[1]):
            r[image[i][j][0]] += 1
            g[image[i][j][1]] += 1
            b[image[i][j][2]] += 1
            lbp[lbp_calculated_pixel(img_gray, i, j)] += 1

    r_sum = sum(r)
    g_sum = sum(g)
    b_sum = sum(b)
    lbp_sum = sum(lbp)

    for i in range(0, 256):
        r[i] = r[i] / r_sum
        g[i] = g[i] / g_sum
        b[i] = b[i] / b_sum
        lbp[i] = lbp[i] / lbp_sum

    hist = {
        'r': r,
        'g': g,
        'b': b,
        'lbp': lbp,
        'imageName': image_name
    }
    return hist


def get_dist(value):
    return float(value['dist'])


def main():
    histograms = []
    images = load_images("database/train")
    print("Creating database...")
    for i in range(0, 70):
        histograms.append(histogram(images[i]))
    image_name = input("Please give test image's path: ")
    test = histogram(image_name)
    print("Test picture :" + image_name)

    # Finding rgb distance
    dist_rgb = np.zeros(70, np.float16)
    names_rgb = []
    for i in range(0, 70):
        for j in range(0, 256):
            dist_rgb[i] += abs(histograms[i]['r'][j] - test['r'][j]) + abs(histograms[i]['g'][j] - test['g'][j]) \
                           + abs(histograms[i]['b'][j] - test['b'][j])
        names_rgb.append(histograms[i]['imageName'])

    distance_rgb = []
    for i in range(0, 70):
        value_rgb = {
            'dist': dist_rgb[i],
            'name': names_rgb[i]
        }
        distance_rgb.append(value_rgb)
    distance_rgb.sort(key=get_dist)
    print("With rgb distance")
    for i in range(0, 5):
        print(distance_rgb[i]['name'])

    # Finding lbp distance
    dist_lbp = np.zeros(70, np.float16)
    names_lbp = []
    for i in range(0, 70):
        for j in range(0, 256):
            dist_lbp[i] += abs(histograms[i]['lbp'][j] - test['lbp'][j])
        names_lbp.append(histograms[i]['imageName'])

    distance_lbp = []
    for i in range(0, 70):
        value_lbp = {
            'dist': dist_lbp[i],
            'name': names_lbp[i]
        }
        distance_lbp.append(value_lbp)
    distance_lbp.sort(key=get_dist)
    print("With lbp distance")
    for i in range(0, 5):
        print(distance_lbp[i]['name'])


if __name__ == '__main__':
    main()
