import matplotlib
matplotlib.use('Agg')
from B_mode_outputs import image_save
import numpy as np
import os
import pytest

B_mode_array = np.absolute(np.empty([5, 5]))


def test_image_save():
    assert not os.path.isfile('bmode.png')
    image_save('bmode.png', B_mode_array, 10, 10, 10, 10, 10)
    assert os.path.isfile('bmode.png')
    os.remove('bmode.png')


def test_image_save_wrong_type():
    with pytest.raises(ValueError):
        image_save('bmode.bmp', B_mode_array, 10, 10, 10, 10, 10)
