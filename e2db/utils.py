from base64    import encodestring
from io        import BytesIO
from operator  import methodcaller
from pipetools import pipe
from qrcode    import make

def qr_image(data):
    """a QR code of the given data as a raw PNG"""
    
    image = BytesIO()
    make(data).save(image) # generate QR and save it to `image`
    return image.getvalue()

"""HTML containing a Base64 data URI of the given image"""
inline = pipe | encodestring | methodcaller('decode') | '<img src="data:image/png;base64,{}">'.format

"""HTML containing an inlined QR code of the given data"""
qr_page = pipe | qr_image | inline
