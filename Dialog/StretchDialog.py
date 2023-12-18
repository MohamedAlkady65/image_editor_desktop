from .CustomSliderDialog import CustomSliderDialog
from .SliderPart import SliderPart

class StrechDialog(CustomSliderDialog):

    def __init__(self, ):
        super().__init__(title='Contrast Stretching', options_order=5)

    def build_main(self):
        self.min = SliderPart(master=self, title="Minimum Value Of Result Image", min=0, max=255, initial=0, order=1, )
        self.max = SliderPart(master=self, title="Maximum Value Of Result Image", min=0, max=255, initial=255, order=3, )

    def _ok_event(self, event=None):
        self._user_input = ( int(self.min.get()), int(self.max.get()),)
        self.grab_release()
        self.destroy()
