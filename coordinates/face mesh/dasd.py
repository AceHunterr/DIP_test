import cv2
import matplotlib.pyplot as plt
import mediapipe as mp
import json
import ast
# import re

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()

image = cv2.imread('../img3.jpeg')
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

h, w, _ = image.shape
print(h, w)
result = face_mesh.process(rgb)
print(result)

coordinates_list = []


for facial_landmarks in result.multi_face_landmarks:
    for i in range(0, 468):
        pt = facial_landmarks.landmark[i]
        x = pt.x*w
        y = pt.y*h

        # result = 'x:{},y:{}'.format(x,y)
        # res = "{{{}}}".format(result)

        # my_dict = ast.literal_eval("{" + res.replace(":", ": ") + "}")


        # # print(result)
        # print(my_dict)
        # # final_res = json.loads(res)
        # # print(final_res)
        # # print(type(result))
        # # print(type(final_res))

        # result = {'x': x, 'y': y}
        # res = json.dumps(result)

        # print(res)
        # final_res = json.loads(res)
        # print(final_res)
        # print(type(final_res))


        # result = "{{x: {}, y: {}}}".format(x, y)

        result = "{{x:{}, y:{}}}".format(x, y)
        result_dict = json.loads(result.replace('x', '"x"').replace('y', '"y"'))
        # result_dict = dict(item.split(":") for item in result.split(","))
        # result_dict = dict(item.split(":") for item in result.split(","))


        print(result)

        # result_dict = ast.literal_eval(result)
        print(result_dict)
        print(type(result_dict))

        coordinates_list.append(result_dict)
        cv2.circle(image, (int(x), int(y)), 1, (255, 0, 0), 1)


print(coordinates_list)

def convert_to_json(list):
    json_data = json.dumps(list)

    with open("my_list.json","w") as outfile:
        outfile.write(json_data)


convert_to_json(coordinates_list)


def show(title='Images', image=None, size=10):
    w, h = image.shape[0], image.shape[1]
    aspect_ratio = w/h
    plt.figure(figsize=(size*aspect_ratio, size))
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.show()


show('After face mesh', image)
