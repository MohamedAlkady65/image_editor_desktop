from customtkinter import (set_appearance_mode, set_default_color_theme, CTkButton,
                           CTkLabel, CTkFrame, CENTER, NORMAL, DISABLED, CTkSwitch, StringVar)
from warnings import filterwarnings

class View:
    def __init__(self, root):
        self.root = root
        filterwarnings("ignore")
        set_appearance_mode("light")
        set_default_color_theme("blue")
        self.root.geometry('%dx%d+%d+%d' % self.window_geometry(1280, 720))
        self.root.title("Image Processing Desktop Application")
        self.root.configure()
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)
        self.main = None
        self.image = None
        self.image_container = None
        self.image_label = None


    def init(self, controller):
        self.controller = controller
        self.build_gui()

    def window_geometry(self, width_window, height_window):
        width_screen = self.root.winfo_screenwidth()
        height_screen = self.root.winfo_screenheight()
        x = (width_screen / 2) - (width_window / 2)
        y = (height_screen / 2) - (height_window / 2) -50
        return width_window, height_window, x, y

    def build_gui(self):
        self.build_menu()
        self.build_image_container()
        self.build_options_container()

    def build_image_container(self):
        self.main = CTkFrame(self.root)
        self.main.grid(row=1, column=0, sticky='nsew')
        self.image_container = CTkFrame(master=self.main, corner_radius=10)
        self.image_container.place(relwidth=0.6, relheight=0.8, relx=0.2, rely=0.1)
        self.image_label = CTkLabel(
            master=self.image_container, text="", corner_radius=10
        )
        self.image_label.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.image_container.bind("<Configure>", lambda  e : self.show_image())

    def build_options_container(self):
        options = CTkFrame(self.root)
        options.grid(row=2, column=0, sticky='sew')


        for x in range(3):
            options.grid_rowconfigure(x, weight=1)

        for x in range(8):
            options.grid_columnconfigure(x, weight=1)

        (CTkButton(options, text="Gray", command=self.controller.gray_img)
         .grid(row=0, column=0, padx=10, pady=10))

        (CTkButton(options, text="Blur", command=self.controller.blur_img)
         .grid(row=0, column=1, padx=10, pady=10))

        (CTkButton(options, text="Equalize", command=self.controller.equalized_img)
         .grid(row=0, column=2, padx=10, pady=10))

        (CTkButton(options, text="Negative", command=self.controller.negative_img)
         .grid(row=0, column=3, padx=10, pady=10))

        (CTkButton(options, text="Log", command=self.controller.log_img)
         .grid(row=0, column=4, padx=10, pady=10))

        (CTkButton(options, text="Gamma", command=self.controller.gamma_img)
         .grid(row=0, column=5, padx=10, pady=10))


        (CTkButton(options, text="Contrast Stretching", command=self.controller.stretch_img)
         .grid(row=0, column=6, padx=10, pady=10))

        (CTkButton(options, text="Median", command=self.controller.median_img)
         .grid(row=0, column=7, padx=10, pady=10))

        (CTkButton(options, text="Min", command=self.controller.min_img)
         .grid(row=1, column=0, padx=10, pady=10))

        (CTkButton(options, text="Max", command=self.controller.max_img)
         .grid(row=1, column=1, padx=10, pady=10))

        (CTkButton(options, text="Thredshold", command=self.controller.threshold_img)
         .grid(row=1, column=2, padx=10, pady=10))

        (CTkButton(options, text="Sobel", command=self.controller.sobel_img)
         .grid(row=1, column=3, padx=10, pady=10))

        (CTkButton(options, text="Canny", command=self.controller.canny_img)
         .grid(row=1, column=4, padx=10, pady=10))

        (CTkButton(options, text="Clustring", command=self.controller.cluster_img)
         .grid(row=1, column=5, padx=10, pady=10))

        (CTkButton(options, text="Rotate", command=self.controller.rotate_img)
         .grid(row=1, column=6, padx=10, pady=10))

        (CTkButton(options, text="Translate", command=self.controller.translate_img)
         .grid(row=1, column=7, padx=10, pady=10))


        (CTkButton(options, text="Gaussain Noise", command=self.controller.gaussian_noise_img)
         .grid(row=2, column=0, padx=10, pady=10))

        (CTkButton(options, text="Salt And Pepper Nosie", command=self.controller.SandP_noise_img)
         .grid(row=2, column=1, padx=10, pady=10))

        (CTkButton(options, text="Sharp", command=self.controller.sharp_img)
         .grid(row=2, column=2, padx=10, pady=10))

        (CTkButton(options, text="Colored Edge", command=self.controller.colored_edge_img)
         .grid(row=2, column=3, padx=10, pady=10))

        (CTkButton(options, text="Boundary", command=self.controller.boundry_img)
         .grid(row=2, column=4, padx=10, pady=10))




    def build_menu(self):
        menu = CTkFrame(self.root, height=50)
        menu.grid(row=0, column=0, sticky='new')

        menu.columnconfigure(0, weight=1)
        menu.columnconfigure(1, weight=1)
        menu.columnconfigure(2, weight=30)
        menu.columnconfigure(3, weight=1)
        menu.columnconfigure(4, weight=1)
        menu.columnconfigure(5, weight=1)
        menu.columnconfigure(6, weight=1)

        select_btn = CTkButton(menu, text="Select", command=self.controller.select_img)
        select_btn.grid(row=0, column=0, padx=10, pady=10, sticky='w')

        CTkLabel(menu, text="").grid(row=0, column=2)

        self.undo_btn = CTkButton(menu, text="Undo", command=self.controller.undo)
        self.apply_btn = CTkButton(menu, text="Apply", command=self.controller.apply)
        self.restore_btn = CTkButton(menu, text="Restore", command=self.controller.restore)
        self.save_btn = CTkButton(menu, text="Save", command=self.controller.save)

        self.undo_btn.grid(row=0, column=3, padx=10, pady=10, sticky='e')
        self.apply_btn.grid(row=0, column=4, padx=10, pady=10, sticky='e')
        self.restore_btn.grid(row=0, column=5, padx=10, pady=10, sticky='e')
        self.save_btn.grid(row=0, column=6, padx=10, pady=10, sticky='e')

        self.undo_btn.configure(state=DISABLED)
        self.apply_btn.configure(state=DISABLED)
        self.restore_btn.configure(state=DISABLED)
        self.save_btn.configure(state=DISABLED)

        self.dark_mode(menu)

    def dark_mode(self, menu):
        switch_var = StringVar(value="off")

        def switch_event():
            value = switch_var.get()

            if value == "on":
                set_appearance_mode("dark")
            else:
                set_appearance_mode("light")

        switch_1 = CTkSwitch(master=menu, text="Dark Mode", command=switch_event,
                             variable=switch_var, onvalue="on", offvalue="off")
        switch_1.grid(row=0, column=1, padx=10, pady=10, sticky='e')

    def apply_undo_btns_status(self, show):
        if show:
            self.undo_btn.configure(state=NORMAL)
            self.apply_btn.configure(state=NORMAL)
        else:
            self.undo_btn.configure(state=DISABLED)
            self.apply_btn.configure(state=DISABLED)

    def restore_btn_status(self, show):
        if show:
            self.restore_btn.configure(state=NORMAL)
        else:
            self.restore_btn.configure(state=DISABLED)

    def save_btn_status(self, show):
        if show:
            self.save_btn.configure(state=NORMAL)
        else:
            self.save_btn.configure(state=DISABLED)


    def show_image(self):
        if self.image is None:
            return
        w, h = self.image_container.winfo_width(), self.image_container.winfo_height()
        img = self.controller.prepare_image_to_show(self.image, w, h)
        self.image_label.configure(image=img)
        self.image_label.image = img





