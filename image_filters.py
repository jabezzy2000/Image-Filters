import image_io


# read file
# image = image_io.read_file(insert path to image here)
# example: image_io.read_file('images/flowers.jpeg')


def red_stripes(image_matrix):
    length = len(image_matrix) - 1
    for row_of_lists in range(length):
        if 0 <= row_of_lists < 50 or 100 <= row_of_lists < 150 or 200 <= row_of_lists < 250 or 300 <= row_of_lists < 350 or 400 <= row_of_lists < 450 or 500 <= row_of_lists < 550 or 600 <= row_of_lists <= 650 or 700 <= row_of_lists <= 750:
            for pixels in image_matrix[row_of_lists]:
                pixels[0] = 255
        else:
            pass
    for lists in image_matrix[339]:
        lists[0] = 255
    return image_matrix

    image_io.write_to_file(image, red_stripes(image_matrix))


# image_io.read_file('images/flowers.jpeg')


def grayscale(image_matrix):
    for row_of_lists in image_matrix:
        for pixels in row_of_lists:
            avg = (pixels[0] + pixels[1] + pixels[2]) // 3
            pixels[0] = avg
            pixels[1] = avg
            pixels[2] = avg

    return image_matrix
    image_io.write_to_file(image, grayscale(image_matrix))


def invert_colors(image_matrix):
    for row_of_lists in image_matrix:
        for pixels in row_of_lists:
            factor = 255
            pixels[0] = 255 - pixels[0]
            pixels[1] = 255 - pixels[1]
            pixels[2] = 255 - pixels[2]

    return image_matrix
    image_io.write_to_file(image, invert_colors(image_matrix))


def flip(image_matrix):
    length = len(image_matrix)

    temp = []
    # image = image_io.read_file(image_matrix)
    for row_of_lists in range(length - 1, -1, -1):
        temp.append(image_matrix[row_of_lists])
    #   image_matrix = temp

    return temp
    image_io.write_to_file('images/flowers.jpeg', temp)


def sepia(image_matrix):
    length = len(image_matrix)
    for row_of_lists in image_matrix:
        for pixels in row_of_lists:
            red = (pixels[0] * 0.393) + (pixels[1] * 0.769) + (pixels[2] * 0.189)
            if red > 255:
                red = 255
            else:
                red = int(red)
            green = (pixels[0] * 0.349) + (pixels[1] * 0.686) + (pixels[2] * 0.168)
            if green > 255:
                green = 255
            else:
                green = int(green)
            blue = (pixels[0] * 0.272) + (pixels[1] * 0.534) + (pixels[2] * 0.131)
            if blue > 255:
                blue = 255
            else:
                blue = int(blue)

            pixels[0] = red
            pixels[1] = green
            pixels[2] = blue

    return image_matrix
    image_io.write_to_file(image, sepia(image_matrix))

