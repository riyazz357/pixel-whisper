# 🕵️ Pixel Whisper (Steganography Tool)

A Python-based CLI tool that hides secret text messages inside image files using **Least Significant Bit (LSB)** manipulation. Built as part of the "15 Days, 15 Projects" challenge (Day 2).

## 🚀 How It Works
Digital images are made of pixels, and each pixel has Red, Green, and Blue (RGB) values. This tool modifies the **last bit** of these values to store binary data.
* **Original Pixel:** `11001000` (Value: 200)
* **Encoded Pixel:** `11001001` (Value: 201)
* **Result:** The color change is so small (1/255th difference) that the human eye cannot detect it.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Libraries:** * `Pillow` (PIL) - For image processing.
    * `NumPy` - For efficient pixel array manipulation.

## ⚙️ Installation

1.  Clone the repository:
    ```bash
    git clone [https://github.com/yourusername/pixel-whisper.git](https://github.com/yourusername/pixel-whisper.git)
    cd pixel-whisper
    ```

2.  Install dependencies:
    ```bash
    pip install pillow numpy
    ```

## 🖥️ Usage

1.  **Prepare an Image:**
    * Place a **PNG** image named `input.png` in the project folder. 
    * *(Note: JPGs don't work well because their compression destroys pixel data).*

2.  **Run the Script:**
    ```bash
    python stego.py
    ```

3.  **Choose Mode:**
    * **Encode (E):** Enter your secret message. The script will generate `secret_image.png`.
    * **Decode (D):** The script reads `secret_image.png` and extracts the hidden text.

## 🔍 Code logic
* **Delimiter:** The script automatically appends `#####` to your message. When decoding, it looks for this pattern to know exactly where the message ends.
* **Binary Conversion:** Converts every character of your message into 8-bit binary strings (ASCII).
* **Pixel Traversal:** Iterates through the image matrix row by row, modifying RGB channels sequentially.

## ⚠️ Limitations
* **Image Size:** The amount of text you can hide depends on the image resolution. A 500x500 image can hold huge amounts of text.
* **Format:** Only supports lossless formats like **PNG**. Saving as JPG will corrupt the hidden data.
