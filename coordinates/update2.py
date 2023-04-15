import cv2
import matplotlib.pyplot as plt
import mediapipe as mp
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()
image = cv2.imread('mehul.jpeg')
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
h, w, _ = image.shape
# print(h, w)
result = face_mesh.process(rgb)

l_lips = [61, 185, 40, 39, 37, 0, 267, 269, 270, 409, 291, 306, 292, 308, 415, 310, 311, 312, 13, 82,
          81, 80, 191, 78, 62, 76, 61, 146, 91, 181, 84, 17, 314, 405, 321, 375, 291,
          306, 292, 308, 324, 318, 402, 317, 14, 87, 178, 88, 95, 78, 62, 76, 61]

l_nose = [193, 122, 196, 3, 134, 115, 219, 235, 240, 99, 242, 125, 44, 237, 218, 219,
          235, 240, 99, 242, 125, 19, 354, 462, 328, 460, 455, 439, 438, 457, 274, 354,
          462, 328, 460, 455, 439, 344, 363, 248, 419, 351, 417]

l_lefteye = [243, 190, 56, 28, 27, 29, 30, 247,
             130, 25, 110, 24, 23, 22, 26, 112, 243, 190, 56, 28]

l_righteye = [463, 341, 256, 252, 253, 254, 339, 255, 259, 467, 260, 259,
              257, 258, 286, 414, 463, 362, 382, 381, 380, 374, 373,
              390, 249, 263, 466, 388, 387, 386, 385, 384, 398, 362, 463]

l_everything = [10, 109, 67, 103, 54, 21, 162, 127, 234, 93, 132, 58, 172, 136, 150, 149, 176, 148, 152, 377, 400,
                378, 379, 365, 397, 288, 361, 323, 454, 356, 389, 251, 284, 332, 297, 338, 10, 151, 9, 55, 107, 66, 105, 63, 70, 53, 52, 65, 55, 193, 243, 190, 56, 28, 27, 29, 30, 247,
                130, 25, 110, 24, 23, 22, 26, 112, 243, 133, 173, 157, 158, 159, 160, 161, 246, 33, 7,
                163, 144, 145, 153, 154, 155, 133, 243, 244, 245, 122, 196, 3, 134, 115, 219, 235, 240, 99, 242, 125, 44, 237, 218, 219,
                235, 240, 99, 242, 125, 19, 94, 2, 164, 37, 39, 40, 185, 61, 185, 40, 39, 37, 0, 267, 269, 270, 409, 291, 306, 292, 308, 415, 310, 311, 312, 13, 82,
                81, 80, 191, 78, 62, 76, 61, 146, 91, 181, 84, 17, 314, 405, 321, 375, 291,
                306, 292, 308, 324, 318, 402, 317, 14, 87, 178, 88, 95, 78, 62, 76, 61, 185, 40, 39, 37, 164, 2, 94, 19, 354, 462, 328, 460, 455, 439, 438, 457, 274, 354,
                462, 328, 460, 455, 439, 344, 363, 248, 419, 351, 465, 464, 463, 341, 256, 252, 253, 254, 339, 255, 359, 467, 260, 259,
                257, 258, 286, 414, 463, 362, 382, 381, 380, 374, 373,
                390, 249, 263, 466, 388, 387, 386, 385, 384, 398, 362, 463, 417, 285, 295, 282, 283, 276, 293, 334, 296, 336, 285, 9, 151, 10]
l7 = [159, 160, 145, 153]
l11 = [386, 387, 374, 380]


l4 = [55, 107, 66, 105, 63, 70, 53, 52, 65, 55]  # left eyebrow
l5 = [243, 190, 56, 28, 27, 29, 30, 247, 130, 25,
      110, 24, 23, 22, 26, 112, 243]  # left eye outer
l6 = [133, 173, 157, 158, 159, 160, 161, 246, 33, 7,
      163, 144, 145, 153, 154, 155, 133]  # left eye inner
# left eye ball-->make sure to make it circular first


