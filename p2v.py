import cv2
 
fps = 5  
size = (480, 640)
# fourcc = cv2.VideoWriter_fourcc(*'DIVX')
fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
videowriter = cv2.VideoWriter("video_0.avi",fourcc,fps,size)
 
for i in range(0, 2000, 5):
    # path = "./video_left/" + str(i) + ".png"
    path = "./image_256/" + str("%06d" % i) + ".jpg"
    print(path)
    img = cv2.imread(path)
    # if i==1:
    #     cv2.imshow('image', img)
    #     cv2.waitKey(1000)
    videowriter.write(img)
cv2.destroyAllWindows()