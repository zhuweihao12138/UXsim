from PIL import Image
import numpy as np
import imageio

# 读取GIF文件
reader = imageio.get_reader('outsioufalls_matsim3/anim_network_fancy.gif')

# 准备写入MP4文件，这里我们不指定fps，稍后会手动设置
writer = imageio.get_writer('outsioufalls_matsim3/anim_network_fancy.mp4', fps=16)  # 假设帧率是10

# 读取每一帧并转换为RGB格式
for i, im in enumerate(reader):
    # 将图像转换为RGB格式
    if im.shape[-1] == 4:  # 如果是RGBA，转换为RGB
        im = im[:,:,:3]
    elif im.shape[-1] == 1:  # 如果是灰度图，转换为RGB
        im = np.stack((im,)*3, axis=-1)

    # 写入MP4文件
    writer.append_data(im)

# 完成写入并关闭文件
del writer