l8 = [285, 295, 282, 283, 276, 293, 334, 296, 336, 285]  # right eyebrow
l9 = [359, 467, 260, 259, 257, 258, 286, 414, 463, 341,
      256, 252, 253, 254, 339, 255, 359]  # right eye outer
l10 = [263, 466, 388, 387, 386, 385, 384, 398, 362, 382,
       381, 380, 374, 373, 390, 249, 263]  # right eye inner
l11 = [386, 374, 380, 384, 385, 386]
# right eye ball-->make sure to make it circular first

l121 = [10, 109, 67, 103, 54, 21, 162, 127, 234, 93, 132, 58, 172, 136, 150, 149, 176, 148, 152, 377, 400,
        378, 379, 365, 397, 288, 361, 323, 454, 356, 389, 251, 284, 332, 297, 338, 10]  # face




l1 = len(l_everything)
length_lips = len(l_lips)
length_nose = len(l_nose)
length_lefteye = len(l_lefteye)
length_righteye = len(l_righteye)

length_left_eyebrow = len(l4)
length_left_eye_outer = len(l5)
length_left_eye_inner = len(l6)

length_right_eyebrow = len(l8)
length_right_eye_outer = len(l9)
length_right_eye_inner = len(l10)

length_face = len(l121)

X = []
Y = []
Z = []
for i in range(l1):
    for facial_landmarks in result.multi_face_landmarks:
        pt = facial_landmarks.landmark[l_everything[i]]
        x = pt.x*w
        y = pt.y*h
      #   z = pt.z
        X.append(x)
        Y.append(y)
      #   Z.append(z)
        # print('{ x:', x, ', y:', y, '},')
        # cv2.circle(image, (int(x), int(y)), 2, (0, 0, 0), -1)
# print(X)
# print(Y)



L = len(X)
print(L)
i = 0
while(i < L):
      print(' { x:', X[i], ', y:', Y[i], '' '', '},')
      # print('{x:',X[i], ',y:',Y[i]}')
      i = i+1

# print()

# X1 = []
# Y1 = []
# l2 = len(Y)
# i = 0
# while(i < l2-1):
#     x1 = X[i]
#     x2 = X[i+1]
#     j = 0
#     while(j <= 2):
#         d = (x1*(2-j)+x2*j)/2
#         X1.append(d)
#         j = j+1
#     y1 = Y[i]
#     y2 = Y[i+1]
#     j = 0
#     while(j <= 2):
#         d = (y1*(2-j)+y2*j)/2
#         Y1.append(d)
#         j = j+1
#     i = i+1
# # print(X1)
# # print(Y1)
# L = len(X1)
# i = 0
# while(i < L):
#     print('{ x:', X1[i], ', y:', Y1[i], '},')
#     i = i+1


l4 = [55, 107, 66, 105, 63, 70, 53, 52, 65, 55]  # left eyebrow
l5 = [243, 190, 56, 28, 27, 29, 30, 247, 130, 25,
      110, 24, 23, 22, 26, 112, 243]  # left eye outer
l6 = [133, 173, 157, 158, 159, 160, 161, 246, 33, 7,
      163, 144, 145, 153, 154, 155, 133]  # left eye inner
# left eye ball-->make sure to make it circular first


l8 = [285, 295, 282, 283, 276, 293, 334, 296, 336, 285]  # right eyebrow
l9 = [359, 467, 260, 259, 257, 258, 286, 414, 463, 341,
      256, 252, 253, 254, 339, 255, 359]  # right eye outer
l10 = [263, 466, 388, 387, 386, 385, 384, 398, 362, 382,
       381, 380, 374, 373, 390, 249, 263]  # right eye inner
l11 = [386, 374, 380, 384, 385, 386]
# right eye ball-->make sure to make it circular first

l121 = [10, 109, 67, 103, 54, 21, 162, 127, 234, 93, 132, 58, 172, 136, 150, 149, 176, 148, 152, 377, 400,
        378, 379, 365, 397, 288, 361, 323, 454, 356, 389, 251, 284, 332, 297, 338, 10]  # face


