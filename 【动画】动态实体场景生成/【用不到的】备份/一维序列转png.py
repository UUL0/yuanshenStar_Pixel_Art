import sys
import os

try:
    from PIL import Image
    print("✓ Pillow 已安装")
except ImportError:
    print("✗ 请先安装 Pillow：pip install Pillow")
    sys.exit(1)


def bin_to_png(bin_path, png_path, width, height):
    """将 BIN 序列转回 PNG 图像（BIN 左下角为起点）"""
    with open(bin_path, 'rb') as f:
        raw = f.read()

    expected_size = width * height * 4
    if len(raw) != expected_size:
        raise ValueError(
            f"文件大小 {len(raw)} 字节与 {width}×{height}×4={expected_size} 不匹配"
        )

    # 用 Pillow 从原始字节创建图像（此时第0行是左下角的数据）
    img = Image.frombytes('RGBA', (width, height), raw)

    # 上下翻转，使第0行变为图像顶部（Pillow 默认顺序）
    img = img.transpose(Image.FLIP_TOP_BOTTOM)

    img.save(png_path)


def main():
    if len(sys.argv) < 4:
        print("用法: python script.py <输入BIN文件夹> <输出PNG文件夹> <宽度> <高度>")
        print("示例: python script.py ./bin_input ./png_output 64 64")
        sys.exit(1)

    input_folder = sys.argv[1]
    output_folder = sys.argv[2]
    width = int(sys.argv[3])
    height = int(sys.argv[4])

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.bin'):
            bin_path = os.path.join(input_folder, filename)
            png_path = os.path.join(output_folder, filename.replace('.bin', '.png'))
            bin_to_png(bin_path, png_path, width, height)
            print(f"✓ {filename} → {os.path.basename(png_path)}")


if __name__ == '__main__':
    main()
