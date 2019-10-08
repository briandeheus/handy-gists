def resize_image(img: Image, target=800) -> Image:
    o_w, o_h = img.size
    ratio = target / min((o_h, o_w))
    return img.resize((int(o_w * ratio), int(o_h * ratio)), Image.ANTIALIAS)


def crop_image(img: Image, width=800, height=800) -> Image:
    o_w, o_h = img.size
    left = (o_w - width) / 2
    upper = (o_h - height) / 2
    right = left + width
    lower = upper + height

    return img.crop(box=(left, upper, right, lower))
