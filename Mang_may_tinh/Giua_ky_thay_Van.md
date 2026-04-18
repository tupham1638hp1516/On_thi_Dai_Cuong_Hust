Getting Statarted:
Gửi câu hỏi lên cho NotebookLM để hỏi nó câu hỏi này nằm ở đâu + Hỏi Gemini
Nếu giải thích khó quá thì chụp lại slide xong bảo gemini giải thích thật dễ hiểu dựa trên sơ đồ của slide
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

1. Các thiết bị thuộc Tầng Liên kết dữ liệu (Data Link Layer - Layer 2)
Ở tầng này, các thiết bị làm việc với địa chỉ vật lý (MAC Address) và đóng gói dữ liệu thành các Frame.

D. Switch (Bộ chuyển mạch): Là thiết bị trung tâm trong mạng LAN hiện đại, có khả năng học địa chỉ MAC và chỉ chuyển tiếp dữ liệu đến cổng chứa thiết bị đích.

E. Bridge (Cầu nối): Một thiết bị kết nối hai phân đoạn mạng LAN khác nhau và kiểm soát việc lưu thông dữ liệu giữa chúng dựa trên địa chỉ MAC. Switch có thể được coi là một "Multi-port Bridge" (Cầu nối nhiều cổng).

2. Tại sao các lựa chọn khác không đúng?
A. Repeater & B. Hub: Hoạt động ở Tầng Vật lý (Physical Layer - Layer 1). Chúng chỉ đơn thuần là khuếch đại hoặc chuyển tiếp tín hiệu điện/quang mà không hề đọc hay hiểu nội dung của gói dữ liệu.

C. Router: Hoạt động ở Tầng Mạng (Network Layer - Layer 3). Router làm việc với địa chỉ IP và thực hiện việc định tuyến (tìm đường đi) giữa các mạng khác nhau.

F. Máy tính cá nhân (PC): Mặc dù PC có card mạng (NIC) hoạt động ở tầng 2, nhưng bản thân máy tính là một thiết bị đầu cuối (End-host) chạy các ứng dụng ở tất cả 7 tầng của mô hình OSI (từ Physical đến Application). Trong các câu hỏi phân loại thiết bị mạng đặc trưng, PC thường không được xếp riêng vào Layer 2.

Tóm tắt nhanh:

Layer 1: Hub, Repeater, Cable.

Layer 2: Switch, Bridge, NIC.

Layer 3: Router, Layer 3 Switch.
Đáp án đúng: D & E
Câu 15: Đâu là ưu điểm của thuật toán định tuyến link-state so với distance-vector?
A. Độ tin cậy cao hơn
B. Số lượng thông điệp trao đổi ít hơn
C. Tốc độ hội tụ như nhau
D. Không đáp án nào đúng
Trong các giao thức định tuyến:

Distance-vector (DV): Hoạt động theo nguyên tắc "đồn thổi" (routing by rumor). Mỗi router nhận bảng định tuyến từ hàng xóm và tin tưởng hoàn toàn vào đó. Nếu một router quảng bá thông tin sai, lỗi này sẽ lan truyền ra toàn mạng (ví dụ: lỗi "count-to-infinity"). Kiến thức mà router biết chỉ là cục bộ(dựa trên những router xung quanh)

Link-state (LS): Mỗi router tự xây dựng một bản đồ toàn cảnh (topology database) của toàn mạng. Các router chỉ quảng bá trạng thái các liên kết trực tiếp của mình. Nếu một router bị lỗi và gửi thông tin sai về các liên kết của nó, nó chỉ ảnh hưởng đến các node đi qua nó chứ không làm hỏng logic tính toán của các node khác như DV. Kiến thức mà router biết là toàn cục.

Dễ thấy số lượng thông điệp trao đổi của link-state sẽ phải nhiều hơn DV

