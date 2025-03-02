from PIL import Image, ImageDraw

img = Image.open("photos.png")

bw = img.convert("L")


# bw.show()

img_height = img.height
img_width = img.width


dots = 90
color = "black"

# dot_size = min(img_height / dots, img_width / dots)
dot_size = 6

matrix = []

max_bw = 0

for x in range(dots):
    x_row = []

    for y in range(dots):
        current_pixel = bw.getpixel(((img_width / dots) * x, (img_height / dots) * y))
        x_row.append(current_pixel)
        if max_bw < current_pixel:
            max_bw = current_pixel

    matrix.append(x_row)

# print(matrix)


dot_img = Image.new(mode="L", size=(img_width, img_height), color=color)

draw = ImageDraw.Draw(dot_img)


contrast_factor = 1

for x_row in range(len(matrix)):
    for y in range(len(matrix[x_row])):

        x_val = (img_width / dots) * x_row
        y_val = (img_height / dots) * y

        current_pixel_bw = matrix[x_row][y]
        contrasted_pixel = min(
            int((((current_pixel_bw) / max_bw) * 255) * contrast_factor),
            255,
        )  # increase contrast
        # print(current_pixel_bw, contrasted_pixel)
        draw.circle(
            (x_val, y_val),
            current_pixel_bw / (255 / dot_size),
            (contrasted_pixel),
        )

dot_img.save("dot_img.png")
dot_img.show()
