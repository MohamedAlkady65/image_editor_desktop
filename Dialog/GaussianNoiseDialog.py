from .CustomSliderDialog import CustomSliderDialog
from .SliderPart import SliderPart

class GaussianNoiseDialog(CustomSliderDialog):

    def __init__(self, ):
        super().__init__(title='Gaussian Noise', options_order=7)

    def build_main(self):
        self.mean = SliderPart(master=self, title="Mean", min=-1, max=1, initial=0, order=0,isReal=True )
        self.variance = SliderPart(master=self, title="Variance", min=0, max=2, initial=0, order=2,isReal=True )

    def _ok_event(self, event=None):
        mean = float(self.mean.get())
        variance = float(self.variance.get())


        self._user_input = (mean, variance)

        self.grab_release()
        self.destroy()



