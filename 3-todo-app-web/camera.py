import streamlit as st
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


def main():
    st.subheader("Image Filters")

    uploaded_image = st.file_uploader("Upload Image")

    options = ['Gray', 'Blur', 'Contour', 'Sharpen', 'Find Edges', 'Emboss', 'Edge Enhance', 'Detail']
    selected_option = st.selectbox("Choose a filter", options)
    st.write("You selected:", selected_option)

    with st.expander("Start camera"):
        camera_image = st.camera_input("Camera")

    if camera_image:
        img = apply_filter(selected_option, camera_image)
        st.image(img, caption="Filtered camera Image", use_column_width=True)

    if uploaded_image:
        img = apply_filter(selected_option, uploaded_image)
        st.image(img, caption="Filtered Image", use_column_width=True)


if __name__ == '__main__':
    main()
