# Measuring-distance-from-camera-to-object
Measuring distance from camera to object in image

Một bài toán phổ biến của computer vision là xác định khoảng cách từ camera đến một vật thể xác định nào đó.
Có nhiều các để thực hiện việc đo khoảng cách này như dựa vào intrinsic parameters (thông số nội tại) của camera [xem thêm](https://github.com/huytranvan2010/Object-tracking-in-video-by-color) hay dựa vào tính chất của
tam giác đồng dạng (triangle similarity)

**Các bước thực hiện**
1. Xác định vật đánh dấu (marker)
Cần chọn được marker trước khi đi hiệu chuẩn (calibrate) hệ thống. Sau khi chọn được marker, điều lý tưởng là marker và surroundings có độ tương phản cao (high constrast)
2. Hiệu chuẩn ban đầu (initial calibration)
Để hiệu chuẩn được hệ thống cần thỏa mãn 2 điều kiện sau.
    - Biết trước kích thước (dimensions) của marker mà chúng ta muốn detect
    - Biết được khoảng cách hiện tại từ camera đến marker
Nếu không thỏa mãn được 2 điều kiện này thì không hiệu chuẩn được hệ thống.