Hội tụ là toàn bộ router đồng ý với nhau về đường đi đúng => Do đó tốc độ hội tụ của LS sẽ nhanh hơn DV
=> Đáp án đúng: A
Câu 16: Đâu là nhận xét sai về hệ tự trị trong định tuyến (Autonomous System)
A. Trong một AS, các router sẽ triển khai chính sách định tuyến giống nhau
B. Giao thức định tuyến nội miền(Intra-domain) được sử dụng bên trong AS
C. Giao thức định tuyến liên miền(Inter-domain) được sử dụng để kết nối các AS với nhau
D. Số lượng các AS là cố định
Ta hình dung nếu Internet là một thành phố khổng lồ thì AS sẽ là một tòa nhà được quản lý riêng ở trong đó(đó có thể là 1 ISP, 1 trường đại học, vv)
Vì vậy nên số lượng AS không thể cố định được, nó có thể được tạo mới, xóa đi, hay gộp lại.
Các đáp án còn lại đúng vì:
A. AS giống như một tổ chức quản lý, nên rõ ràng các router sẽ phải có chính sách giống nhau
B + C: Bên trong 1 tòa nhà thì phải có "nội miền" còn giữa các tòa nhà thì phải có "liên miền"
Câu 17: Tác dụng của Dynamic Host Configuration Protocol là gì?
A. Cung cấp địa chỉ IP tự động từ một máy chủ khi có một máy tính tham gia vào mạng
B. Truyền địa chỉ IP giữa các máy tính
C. Cấu hình bảng định tuyến máy tính
D. Thiết lập cấu hình máy tính thông qua kết nối từ xa
DHCP là giao thức giúp máy tính tự động nhận cấu hình mạng
Khi một máy mới vào mạng, DHCP server sẽ tự động cấp:
1. Địa chỉ IP
2. Subnet mask
3. Default gateway
4. DNS
Dễ thấy thì A là đáp án đúng
Câu 18: Chức năng chính của các giao thức đa truy cập( multiple access) trong tầng liên kết dữ liệu là gì (2 lựa chọn)
A. Cho máy tính tham gia vào mạng mới
B. Xác định cách các nút chia sẻ kênh
C. Truyền thông về chia sẻ kênh phải sử dụng chính kênh đó
D. Giúp máy tính truy cập vào video, âm thanh, hình ảnh trên Internet
Khi có nhiều máy tính cùng nối vào 1 đường truyền chung mà ai cũng gửi cùng lúc thì sẽ bị đụng nhau. => Giao thức đa truy cập sẽ quyết định ai được nói và nói khi nào.
Phân tích các đáp án đúng:
B. Đây là chức năng chính của giao thức đa truy cập, sẽ có một bộ luật để quyết định và giao thức MAC chính là bộ luật đó
C. Do không có kênh điều khiển riêng, các node phải sử dụng chính kênh truyền dữ liệu để quan sát trạng thái và tự quyết định thời điểm truyền, nhằm giảm thiểu xung đột trong môi trường phân tán.
Các đáp án sau sai:
A. Đây là việc của DHCP
D. Đây là việc của tầng ứng dụng
Câu 19: Hạn chế của giao thức định tuyến động là gì?
A. Không thể sử dụng liên kết dự phòng
B. Khó quản lý
C. Khó thích ứng với sự thay đổi của cấu trúc mạng
D. Không an toàn
Ta chọn đáp án D dựa trên slide:
Định tuyến tĩnh: Các mục trong bảng định tuyến được sửa đổi thủ công bởi người quản trị
Định tuyến động: Tự động cập nhật bảng định tuyến các giao thức định tuyến
Câu 20: Mạng sử dụng bit parity chẵn để phát hiện lỗi do truyền mạng gây ra. Tìm bit parity chẵn của dữ liệu 1001  1100?
Nếu số bit 1 chẵn → parity = 0
Nếu số bit 1 lẻ → parity = 1
Vậy bit parity chẵn cuart dữ liệu là 0
Câu 21: Datagram (1011 1000 0011 1100) được gửi sử dụng mã vòng CRC để phát hiện lỗi. Biết rằng G = 10011, hãy tính mã CRC của datagram bên trên
Mã CRC chính là số dư của phép chia nhị phân giữa dữ liệu (đã được thêm các bit 0) cho đa thức phát sinh G
Ta thấy G có 5 bit => Ta phải thêm 5-1 = 4 bit 0 vào sau dữ liệu
Ta được 1011 1000 0011 1100 0000
Để chia thì ta làm như sau:
Lấy 10111 XOR 10011 = 00100
Sau đó ta hạ bit tiếp theo xuống, ở đây là 0, vậy ta được: 01000
Vì bit đầu bên trái là 0 nên ta lại hạ tiếp: 10000
Sau đó ta XOR: 10 000 XOR 10 011 = 00011
Làm liên tục đến cuối cùng ta thu được CRC = 1100
Câu 22: Trong số các kiến trúc phân phối quang(optical - distribution) cái mà được chuyển mạch Ethernet là?
A. PON
B. MON
C. AON
D. NON
Ta có thể chia công nghệ mạng thành 2 loại
Shared(Hub, Wifi, PON)                        Switch(Ethernet, AON)
Rẻ                                             Đắt
Đơn giản                                       Phức tạp
Dễ nghẽn                                       Hiệu năng cao
Khó tối ưu                                     Có điều khiển
=> Đáp án đúng: C
Câu 23: Thiết bị chuyển mạch(Switch) được liên kết với mạng nào?
A. Bus
B. Ring
C. Star
D. Mesh
Thấy switch / hub (trung tâm) → chọn Star
Thấy chia sẻ 1 đường → Bus
Thấy vòng tròn → Ring
=> Đáp án đúng: C
Câu 24: Thiết bị nào không phải là thiết bị đầu cuối?
A. Switch
B. Server
C. Máy tính
D. Điện thoại thông minh
Thiết bị đầu cuối là thiết bị tạo ra dữ liệu hoặc tiêu thụ dữ liệu
=> Đáp án đúng: A
Câu 25: Kỹ thuật đa truy cập(multiple access) nào được sử dụng bởi chuẩn IEEE 802.11 cho wireless LAN?
A. CDMA
B. CSMA/ CA
C. CSMA/ CD
D. ALOHA
Kỹ thuật CSMA/ CD sẽ thường được sử dụng trong mạng Ethernet nhờ ưu thế về đường truyền (nếu bị va chạm thì sửa lại vì đường truyền có thể nghe được sau khi gửi- nhận biết được)
Kỹ thuật CSMA/ CA thì khác, nó sinh ra để khắc phục điểm yếu của đường truyền wireless (không nghe được khi đã truyền đi dẫn đến khả năng bị va chạm cao). Kỹ thuật này là các luật giúp tránh bị va chạm
ALOHA gửi hoàn toàn ngẫu nhiên
CDMA thì dùng trong 3G
=> Đáp án đúng: B
Câu 26: Trường nào giúp kiểm tra sự sắp xếp của các fragments?
A. Flag
B. TTL (Time to Live)
C. Identifier
D. Offset
Khi một gói IP bị chia nhỏ (fragment):
 Mỗi mảnh cần trả lời 2 câu hỏi:
