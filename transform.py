from PIL import Image

image1 = Image.open(r'test.jpg')
im1 = image1.convert('RGB')
im1.save(r'result.pdf')
