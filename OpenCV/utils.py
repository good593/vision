
import numpy as np 

import matplotlib.pyplot as plt

def convert_bgr_to_rgb(p_img):
  B_img = p_img[:,:,0]
  G_img = p_img[:,:,1]
  R_img = p_img[:,:,2]

  return np.dstack([R_img, G_img, B_img])

def show_img_of_plt(p_img, is_bgr:bool=False):
  if len(p_img.shape) == 2:
    plt.imshow(p_img, cmap='gray', interpolation='bicubic')
    plt.show()
    return 

  if is_bgr:
    p_img = convert_bgr_to_rgb(p_img)
    
  plt.imshow(p_img)
  plt.show()