Tôi thuộc gói nào?
Tôi nằm ở vị trí nào trong gói đó?
Flag dùng để báo còn fragment nữa hay không
TTL dùng để giới hạn số hop (không liên quan gì fragment)
Identifier dùng để nhận biết các fragment thuộc cùng 1 gói
Offset cho biết vị trí của fragment trong gói gốc
=> Đáp án đúng: D
Câu 27: Đâu là tốc độ truyền dữ liệu nhanh nhất dưới đây:
A. bps
B. Kbps
C. Mbps
D. Gbps
Câu này khó quá
Câu 28: Địa chỉ IPv4 nào là hợp lệ cho địa chỉ IP public nếu sử dụng phương pháp CIDR để cấp phát địa chỉ IP?
A. 192.168.1.16
B. 10.0.0.1
C. 23.3.4.256
D. 11.0.0.1
E. 172.15.4.9
F. 172.16.9.4
IPv4 là địa chỉ dạng:
 a.b.c.d (4 số)
Mỗi số:
 từ 0 → 255
IP public không nằm trong dải private
Dải IP Private là:
10.0.0.0 → 10.255.255.255
172.16.0.0 → 172.31.255.255
192.168.0.0 → 192.168.255.255
=> Đáp án đúng: D và E
Câu 29: Trong classful addressing, phần lớn các địa chỉ có đặc điểm nào sau đây:
A. Được tổ chức
B. Bị lãng phí
C. Bị chặn
D. Giao tiếp với nhau
Classful addressing là một cách chia địa chỉ IP thành 3 loại lớp khác nhau là A,B,C. Nhưng vì mỗi một lớp luôn cố định với một số máy riêng biệt nên nếu một công ty có số lượng máy vượt quá mức C nhưng lại không quá nhiều dẫn đến phải chọn lớp B => Lãng phí rất nhiều địa chỉ.
=> Đáp án đúng: B
Câu 30: Điều gì sẽ xảy ra nếu MTU của kết nối mạng quá nhỏ?
A. Nó làm tăng xác suất xảy ra lỗi
B. Nó làm giảm hiệu suất truyền dữ liệu vì tiêu đề có kích thước cố định
C. Nó làm tăng tắc nghẽn mạng do số lượng gói tin
D. Nó làm giảm băng thông kết nối mạng
Tiêu đề luôn có một kích thước cố định, và % dung lượng đường truyền luôn <100% vì còn phải trừ đi gói tin=> Nếu MTU càng lớn thì hiệu suất sẽ càng lớn.
Lấy ví dụ gói tin 1460 byte, tiêu đề 40 byte
+) Nếu MTU =1500 thì ta có hiệu suất sử dụng đường truyền là 1460/1500 ~ 97%
+) Nếu MTU =100 thì ta có hiệu suất sử dụng đường truyền là 60/100 ~ 60%
Như vậy đáp án B là đáp án đúng
A. Sai vì: Xác suất lỗi bit phụ thuộc vào chất lượng dây cáp, nhiễu điện từ hoặc sóng WiFi, và gói tin nhỏ thực ra còn khó bị lỗi hơn gói tin lớn (vì nó đi qua dây nhanh hơn, ít cơ hội gặp nhiễu hơn).

