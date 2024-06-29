def bbox_center(bbox):
    x1,y1,x2,y2 = bbox 
    box_center = int((x1+x2)/2),int((y1+y2)/2)
    return box_center


def bbox_width(bbox):
    x1,y1,x2,y2 = bbox 
    box_width = x2-x1
    return box_width
