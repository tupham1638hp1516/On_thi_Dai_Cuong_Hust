Câu 1: Sử dụng mặt nạ mạng 255.255.240.0 để chia mạng 172.16.0.0 /16 thành các mạng con. Số lượng mạng con là bao nhiêu?
Bây giờ ta có 172.16.0.0/16 là đang bị khóa cứng 16 bit
255.255.240.0 => Với 255 đầu tiên (full số 1), nó sẽ khóa cứng 172; Với 255 tiếp theo, nó lại khóa cứng 16; 240 viết dưới dạng nhị phân thì sẽ là 1111 0000, như vậy nó sẽ khóa cứng 4 số nữa. Mà mạng ban đầu là /16, như vậy ta sẽ thừa ra 4, vậy tức là có 2^4 = 16 mạng con.
Câu 2:
Host                                             Interface
a1-a1-b2-b2-c3-c3                                 e0
a2-a2-b3-b3-c4-c4                                 e1
aa-bb-cc-11-22-33                                 e2
bc-bc-ac-ac-11-11                                 e3

Bảng MAC/CAM của một switch có nội dung như sau. Switch thực 
hiện những xử lý nào nếu nhận thành công một gói tin có địa chỉ 
nguồn là a3-a3-b3-b3-c3-c3 và địa chỉ đích là bb-bb-bb-cc-cc-cc?
(Chọn tất cả đáp án đúng)

Thêm địa chỉ đích vào bảng MAC/CAM
Gửi lại gói tin cho nút nguồn
Gửi gói tin ra tất cả các cổng trừ cổng nhận
Thêm địa chỉ nguồn vào bảng MAC/CAM
Báo lỗi cho nút nguồn
Hủy gói tin
Dễ thấy đáp án đúng sẽ là:
Thêm địa chỉ nguồn vào bảng MAC/CAM
Gửi gói tin ra tất cả các cổng trừ cổng nhận
Câu 3:
Những phát biểu nào là SAI về hoạt động của kỹ thuật chuyển mạch gói?(Chọn tất cả đáp án đúng)

Gói tin của các liên kết khác nhau được truyền trên cùng một đường truyền vật lý
Độ trễ trong mạng không phụ thuộc vào tải
Trên cùng một liên kết vật lý, tất cả các gói tin đều được truyền với tốc độ như nhau.
Các gói tin từ một nguồn cùng một đích thì đi qua tất cả các chặng giống nhau
