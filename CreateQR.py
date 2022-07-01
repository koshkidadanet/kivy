import PIL
import qrcode
import zlib
from PIL import Image, ImageDraw, ImageFont
import textwrap
import os


def createQrCode(InvNumber):
  str1 = InvNumber
  long_text_compressed = zlib.compress(str1.encode('utf-8'))
  qr = qrcode.QRCode(
      version=1,
      error_correction=qrcode.constants.ERROR_CORRECT_L,
      box_size=10,
      border=2,
  )
  qr.add_data(str1)
  qr.make(fit=True)
  img = qr.make_image(fill_color="black", back_color="white")
  img.save("..\\img\\QrCode.png")
  return img


def createImageWithName(ItemName):
  img = createNewImage(350,150)
  drawImage = ImageDraw.Draw(img)
  font = ImageFont.truetype("..\\ArialMT.ttf", 20)
  lines = wrapString(ItemName,30)
  drawImage = insertLinesIntoImage(lines,drawImage)
  img.save('..\\img\\Name.png')
  return img


def createImageWithInvNumber(InvNumber):
  img = createNewImage(150,20)
  drawImage = ImageDraw.Draw(img)
  font = ImageFont.truetype("..\\ArialMT.ttf", 18)
  drawImage.text((75,0), InvNumber, fill=(0,0,0),font = font, anchor='mt')
  img.save('..\\img\\InvNumber.png')
  return img


def mergeImages(QrCode,ItemName,InvNumber,number):
  new_image = createNewImage(470,160)
  ResizedQr = ResizeImage(QrCode,150,150)
  new_image.paste(ResizedQr,(0,0))
  new_image.paste(ItemName,(150,0))
  new_image.paste(InvNumber,(0,142))
  new_image.save('..\\img\\'+str(number)+".jpg","JPEG")
  return new_image


def ResizeImage(Image,x,y):
  Image = Image.resize((x,y))
  return Image


def createNewImage(x,y):
  new_image = Image.new('RGB',(x,y),(255,255,255))
  return new_image


def wrapString(string,n):
  lines = textwrap.wrap(string, width=n)
  return lines


def insertLinesIntoImage(lines,drawImage):
  y = 10
  font = ImageFont.truetype("..\\ArialMT.ttf", 20)
  for line in lines:
    drawImage.text((0,y), line, fill=(0,0,0),font = font)
    y += 20
  return drawImage

def itog(name,numb,cab):
  ImageWithName = createImageWithName(name)
  ImageWithNumber = createImageWithInvNumber(numb)
  QrCode = createQrCode(numb)
  mergeImages(QrCode, ImageWithName, ImageWithNumber, str(numb)+'_'+str(cab))
  os.remove('..\\img\\QrCode.png')
  os.remove('..\\img\\Name.png')
  os.remove('..\\img\\InvNumber.png')
