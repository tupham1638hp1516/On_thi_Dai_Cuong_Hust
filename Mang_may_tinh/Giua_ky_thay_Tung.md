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

Câu 7:
Những yếu tố nào sau đây ảnh hưởng đến giá trị Round Trip Time 
trong quá trình truyền?(Chọn tất cả đáp án đúng)
(1 Điểm)
Tốc độ xử lý của nút đích
Khoảng cách giữa nút nguồn và đích
Băng thông
Số nút chuyển tiếp phải qua trên đường truyền
Tải của mạng

=> Tất cả các đáp án đều đúng

Câu 8:
Địa chỉ IP nào sau đây không nằm cùng mạng với các địa chỉ còn lại?
(1 Điểm)
172.16.40.113 /19
172.16.50.114 /19
172.16.60.115 /19
172.16.30.112 /19

=> Đáp án là 172.16.30.112/ 19 vì 19 bit Họ của nó là 172.16.000 ... trong khi các mạng khác là 172.16.001 ....

Câu 9:
Trong chồng giao thức TCP/IP, giao thức nào sau đây nằm ở tầng 
mạng?(Chọn tất cả đáp án đúng)
(1 Điểm)
ICMP
IP
DHCP
UDP
TCP

IP (Internet Protocol): Là giao thức cốt lõi và quan trọng nhất của tầng mạng. Nó làm nhiệm vụ cung cấp địa chỉ logic (địa chỉ IP) cho các thiết bị và định tuyến đường đi cho các gói tin.

ICMP (Internet Control Message Protocol): Nằm cùng tầng mạng với IP và là một giao thức hỗ trợ cực kỳ quan trọng. Nó không truyền dữ liệu người dùng mà chuyên dùng để gửi các thông báo lỗi hoặc thông tin kiểm tra tình trạng mạng. (Ví dụ: Khi bạn gõ lệnh ping để xem mạng có thông không, chính là bạn đang sử dụng giao thức ICMP).

TCP (Transmission Control Protocol) và UDP (User Datagram Protocol): Cả hai đều nằm ở tầng Giao vận (Transport Layer). Tầng này nằm ngay phía trên tầng mạng, chịu trách nhiệm thiết lập kết nối và chuyển phát dữ liệu giữa các phần mềm/ứng dụng (như trình duyệt web, game) một cách tin cậy (TCP) hoặc nhanh chóng (UDP).

DHCP (Dynamic Host Configuration Protocol): Nằm ở tầng Ứng dụng (Application Layer), tức là tầng trên cùng. Mặc dù DHCP liên quan đến IP (làm nhiệm vụ cấp phát địa chỉ IP tự động cho máy tính), bản thân nó lại là một ứng dụng chạy trên nền tảng của mạng chứ không phải giao thức hạ tầng.

Câu 10:
Liên kết giữa 2 nút A và B có tốc độ truyền tin là 8 Mbps và độ dài là 200 km. Thời gian để truyền hết một gói tin có kích thước 2000 byte là bao nhiêu mili giây? (Chỉ ghi giá trị số)
Tốc độ truyền tin ở đây còn được hiểu là băng thông (nhìn vào đơn vị của nó là Mbps)
Còn một cái khác là tốc độ lan truyền(tốc độ để 1 bit đi từ điểm A đến điểm B), cái này thì đơn vị thường là (m/s) và thường là 2.10^8 m/s (Trong đề này không có nói)
Đầu tiên ta tính thời gian để nhét hết 2000 byte vào trong đường truyền: 2000*8/8.10^6 = 2(ms)
Sau đó ta tính thời gian để bit cuối cùng đi từ A đến B: 200 000/2*10^8= 1ms
Vậy tổng thời gian sẽ là 3ms
Câu 11:
Phát biểu nào sau đây là đúng về chuyển mạch kênh?(Chọn tất cả đáp án đúng)
(1 Điểm)
A. Các nút chuyển mạch thay đổi lượng tài nguyên cấp phát cho kênh biến thiên theo tải trên đường truyền
B. Các thiết bị chuyển mạch cấp phát tài nguyên cho kênh
C. Nút nguồn sử dụng kênh truyền được cấp để gửi dữ liệu tới nhiều đích
D. Kênh được hủy khi cả 2 bên báo hủy
E. Nút nguồn gửi thông điệp xin thiết lập kênh

A là sai vì tài nguyên cấp phát cho kênh sẽ cố định không thay đổi (chuyển mạch kênh)
B là đúng vì Router/ Switch trên đường đi từ A đến B sẽ cấp phát tài nguyên cho kênh và giữ nguyên tài nguyên đó
C là sai vì chuyển mạch kênh được sử dụng cho liên kết điểm-điểm
D là sai vì chỉ cần 1 trong 2 bên báo hủy là được
E đúng vì nút nguồn sẽ gửi thông điệp cho mạng để thiết lập kênh với một nút đích

