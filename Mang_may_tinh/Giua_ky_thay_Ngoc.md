Câu 1: Khẳng định nào sau đây sai về hệ tự trị (AS) trong định tuyến?
A. Chính sách định tuyến chung được áp dụng ở cùng một AS
B. Các giao thức định tuyến cục bộ được dùng bên trong các AS
C. Các giao thức định tuyến liên vùng được dùng để kết nối các AS với nhau
D. Số lượng các AS là cố định
=> Đáp án đúng là: D (3 đáp án A,B,C đều là đặc điểm của hệ tự trị, số lượng hệ tự trị thì thay đổi được, đơn giản là một công ty/ trường học nào đó đăng ký mạng là được)
Câu 2: Mục đích của DHCP là gì
A. Cho phép gán địa chỉ IP động từ server mạng khi một máy tính gia nhập một mạng
B. Chuyển giao địa chỉ IP giữa các máy tính
C. Cấu hình bảng định tuyến của các máy tính
D. Cấu hình máy tính qua đường kết nối từ xa
DHCP (Dynamic Host Configuration Protocol) là giao thức tự động cấp phát cấu hình mạng.

Bạn chỉ cần nhớ 3 ý cốt lõi sau:

Nhiệm vụ chính: Tự động gán địa chỉ IP (cùng với Subnet Mask, Default Gateway và DNS) cho bất kỳ thiết bị nào vừa mới kết nối vào mạng.

Tiện lợi: Giúp người dùng "cắm là chạy" (Plug and Play) hoặc bắt Wi-Fi là dùng được ngay, không cần phải gõ thông số cấu hình bằng tay cho từng thiết bị.

An toàn: Quản lý kho địa chỉ IP tập trung, tự động thu hồi IP của máy đã ngắt kết nối để cấp cho máy khác, giúp loại bỏ hoàn toàn lỗi "xung đột IP" (hai máy bị trùng một IP dẫn đến mất mạng).

Ví dụ dễ hiểu: DHCP Server giống như quầy lễ tân khách sạn. Khách (máy tính) đến sẽ tự động được phát một thẻ phòng (địa chỉ IP) để dùng tạm thời. Khi khách trả phòng, thẻ đó sẽ được thu lại để phát cho người tiếp theo.
=> Đáp án đúng: A
Câu 3: Trong các khẳng định sau về VLAN(Virtual LAN), khẳng định nào là sai?
A. VLAN cho phép gom nhóm, quản lý các máy tính về mặt logic thay vì vị trí địa lý từng máy
B. VLAN cho phép giảm bớt lưu lượng trong mạng LAN nhờ giảm số khung tin quảng bá trong mạng
C. VLAN giúp giảm độ phức tạp và giá thành vận hành mạng
D. VLAN cho phép tăng tính bảo mật mạng nhờ có thể phân quyền người dùng theo nhóm, phân vùng
=> Đáp án đúng: C
4 đặc điểm cốt lõi của VLAN:
Gom nhóm logic: Chia mạng dựa trên chức năng (Kế toán, Kỹ thuật...) thay vì vị trí chỗ ngồi vật lý.

Chia nhỏ miền quảng bá (Broadcast Domain): Giới hạn phạm vi gửi tin quảng bá, giúp giảm lưu lượng thừa và tăng hiệu suất mạng.

Tăng tính bảo mật: Cách ly hoàn toàn dữ liệu giữa các phòng ban ở Tầng 2.

