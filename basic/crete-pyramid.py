from PIL import Image, ImageDraw

def create_pyramid_image(size, levels):
    # Create a blank image with a white background
    img = Image.new('RGB', size, 'white')
    draw = ImageDraw.Draw(img)

    # Calculate the base width for the pyramid
    base_width = size[0] // (2 ** (levels - 1))

    # Draw the pyramid levels
    for level in range(levels):
        pyramid_width = base_width * (2 ** level)
        x_start = (size[0] - pyramid_width) // 2
        x_end = x_start + pyramid_width
        y_start = size[1] - (level + 1) * base_width
        y_end = size[1] - level * base_width

        draw.rectangle([x_start, y_start, x_end, y_end], outline='black')

    return img

def save_image(img, filename):
    img.save(filename)
    print(f"Image saved as {filename}")

if __name__ == "__main__":
    # Set the size and levels of the pyramid
    image_size = (400, 400)
    pyramid_levels = 5

    # Create and save the pyramid image
    pyramid_image = create_pyramid_image(image_size, pyramid_levels)
    save_image(pyramid_image, "pyramid_image.png")
