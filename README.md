# QR Code Generator

A simple Python script to generate a QR code and export it as a PNG
image.

------------------------------------------------------------------------

## 💻 Usage

### 1. Clone the repository

``` bash
git clone https://github.com/AnasLakhani/qr-code-generator.git
cd qr-code-generator
```

### 2. Create the Python script

Create a file named `main.py` and paste the following code:

``` python
import qrcode

# 1. The data you want to encode
data = "https://github.com/AnasLakhani"

# 2. Configure the QR Code
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

# 3. Export as PNG
img = qr.make_image(fill_color="black", back_color="white")
img.save("my_qrcode.png")

print("✅ QR Code saved successfully as my_qrcode.png")
```

### 3. Run the script

``` bash
python main.py
```

After running the script, a file named `my_qrcode.png` will be created
in the project directory.

------------------------------------------------------------------------

## ⚙️ Configuration

You can customize the `QRCode` parameters to change the look of the
image:

  ------------------------------------------------------------------------
  Parameter                  Default            Description
  -------------------------- ------------------ --------------------------
  version                    1                  Controls the size of the
                                                QR grid, range is 1 to 40

  box_size                   10                 Number of pixels for each
                                                QR box

  border                     4                  Thickness of the white
                                                border

  fill_color                 black              Color of the QR code

  back_color                 white              Background color
  ------------------------------------------------------------------------

------------------------------------------------------------------------

## 📄 License

This project is open source and available under the MIT License.

------------------------------------------------------------------------

### Developed by Anas Lakhani
