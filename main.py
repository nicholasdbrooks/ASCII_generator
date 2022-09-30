import PIL.Image
import numpy as np

# Sources Used: https://scipython.com/blog/ascii-art/,
# https://levelup.gitconnected.com/python-ascii-art-generator-60ba9eb559d7


def resize(image, new_width=100):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio * 0.5)
    return image.resize((new_width, new_height))


def to_greyscale(image):
    return image.convert("L")


def pixel_to_ascii(image):
    ascii_chars = ('$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|'
                   '()1{}[]?-_+~<>i!lI;:,"^`\'.            ')
    # contrast: [-10, 10] higher=more contrast, lower=less contrast
    contrast = 10
    ascii_chars = ascii_chars[:-11+contrast]
    n = len(ascii_chars)
    arr = np.array(image)
    ascii_str = ""
    for i in range(image.height):
        for j in range(image.width):
            p = arr[i, j]
            k = int(np.floor(p/256 * n))
            ascii_str += ascii_chars[n-1-k]
    return ascii_str


def main():
    path = input("Enter the path to the image file: \n")
    try:
        image = PIL.Image.open(path)
    except:
        print(path, "Unable to find image")

    # resize image
    image = resize(image)

    # convert to greyscale
    greyscale_image = to_greyscale(image)

    # convert greyscale image to ascii chars
    ascii_str = pixel_to_ascii(greyscale_image)

    img_width = greyscale_image.width
    ascii_str_len = len(ascii_str)
    ascii_img=""

    # split the string based on width of the image
    for i in range(0, ascii_str_len, img_width):
        ascii_img += ascii_str[i:i+img_width] + "\n"

    fullpath = "artfolder/"
    filename = input("Name for ASCII art file (no extension): \n")
    # save the string to a file
    fullpath += filename + ".txt"
    with open(fullpath, "w") as f:
        f.write(ascii_img)


main()
