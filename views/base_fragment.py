from base_view import BaseView

class BaseFragment(BaseView):

    def __init__(self, boundsRect):
        """ create a fragment with a bounding rect """
        self.boundsRect = boundsRect

    def draw(self, surface):
        """ draw the fragment within the bounds """
