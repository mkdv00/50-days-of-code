from PIL import Image, ImageFilter


def apply_filter(option, photo):
    img = Image.open(photo)

    match option:
        case 'Blur':
            img = img.filter(ImageFilter.BLUR)
        case 'Contour':
            img = img.filter(ImageFilter.CONTOUR)
        case 'Detail':
            img = img.filter(ImageFilter.DETAIL)
        case 'Edge Enhance':
            img = img.filter(ImageFilter.EDGE_ENHANCE)
        case 'Emboss':
            img = img.filter(ImageFilter.EMBOSS)
        case 'Find Edges':
            img = img.filter(ImageFilter.FIND_EDGES)
        case 'Sharpen':
            img = img.filter(ImageFilter.SHARPEN)
        case 'Gray':
            img = img.convert('L')

    return img