Câu 12:
Sử dụng đa thức sinh G(x) = x^3 + x + 1, tính mã CRC cho chuỗi bit 1000 100
Ta mã hóa đa thức sinh G(x) được dãy bit sau: 1011
Vì G có tất cả 4 bit, ta thêm 3 bit 0 vào đằng sau chuỗi gốc, ta được: 1000 1000 00
Giờ ta thực hiện phép chia lấy dư(lấy chuỗi gốc chia cho G)
1000 XOR 1011 = 0011
Ta hạ 1 bit được 00111 => 0111
Ta tiếp tục hạ 1 bit được 01110 => 1110
Ta lấy 1110 XOR 1011 ta được 0101
Ta hạ 1 bit được 01010 => 1010
Ta lấy 1010 XOR 1011 ta được 0001
Ta hạ 1 bit được 00010 => 0010
Ta hạ 1 bit được 00100 => 0100
Ta hạ nốt 1 bit cuối được 01000 => 1000
Ta lấy 1000 XOR 1011 ta được 0011
Vì chuỗi đa thức sinh có 4 bit nên ta chỉ lấy số dư là 3 bit cuối => 011
Vậy mã CRC cho chuỗi bit 1000 100 là 011

Câu 13: Địa chỉ MAC được dùng ở tầng nào trong mô hình TCP/IP
(1 Điểm)
Tầng liên kết dữ liệu
Tầng vật lý
Tầng ứng dụng
Tầng giao vận
Tầng mạng
=> Đáp án là tầng liên kết dữ liệu (data link)
Câu 14: Hoạt động định tuyến thực hiện trên tầng nào trong mô hình TCP/IP
(1 Điểm)
Tầng giao vận
Tầng ứng dụng
Tầng vật lý
Tầng mạng
Tầng liên kết dữ liệu
=> Đáp án là tầng mạng
Câu 15: Phát biểu nào sau đây là đúng về hoạt động của phương pháp điều 
khiển truy nhập đường truyền Slotted Aloha?(Chọn tất cả đáp án đúng)
(1 Điểm)
Đồng bộ thời gian giữa các nút
Kiểm tra trạng thái đường truyền trước khi gửi dữ liệu
Phát hiện đụng độ và thông báo cho các nút trong mạng
Mỗi nút mạng được phép truyền trong khe thời gian dành riêng cho nút mạng đó
Thuộc nhóm phương pháp điều khiển truy nhập ngẫu nhiên
Truyền nhiều khung tin nhất có thể trong một khung thời gian (frame time)

Đáp án đúng là:

Đồng bộ thời gian giữa các nút

Thuộc nhóm phương pháp điều khiển truy nhập ngẫu nhiên

Giải thích chi tiết:

Đồng bộ thời gian giữa các nút (Đúng): Giao thức Slotted ALOHA chia trục thời gian thành các khe (slot) rời rạc, mỗi khe có độ dài bằng đúng thời gian truyền một khung tin (frame). Tất cả các nút trong mạng bắt buộc phải được đồng bộ đồng hồ để chỉ bắt đầu truyền dữ liệu vào đúng thời điểm mở đầu của một khe thời gian. Điều này giúp giảm tỷ lệ đụng độ xuống một nửa so với Pure ALOHA.

Thuộc nhóm truy nhập ngẫu nhiên (Đúng): ALOHA thì luôn là ngẫu nhiên

Tại sao các phương án khác sai:

Kiểm tra trạng thái đường truyền trước khi gửi: Đây là cơ chế của CSMA

Phát hiện đụng độ và thông báo: Đây là cơ chế của giao thức CSMA/CD 

Mỗi nút được cấp khe thời gian dành riêng: Đây là đặc điểm của phương pháp phân chia kênh theo thời gian TDMA. Trong Slotted ALOHA, không có khe nào là "dành riêng", mọi khe thời gian đều mở cho mọi nút cùng cạnh tranh truy cập.

Truyền nhiều khung tin nhất có thể trong một frame time: Khái niệm này sai. Theo thiết kế, mỗi khe thời gian (slot) trong Slotted ALOHA chỉ vừa đủ để truyền chính xác một khung tin tiêu chuẩn.

Câu 16: Địa chỉ 241.134.23.12 thuộc phân lớp nào?
(1 Điểm)
A
D
C
E
B

Từ 224 đến 239 là lớp D, còn từ 240 đến 255 là lớp E
=> Đáp án là: E
Câu 17:
Host                                             Interface
a1-a1-b2-b2-c3-c3                                 e0
a2-a2-b3-b3-c4-c4                                 e1
aa-bb-cc-11-22-33                                 e2
bc-bc-ac-ac-11-11                                 e3
Bảng MAC/CAM của một switch có nội dung như sau. Switch thực hiện những xử lý nào nếu trên cổng e2 nhận thành công một gói tin có địa chỉ nguồn là bc-bc-ac-ac-11-11 và địa chỉ đích là a1-a1-b2-b2
c3-c3?(Chọn tất cả đáp án đúng)

