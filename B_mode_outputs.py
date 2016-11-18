import matplotlib.pyplot as plt


def image_plot(B_mode_array, beam_spacing, axial_samples, num_beams, f_s, c):
    lateral_distance = beam_spacing * num_beams
    depth_distance = c * axial_samples / f_s / 2
    extent_array=[0, lateral_distance, depth_distance,0]
    plt.imshow(B_mode_array, aspect='auto', extent=extent_array, cmap='Greys_r')
    plt.title('B-mode Ultrasound Image')
    plt.xlabel('Depth (m)')
    plt.ylabel('Distance (m)')
    plt.show()
    return extent_array


def image_save(image_filename, B_mode_array):
    try:
        plt.imsave(image_filename, B_mode_array, cmap='Greys_r')
    except IOError:
        print('There is no more space, please delete something on your hard-drive')
        raise IOError
    except ValueError:
        print('You used an nsupported file format. eps, jpeg, jpg, pdf, pgf, png, ps, raw, rgba,'
              ' svg, svgz, tif, tiff are supported')
        raise ValueError
