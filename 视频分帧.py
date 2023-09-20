import cv2
import os

def extract_frames(video_path, output_path):
    # 创建输出文件夹
    video_name = os.path.splitext(os.path.basename(video_path))[0]
    output_folder = os.path.join(output_path, video_name)
    os.makedirs(output_folder, exist_ok=True)
            

    # 打开视频文件
    cap = cv2.VideoCapture(video_path)
    frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_count += 1
        if frame_count % 10 == 0:
            frame_path = os.path.join(output_folder, f'frame_{frame_count:04d}.jpg')
            cv2.imwrite(frame_path, frame)

    cap.release()

    print(f'{frame_count} frames extracted successfully.')

if __name__ == '__main__':
    root_dir = r'D:\Documents\WXWork\1688858136411093\Cache\Video\2023-09'
    import glob

    for video_path in glob.glob(os.path.join(root_dir, '*.mp4')):
        print(video_path)
        import argparse

        parser = argparse.ArgumentParser(description='Extract frames from a video.')
        parser.add_argument('--video_path', type=str, default=video_path)
        parser.add_argument('--output_path', type=str, default=r'E:\data\images')

        args = parser.parse_args()

        if os.path.isdir(args.video_path):
            for root, dirs, files in os.walk(args.video_path):
                for file in files:
                    if file.lower().endswith(('.mp4', '.avi', '.mkv', '.mov')):
                        video_path = os.path.join(root, file)
                        extract_frames(video_path, args.output_path)
        elif os.path.isfile(args.video_path):
            extract_frames(args.video_path, args.output_path)
        else:
            print('Invalid input path.')
