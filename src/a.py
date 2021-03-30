import cv2 as cv
import os
import numpy as np

BODY_PARTS = {
                "손목": 0,
                "엄지0": 1, "엄지1": 2, "엄지2": 3, "엄지3": 4,
                "검지0": 5, "검지1": 6, "검지2": 7, "검지3": 8,
                "중지0": 9, "중지1": 10, "중지2": 11, "중지3": 12,
                "약지0": 13, "약지1": 14, "약지2": 15, "약지3": 16,
                "소지0": 17, "소지1": 18, "소지2": 19, "소지3": 20,
            }

POSE_PAIRS = [["손목", "엄지0"], ["엄지0", "엄지1"],
                ["엄지1", "엄지2"], ["엄지2", "엄지3"],
                ["손목", "검지0"], ["검지0", "검지1"],
                ["검지1", "검지2"], ["검지2", "검지3"],
                ["손목", "중지0"], ["중지0", "중지1"],
                ["중지1", "중지2"], ["중지2", "중지3"],
                ["손목", "약지0"], ["약지0", "약지1"],
                ["약지1", "약지2"], ["약지2", "약지3"],
                ["손목", "소지0"], ["소지0", "소지1"],
                ["소지1", "소지2"], ["소지2", "소지3"]]


# BODY_PARTS = {
#                 "Wrist": 0,
#                 "ThumbMetacarpal": 1, "ThumbProximal": 2, "ThumbMiddle": 3, "ThumbDistal": 4,
#                 "IndexFingerMetacarpal": 5, "IndexFingerProximal": 6, "IndexFingerMiddle": 7, "IndexFingerDistal": 8,
#                 "MiddleFingerMetacarpal": 9, "MiddleFingerProximal": 10, "MiddleFingerMiddle": 11, "MiddleFingerDistal": 12,
#                 "RingFingerMetacarpal": 13, "RingFingerProximal": 14, "RingFingerMiddle": 15, "RingFingerDistal": 16,
#                 "LittleFingerMetacarpal": 17, "LittleFingerProximal": 18, "LittleFingerMiddle": 19, "LittleFingerDistal": 20,
#             }

# POSE_PAIRS = [["Wrist", "ThumbMetacarpal"], ["ThumbMetacarpal", "ThumbProximal"],
#                ["ThumbProximal", "ThumbMiddle"], ["ThumbMiddle", "ThumbDistal"],
#                ["Wrist", "IndexFingerMetacarpal"], ["IndexFingerMetacarpal", "IndexFingerProximal"],
#                ["IndexFingerProximal", "IndexFingerMiddle"], ["IndexFingerMiddle", "IndexFingerDistal"],
#                ["Wrist", "MiddleFingerMetacarpal"], ["MiddleFingerMetacarpal", "MiddleFingerProximal"],
#                ["MiddleFingerProximal", "MiddleFingerMiddle"], ["MiddleFingerMiddle", "MiddleFingerDistal"],
#                ["Wrist", "RingFingerMetacarpal"], ["RingFingerMetacarpal", "RingFingerProximal"],
#                ["RingFingerProximal", "RingFingerMiddle"], ["RingFingerMiddle", "RingFingerDistal"],
#                ["Wrist", "LittleFingerMetacarpal"], ["LittleFingerMetacarpal", "LittleFingerProximal"],
#                ["LittleFingerProximal", "LittleFingerMiddle"], ["LittleFingerMiddle", "LittleFingerDistal"]]

#손가락 특정 부분이 검출되었는지 판정하기 위해 사용되는 스레숄드
threshold = 0.1

#파이썬 소스 코드 파일의 위치를 찾습니다. 비주얼 스튜디오 코드에서 서브 폴더에 파이썬 코드와 데이터를 둘 경우
#데이터의 위치를 올바로 찾기위해서는 파이썬 소스 코드 파일의 위치를 알아야함.
path = os.path.dirname(os.path.abspath(__file__))

#모델을 구성하는 레이어들의 속성이 포함되어 있습니다.
#이미지를 입력으로 학습이 완료된 모델을 사용하려면 필요
protoFile = path + "/" + "pose_deploy.prototxt"
#protoFile = "pose_deploy.prototxt"

#학습 완료된 모델이 저장되어있는 파일입니다.
weightsFile = path + "/" + "pose_iter_102000.caffemodel"
#weightsFile = "pose_iter_102000.caffemodel"

#네트워크 모델을 불러옵니다.
net = cv.dnn.readNetFromCaffe(protoFile, weightsFile)

#백엔드로 쿠다를 사용하여 속도향상을 꾀함
net.setPreferableBackend(cv.dnn.DNN_BACKEND_CUDA)
#쿠다 디바이스에 계산을 요청
net.setPreferableTarget(cv.dnn.DNN_TARGET_CUDA)

