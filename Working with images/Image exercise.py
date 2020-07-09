from PIL import Image

mask = Image.open(r'mask.png')
#mask.size # 505, 251

words =Image.open(r'word_matrix.png')
#words.size # 1015, 559

new_mask = mask.resize((1015, 559))

new_mask.putalpha(200)
words.paste(im=new_mask, box =(0,0), mask =new_mask)

words.show()