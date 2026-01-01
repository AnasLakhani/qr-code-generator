import qrcode

# The data you want to encode
data = "https://share.google/LWV9RQXBkWTdYmzuY"

# Create the QR code object
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(data)
qr.make(fit=True)

# Create an image (PNG) from the QR code instance
img = qr.make_image(fill_color="#14463d", back_color="white")

# Save the file
img.save("map.png")

print("QR code saved as map.png")