Getting Statarted
Câu 1: Trong các nhận xét sau, nhận xét nào về NAT là đúng?
A. Tốn kém địa chỉ IP
B. Không hiệu quả đối với mạng kích thước lớn
C. Tăng chi phí khi thay đổi nhà cung cấp dịch vụ mạng
D. Tăng tính bảo mật của mạng LAN
NAT là cơ chế giúp Dữ liệu chuyển tiếp từ mạng LAN sang mạng Internet và ngược lại. NAT được thực hiện trên bộ định tuyến.
Lợi ích:
1. Tiết kiệm địa chỉ IP công cộng
2. Che giấu địa chỉ riêng
3. Giảm chi phí cấu hình khi thay đổi ISP
=> Đáp án đúng: D
Câu 2: Server là các máy tính cung cấp tài nguyên cho các máy tính khác được kết nối với nhau thông qua:
A. Network
B. Server
C. Hệ thống Backup
D. Modem
=> Đáp án đúng: A
Câu 3: Kiểu mạng nào sẽ sử dụng đường điện thoại (phonelines)
A. WAN (Wide Area Network)
B. LAN (Local Area Network)
C. Wireless
D. WWAN (Wireless WAN)
Ta phân loại liên kết:
Điểm - Điểm                                       Điểm - Đa điểm
Bảo mật và riêng tư                               Kiểm soát và phân phối dữ liệu dễ dàng
Tốc độ ổn định và không phải chia sẻ băng thông   Tiết kiệm chi phí, chỉ cần 1 thiết bị
                                                  trung chuyển và chia sẻ hạ tầng
Nếu đường truyền có vấn đề gì thì dễ xác định     Dễ mở rộng
Phonelines là p2p => WAN hoặc WWAN, mà phonelines là đường truyền vật lý nên ta chọn WAN
=> Đáp án đúng: A
Câu 4: Một thiết bị kết nối tới một hệ thống mạng mà không sử dụng dây cáp thì được gọi là gì?
A. Phân tán
B. Tập trung
C. Dây cáp
D. Không dây
=> Đáp án đúng: Không dây
Câu 5: Trong kiến trúc mạng OSI, routing được thực thi bởi tầng nào?
A. Tầng mạng
B. Tầng giao vận
C. Tầng liên kết dữ liệu
D. Tầng ứng dụng
Mô hình OSI/ ISO:
Application: Cung cấp các ứng dụng trên mang (web, email, truyền file,...)
Presentation: Biểu điễn dữ liệu của ứng dũng mã hóa, nén, chuyển đổi,...
Tầng phiên(Session): Quản lý phiên làm việc, đồng bộ hóa phiên, khôi phục quá trình trao đổi dữ liệu.
Transport: Xử lý việc truyền, nhận dữ liệu cho các ứng dụng chạy trên nút mạng đầu cuối
Network: Chọn đường(định tuyến), chuyển tiếp gói tin từ nguồn đến đích.
Data Link: Truyền dữ liệu trên các tầng liên kết vật lý giữa các nút mạng kế tiếp nhau.
Physical: Chuyển dữ liệu bit thành tín hiệu và truyền.
=> Đáp án: Tầng mạng (A)
Câu 6: Giả sử đường truyền dẫn từ A đến B thông qua 3 kết nối có băng thông 4Mbps, 1Mbps và 2Mbps. Nếu tất cả các liên kết chỉ phục vụ kết nối giữa A và B và độ trễ lan truyền gẫn như bằng 0 thì A cần chuyền một tệp 20MB sang B trong bao nhiêu giây?
Áp dụng nguyên lý nút thắt cổ chai => Bị giới hạn bởi 1Mbps
Vì độ trễ lan truyền ~0 nên thời gian truyền 20MB với băng thông 1Mbps sẽ là: 20.8=160 (giây)
Câu 7: Mô hình ICP/IP gồm bao nhiêu tầng?
=> 5 tầng
8. Thành phần nào dưới đây không được sử dụng trong mạng LAN
A. Card mạng
B. Máy tính
C. Dây cáp
D. Modem
Modem là thiết bị kết nối mạng nội bộ với ISP ra môi trường mạng diện rộng, chứ không có vai trò kết nối các máy tính bên trong nội bộ mạng LAN
=> Đáp án đúng: D Modem
Câu 9: Phương tiện truyền dẫn nào cho phép truyền dữ liệu tốc độ cao nhất trong mạng:
A. Cáp đồng trục
B. Cáp xoắn đôi
C. Cáp quang
D. Cáp điện
=> Đáp án đúng: Cáp quang
Câu 10: Đâu là tên gọi khác cho topology mạng có kết nối đầy đủ
A. Mesh
B,. Tree
C. Cáp quang
D. Ring
Mesh là lưới
=> Đáp án đúng: A. Mesh
Câu 11: Các thiết bị trên tầng liên kết dữ liệu sử dụng định dạng gì:
A. Địa chỉ MAC
B. Địa chỉ IP
C. Số hiệu cổng(Port)
D. None
Định danh trên TCP/IP
Application: Tên miền
TCP/UDP (Transport): Port number
IP(Mạng): IP address
Data link: MAC address
Physical: Không có
=> Đáp án đúng: A
Câu 12: Cho kết nối mạng giữa 2 máy chủ có RTT là 100ms, tốc độ băng thông là 30Mbps và kích thước tải trọng tối đa là 1500 byte. Nếu chúng ta cần truyền 15 000 byte Dữ liệu bằng cách sử dụng cơ chế Stop-and-Wait, sẽ mất bao lâu để hoàn thành việc truyền dữ liệu?
Ta có:
Số khung tin: 15 000/ 1500 = 10(Frame)
1500 byte = 12. 10^3 bit
T transmit: 12.10^3/ 30.10^6 = 0,4 (ms)
T tổng = 10 x (100+0,4) = 1004 (ms)
Vây kết quả là 1004 ms
Câu 13: Đâu là nhận xét đúng về bảng định tuyến trong bộ định tuyến?
A. Bộ định tuyến tham khảo bảng định tuyến để xác định đường đi tối ưu đến đích, thông qua xem xét địa chỉ IP đích của các gói tin đến.
B. Bộ định tuyến tham khảo bảng định tuyến để xác định đường dẫn tối ưu đến đích, thông qua xem xét địa chỉ IP nguồn của các gói tin đến.
C. Nếu bộ định tuyến không thể tìm thấy mục phù hợp trong bảng, nó sẽ phát gói tin đến tất cả các cổng ngoài trừ cổng đến.
D. Nếu bộ định tuyến không thể tìm thấy mục phù hợp trong bảng định tuyến, nó sẽ phát gói tin đến tất cả các cổng
Nếu bộ định tuyến không tìm thấy đích phù hợp, nó sẽ hủy gói tin và báo lỗi.
=> Đáp án đúng: A
Câu 14: Thiết bị nào sau đây đang hoạt động ở tầng liên kết dữ liệu trong mô hình tham chiếu OSI(có thể có nhiều lựa chọn)
A. Repeater
B. Hub
C. Router
D. Switch
E. Bridge
F. Máy tính cá nhân