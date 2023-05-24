import array_huruf
import matplotlib.pyplot as plt

JARAK_HURUF = 5


def place_letter_with_transparency(image, letter, y_start, x_start):
    for y in range(30):
        for x in range(23):
            if letter[y][x] == 1:
                image[y_start + y, x_start + x] += 50  # pemudaran warna

def place_letter_with_no_transparency(image, letter, y_start, x_start):
    for y in range(30):
        for x in range(23):
            if letter[y][x] == 1:
                image[y_start + y, x_start + x] = [255, 255, 255]  # pemudaran warna

def add_text_to_image(image, text):
    start_y = 25
    start_x = 50
    for letter in text:
        if letter != ' ':
            place_letter_with_no_transparency(image, array_huruf.get[letter], start_y, start_x)
        start_x += 28 + JARAK_HURUF

    plt.imsave(f'image_modified.jpg', image)

def add_watermark_to_image(image, text):
    start_y = 25
    start_x = 50
    for letter in text:
        if letter != ' ':
            place_letter_with_transparency(image, array_huruf.get[letter], start_y, start_x)
        start_x += 28 + JARAK_HURUF

    plt.imsave(f'image_modified.jpg', image)