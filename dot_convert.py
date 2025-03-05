from PIL import Image, ImageDraw
import argparse
import numpy as np


def convert_image(
    file_name: str, dots: int, dot_size: int, color: str, contrast_factor: float
):

    img = (
        Image.fromarray(file_name)
        if isinstance(file_name, np.ndarray)
        else Image.open(file_name)
    )
    bw = img.convert("L")

    img_height = img.height
    img_width = img.width

    matrix = []
    max_bw = 0

    for x in range(dots):
        x_row = []

        for y in range(dots):
            current_pixel = bw.getpixel(
                ((img_width / dots) * x, (img_height / dots) * y)
            )
            x_row.append(current_pixel)
            if max_bw < current_pixel:
                max_bw = current_pixel

        matrix.append(x_row)

    dot_img = Image.new(mode="L", size=(img_width, img_height), color=color)
    draw = ImageDraw.Draw(dot_img)

    for x_row in range(len(matrix)):
        for y in range(len(matrix[x_row])):

            x_val = (img_width / dots) * x_row
            y_val = (img_height / dots) * y

            current_pixel_bw = matrix[x_row][y]
            contrasted_pixel = min(
                int((((current_pixel_bw) / max_bw) * 255) * contrast_factor),
                255,
            )  # increase contrast

            draw.circle(
                (x_val, y_val),
                current_pixel_bw / (255 / dot_size),
                (contrasted_pixel),
            )

    return dot_img


if __name__ == "__main__":
    # get args from command line
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", type=str, required=True)
    parser.add_argument("--output", type=str, required=True)
    parser.add_argument("--dots", type=int, required=False, default=90)
    parser.add_argument("--dot_size", type=int, required=False, default=6)
    parser.add_argument("--color", type=str, required=False, default="black")
    parser.add_argument("--contrast_factor", type=float, required=False, default=1)

    args = parser.parse_args()

    dot_img = convert_image(
        args.file,
        args.dots,
        args.dot_size,
        args.color,
        args.contrast_factor,
    )

    print(f"Saving image to {args.output}")
    print(dot_img)
    # save the image
    dot_img.save(args.output)