# l = len(list)
# for i in range(l):
#     for facial_landmarks in result.multi_face_landmarks:
#         pt = facial_landmarks.landmark[list[i]]
#         x = pt.x*w
#         y = pt.y*h
#         print('{ x:', x, ', y:', y, '},')
#         cv2.circle(image, (int(x), int(y)), 2, (0, 0, 0), -1)
# print()


# l = len(list)
# for i in range(l):
#     for facial_landmarks in result.multi_face_landmarks:
#         pt = facial_landmarks.landmark[list[i]]
#         x = pt.x*w
#         y = pt.y*h
#         print('{ x:', x, ', y:', y, '},')
#         cv2.circle(image, (int(x), int(y)), 2, (0, 0, 0), -1)
# print()


# l = len(list)
# for i in range(l):
#     for facial_landmarks in result.multi_face_landmarks:
#         pt = facial_landmarks.landmark[list[i]]
#         x = pt.x*w
#         y = pt.y*h
#         print('{ x:', x, ', y:', y, '},')
#         cv2.circle(image, (int(x), int(y)), 2, (0, 0, 0), -1)
# print()


# l = len(list)
# for i in range(l):
#     for facial_landmarks in result.multi_face_landmarks:
#         pt = facial_landmarks.landmark[list[i]]
#         x = pt.x*w
#         y = pt.y*h
#         print('{ x:', x, ', y:', y, '},')
#         cv2.circle(image, (int(x), int(y)), 2, (0, 0, 0), -1)
# print()


# l = len(list)
# for i in range(l):
#     for facial_landmarks in result.multi_face_landmarks:
#         pt = facial_landmarks.landmark[list[i]]
#         x = pt.x*w
#         y = pt.y*h
#         print('{ x:', x, ', y:', y, '},')
#         cv2.circle(image, (int(x), int(y)), 2, (0, 0, 0), -1)
# print()


# l = len(list)
# for i in range(l):
#     for facial_landmarks in result.multi_face_landmarks:
#         pt = facial_landmarks.landmark[list[i]]
#         x = pt.x*w
#         y = pt.y*h
#         print('{ x:', x, ', y:', y, '},')
#         cv2.circle(image, (int(x), int(y)), 2, (0, 0, 0), -1)
# print()


# l = len(list)
# for i in range(l):
#     for facial_landmarks in result.multi_face_landmarks:
#         pt = facial_landmarks.landmark[list[i]]
#         x = pt.x*w
#         y = pt.y*h
#         print('{ x:', x, ', y:', y, '},')
#         cv2.circle(image, (int(x), int(y)), 2, (0, 0, 0), -1)
# print()


# l = len(list)
# for i in range(l):
#     for facial_landmarks in result.multi_face_landmarks:
#         pt = facial_landmarks.landmark[list[i]]
#         x = pt.x*w
#         y = pt.y*h
#         print('{ x:', x, ', y:', y, '},')
#         cv2.circle(image, (int(x), int(y)), 2, (0, 0, 0), -1)
# print()


# l = len(list)
# for i in range(l):
#     for facial_landmarks in result.multi_face_landmarks:
#         pt = facial_landmarks.landmark[list[i]]
#         x = pt.x*w
#         y = pt.y*h
#         print('{ x:', x, ', y:', y, '},')
#         cv2.circle(image, (int(x), int(y)), 2, (0, 0, 0), -1)
# print()


# l = len(list)
# for i in range(l):
#     for facial_landmarks in result.multi_face_landmarks:
#         pt = facial_landmarks.landmark[list[i]]
#         x = pt.x*w
#         y = pt.y*h
#         print('{ x:', x, ', y:', y, '},')
#         cv2.circle(image, (int(x), int(y)), 2, (0, 0, 0), -1)


# # def show(title='Images', image=None, size=10):
# #     w, h = image.shape[0], image.shape[1]
# #     aspect_ratio = w/h
# #     plt.figure(figsize=(size*aspect_ratio, size))
# #     plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
#     plt.title(title)
#     plt.show()
# show('After face mesh', image)
