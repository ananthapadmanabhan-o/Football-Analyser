from utils import read_video, save_video

def main():

    video_frame = read_video('input_video/video_01.mp4')

    save_video(video_frame,'output_video/output_video_01.avi')

if __name__=='__main__':
    main()