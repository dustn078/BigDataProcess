from Q7_1 import Camera

# 모듈로부터 Camera 클래스를 가져오고, 인스턴스를 생성하여 사용
if __name__ == "__main__":
    nikon = Camera(2000, 2.5)
    nikon.take_picture()