import numpy as np
import cv2
from customtkinter import filedialog , CTkInputDialog ,os
from PIL import Image, ImageTk
from Dialog.CustomSliderDialog import CustomSliderDialog
from Dialog.CannyDialog import CannyDialog
from Dialog.SobelDialog import SobelDialog
from Dialog.StretchDialog import StrechDialog
from Dialog.GaussianNoiseDialog import GaussianNoiseDialog
import os

class Controller:
    def __init__(self, view, model):
        self.original_image = None
        self.current_image = None
        self.edited_image = None
        self.image_name = None
        self.view = view
        self.model = model

    def select_img(self):
        filename = filedialog.askopenfilename(initialdir=os.getcwd(),
                                              filetypes=(("PNG File", "*.png"),("JGP File", "*.jpg"), ))
        if filename ==""or filename is None:
            return

        self.image_name = os.path.basename(filename)
        self.original_image = np.array(Image.open(filename))
        self.current_image = self.original_image
        self.view.image = self.current_image
        self.view.show_image()
        self.edited_image = None
        self.refresh_menu()

    def apply(self):
        self.current_image = self.edited_image
        self.edited_image = None
        self.refresh_menu()

    def restore(self):
        self.current_image = self.original_image
        self.view.image = self.current_image
        self.view.show_image()
        self.edited_image = None
        self.refresh_menu()

    def undo(self):
        self.view.image = self.current_image
        self.view.show_image()
        self.edited_image = None
        self.refresh_menu()

    def save(self):
        dirname = filedialog.askdirectory()
        if dirname == "" or dirname is None:
            return

        saved_path = os.path.join(dirname,self.image_name)
        saved_path = os.path.normpath(saved_path)

        if self.edited_image is None:
            saved_image = self.current_image
        else:
            saved_image = self.edited_image

        saved_image = cv2.cvtColor(saved_image,cv2.COLOR_RGB2BGR)
        cv2.imwrite(saved_path,saved_image)


    def refresh_menu(self):
        if self.current_image is not self.original_image and self.original_image is not None:
            self.view.restore_btn_status(True)
        else:
            self.view.restore_btn_status(False)

        if self.edited_image is None:
            self.view.apply_undo_btns_status(False)
        else:
            self.view.apply_undo_btns_status(True)

        if self.current_image is None:
            self.view.save_btn_status(False)
        else:
            self.view.save_btn_status(True)

    def gray_img(self):
        if self.current_image is None:
            return

        self.edited_image = self.model.grey(self.current_image)
        self.view.image = self.edited_image
        self.view.show_image()
        self.refresh_menu()

    def threshold_img(self):
        if self.current_image is None:
            return

        best_value = self.model.threashold_value_using_otsu(self.current_image)

        choosen_value = CustomSliderDialog(text=f"Choose threshold value\nBest value is {best_value} using otsu method",
                                           title='Threshold', initial_value=best_value).get_input()

        if choosen_value is None:
            return

        choosen_value = int(choosen_value)

        self.edited_image = self.model.threashold(self.current_image, choosen_value)
        self.view.image = self.edited_image
        self.view.show_image()
        self.refresh_menu()

    def equalized_img(self):
        if self.current_image is None:
            return

        self.edited_image = self.model.equalize(self.current_image)
        self.view.image = self.edited_image
        self.view.show_image()
        self.refresh_menu()

    def log_img(self):
        if self.current_image is None:
            return

        self.edited_image = self.model.log(self.current_image)
        self.view.image = self.edited_image
        self.view.show_image()
        self.refresh_menu()

    def negative_img(self):
        if self.current_image is None:
            return

        self.edited_image = self.model.negative(self.current_image)
        self.view.image = self.edited_image
        self.view.show_image()
        self.refresh_menu()

    def blur_img(self):
        if self.current_image is None:
            return

        choosen_value = CustomSliderDialog(text=f"Choose kernal size", min_value=1, max_value=100,
                                           title='Gaussian Blur Filter', ).get_input()

        if choosen_value is None:
            return

        choosen_value = int(choosen_value)

        choosen_value = choosen_value + (1 if choosen_value % 2 == 0 else 0)

        self.edited_image = self.model.blur(self.current_image, choosen_value)
        self.view.image = self.edited_image
        self.view.show_image()
        self.refresh_menu()

    def median_img(self):
        if self.current_image is None:
            return

        choosen_value = CustomSliderDialog(text=f"Choose kernal size", min_value=1, max_value=100,
                                           title='Median Filter', ).get_input()

        if choosen_value is None:
            return

        choosen_value = int(choosen_value)
        choosen_value = choosen_value + (1 if choosen_value % 2 == 0 else 0)

        self.edited_image = self.model.median(self.current_image, choosen_value)
        self.view.image = self.edited_image
        self.view.show_image()
        self.refresh_menu()

    def min_img(self):
        if self.current_image is None:
            return

        choosen_value = CustomSliderDialog(text=f"Choose kernal size", min_value=1, max_value=100,
                                           title='Min Filter', ).get_input()

        if choosen_value is None:
            return

        choosen_value = int(choosen_value)
        choosen_value = choosen_value + (1 if choosen_value % 2 == 0 else 0)

        self.edited_image = self.model.min(self.current_image, choosen_value)
        self.view.image = self.edited_image
        self.view.show_image()
        self.refresh_menu()

    def max_img(self):
        if self.current_image is None:
            return

        choosen_value = CustomSliderDialog(text=f"Choose kernal size", min_value=1, max_value=100,
                                           title='Max Filter', ).get_input()

        if choosen_value is None:
            return

        choosen_value = int(choosen_value)
        choosen_value = choosen_value + (1 if choosen_value % 2 == 0 else 0)

        self.edited_image = self.model.max(self.current_image, choosen_value)
        self.view.image = self.edited_image
        self.view.show_image()
        self.refresh_menu()

    def gamma_img(self):
        if self.current_image is None:
            return

        choosen_value = CustomSliderDialog(text=f"Choose Gamma value",
                                           min_value=0, max_value=2, initial_value=1,
                                           isreal=True, title='Gamma', ).get_input()

        if choosen_value is None:
            return

        self.edited_image = self.model.gamma(self.current_image, choosen_value)
        self.view.image = self.edited_image
        self.view.show_image()
        self.refresh_menu()

    def stretch_img(self):
        if self.current_image is None:
            return

        choosen_values = StrechDialog().get_input()

        if choosen_values is None:
            return

        min_out, max_out = choosen_values

        self.edited_image = self.model.stretch(self.current_image, min_out=min_out, max_out=max_out)
        self.view.image = self.edited_image
        self.view.show_image()
        self.refresh_menu()

    def sobel_img(self):
        if self.current_image is None:
            return

        choosen_value = SobelDialog().get_input()

        if choosen_value is None:
            return

        self.edited_image = self.model.sobel(self.current_image, m=choosen_value)

        self.view.image = self.edited_image
        self.view.show_image()
        self.refresh_menu()

    def canny_img(self):
        if self.current_image is None:
            return

        choosen_values = CannyDialog().get_input()

        if choosen_values is None:
            return

        kernal_size, min_value, max_value = choosen_values

        self.edited_image = self.model.canny(self.current_image, kernal_size, min_value, max_value)
        self.view.image = self.edited_image
        self.view.show_image()
        self.refresh_menu()

    def cluster_img(self):
        if self.current_image is None:
            return

        choosen_value = CustomSliderDialog(text=f"Choose number of clusters", min_value=2, max_value=10,
                                           title='Clustring', ).get_input()

        if choosen_value is None:
            return

        choosen_value = int(choosen_value)

        self.edited_image = self.model.clustered_img(self.current_image, choosen_value)
        self.view.image = self.edited_image
        self.view.show_image()
        self.refresh_menu()

    def rotate_img(self):
        if self.current_image is None:
            return

        rotate_value = CTkInputDialog(title="Rotate", text="Enter Rotate Angle").get_input()

        if rotate_value is None:
            return

        try:
            rotate_value = int(rotate_value)
        except:
            return

        self.edited_image = self.model.rotate(self.current_image, rotate_value)
        self.view.image = self.edited_image
        self.view.show_image()
        self.refresh_menu()

    def translate_img(self):
        if self.current_image is None:
            return

        value = CTkInputDialog(title="Translate", text="Enter X Y values respectively seperated by space").get_input()

        if value is None:
            return

        try:
            x, y = value.split(" ")
            x, y = int(x), int(y)
        except:
            return

        self.edited_image = self.model.translate(self.current_image, x, y)
        self.view.image = self.edited_image
        self.view.show_image()
        self.refresh_menu()

    def gaussian_noise_img(self):
        if self.current_image is None:
            return

        choosen_value = GaussianNoiseDialog().get_input()

        if choosen_value is None:
            return

        mean, var = choosen_value

        self.edited_image = self.model.gaussian_noise(self.current_image, mean, var)
        self.view.image = self.edited_image
        self.view.show_image()
        self.refresh_menu()

    def SandP_noise_img(self):
        if self.current_image is None:
            return

        amount = CustomSliderDialog(text=f"Choose amount of noise",
                                    min_value=0, max_value=100, initial_value=0,
                                    title='Salt And Pepper Nosie', ).get_input()

        if amount is None:
            return
        amount = amount / 100
        self.edited_image = self.model.SandP_noise(self.current_image, amount)
        self.view.image = self.edited_image
        self.view.show_image()
        self.refresh_menu()

    def sharp_img(self):
        if self.current_image is None:
            return

        self.edited_image = self.model.sharp(self.current_image)

        self.view.image = self.edited_image
        self.view.show_image()
        self.refresh_menu()

    def boundry_img(self):
        if self.current_image is None:
            return

        self.edited_image = self.model.boundry(self.current_image)

        self.view.image = self.edited_image
        self.view.show_image()
        self.refresh_menu()

    def colored_edge_img(self):
        if self.current_image is None:
            return

        self.edited_image = self.model.colored_edge(self.current_image)

        self.view.image = self.edited_image
        self.view.show_image()
        self.refresh_menu()

    def prepare_image_to_show(self, img, width, height):

        def cv2img_to_tkimg(img):
            img = Image.fromarray(img)
            img = ImageTk.PhotoImage(img)
            return img

        def resize_image_no_distortion(img, container_width, container_height):
            img_height, img_width = img.shape[:2]
            width , height = container_width ,container_height

            if img_width > img_height:
                r = width / img_width
                height = img_height * r

                if height > container_height:
                    height = container_height
                    r = height / img_height
                    width = img_width * r

            else :
                r = height / img_height
                width = img_width * r

                if width > container_width:
                    width = container_width
                    r = width / img_width
                    height = img_height * r





            return cv2.resize(img, (int(width), int(height)))

        img = resize_image_no_distortion(img, width, height)
        img = cv2img_to_tkimg(img)
        return img
