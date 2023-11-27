import qrcode
data = "맥크리스피 스리라차버거세트"
img = qrcode.make(data=data)
img.show()