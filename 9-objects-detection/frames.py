import cv2


def get_pixels_in_display(frame):
    pixels_count = 0
    for fragments in frame[0]:
        for _ in fragments:
            pixels_count += 1

    return pixels_count


def gray_frame(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return gray


def gaussian_blur_frame(frame):
    gray_frame_gau = cv2.GaussianBlur(frame, (21, 21), 0)
    return gray_frame_gau
