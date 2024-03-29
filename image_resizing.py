import cv2
import os


def resize_image(image_path: str, new_height: int, n_width: int):

    """Outputs another folder where all images are resized to the et dimensions.
    Make sure the path you input is the root path reaching the input image. Height and Width in pixels."""

    errors = 0

    # Image Dimensions
    h = new_height
    w = new_width
    #

    # Directory
    input_folder = rf"{image_path}"
    os.makedirs(rf"{input_folder} Resized", exist_ok=True)
    #

    # Reading and Processing all Images
    for img_name in os.listdir(input_folder):
        try:
            filepath = os.path.join(input_folder, img_name)
            image = cv2.imread(filepath)
            edit = cv2.resize(image, (w, h), interpolation=cv2.INTER_AREA)

            if img_name == os.listdir(input_folder)[0]:
                image = edit
                cv2.imshow("First Edit", image)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

            cv2.imwrite(rf"{input_folder} Resized/{img_name}", edit)

        except TypeError:
            errors += 1

    plural_noun = {True: "", False: "s"}[errors < 1]
    plural_verb = {True: "was", False: "were"}[errors < 1]
    print(f"Done. {errors} image{plural_noun} {plural_verb} unsuccessfully processed.")


input_folder = r"C:\Users\cotyl\OneDrive\Desktop\CCIHP_icip\test_folder"
new_height = 300
new_width = 300
resize_image(input_folder, new_height, new_width)
