import sys
import os

try:
    from PIL import Image
    print("✓ Pillow 已安装")
except ImportError:
    print("✗ 请先安装 Pillow：pip install Pillow")
    sys.exit(1)


def png_to_bin(png_path, bin_path):
    """PNG 转 BIN：左下角为起点，从下往上、从左到右存储 RGBA 像素"""
    with Image.open(png_path) as img:
        img = img.convert('RGBA')
        flipped = img.transpose(Image.FLIP_TOP_BOTTOM)   # 上下翻转
        rgba_data = flipped.tobytes()

        with open(bin_path, 'wb') as f:
            f.write(rgba_data)


def main():
    if len(sys.argv) != 3:
        print("用法: python script.py <输入PNG文件夹> <输出BIN文件夹>")
        sys.exit(1)

    input_folder = sys.argv[1]
    output_folder = sys.argv[2]

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.png'):
            png_path = os.path.join(input_folder, filename)
            bin_path = os.path.join(output_folder, filename.replace('.png', '.bin'))
            png_to_bin(png_path, bin_path)
            print(f"✓ {filename} → {os.path.basename(bin_path)}")


if __name__ == '__main__':
    main()
