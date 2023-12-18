import cv2
import numpy as np
from skimage.util import random_noise
from  sklearn.cluster import  KMeans
from PIL import Image, ImageFilter
import imutils

class Model:
    def grey(self, img):
        if len(img.shape) == 2:
            return img
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        return gray_img

    def equalize(self, img):
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        equalized_img = cv2.equalizeHist(gray_image)
        return equalized_img

    def threashold_value_using_otsu(self,img):
        grey = self.grey(img)
        value = cv2.threshold(grey, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[0]
        return int(value)

    def threashold(self,img,value):
        grey = self.grey(img)
        threashold_img = cv2.threshold(grey, value, 255, cv2.THRESH_BINARY)[1]
        return threashold_img

    def stretch(self, img,min_out=0,max_out=255):
        min_in, max_in = np.min(img), np.max(img)
        stretch_img = np.uint8((img - min_in) * ((max_out - min_out) / (max_in - min_in)) + min_out)
        return stretch_img

    def negative(self, img):
        negative_img = 255 - img
        return negative_img

    def log(self, img):
        c = 255 / np.log(1 + np.max(img))
        log_img = np.uint8(c * np.log(1 + img))
        return log_img

    def gamma(self, img, gamma=1):
        norm_img = img / 255.0
        power_img = np.power(norm_img, gamma)
        power_img = np.uint8(power_img * 255)
        return power_img

    def blur(self, img, s=3):
        mask = (s, s)
        gauss_img = cv2.GaussianBlur(img, mask, 0)
        return gauss_img

    def median(self, img, s=3):
        median_img = cv2.medianBlur(img, s)
        return median_img


    def min(self,img,s=3):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        min_img = img.filter(ImageFilter.MinFilter(s))
        min_img = cv2.cvtColor(np.array(min_img), cv2.COLOR_RGB2BGR)
        return min_img

    def max(self,img,s=3):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        max_img = img.filter(ImageFilter.MaxFilter(s))
        max_img = cv2.cvtColor(np.array(max_img), cv2.COLOR_RGB2BGR)
        return max_img

    def canny(self, img,kernal_size=3,min_value=100,max_value=200):
        img_canny = cv2.Canny(self.grey(img), min_value, max_value,apertureSize=kernal_size)
        return img_canny

    def sobel(self, img, m='both'):
        grey = self.grey(img)

        if m == 'vertical':
            soble_x_img = cv2.Sobel(grey, -1, 1, 0)
            return soble_x_img
        elif m == 'horizontal':
            soble_y_img = cv2.Sobel(grey, -1, 0, 1)
            return soble_y_img
        else:
            soble_x_img = cv2.Sobel(grey, -1, 1, 0)
            soble_y_img = cv2.Sobel(grey, -1, 0, 1)
            soble_xy_img = cv2.addWeighted(soble_x_img, 1, soble_y_img, 1, 0)
            return soble_xy_img


    def gaussian_noise(self,img,mean=0,var=0.01):
            noised_img = random_noise(img, mode='gaussian', mean=mean, var=var)
            noised_img = np.uint8(noised_img * 255)
            return  noised_img

    def SandP_noise(self,img,amount = 0):
        noised_img = random_noise(img, mode='s&p', amount=amount)
        noised_img = np.uint8(noised_img * 255)
        return  noised_img

    def rotate(self, img, angle=0):
        rotated_img = imutils.rotate(img, angle)
        return rotated_img

    def translate(self, img, x=0, y=0):
        translated_img = imutils.translate(img, x, y)
        return translated_img


    def boundry(self, img,):
        flt = np.array([[1, 1, 1], [1, -7, 1], [1, 1, 1]])
        filtered_img = cv2.filter2D(img, -1, flt)
        return filtered_img

    def colored_edge(self, img,):
        flt = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
        filtered_img = cv2.filter2D(img, -1, flt)
        return filtered_img

    def sharp(self, img,):
        flt = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
        filtered_img = cv2.filter2D(img, -1, flt)
        return filtered_img



    def clustered_img(self,img,n=3):
        kmeans= KMeans(n_clusters=n,random_state=0)
        grey = self.grey(img)
        w,h = grey.shape
        reshaped = grey.reshape(w*h,1)
        kmeans.fit(reshaped)
        labels = kmeans.predict(reshaped)
        centers = kmeans.cluster_centers_.astype(int)
        segmented_img =  np.uint8(centers[labels].reshape(w,h))
        return segmented_img




