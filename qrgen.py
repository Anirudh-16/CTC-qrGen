import qrcode

def qrgen(gen):
    qr = qrcode.make(gen)
    qr.save("qrcode.png")
    return "qrcode.png"