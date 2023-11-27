import os

mapping =  {
  'dirt': 0, 
  'pens': 1, 
  'paper_and_notebooks':2,
  'keys': 3,
  'usb_sticks': 4,
  'other': 5,
  'rulers': 6,
  'business_cards': 7,
  'scissors': 8,
  'tapes': 9}

def convert_to_yolo_format(l,image_height=1024,image_width=1280):
    
    class_id = mapping[l[5]]  # 对象类别
    x_min, y_min, x_max, y_max = map(float, l[1:5])  # 边界框坐标
        
        # 计算边界框中心坐标、宽度和高度，并将其归一化
    x_center = (x_min + x_max) / (2.0 * image_width)
    y_center = (y_min + y_max) / (2.0 * image_height)
    bbox_width = (x_max - x_min) / image_width
    bbox_height = (y_max - y_min) / image_height
        
    # 将转换后的标签信息添加到列表中
    yolo_label = f"{class_id} {x_center} {y_center} {bbox_width} {bbox_height}"
    
    return yolo_label


file_path = r"C:\Users\c1257\Desktop\yolov5-master\datasets\test\blended_training_floor_images (TestSynthTF)"  # 替换为你的文件路径
with open(os.path.join(file_path,'bbox_labels.txt'), "r") as file:
    # 逐行读取文件内容
    line = file.readline()
    l = line.split()
    pic_name = l[0]
    label_file = open(os.path.join(file_path, pic_name+".txt"),"w")
    output = convert_to_yolo_format(l)
    label_file.write(output+"\n")
    line = file.readline()
    while line:
        # 处理每行的数据
        l = line.split()
        if l[0] == pic_name:
            output = convert_to_yolo_format(l)
            label_file.write(output+"\n")
        else:
            label_file.close()
            l = line.split()
            pic_name = l[0]
            label_file = open(os.path.join(file_path, pic_name+".txt"),"w")
            output = convert_to_yolo_format(l)
            label_file.write(output+"\n")


        # 读取下一行
        line = file.readline()
