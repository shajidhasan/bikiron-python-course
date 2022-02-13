from PIL import Image
from glob import glob
from os.path import join, basename

images = glob("images/*.jpg")
watermark = Image.open("watermark.png")
wm_w, wm_h = watermark.size
factor = 1 / 10
margin_factor = 1 / 30

for image in images:
    im = Image.open(image)
    im_w, im_h = im.size
    n_w, n_h = (int(im_w * factor), int(wm_h * (im_w * factor / wm_w)))
    wm = watermark.resize((n_w, n_h), Image.ANTIALIAS)
    margin = int(im_w * margin_factor)
    im.paste(wm, (im_w - n_w - margin, im_h - n_h - margin), wm)
    
    output_path = join('watermarked', basename(image))
    im.save(output_path)

print("Kaaj shesh! 'Watermarked' folder ta check kor.")
