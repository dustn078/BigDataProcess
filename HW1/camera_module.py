class Camera:
    def __init__(self, resolution, zoom_factor):
        self.resolution = resolution
        self.zoom_factor = zoom_factor

    def take_picture(self):
        print("찰칵")
        print(f"사진이 저장되었습니다. (화소: {self.resolution}만, 배율: {self.zoom_factor}x)")

# 테스트 코드
if __name__ == "__main__":
    canon = Camera(2430, 1.0)
    canon.take_picture()

    sony = Camera(2410, 3.0)
    sony.take_picture()