Gửi gói tin ra tất cả các cổng trừ cổng nhận
Gửi gói tin ra cổng e0
Gửi trả lại gói tin cho nút nguồn
Gửi báo lỗi cho nút nguồn
Gửi gói tin ra cổng e3
Hủy gói tin
Cập nhật cổng chuyển tiếp tới địa chỉ bc-bc-ac-ac-11-11 là e2

Đáp án đúng là:
1) Cập nhật cổng chuyển tiếp tới địa chỉ bc-bc-ac-ac-11-11 là e2
2) Gửi gói tin ra cổng e0
Câu 18:
Trong kiến trúc phân tầng, khi nhận được dữ liệu từ tầng cao hơn chuyển xuống, tầng dưới xử lý như thế nào?
(1 Điểm)
Thêm tiêu đề cho gói tin
Sửa thông tin phần tiêu đề
Loại bỏ phần tiêu đề của gói tin
Thay thế tiêu đề của gói tin bằng tiêu đề mới
=> Đáp án đúng là: Thêm tiêu đề cho gói tin
Câu 19:
Trong hình trạng (topology) mạng nào sau đây, sự cố xảy ra trên đường truyền vật lý có thể cản trở đến quá trình truyền dữ liệu toàn bộ mạng?
(1 Điểm)
Mạng hình trục (Bus)
Mạng hình sao (Star)
Mạng hình vòng (Ring)
Tất cả các hình trạng trên
=> Đáp án đúng là Bus và Ring
Câu 20:

Khác với chuẩn không vi sai, Manchester vi sai không nhìn vào hướng lên/xuống ở giữa chu kỳ để quyết định bit. Ở giữa chu kỳ, nó luôn luôn đảo mức (từ cao xuống thấp hoặc thấp lên cao) để đồng bộ xung nhịp đồng hồ.

Giá trị của bit (0 hay 1) được quyết định bằng việc có hay không có sự chuyển mức ngay tại vạch bắt đầu của chu kỳ bit:

Bit 0: CÓ sự đảo chiều điện áp ngay tại đầu chu kỳ bit. (Nếu tín hiệu trước đó đang ở mức cao thì gập xuống thấp, đang thấp thì gập lên cao).

Bit 1: KHÔNG CÓ sự đảo chiều ở đầu chu kỳ bit. Tín hiệu sẽ tiếp nối đi ngang từ chu kỳ trước sang.

**Câu hỏi:**

Khi sử dụng phương pháp điều chế Manchester vi sai, xung tín hiệu trên đường truyền như hình vẽ sau. Chuỗi bit đang được truyền đi là gì?
(1 Điểm)


     |       |       |       |       |       |       |       |       |
+V ──┐       ┌───────┐       ┌───┐   ┌───┐           ┌───┐   ┌───┐
     │       │       │       │   │   │   │           │   │   │   │
-V   └───────┘       └───────┘   └───┘   └───────────┘   └───┘   └───

Đáp án là: 011100100

Câu 21: Phương pháp điều khiển truy cập đường truyền nào sau đây không 
nằm cũng nhóm với các phương pháp còn lại?
(1 Điểm)
Aloha
CSMA
FDMA
=> Đáp án đúng là: FDMA (Đây là nhóm phân chia sẵn tài nguyên)

Câu 22: Ưu điểm của phương pháp CSMA/CD so với Token Passing là gì?
(1 Điểm)
Xác suất đụng độ thấp hơn
Có cơ chế vãn hồi đụng độ
Đơn giản hơn
Hiệu suất sử dụng đường truyền cao hơn
Tất cả các đáp án trên

Token Passing: Phương pháp này sử dụng một "thẻ bài" (Token) truyền vòng quanh mạng. Chỉ trạm nào cầm thẻ bài mới được phép gửi dữ liệu. Nhờ cơ chế xếp hàng này, Token Passing triệt tiêu hoàn toàn sự đụng độ (xác suất đụng độ = 0).
=> Do đó đáp án đúng là: Đơn giản hơn (Token Passing không có đụng độ)

Câu 23: Các chuẩn Fast Ethernet có tốc độ truyền tin tối đa là bao nhiêu?
(1 Điểm)

1 Gbps
54 Mbps
10 Gbps
100 Mbps
10 Mbps
=> Đáp án đúng là: 10 Mbps
Câu 24: Phương pháp mã hóa nào sau đây sử dụng đề điều chế dữ liệu số-tín
hiệu số?(Chọn tất cả đáp án đúng)
(1 Điểm)
Mã checksum
Mã Unipolar NRZ-L
Mã parity
Mã vòng CRC
Mã Unipolar NRZ-I

Mã parity, mã checksum, mã vòng CRC là nhóm phát hiện lỗi (Nằm ở tầng 2 hoặc tầng 4)
=> Đáp án đúng là: MÃ Unipolar NRZ-L và NRZ-I