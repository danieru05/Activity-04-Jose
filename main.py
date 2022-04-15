import cv2
filePath = 'miss u guys.jpg'
windowTitle = 'miss ko na kayo mga kaklase ko huhu'
readCvImage = cv2.imread(filePath, 1)
cv2.imshow(windowTitle, readCvImage)
cv2.waitKey(0)
cv2.destroyAllWindows()