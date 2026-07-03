from io import StringIO
import os
import struct
import sys

try:
    from PIL import Image
    print("Pillow 已安装")
except ImportError:
    print("请先安装 Pillow：pip install Pillow")
    sys.exit(1)

# 以XY排列布局
# 按从左下角开始，从左到右，从下到上的顺序

def 生成静态画像素实体(RGBA_DATA,output_file,dW=0,dH=0):
    # 通过HEX编辑器或解封装gia，最后几行中查看
    导出参数ID="100000000-1782032127-1073741832" # 你账号导出gia的最后参数字符串(例如：xxxxxxxxx-xxxxxxxxxx-xxxxxxxxxx，似乎是账号UID+"-"+ID1+"-"+ID2)
    版本号="6.7.0" #当前版本的版本号

    # 设定起始初始参数
    GUID起始值=1077943195
    # 也可以自行修改，以X或Z轴方向排列，Y是高度，图像从下之上0~N绘制
    起始坐标X=-15.0 # "画布"的位置，以YZ为基准，是以上下左右为布局，可以导入后整体缩放或旋转
    起始坐标Y=0.0
    起始坐标Z=-15.0
    实体缩放X=1.0 # 可以导入后整体缩放
    实体缩放Y=1.0
    实体缩放Z=1.0
    实体名称="静态画像素实体"
    X间距=1.0
    Y间距=1.0
    透明像素跳过=1 # 如果是透明像素则不生成静态实体（空一格）

    参数00="{\n"
    参数0="  '01:"
    参数1=":embedded message': \n    {\n      '01:00:embedded message': \n        {\n          '02:00:Varint': 1,\n          '03:01:Varint': 2,\n          '04:02:Varint': "
    参数2="\n        },\n      '02:01:embedded message': \n        {\n          '02:00:Varint': 1,\n          '03:01:Varint': 1,\n          '04:02:Varint': 1077936131\n        },\n      '03:02:string': '"
    参数3="',\n      '05:03:Varint': 3,\n      '12:04:embedded message': \n        {\n          '01:00:embedded message': \n            {\n              '01:00:Varint': "
    参数4=",\n              '02:01:embedded message': \n                {\n                  '01:00:Varint': 1077936131\n                },\n              '05:02:embedded message': \n                {\n                  '01:00:Varint': 1,\n                  '11:01:embedded message': \n                    {\n                      '01:00:string': '"
    参数5="',\n                      '02:01:Varint': 1\n                    }\n                },\n              '05:03:embedded message': \n                {\n                  '01:00:Varint': 13,\n                  '22:01:embedded message': \n                    {\n                      '04:00:Varint': 4294967295\n                    }\n                },\n              '05:04:embedded message': \n                {\n                  '01:00:Varint': 14,\n                  '23:01:embedded message': \n                    {\n                      '01:00:embedded message': \n                        {\n                          '03:00:string': 'MPActionGroup'\n                        }\n                    }\n                },\n              '05:05:embedded message': \n                {\n                  '01:00:Varint': 38,\n                  '48:01:embedded message': \n                    {\n                      '01:00:32-bit': 1.0\n                    }\n                },\n              '05:06:embedded message': \n                {\n                  '01:00:Varint': 40,\n                  '50:01:embedded message': \n                    {\n                    }\n                },\n              '05:07:embedded message': \n                {\n                  '01:00:Varint': 111,\n                  '93:01:embedded message': \n                    {\n                    }\n                },\n              '05:08:embedded message': \n                {\n                  '01:00:Varint': 61,\n                  '65:01:embedded message': \n                    {\n                    }\n                },\n              '05:09:embedded message': \n                {\n                  '01:00:Varint': 62,\n                  '66:01:embedded message': \n                    {\n                    }\n                },\n              '05:10:embedded message': \n                {\n                  '01:00:Varint': 19,\n                  '28:01:embedded message': \n                    {\n                    }\n                },\n              '05:11:embedded message': \n                {\n                  '01:00:Varint': 52,\n                  '62:01:embedded message': \n                    {\n                    }\n                },\n              '06:12:embedded message': \n                {\n                  '01:00:Varint': 1,\n                  '11:01:embedded message': \n                    {\n                      '01:00:embedded message': \n                        {\n                          '01:00:32-bit': "
    参数6=",\n                          '02:01:32-bit': "
    参数7=",\n                          '03:02:32-bit': "
    参数8="\n                        },\n                      '02:01:embedded message': \n                        {\n                        },\n                      '03:02:embedded message': \n                        {\n                          '01:00:32-bit': "
    参数9=",\n                          '02:01:32-bit': "
    参数10=",\n                          '03:02:32-bit': "
    参数11="\n                        },\n                      '501:03:Varint': 4294967295\n                    }\n                },\n              '06:13:embedded message': \n                {\n                  '01:00:Varint': 2,\n                  '12:01:embedded message': \n                    {\n                    }\n                },\n              '06:14:embedded message': \n                {\n                  '01:00:Varint': 3,\n                  '13:01:embedded message': \n                    {\n                    }\n                },\n              '06:15:embedded message': \n                {\n                  '01:00:Varint': 4,\n                  '14:01:embedded message': \n                    {\n                      '01:00:Varint': 1\n                    }\n                },\n              '06:16:embedded message': \n                {\n                  '01:00:Varint': 5,\n                  '15:01:embedded message': \n                    {\n                      '01:00:Varint': 1,\n                      '02:01:Varint': 1\n                    }\n                },\n              '06:17:embedded message': \n                {\n                  '01:00:Varint': 6,\n                  '16:01:embedded message': \n                    {\n                    }\n                },\n              '06:18:embedded message': \n                {\n                  '01:00:Varint': 7,\n                  '17:01:embedded message': \n                    {\n                      '01:00:32-bit': 1.0,\n                      '02:01:32-bit': 1.0,\n                      '03:02:32-bit': 1.0,\n                      '05:03:Varint': 1,\n                      '06:04:embedded message': \n                        {\n                          '02:00:Varint': 10200002\n                        },\n                      '08:05:32-bit': 0.10000000149011612,\n                      '09:06:32-bit': 0.10000000149011612,\n                      '10:07:32-bit': 0.10000000149011612,\n                      '11:08:32-bit': 0.10000000149011612,\n                      '12:09:32-bit': 0.10000000149011612,\n                      '13:10:32-bit': 0.10000000149011612,\n                      '14:11:32-bit': 0.10000000149011612,\n                      '15:12:32-bit': 0.10000000149011612\n                    }\n                },\n              '06:19:embedded message': \n                {\n                  '01:00:Varint': 8,\n                  '18:01:embedded message': \n                    {\n                      '01:00:Varint': 1,\n                      '501:01:Varint': 1\n                    }\n                },\n              '06:20:embedded message': \n                {\n                  '01:00:Varint': 11,\n                  '21:01:embedded message': \n                    {\n                      '01:00:embedded message': \n                        {\n                          '01:00:string': 'GI_RootNode',\n                          '02:01:embedded message': \n                            {\n                            },\n                          '03:02:embedded message': \n                            {\n                            },\n                          '502:03:string': '中心原点',\n                          '504:04:Varint': 1,\n                          '505:05:string': 'RootNode'\n                        }\n                    }\n                },\n              '06:21:embedded message': \n                {\n                  '01:00:Varint': 12,\n                  '22:01:embedded message': \n                    {\n                      '501:00:Varint': 1\n                    }\n                },\n              '06:22:embedded message': \n                {\n                  '01:00:Varint': 16,\n                  '26:01:embedded message': \n                    {\n                    }\n                },\n              '06:23:embedded message': \n                {\n                  '01:00:Varint': 17,\n                  '27:01:embedded message': \n                    {\n                    }\n                },\n              '06:24:embedded message': \n                {\n                  '01:00:Varint': 19,\n                  '29:01:embedded message': \n                    {\n                      '01:00:Varint': 1\n                    }\n                },\n              '06:25:embedded message': \n                {\n                  '01:00:Varint': 20,\n                  '30:01:embedded message': \n                    {\n                    }\n                },\n              '06:26:embedded message': \n                {\n                  '01:00:Varint': 22,\n                  '32:01:embedded message': \n                    {\n                      '01:00:Varint': 1,\n                      '03:01:Varint': "
    # 引用ARGB
    参数11_ARGB=",\n                      '04:02:32-bit': "
    参数12=",\n                      '05:03:Varint': "
    参数13=",\n                      '06:04:Varint': 6700\n                    }\n                },\n              '08:27:Varint': 10009001\n            },\n          '02:01:Varint': 1402,\n          '04:02:Varint': 10009001\n        }\n    },\n"

    # =====公共引用
    引用参数0="  '02:"
    引用参数1=":embedded message': \n    {\n      '01:00:embedded message': \n        {\n          '02:00:Varint': 1,\n          '03:01:Varint': 1,\n          '04:02:Varint': 1077936131\n        },\n      '03:01:string': '静态颜色测试2',\n      '05:02:Varint': 1,\n      '11:03:embedded message': \n        {\n          '01:00:embedded message': \n            {\n              '01:00:Varint': 1077936131,\n              '02:01:Varint': 10009001,\n              '06:02:embedded message': \n                {\n                  '01:00:Varint': 1,\n                  '11:01:embedded message': \n                    {\n                      '01:00:string': '静态颜色测试2',\n                      '02:01:Varint': 1\n                    }\n                },\n              '06:03:embedded message': \n                {\n                  '01:00:Varint': 13,\n                  '22:01:embedded message': \n                    {\n                      '04:00:Varint': 4294967295\n                    }\n                },\n              '06:04:embedded message': \n                {\n                  '01:00:Varint': 14,\n                  '23:01:embedded message': \n                    {\n                      '01:00:embedded message': \n                        {\n                          '03:00:string': 'MPActionGroup'\n                        }\n                    }\n                },\n              '06:05:embedded message': \n                {\n                  '01:00:Varint': 38,\n                  '48:01:embedded message': \n                    {\n                      '01:00:32-bit': 1.0\n                    }\n                },\n              '06:06:embedded message': \n                {\n                  '01:00:Varint': 40,\n                  '50:01:embedded message': \n                    {\n                    }\n                },\n              '06:07:embedded message': \n                {\n                  '01:00:Varint': 111,\n                  '93:01:embedded message': \n                    {\n                    }\n                },\n              '06:08:embedded message': \n                {\n                  '01:00:Varint': 61,\n                  '65:01:embedded message': \n                    {\n                    }\n                },\n              '06:09:embedded message': \n                {\n                  '01:00:Varint': 62,\n                  '66:01:embedded message': \n                    {\n                    }\n                },\n              '07:10:embedded message': \n                {\n                  '01:00:Varint': 1,\n                  '11:01:embedded message': \n                    {\n                      '01:00:embedded message': \n                        {\n                          '01:00:32-bit': 1.2351875305175781,\n                          '02:01:32-bit': 0.25,\n                          '03:02:32-bit': -9.769210815429688\n                        },\n                      '02:01:embedded message': \n                        {\n                        },\n                      '03:02:embedded message': \n                        {\n                          '01:00:32-bit': 1.0,\n                          '02:01:32-bit': 1.0,\n                          '03:02:32-bit': 1.0\n                        },\n                      '501:03:Varint': 4294967295\n                    }\n                },\n              '07:11:embedded message': \n                {\n                  '01:00:Varint': 2,\n                  '12:01:embedded message': \n                    {\n                    }\n                },\n              '07:12:embedded message': \n                {\n                  '01:00:Varint': 3,\n                  '13:01:embedded message': \n                    {\n                    }\n                },\n              '07:13:embedded message': \n                {\n                  '01:00:Varint': 4,\n                  '14:01:embedded message': \n                    {\n                      '01:00:Varint': 1\n                    }\n                },\n              '07:14:embedded message': \n                {\n                  '01:00:Varint': 5,\n                  '15:01:embedded message': \n                    {\n                      '01:00:Varint': 1,\n                      '02:01:Varint': 1\n                    }\n                },\n              '07:15:embedded message': \n                {\n                  '01:00:Varint': 6,\n                  '16:01:embedded message': \n                    {\n                    }\n                },\n              '07:16:embedded message': \n                {\n                  '01:00:Varint': 7,\n                  '17:01:embedded message': \n                    {\n                      '01:00:32-bit': 1.0,\n                      '02:01:32-bit': 1.0,\n                      '03:02:32-bit': 1.0,\n                      '05:03:Varint': 1,\n                      '06:04:embedded message': \n                        {\n                          '02:00:Varint': 10200002\n                        },\n                      '08:05:32-bit': 0.10000000149011612,\n                      '09:06:32-bit': 0.10000000149011612,\n                      '10:07:32-bit': 0.10000000149011612,\n                      '11:08:32-bit': 0.10000000149011612,\n                      '12:09:32-bit': 0.10000000149011612,\n                      '13:10:32-bit': 0.10000000149011612,\n                      '14:11:32-bit': 0.10000000149011612,\n                      '15:12:32-bit': 0.10000000149011612\n                    }\n                },\n              '07:17:embedded message': \n                {\n                  '01:00:Varint': 8,\n                  '18:01:embedded message': \n                    {\n                      '01:00:Varint': 1,\n                      '501:01:Varint': 1\n                    }\n                },\n              '07:18:embedded message': \n                {\n                  '01:00:Varint': 11,\n                  '21:01:embedded message': \n                    {\n                      '01:00:embedded message': \n                        {\n                          '01:00:string': 'GI_RootNode',\n                          '02:01:embedded message': \n                            {\n                            },\n                          '03:02:embedded message': \n                            {\n                            },\n                          '502:03:string': '中心原点',\n                          '504:04:Varint': 1,\n                          '505:05:string': 'RootNode'\n                        }\n                    }\n                },\n              '07:19:embedded message': \n                {\n                  '01:00:Varint': 12,\n                  '22:01:embedded message': \n                    {\n                      '501:00:Varint': 1\n                    }\n                },\n              '07:20:embedded message': \n                {\n                  '01:00:Varint': 16,\n                  '26:01:embedded message': \n                    {\n                    }\n                },\n              '07:21:embedded message': \n                {\n                  '01:00:Varint': 17,\n                  '27:01:embedded message': \n                    {\n                    }\n                },\n              '07:22:embedded message': \n                {\n                  '01:00:Varint': 19,\n                  '29:01:embedded message': \n                    {\n                      '01:00:Varint': 1\n                    }\n                },\n              '07:23:embedded message': \n                {\n                  '01:00:Varint': 20,\n                  '30:01:embedded message': \n                    {\n                    }\n                },\n              '07:24:embedded message': \n                {\n                  '01:00:Varint': 22,\n                  '32:01:embedded message': \n                    {\n                      '01:00:Varint': 1,\n                      '03:01:Varint': 4294967295,\n                      '04:02:32-bit': 100.0,\n                      '05:03:Varint': 16777215,\n                      '06:04:Varint': 6700\n                    }\n                },\n              '10:25:Varint': 1\n            }\n        }\n    },\n"
    引用参数2="  '03:"
    引用参数3=":string': '"
    引用参数4="-\\示例静态场景组.gia',\n"
    引用参数5="  '05:"
    引用参数6=":string': '"
    版本号="6.7.0"
    引用参数7="'\n}"

    # 写入文件流程：
    # 参数00
    # 实体循环：
    # 参数0+排序ID+参数1+实体GUID+参数2+实体名称+参数3+实体GUID+参数4+实体名称+参数5+实体位置X+参数6+实体位置Y+参数7+实体位置Z+参数8+实体缩放X+参数9+实体缩放Y+参数10+实体缩放Z+参数11+引用ARGB+参数11_ARGB+实体颜色透明度+参数12+实体颜色+参数13
    # 实体循环结束

    # 引用参数0+排序ID+引用参数1+引用参数2+排序ID+引用参数3+导出参数ID+引用参数4+引用参数5+排序ID+引用参数6+版本号+引用参数7

    # 预拼接模板 + StringIO 批量写入
    # 缓冲区
    buffer = StringIO()

    # 开始循环
    实体数量=0
    # 以下是生成的计数用的
    实体GUID=0
    EnX=起始坐标X
    EnY=起始坐标Y
    EnZ=起始坐标Z

    实体位置X=起始坐标X
    实体位置Y=起始坐标Y
    实体位置Z=起始坐标Z

    排序ID=0


    buffer.write(参数00)
    for VY in range(dH):
        实体位置Z=EnZ # 重设起始
        # 实体位置X=EnX # 以X轴为排列或Z轴排列
        for VX in range(dW):
            RGBA_offset = 实体数量 * 4
            RGB_int = (RGBA_DATA[RGBA_offset] << 16) | (RGBA_DATA[RGBA_offset+1] << 8) | (RGBA_DATA[RGBA_offset+2] )
            Alp_int =RGBA_DATA[RGBA_offset+3] # 0~255的值
            if Alp_int > 0 or (Alp_int == 0 and 透明像素跳过 != 1): # 判断透明度为0时是否要执行空格
                实体颜色=RGB_int & 0xFFFFFF # 十进制RGB值
                实体颜色透明度=float(round(Alp_int * (100 / 255))) # 映射到 0-100浮点数
                引用ARGB=((Alp_int<<24) | RGB_int) & 0xFFFFFFFF
                实体GUID=GUID起始值+实体数量
                实体循环结果=f"{参数0}{排序ID:02d}{参数1}{实体GUID}{参数2}{实体名称}{排序ID:02d}{参数3}{实体GUID}{参数4}{实体名称}{排序ID:02d}{参数5}{实体位置X}{参数6}{实体位置Y}{参数7}{实体位置Z}{参数8}{实体缩放X}{参数9}{实体缩放Y}{参数10}{实体缩放Z}{参数11}{引用ARGB}{参数11_ARGB}{实体颜色透明度}{参数12}{实体颜色}{参数13}"
                buffer.write(实体循环结果)
                排序ID+=1
            实体位置Z += X间距
            # 实体位置X += X间距 # 以X轴为排列或Z轴排列
            实体数量+=1
        实体位置Y += Y间距

    buffer.write(f"{引用参数0}{排序ID}{引用参数1}")
    排序ID+=1
    buffer.write(f"{引用参数2}{排序ID}{引用参数3}{导出参数ID}{引用参数4}")
    排序ID+=1
    buffer.write(f"{引用参数5}{排序ID}{引用参数6}{版本号}{引用参数7}")

    # ========== 一次性写入文件 ==========
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(buffer.getvalue())
    print(f"图像大小：{dW}*{dH} 本次生成{排序ID}个静态实体 场景数据写入{output_file}")


def png_to_byte(png_file):
    """PNG 转 一维字节序列：左下角为起点，从下往上、从左到右存储 RGBA 像素"""
    with Image.open(png_file) as img:
        img = img.convert('RGBA')
        flipped = img.transpose(Image.FLIP_TOP_BOTTOM)   # 上下翻转
        width, height = img.size
        rgba_data = flipped.tobytes()
        return rgba_data,width , height

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("用法: python script.py <png图像> <输出文件>")
        sys.exit(1)

    png_file = sys.argv[1]
    output_file = sys.argv[2]
    RGBA_DATA,dW , dH=png_to_byte(png_file)
    生成静态画像素实体(RGBA_DATA,output_file,dW,dH)








