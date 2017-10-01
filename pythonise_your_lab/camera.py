import numpy as np
import pygame.camera
from pygame.surfarray import pixels3d


class Camera:
    def __init__(self, cam_number=0):
        # there may be more than one camera accessible
        pygame.camera.init()
        camlist = pygame.camera.list_cameras()
        self.cam = pygame.camera.Camera(camlist[cam_number])

    def grab_color(self):
        self.cam.start()
        img = self.cam.get_image()
        self.cam.stop()
        # the cam is a color cam => the bit depth is 24 bits (8 bits / color)
        # convert it to a 3d numpy array. the last
        # index corresponds to the color
	return pixels3d(img)

    def grab(self):
        # gray image is the mean of a color image over the 3 colors
        # round the result to nearest integer
	return np.rint(np.mean(self.grab_color(), axis=2)).astype(int)