#영상을 가져오기 위해 웹캡과 연결할 준비를
cap = cv.VideoCapture(0)

#네트워크에서 사용할 이미지 크기
inputHeight = 368
inputWidth = 368
inputScale = 1.0/255

# 아무키나 누르게 되면 루프 중지
while cv.waitKey(1) < 0:
    #웹캠으로부터 영상을 하나 가져옵니다.
    hasFrame, frame = cap.read()
    #속도가 느릴경우 이미지 사이즈 변경, 쿠다를 사용할 경우 이미지를 줄일 필요 x
   # frame = cv.resize(frame, dsize=(320, 240), interpolation=cv.INTER_AREA)

    #웹캠으로부터 영상을 가져올 수 없으면 루프를 중
    if not hasFrame:
        cv.waitKey()
        break

    #원본이미지의 너비와 높이
    frameWidth = frame.shape[1]
    frameHeight = frame.shape[0]

    # (inputWidth, inputHeight)로 이미지 크기를 조정하고 4차원 행렬인 blob으로 변환합니다. 네트워크에 이미지를 입력하기 위한 전처리 과정입니다.
    # mean subtraction를 수행하여 원본 이미지의 픽셀에서 평균값을 뺍니다. 여기에선 평균갑으로 0을 주고 있어 빼지 않습니다.
    inp = cv.dnn.blobFromImage(
        frame, #입력 이미지
        inputScale, #픽셀값 범위를 0~1 사이 값으로 정규화, 인식 결과 좋아짐
        (inputWidth, inputHeight), #컨볼루션 뉴럴 네트워크에서 요구하는 크기로 이미지 크기를 조정
        (0, 0, 0), #입력 영상에서 뺄 mean subtraction 값. 현재는 0으로 설정하여 픽셀에서 빼지 않음
        swapRB=False, #openCV의 BGR순서를 RGB로 바꾸기 위해 사용. False이므로 바꾸지 않음.
        crop=False)
    #inp.shape를 출력 => (1, 3, 368, 368)

    #다음처럼 blob 영상을 출력해볼 수 있습니다. 앞에서 mean subtration 값을 바꾸어보면 이미지가 변하게 됩니다.
    imgb = cv.dnn.imagesFromBlob(inp)
    cv.imshow('inp', (imgb[0]*255.0).astype(np.uint8))

    #네트워크 입력을 지정
    net.setInput(inp)

    #네트워크의 출력을 얻기위해 포워드 패스(forward pass)를 수행
    out = net.forward()

    points = []

    #손가락을 구성하는 모든 부분에 대하여
    for i in range(len(BODY_PARTS)):
        #히트맵을 가지고
        heatMap = out[0, i, :, :]

        #최대값(conf)과 최대값의 위치(point)를 찾습니다.
        _, conf, _, point = cv.minMaxLoc(heatMap)

        #원본 영상에 맞게 좌표를 조정(앞에서 이미지 크기를 조정하였기 때문)
        x = int((frameWidth * point[0]) / out.shape[3])
        y = int((frameHeight * point[1]) / out.shape[2])

        #히트맵의 최대값이 스레숄드보다 크다면 손가락을 구성하는 특정 부분을 감지한 것
        #스레숄드 threshold가 작으면 손가락 부분이 잘 검출되지만 주변의 다른 물체를 같이 연결하여 손가락으로 오인식하는 것이 많아지고
        #스레숄드가 커지면 손가락 부분이 덜 검출되며 주변의 다른 물체를 같이 연결하여 손가락으로 오인식하는게 줄어드는 듯함.
        if conf > threshold:
            #해당 부분에 원과 숫자를 표시한 후, 해당 좌표를 리스트에 삽입.
            cv.circle(frame, (x, y), 3, (0, 255, 255), thickness=-1, lineType=cv.FILLED)
            cv.putText(frame, "{}".format(i), (x, y), cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 1, lineType=cv.LINE_AA)
            points.append((x, y))
        else:
            points.append(None)


    #모든 손가락 연결 관계에 대
    for pair in POSE_PAIRS:
        partFrom = pair[0]
        partTo = pair[1]

        idFrom = BODY_PARTS[partFrom]
        idTo = BODY_PARTS[partTo]

        #앞 과정에서 두 부분이 모두 검출되어
        #두 부분이 모두 존재하면 연결하는 선을 그려줌
        if points[idFrom] and points[idTo]:
            cv.line(frame, points[idFrom], points[idTo], (0, 255, 0), 1)

    #추론하는데 걸린 시간을 화면에 출력
    t, _ = net.getPerfProfile()
    freq = cv.getTickFrequency() / 1000
    cv.putText(frame, '%.2fms' % (t / freq), (10, 20), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))

    #손가락 검출 결과가 반영된 영상을 보여주게 됨
    cv.imshow('OpenPose using OpenCV', frame)