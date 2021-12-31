from PIL import Image
filen = r'icon.png'
img = Image.open(filen)
img.save('icon.ico', format = 'ICO', sizes=[(64,64)])
