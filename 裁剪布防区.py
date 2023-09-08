import cv2
import os

def crop_video(input_path, output_folder, x1, y1, x2, y2):
    # 创建输出文件夹
    os.makedirs(output_folder, exist_ok=True)

    # 处理输入路径是文件夹的情况
    if os.path.isdir(input_path):
        # 遍历文件夹中的所有视频文件
        for file_name in os.listdir(input_path):
            if file_name.endswith(('.mp4', '.avi', '.mov')):  # 确认文件是视频文件
                video_path = os.path.join(input_path, file_name)
                crop_single_video(video_path, output_folder, x1, y1, x2, y2)
    else:
        # 处理输入路径是单个视频文件的情况
        crop_single_video(input_path, output_folder, x1, y1, x2, y2)

def crop_single_video(input_path, output_folder, x1, y1, x2, y2):
    # 打开视频
    cap = cv2.VideoCapture(input_path)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # 获取视频的帧率、宽度和高度
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # 创建 VideoWriter 对象，用于保存裁剪后的视频
    video_name = os.path.splitext(os.path.basename(input_path))[0] + '_cropped.mp4'
    out_path = os.path.join(output_folder, video_name)
    out = cv2.VideoWriter(out_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (x2-x1, y2-y1))

    # 开始裁剪视频
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # 裁剪帧
        cropped_frame = frame[y1:y2, x1:x2]

        # 将裁剪后的帧写入输出视频
        out.write(cropped_frame)

    # 释放 VideoCapture 和 VideoWriter 对象
    cap.release()
    out.release()
    cv2.destroyAllWindows()

# 示例用法
input_path = 'path_to_input_video_or_folder'  # 输入视频或视频文件夹路径
output_folder = 'output_folder_path'          # 输出文件夹路径
x1, y1, x2, y2 = 100, 100, 400, 400           # 框坐标 (x1, y1, x2, y2)

crop_video(input_path, output_folder, x1, y1, x2, y2)
