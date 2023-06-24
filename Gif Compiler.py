# Uses Pillow
# Code retrieved from https://www.blog.pythonlibrary.org/2021/06/23/creating-an-animated-gif-with-python/

from PIL import Image


def make_gif(frame_folder):
    frames = [Image.open(image) for image in [frame_folder + "/Visualization_" + str(i) + ".png" for i in range(-5,6)]]
    frame_one = frames[0]
    frame_one.save("EignevalueVisChange.gif", format="GIF", append_images=frames,
                   save_all=True, duration=100, loop=0)


if __name__ == "__main__":
    make_gif("./Visualizations")