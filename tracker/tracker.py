from ultralytics import YOLO


class Tracker:
    
    def __init__(self,model_path):
        self.model = YOLO(model_path)


    def detect_frames(self,frames):
        batch_size = 20
        detections = []

        for i in range(0,len(frames),batch_size):
            detection_batch = self.model.predict(frames[i:i+batch_size],conf=0.1)
            detections += detection_batch
        
        return detections


    def get_object_tracker(self,frames):

        detections =  self.detect_frames(frames)
