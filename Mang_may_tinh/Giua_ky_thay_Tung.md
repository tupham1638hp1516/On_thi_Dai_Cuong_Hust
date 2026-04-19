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

A. Gói tin của các liên kết khác nhau được truyền trên cùng một đường truyền vật lý
B. Độ trễ trong mạng không phụ thuộc vào tải
C. Trên cùng một liên kết vật lý, tất cả các gói tin đều được truyền với tốc độ như nhau.
D. Các gói tin từ một nguồn cùng một đích thì đi qua tất cả các chặng giống nhau

Đáp án A sai vì đây là đặc điểm của truyền mạch gói, truyền mạch kênh thì sẽ trên đường truyền riêng biệt
Đáp án B đúng vì độ trễ trong mạng của chuyển mạch gói phụ thuộc vào tải trọng, nếu có quá nhiều gói tin cùng được gửi thì có thể gây trễ (các gói tin bị kẹt nếu cùng chọn 1 đường)
Đáp án C sai vì dĩ nhiên là các gói sẽ được truyền với tốc độ như nhau rồi, nếu phải so sánh chuyển mạch gói và chuyển mạch kênh thì phải là tốc độ truyền "tin"
Đáp án D đúng vì các gói tin có thể chọn chặng đường bất kỳ mà nó cho là phù hợp
=> Đáp án đúngL B & D
câu 4: Sử dụng mã CRC với đa thức sinh G(x) = x^3 + x + 1. Chuỗi bit biểu diễn cho đa thức này là gì?
Đáp án là: 1011
Câu 5:
Địa chỉ nào sau đây có thể gán được cho một nút mạng?
(1 Điểm)
230.12.3.1
172.20.64.0 /15
10.24.0.0 /13
127.0.0.1
192.168.1.113 /28
Bây giờ ta bắt đầu đi vào phân tích
Đáp án số 1: 230.12.3.1 => Địa chỉ đầu là 230 nên nó sẽ thuộc lớp D(Multicase) theo Classful Addressing => Loại (Chỉ A,B,C được chọn làm nút mạng)
Đáp án số 2: 172.20.64.0/15 Dễ thấy ở đoạn số 3 có 64 nên chắc chắn đây là một địa chỉ bình thường
Đáp án số 3: 10.24.0.0/13: 10 là địa chỉ Họ, 13-8=5; ta xét 24 viết dưới dạng: 0001 1000, ta lấy 5 bit cố định, 3 bit còn lại là 000=> Vậy suy ra đây là địa chỉ mạng(network address) => Không chọn
Đáp án số 4: 127.0.0.1: Cứ bắt đầu bằng 127 thì là địa chỉ loopback => Loại
Đáp án số 5: 192.168.1.113/28 => Đây chắc chắn là địa chỉ bình thường

Câu 6:
**Câu hỏi (1 Điểm):**
Khi sử dụng phương pháp điều chế Bipolar NRZ, xung tín hiệu trên đường truyền như hình vẽ sau. Chuỗi bit đang được truyền đi là gì?

**Đồ thị tín hiệu:**
```text
+V |        +------+        +------+
 0 |--------+      |        |      +--------------------------------
-V |               +--------+
   |   T1   |   T2   |   T3   |   T4   |   T5   |   T6   |   T7   |   T8   |

01110000

