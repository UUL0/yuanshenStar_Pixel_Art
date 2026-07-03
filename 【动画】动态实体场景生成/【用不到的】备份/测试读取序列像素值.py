import os
import struct


class BinSequenceLoader:
    """一次性加载所有 BIN 序列文件，支持按文件序号和像素索引读取像素值"""

    def __init__(self, folder_path, width, height):
        """
        folder_path: BIN 文件所在文件夹
        width:  图片宽度
        height: 图片高度
        """
        self.width = width
        self.height = height
        self.pixels_per_frame = width * height * 4  # 每帧的字节数
        self.frames = {}  # 文件序号 → 像素字节数据

        # 获取所有 .bin 文件，按数字文件名排序
        bin_files = []
        for fname in os.listdir(folder_path):
            if fname.lower().endswith('.bin'):
                try:
                    seq = int(os.path.splitext(fname)[0])  # 提取数字序号
                    bin_files.append((seq, os.path.join(folder_path, fname)))
                except ValueError:
                    continue  # 跳过非纯数字文件名

        bin_files.sort(key=lambda x: x[0])  # 按序号从小到大排序

        # 一次性加载所有文件
        for seq, filepath in bin_files:
            with open(filepath, 'rb') as f:
                data = f.read()
            if len(data) != self.pixels_per_frame:
                raise ValueError(
                    f"文件 {filepath} 大小 {len(data)} 字节，"
                    f"期望 {self.pixels_per_frame} 字节"
                )
            self.frames[seq] = data

        self.frame_numbers = sorted(self.frames.keys())  # 原始文件序号列表
        self.seq_by_index = {i: seq for i, seq in enumerate(self.frame_numbers) }# 建立连续索引 → 原始序号的映射
        print(f"✓ 已加载 {len(self.frames)} 帧")
        print(f"  帧序号范围: {self.frame_numbers[0]} ~ {self.frame_numbers[-1]}")
        print(f"  每帧尺寸: {width}×{height}")

    def get_pixel_by_index(self, index, pixel_index):
        """
        按连续索引读取像素值（0 对应最小文件序号，1 对应第二小...）

        index:       连续索引（0 到 帧数-1）
        pixel_index: 像素索引（0 为左下角）
        """
        if index < 0 or index >= len(self.frame_numbers):
            raise IndexError(f"索引 {index} 超出范围 [0, {len(self.frame_numbers) - 1}]")
        seq = self.seq_by_index[index]
        return self.get_pixel(seq, pixel_index)

    def get_pixel_xy_by_index(self, index, x, y):
        """按连续索引 + XY 坐标读取像素值"""
        if index < 0 or index >= len(self.frame_numbers):
            raise IndexError(f"索引 {index} 超出范围 [0, {len(self.frame_numbers) - 1}]")
        seq = self.seq_by_index[index]
        return self.get_pixel_xy(seq, x, y)
    def get_pixel(self, frame_seq, pixel_index):
        """
        读取指定帧中指定像素索引的 RGBA 值

        frame_seq:   文件序号（数字）
        pixel_index: 像素索引（0 为左下角，从左到右，从下到上）
        返回: (R, G, B, A) 元组
        """
        if frame_seq not in self.frames:
            raise KeyError(f"帧序号 {frame_seq} 不存在")

        total_pixels = self.width * self.height
        if pixel_index < 0 or pixel_index >= total_pixels:
            raise IndexError(
                f"像素索引 {pixel_index} 超出范围 [0, {total_pixels - 1}]"
            )

        offset = pixel_index * 4
        data = self.frames[frame_seq]
        r, g, b, a = data[offset], data[offset + 1], data[offset + 2], data[offset + 3]
        return (r, g, b, a)

    def get_pixel_xy(self, frame_seq, x, y):
        """
        根据 XY 坐标读取像素值

        frame_seq: 文件序号（数字）
        x: 列坐标（0 = 最左）
        y: 行坐标（0 = 最下）
        返回: (R, G, B, A) 元组
        """
        if x < 0 or x >= self.width:
            raise IndexError(f"X 坐标 {x} 超出范围 [0, {self.width - 1}]")
        if y < 0 or y >= self.height:
            raise IndexError(f"Y 坐标 {y} 超出范围 [0, {self.height - 1}]")

        pixel_index = y * self.width + x
        return self.get_pixel(frame_seq, pixel_index)

    def get_all_pixels(self, frame_seq):
        """获取某一帧的所有像素（返回生成器，适合逐像素处理）"""
        if frame_seq not in self.frames:
            raise KeyError(f"帧序号 {frame_seq} 不存在")

        data = self.frames[frame_seq]
        for i in range(0, len(data), 4):
            yield (data[i], data[i + 1], data[i + 2], data[i + 3])


# ==================== 使用示例 ====================
if __name__ == '__main__':
    import sys

    if len(sys.argv) != 4:
        print("用法: python script.py <BIN文件夹> <宽度> <高度>")
        sys.exit(1)

    folder = sys.argv[1]
    width = int(sys.argv[2])
    height = int(sys.argv[3])

    # 一次性加载所有帧
    loader = BinSequenceLoader(folder, width, height)

    # 方法1：用原始文件序号访问（如文件 5.bin, 6.bin...）
    r, g, b, a = loader.get_pixel(1001, 100)      # 文件 5.bin 的第 100 号像素

    # 方法2：用连续索引访问（0=最小序号文件, 1=第二小...）
    r, g, b, a = loader.get_pixel_by_index(0, 100)   # 最小序号文件的第 100 号像素
    print(r, g, b, a )
    # 查看映射关系
    print("原始序号:", loader.frame_numbers)          # 如 [5, 6, 7, 8, ...]
    print("连续索引0→原始序号:", loader.seq_by_index[0])  # 5

