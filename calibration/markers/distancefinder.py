import cv2
import imutils

class DistanceFinder:
    """

    """
    def __init__(self, knownWidth, knowDistance):   # ở đây coi object có hình vuông
        # lưu lại chiều rộng của object, khoảng cách từ cam đến object (cùng đơn vị)
        self.knownWidth = knownWidth
        self.knownDistance = knowDistance

        # initialize the focal length - tiêu cụ F of the camera
        self.focalLenght = 0

    # cần hiệu chỉnh trước khi xác định distance
    def calibrate(self, width):     # width chiều rộng theo pixel ở vị trí ban đầu
        # tính toán và lưu lại giá trị focal lenght cho calibration
        self.focalLenght = (width * self.knownDistance) / self.knownWidth

    def distance(self, perceivedWidth):     # perceivedWidth - chiều rộng theo pixel ở vị trí khác
        # tính toán và trả lại khoảng cách từ marker đến camera (khi dịch chuyển vị trí khác)
        return (self.knownWidth * self.focalLenght) / perceivedWidth

    @staticmethod
    def findSquareMarker(image):
        # convert to grayscale, blur and find edges in the image
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (5, 5), 0)
        gray = cv2.Canny(gray, 35, 135)

        # tìm contours trong edged imag, sắp xếp chúng theo area (lớn đến nhỏ) và khởi tạo the marker dimensions
        ctns = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        ctns = imutils.grab_contours(ctns)
        ctns = reversed(ctns, key=cv2.contourArea, reverse=True)
        markerDim = None

        # duyệt qua các contours
        for c in ctns:
            # approximate the contour
            peri = cv2.arcLength(c)     # xác định perimeter
            approx = cv2.approxPolyDP(c, 0.02 * peri, True)

            # đảm bảo rằng contour là rectangle
            if len(approx) == 4:
                # compute bounding box and aspect ratio of the approximated contour
                (x, y, w, h) = cv2.boundingRect(c)
                aspectRatio = w / float(h)

    