C. Sai vì: Tắc nghẽn mạng (Congestion) xảy ra khi tổng lưu lượng (tổng số bits) vượt quá khả năng của đường truyền hoặc hàng đợi của Router bị đầy. Ta có thể hiểu MTU là tải trọng tối đa cho 1 cái xe chở hàng, còn tổng lưu lượng là cả cái kho hàng, việc cái xe được chất tối đa bao nhiêu hàng phụ thuộc vào khả năng của chính nó chứ không phải số lượng hàng trong kho.

D. Sai vì: Băng thông (Bandwidth) là độ rộng của đường ống (ví dụ gói cước 100Mbps). MTU nhỏ không làm cái ống hẹp lại.Sự thật: Nó chỉ làm giảm Tốc độ thực tế (Goodput). Tức là ống vẫn to, nước vẫn chảy đầy ống, nhưng trong nước toàn là "rác" (Header) chứ không phải "nước sạch" (Dữ liệu).
Câu 31: Mạng máy tính đầu tiên trên thế giới có tên là?
A. CNNET
B. NSFNET
C. ASAPNET
D. ARPANET
=> Đáp án đúng: D. Không nhớ thì phải chịu
Câu 32: Trong mô hình TCP/IP, khi gói tin được chuyển từ tầng trên xuống tầng dưới thì header sẽ được?
A. Thêm vào
B. Thay đổi
C. Loại bỏ
D. Sắp xếp lại
Khi dữ liệu đi từ tầng trên (Application) xuống tầng dưới cùng (Physical), mỗi tầng sẽ coi toàn bộ khối dữ liệu từ tầng trên chuyển xuống là "phần thân" (Payload) và dán thêm một cái nhãn (Header) của riêng nó vào.
=> Đáp án đúng: A
Câu 33: Địa chỉ Ethernet gồm bao nhiêu bit?
=> 48 bit
Câu 34: Đâu là nhận xét đúng về cơ chế tự học swtich? (Có thể có nhiều lựa chọn đúng)
A. Khi một frame đến switch, switch sẽ cập nhật bảng địa chỉ MAC của nó dựa trên địa chỉ nguồn của frame
B. Khi một frame đến switch, switch sẽ cập nhật bảng địa chỉ MAC của nó dựa trên trường địa chỉ đích của frame
C. Khi một mục trong mảng địa chỉ MAC được thêm vào, nó sẽ tồn tại cho đến khi được cập nhật thông tin mới
D. Một mục trong bảng địa chỉ MAC sẽ hết hạn nếu không được sử dụng và sau khi đã hết thời gian chờ
Slide trang 72 chương 3:
Câu chuyện về "Bác Switch" và Cuốn sổ tay
Hãy tưởng tượng cái Switch ở giữa là một Bác bảo vệ đứng ở sảnh của một tòa nhà có 6 căn phòng (được đánh số từ 1 đến 6). Trong mỗi phòng có một bạn nhỏ (A, B, C, A', B', C').

Bác bảo vệ có một Cuốn sổ tay (MAC Table). Ban đầu, cuốn sổ này trống trơn, bác chẳng biết ai ở phòng nào cả.

📝 Bước 1: "Cháu không nói thì bác không biết"
Khi bạn A (ở phòng số 1) muốn gửi một lá thư cho bạn A'.

Bạn A thò tay ra khỏi cửa phòng 1, đưa thư cho bác bảo vệ.

Bác bảo vệ nhìn vào lá thư thấy ghi: "Người gửi: A".

Bác nhìn lại cửa phòng: "À, hóa ra bạn A đang ở phòng số 1!".

Ngay lập tức, bác mở sổ tay ra và ghi: "Bạn A - Phòng 1". (Giống hệt cái bảng trong slide của ông đấy).

Đây chính là cơ chế tự học: Bác không đi từng phòng để hỏi, bác cứ đợi ai gửi thư thì bác mới ghi tên vào sổ.

🔄 Bước 2: "Ủa, cháu mới chuyển nhà à?"
Slide có ghi một ý là: "Nhận được gói tin trên cổng khác". Nghĩa là:

Hôm sau, bạn A lén lút chuyển sang phòng số 5 ngồi.

Bạn A lại gửi một lá thư từ phòng số 5.

Bác bảo vệ xem thư: "Người gửi: A". Bác nhìn sang sổ cũ thấy ghi phòng 1, nhưng thực tế thư lại bay ra từ cửa số 5.

Bác gạch ngay số 1 đi và ghi mới: "Bạn A - Phòng 5".

⏳ Bước 3: Cái số "60" (TTL) là gì?
Ông nhìn vào cột TTL có số 60 trong slide không?

Đó là "Đồng hồ đếm ngược".

Nếu trong vòng 60 giây mà bạn A không gửi thêm lá thư nào, bác bảo vệ sẽ nghĩ: "Chắc bạn này đi chơi rồi".

Bác sẽ lấy tẩy xóa luôn dòng tên bạn A trong sổ để tiết kiệm chỗ cho người khác.

Như vậy, đáp án đúng sẽ là A và D, B sai thì quá rõ rồi, còn C sai vì không phải địa chỉ sẽ tồn tại cho đến tận khi được cập nhật thông tin mới mà còn vì nếu quá lâu nó không gửi một tin gì, địa chỉ của nó cũng sẽ bị xóa
Câu 35: Một mạng sử dụng 4-bit CHECKSUM để phát hiện lỗi trong quá trình truyền dữ liệu. Mã checksum của dữ liệu 1001 1000 1101 là gì?
Các bước để tính mã checksum:
1. Cộng lần lượt từng khối bit lại với nhau (vdu 1001 + 1000, rồi lại cộng với 1101)
2. Nếu kết quả gồm 5 bit, ta sẽ chỉ lấy 4 bit bên phải rồi cộng thêm với 1
3. Sau khi đã cộng xong hết, ta đảo bit => kết quả cuối cùng là mã checksum
4. Cách để kiểm tra đúng không: Tổng của tất cả các khối bit (tính cả checksum) phải bằng 1111

Bảng định tuyến của 1 router như sau:
Network Address                Next-hop                Interface
192.168.4.0/22                 A                        1
192.168.7.0/24                 B                        2
192.168.0.0/16                 C                        3
10.0.0.128/25                  D                        4
10.0.0.0/26                    E                        5

Bộ định tuyến sẽ thực hiện thao tác nào nếu nhận được gói IP có địa chỉ IP đích như sau:
Câu 36. 192.168.6.31?
A. Chuyển tiếp gói tin tới interface 1
B. Chuyển tiếp gói tin tới interface 2
C. Chuyển tiếp gói tin tới interface 3
D. Chuyển tiếp gói tin tới interface 4
E. Chuyển tiếp gói tin tới interface 5
F. Loại bỏ gói tin

Hãy tưởng tượng ông là Bác Bưu Tá đang đứng trước một ngã tư đường. Trên tay ông là một lá thư cần gửi đến địa chỉ: Số nhà 192.168.6.31.

Ở ngã tư đó, có các biển chỉ đường (chính là cái Bảng định tuyến) như sau:

🚦 Bước 1: Xem các biển chỉ đường
Biển số 3 (Khu vực chung - /16): Biển này ghi "Tất cả những ai có địa chỉ bắt đầu bằng 192.168 thì đi vào Cửa số 3".

Lá thư của mình có bắt đầu bằng 192.168 không? Có! Vậy là có thể đi cửa 3.

Biển số 1 (Khu vực hẻm - /22): Biển này ghi chi tiết hơn: "Những ai có địa chỉ bắt đầu bằng 192.168 và thuộc các xóm 4, 5, 6, 7 thì đi vào Cửa số 1".

Lá thư của mình là xóm số 6, có nằm trong nhóm này không? Có luôn! Vậy là cũng có thể đi cửa 1.

Biển số 2 (Khu vực nhà hàng xóm - /24): Biển này ghi cực kỳ chi tiết: "Chỉ những ai ở đúng xóm 192.168.7 mới được đi Cửa số 2".

Thư của mình là xóm số 6. Sai rồi! Biển này không dành cho mình.

⚖️ Bước 2: Chọn lối đi nào đây? (Quy tắc "Chỉ dẫn chi tiết nhất")
Bây giờ ông đang phân vân giữa Cửa số 3 và Cửa số 1. Cả hai đều đúng, nhưng bác bưu tá phải chọn cái nào?

Trong ngành mạng có một quy tắc cực kỳ dễ thương: "Cái nào ghi càng chi tiết, càng cụ thể thì nghe theo cái đó".

Biển số 3 (/16): Giống như một cái biển to đùng chỉ đường về "Thành phố Hà Nội". (Rất chung chung).

Biển số 1 (/22): Giống như một cái biển nhỏ hơn chỉ đường về "Quận Hai Bà Trưng, Hà Nội". (Chi tiết hơn nhiều).

Vì cái biển số 1 chỉ đường chi tiết hơn (nó biết rõ ông thuộc nhóm xóm 4-5-6-7), nên ông phải đi theo nó. Trong kỹ thuật, cái con số /22 lớn hơn /16 chính là để nói rằng: "Tôi là chỉ dẫn chi tiết hơn đây!".
***
Cái dấu /22 thực chất là gì?
Ông cứ tưởng tượng một địa chỉ IP đầy đủ là một chuỗi gồm 32 con số nhị phân (chỉ có 0 và 1). Cái con số sau dấu gạch chéo (ví dụ /22) chính là "Chiếc khóa".
•	Số 22 nghĩa là: 22 con số đầu tiên đã bị khóa cứng. Đó là "tên của khu phố", ông không được phép chạm vào hay thay đổi.
•	Phần còn lại (32 - 22 = 10): 10 con số cuối cùng là phần ông được tự do thay đổi để đặt số nhà cho từng hộ dân.
Mẹo nhớ: Số đằng sau dấu gạch càng to => Cái khóa càng dài => Tên khu phố càng dài và chi tiết => Khu phố đó càng bé (vì còn ít số để đặt cho số nhà).
•	/8: Cấp cho cả một Quốc gia (Cực kỳ nhiều nhà).
•	/24: Cấp cho một công ty nhỏ (Tầm 254 nhà).
•	/32: Chỉ có đúng 1 căn nhà duy nhất.
________________________________________
2. Tại sao /22 lại là "xóm 4, 5, 6, 7"?
Đây là phần "phép thuật" của toán học, nhưng tôi sẽ chỉ ông cách tính nhẩm của dân Bách Khoa không cần nhị phân:
Một địa chỉ IP có 4 nhóm số (ví dụ: 192 . 168 . 6 . 31).
•	Mỗi nhóm số tối đa là 255 (tổng cộng 256 giá trị tính cả số 0).
•	Mỗi nhóm số này được đại diện bởi 8 cái khóa.
Tính toán nhanh:
1.	Nhóm 1: /8 đầu tiên khóa số 192. (Xong)
2.	Nhóm 2: /8 tiếp theo (tổng là /16) khóa số 168. (Xong)
3.	Nhóm 3: Đây là chỗ "biến hình". Ta đã dùng 16 cái khóa, mà đề bài cho /22, vậy ta còn dư 22-16=6 cái khóa cho nhóm số thứ 3 này.
Trong 1 nhóm số có 8 vị trí, mà ông đã khóa mất 6, vậy còn 2 vị trí để nhảy số.
👉 Bước nhảy (độ rộng của xóm) là: 2^2=4 nhà.
Kết luận: Vì đề bài cho mạng bắt đầu từ số 4 (192.168.4.0), mà xóm này rộng đúng 4 số, nên ông cứ đếm từ 4 đi: 4, 5, 6, 7. Thế là hết xóm!

Câu 37: 192.168.8.31
A. Chuyển tiếp gói tin tới interface 1
B. Chuyển tiếp gói tin tới interface 2
C. Chuyển tiếp gói tin tới interface 3
D. Chuyển tiếp gói tin tới interface 4
E. Chuyển tiếp gói tin tới interface 5
F. Loại bỏ gói tin
Dễ thấy đáp án đúng là C

Nếu gói IP có kích thước dữ liệu (tải trọng) 4926 byte được gửi vào phân đoạn mạng có MTU là 880 byte và giả sử kích thước tiêu đề IP là 20 byte

Trong gói tin IP, có một con số gọi là Fragment Offset (Vị trí của đoạn). Để tiết kiệm bộ nhớ, người ta không đếm từng byte một mà đếm theo cụm 8 byte.

👉 Luật chơi: Kích thước dữ liệu trong mỗi đoạn (trừ đoạn cuối cùng) BẮT BUỘC phải là một số chia hết cho 8.

Câu 38: Chúng ta cần chia gói IP thành bao nhiêu đoạn để đáp ứng yêu cầu của phân đoạn mạng?
880-20=860. Lấy con số chia hết cho 8 gần nhất 860 thì là 856. Lấy 4926/856~5.75 => cần 6 đoạn
Câu 39: Kích thước của dữ liệu trong fragment cuối là bao nhiêu?
4926 - 856 x 5 = 646

Cung cấp mạng có địa chỉ IP sau: 200.23.0.0/22?
Câu 40. Địa chỉ nào không thuộc mạng gốc bên trên?
A. 200.23.2.1
B. 200.23.1.1
C. 200.23.3.1
D. 200.23.4.1
=> 200.23.4.1
Số lượng thiết bị tối đa thuộc về mạng này là bao nhiêu
Ta lấy 32-22=10. Vậy số lượng máy tối đa là 2^10=1024
Câu 42: Chúng ta muốn chia mạng ban đầu thành các mạng con. Mỗi mạng con có 32 PC. Số lượng mạng con tối đa có thể được tạo từ mạng ban đầu là bao nhiêu?
Mỗi mạng con có 32 PC, nhưng vì luôn có 2 địa chỉ là cố định nên ta cần 34 địa chỉ cho mỗi mạng con => 6 bit
Vậy chỉ còn lại 4 bit, tương ứng với 2^4=16 mạng con
Câu 43: Có thể tách bao nhiêu mạng con có độ dài địa chỉ 24 bit từ mạng gốc bên trên
4 mạng con

Bảng chuyển tiếp gói tin(MAC Table) của 1 switch như sau:
Host                                             Interface
12-12-12-ab-ab-ab                                 e1
11-11-11-dd-dd-dd                                 e2
33-33-33-ee-ee-ee                                 e3
55-55-55-cc-cc-cc                                 e4
Câu 44: Switch sẽ làm gì khi nhận được frame có địa chỉ đích 12-12-12-ab-aa-aa và địa chỉ nguồn 33-33-33-ee-ee-ee từ cổng e3
Đáp án là Broadcast, vì switch nằm trong tầng datalink/ mạng LAN, nếu có một địa chỉ đích bị lỗi, nó sẽ broadcase cho tất cả các cổng trừ cổng địa chỉ nguồn(bởi vì cũng chỉ có ít máy tính, nên nó sẽ thông báo hết => Khác với Router nằm ở tầng 3)
Câu 45: Switch sẽ làm gì khi nhận được frame có địa chỉ đích 12-12-12-ab-ab-ab và địa chỉ nguồn 11-11-11-dd-dd-dd từ cổng e3
Đáp án : Thêm/cập nhật địa chỉ 11-11... và chuyển tiếp frame tới cổng e1