#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image
from PIL import PSDraw
origin_name = 'origin.jpg'
modified_name = 'modified.jpg'
text = '7'
box = (1 * 72, 2 * 72, 7 * 72, 10 * 72)
img = Image.open(origin_name)
width, height = img.size
fillColor = "#ff0000"
ps = PSDraw.PSDraw(img)
ps.begin_document(text)
ps.image(box, img, 75)
ps.rectangle(box)
ps.setfont("HelveticaNarrow-Bold", 36)
ps.text((3 * 72, 4 * 72), text)
ps.end_document()
img.save(modified_name)