Cần thiết bị Tầng 3: Để các máy ở hai VLAN khác nhau có thể liên lạc, bắt buộc phải dùng Router hoặc Switch Layer 3 (Inter-VLAN Routing).
Câu 4: Trong các khẳng định sau về cơ chế cập nhật bảng chuyển tiếp và chuyển tiếp gói tin của Switch sau, khẳng định nào là sai? (2 đáp án)
A. Việc cập nhật bảng chuyển tiếp dựa vào thuật toán tìm đường đi với chi phí nhỏ nhất.
B. Khi một khung tin đến Switch mà địa chỉ MAC máy tính chưa có trong bảng chuyển tiếp, khung tin đó luôn luôn được quảng bá ra tất cả các cổng còn lại trừ cổng đến
C. Khi một khung tin đến Switch mà trong bảng chuyển tiếp địa chỉ MAC nguồn có cổng khác với cổng mà khung tin đến thì Switch cập nhật lại cổng ứng với địa chỉ đích
D. Khi một khung tin đến Switch mà địa chỉ MAC nguồn chưa có trong bảng chuyển tiếp mà khung tin đến thì Switch cập nhật lại cổng ứng với địa chỉ đích
E. Khi một khung tin đến Switch mà địa chỉ MAC máy đích khớp với nhiều dòng trong bảng chuyển tiếp của Switch, Switch chọn dòng ứng với đường truyền có băng thông lớn hơn.

Đáp án sai là A và E. vì:
A. Switch học dựa trên việc nhớ và ghi lại, tìm đường đi là dành cho Router
E. Không có chuyện địa chỉ đích với với nhiều cổng được, còn chọn cổng dựa trên băng thông thì là Router
Câu 5: Hai vai trò chính của chức năng điều khiển truy nhập của tầng liên kết dữ liệu là gì?
A. Cho phép máy tính gia nhập vào mạng
B. Xác định cách các nút mạng chia sẻ đường truyền
C. Giao tiếp để chia sẻ đường truyền
D. cho phép máy tính kết nối với mạng Internet
Quản lý chia sẻ tài nguyên (B): tầng MAC quy định quy tắc để các nút không tranh giành nhau dẫn đến đụng độ dữ liệu (ví dụ: dùng CSMA/CD, CSMA/CA hoặc Token Passing).

Giao thức điều khiển (C): Để thực hiện việc chia sẻ, các nút phải có cơ chế giao tiếp, trao đổi các tín hiệu điều khiển (như lắng nghe đường truyền, gửi thông báo đụng độ hoặc chuyển giao thẻ bài) nhằm đảm bảo việc truy nhập diễn ra trật tự.

A (Gia nhập mạng): Thường liên quan đến các giao thức cấu hình (như DHCP ở tầng Ứng dụng) hoặc xác thực bảo mật.

D (Kết nối Internet): Đây là nhiệm vụ của tầng Mạng (Network Layer) với các giao thức định tuyến và địa chỉ IP. Tầng Liên kết dữ liệu chỉ quan tâm đến việc truyền dữ liệu giữa các nút trong cùng một mạng cục bộ (LAN).
Câu 6: Trong các khẳng định sau về định tuyến dạng distance-vector, khẳng định nào là đúng?
A. Mỗi router có đầy đủ thông tin về các kết nối trong mạng để dựng nên đồ thị mạng
B. Tốc độ hội tụ khi có sự thay đổi trong mạng nhanh
C. Giao thức định tuyến dạng distance-vector thường phù hợp với các mạng cỡ nhỏ
D. Các khẳng định khác đều sai
=> Đáp án đúng: C. Distance-vector là nghe "hàng xóm", đơn giản, phù hợp các mạng cỡ nhỏ

Câu 7: Một mạng sử dụng mã parity chẵn để phát hiện lỗi gây ra bởi quá trình truyền dữ liệu. Dữ liệu cần gửi đi là 1001 1100, mã parity được dùng là gì:
=> 0 (Số bit 1 chẵn)

Câu 8: Một gói dữ liệu (1011 1000 0011 1100 )được gửi sử dụng mã CRC. Biết rằng G=10011, tính mã CRC được đính kèm vào gói ban đầu.
=> Đáp án: 1100
Câu 9: Trong các khẳng định sau về giao thức định tuyến RIP (Routing Information Protocal), khẳng định nào là sao?
A. Sử dụng giải thuật link-state
B. Đơn vị chi phí được tính mặc định dựa vào số máy đã đi qua
C. RIP phù hợp với các mạng cỡ nhỏ
D. Định kỳ kiểm tra các router hàng xóm thông qua chính các gói tin cập nhật bảng vector khoảng cách

RIP là giao thức định tuyến theo thuật toán distance-vector
=> Đáp án chọn là: A