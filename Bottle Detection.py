import numpy as np 
import cv2 

# Capturing video through webcam 
webcam = cv2.VideoCapture(0) 

def nothing(x):
    pass

cv2.namedWindow("Tracking")
cv2.createTrackbar("LH", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LS", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LV", "Tracking", 0, 255, nothing)
cv2.createTrackbar("UH", "Tracking", 255, 255, nothing)
cv2.createTrackbar("US", "Tracking", 255, 255, nothing)
cv2.createTrackbar("UV", "Tracking", 255, 255, nothing)
  
# Start a while loop 
while(1): 
      
    # Reading the video from the 
    # webcam in image frames 
    _, imageFrame = webcam.read() 
  
    # Convert the imageFrame in  
    # BGR(RGB color space) to  
    # HSV(hue-saturation-value) 
    # color space 
    hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV) 
  
    l_h = cv2.getTrackbarPos("LH", "Tracking")
    l_s = cv2.getTrackbarPos("LS", "Tracking")
    l_v = cv2.getTrackbarPos("LV", "Tracking")

    u_h = cv2.getTrackbarPos("UH", "Tracking")
    u_s = cv2.getTrackbarPos("US", "Tracking")
    u_v = cv2.getTrackbarPos("UV", "Tracking")

    # Set range for purple color and  
    # define mask 
    purple_lower = np.array([109, 60, 33], np.uint8) 
    purple_upper = np.array([149, 255, 255], np.uint8) 
    purple_mask = cv2.inRange(hsvFrame, purple_lower, purple_upper) 
  
    # Set range for green color and  
    # define mask 
    green_lower = np.array([49, 190, 104], np.uint8) 
    green_upper = np.array([111, 255, 255], np.uint8) 
    green_mask = cv2.inRange(hsvFrame, green_lower, green_upper) 
  
    # Set range for yellow color and 
    # define mask 
    yellow_lower = np.array([0, 58, 137], np.uint8) 
    yellow_upper = np.array([58, 255, 255], np.uint8) 
    yellow_mask = cv2.inRange(hsvFrame, yellow_lower, yellow_upper) 
      
    # Set range for yellow color and 
    # define mask 
    white_lower = np.array([81, 53, 232], np.uint8) 
    white_upper = np.array([111, 255, 255], np.uint8) 
    white_mask = cv2.inRange(hsvFrame, white_lower, white_upper) 
      
     # Set range for yellow color and 
    # define mask 
    red_lower = np.array([l_h, l_s, l_v], np.uint8) 
    red_upper = np.array([u_h, u_s, u_v], np.uint8) 
    red_mask = cv2.inRange(hsvFrame, red_lower, red_upper) 
    # Morphological Transform, Dilation 
    # for each color and bitwise_and operator 
    # between imageFrame and mask determines 
    # to detect only that particular color 
    kernal = np.ones((5, 5), "uint8") 
      
    # For purple color 
    purple_mask = cv2.dilate(purple_mask, kernal) 
    res_purple = cv2.bitwise_and(imageFrame, imageFrame,  
                              mask = purple_mask) 
      
    # For green color 
    green_mask = cv2.dilate(green_mask, kernal) 
    res_green = cv2.bitwise_and(imageFrame, imageFrame, 
                                mask = green_mask) 
      
    # For yellow color 
    yellow_mask = cv2.dilate(yellow_mask, kernal) 
    res_yellow = cv2.bitwise_and(imageFrame, imageFrame, 
                               mask = yellow_mask) 

    # For white color 
    white_mask = cv2.dilate(white_mask, kernal) 
    res_white = cv2.bitwise_and(imageFrame, imageFrame, 
                              mask = white_mask) 
   

    # For red color 
    red_mask = cv2.dilate(red_mask, kernal) 
    res_red = cv2.bitwise_and(imageFrame, imageFrame, 
                              mask = red_mask) 
    #counting
    countG = 0
    countP = 0
    countY = 0 
    countW = 0
    countR = 0
    count = 0

    # Creating contour to track purple color 
    contours, hierarchy = cv2.findContours(purple_mask, 
                                           cv2.RETR_TREE, 
                                           cv2.CHAIN_APPROX_SIMPLE) 

    for pic, contour in enumerate(contours): 
        area = cv2.contourArea(contour) 
        if(area > 300): 
            x, y, w, h = cv2.boundingRect(contour) 
            imageFrame = cv2.rectangle(imageFrame, (x, y),  
                                       (x + w, y + h),  
                                       (150, 32, 138), 2) 
            countP = countP + 1
    wordP = "Purple Bottle: " + str(countP)
    cv2.putText(imageFrame, wordP, (500, 20), 
                cv2.FONT_HERSHEY_SIMPLEX, 
                0.5, (150, 32, 138), 2)     
  
    # Creating contour to track green color 
    contours, hierarchy = cv2.findContours(green_mask, 
                                           cv2.RETR_TREE, 
                                           cv2.CHAIN_APPROX_SIMPLE) 
      
    for pic, contour in enumerate(contours): 
        area = cv2.contourArea(contour) 
        if(area > 300): 
            x, y, w, h = cv2.boundingRect(contour) 
            imageFrame = cv2.rectangle(imageFrame, (x, y),  
                                       (x + w, y + h), 
                                       (56, 180, 110), 2) 
            countG = countG + 1
    wordG = "Green Bottle: " + str(countG)
    cv2.putText(imageFrame, wordG, (500, 35), 
                cv2.FONT_HERSHEY_SIMPLEX,  
                0.5, (21, 168, 2), 2) 
  
    # Creating contour to track blue color 
    contours, hierarchy = cv2.findContours(yellow_mask, 
                                           cv2.RETR_TREE, 
                                           cv2.CHAIN_APPROX_SIMPLE) 
    for pic, contour in enumerate(contours): 
        area = cv2.contourArea(contour) 
        if(area > 300): 
            x, y, w, h = cv2.boundingRect(contour) 
            imageFrame = cv2.rectangle(imageFrame, (x, y), 
                                       (x + w, y + h), 
                                       (2, 162, 168), 2) 
            countY = countY + 1
    wordY = "Gold Bottle: " + str(countY)
    cv2.putText(imageFrame, wordY, (500, 50), 
                cv2.FONT_HERSHEY_SIMPLEX, 
                0.5, (2, 162, 168), 2) 

    contours, hierarchy = cv2.findContours(white_mask, 
                                           cv2.RETR_TREE, 
                                           cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours): 
        area = cv2.contourArea(contour) 
        if(area > 300): 
            x, y, w, h = cv2.boundingRect(contour) 
            imageFrame = cv2.rectangle(imageFrame, (x, y), 
                                       (x + w, y + h), 
                                       (255, 255, 255), 2) 
            countW = countW + 1
    wordW = "Silver Bottle: " + str(countW)
    cv2.putText(imageFrame, wordW, (500, 65), 
                cv2.FONT_HERSHEY_SIMPLEX, 
                0.5, (255, 255, 255), 2)

    contours, hierarchy = cv2.findContours(red_mask, 
                                           cv2.RETR_TREE, 
                                           cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours): 
        area = cv2.contourArea(contour) 
        if(area > 300): 
            x, y, w, h = cv2.boundingRect(contour) 
            imageFrame = cv2.rectangle(imageFrame, (x, y), 
                                       (x + w, y + h), 
                                       (0, 0, 255), 2) 
            countR = countR + 1
    wordR = "Red Bottle: " + str(countR)
    cv2.putText(imageFrame, wordR, (500, 80), 
                cv2.FONT_HERSHEY_SIMPLEX, 
                0.5, (0, 0, 255), 2)


    count = countW + countY + countG + countP
    word = "Total: " + str(count)
    cv2.putText(imageFrame, word, (10, 25), 
                cv2.FONT_HERSHEY_SIMPLEX, 
                1, (0, 0, 255), 2)
              
    # Program Termination 
    cv2.imshow("Multiple Color Detection in Real-TIme", imageFrame)
    cv2.imshow("color_mask", res_red)
    #cv2.imshow("color_mask", kernal)
    if cv2.waitKey(10) & 0xFF == ord('q'): 
        cap.release() 
        cv2.destroyAllWindows() 
        break