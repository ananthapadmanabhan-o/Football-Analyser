from utils import read_video, save_video
from tracker import Tracker
from ultralytics import YOLO
import cv2 as cv


def main():

    video_frames = read_video('input_video/video-02.mp4')

    tracker = Tracker('models/best.pt')

    tracks = tracker.get_object_tracks(video_frames,
                                        read_from_stub=True,
                                        stub_path='stub/tracks.pkl')
    

    output_video_frames = tracker.draw_annotations(video_frames,tracks)

    save_video(output_video_frames,'output_video/output_video_01.avi')


    # model = YOLO('./models/best.pt')

    # img = cv.imread('./input_video/image_01.jpg')

    # res = model.predict(img,save=True,project="runs/detect", name="predict")
    # print(res[0].names)



if __name__=='__main__':
    main()