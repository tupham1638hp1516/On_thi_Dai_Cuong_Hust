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
Câu 10: Trong các khẳng định sau về trường TTL trong gói tin IP, khẳng định nào là SAI?
A. Khi trường TTL giảm về 0, router sẽ hủy bỏ thay vì chuyển tiếp gói tin
B. Mục đích của trường TTL là ngăn chặn việc gói tin IP có thể bị lặp vòng trong mạng
C. Trường TTL giảm một đơn vị khi đi qua 1 router
D. Trường TTL được trả về từ lệnh ping là số giây từ khi gửi gói tin đến khi nhận được gói tin phản hồi
=> Đáp án chọn là: D
TTL (Time To Live): Đây là một con số (đếm bước nhảy), không phải thời gian tính bằng giây. Nó cho biết gói tin phản hồi còn lại bao nhiêu "mạng sống" (số router tối đa có thể đi qua) khi nó quay về đến máy của bạn.

Thời gian (Time): Con số tính bằng mili giây (ms) mà bạn thấy trong kết quả ping (ví dụ: time=15ms) mới là thời gian khứ hồi (RTT - Round Trip Time) từ khi gửi đến khi nhận.
Câu 11: Cho một đường liên kết mạng có băng thông R = 25Mbps. Nếu việc định tuyến qua đoạn mạng này sử dụng giao thức định tuyến OSPF thì chi phí/ giá mặc định trên đoạn mạng này là bao nhiêu
100/25 =4 => Chi phí là 4
Câu 12: Trong các khẳng định sau về định tuyến liên vùng giữa các mạng khác nhau, khẳng định nào là Đúng?
A. Giao thức định tuyến BGP dựa trên thuật toán dạng link-state.
B. Định tuyến BGP giữa các miền tự trị (AS) ưu tiên hiệu năng hơn chính sách
C. Tại các router biên kết nối giữa các miền tự trị (AS) với nhau có 2 bảng định tuyến, một cho định tuyến nội vùng, một cho định tuyến liên vùng
D. Việc quảng bá thông tin định tuyến liên vùng hay không chủ yếu dựa vào chính sách của từng vùng tự trị

Định tuyến liên vùng không sử dụng thuật toán distance-vector hay link-state mà nó sử dụng path-vector. Đặc biệt, BGP của các AS sẽ luôn ưu tiên chính sách > hiệu năng (mạng tao luật tao)
=> Đáp án đúng sẽ là D
Câu 13: Khi mạng xảy ra tình trạng tắc nghẽn sẽ khiến độ trễ nào tăng lên?
=> Đáp án đúng: Trễ hàng đợi
câu 14: Với một đường truyền mạng có tỷ lệ lỗi bit không đổi, khi kích thước gói tin tăng lên thì
A. Tỷ lệ lỗi gói tin tăng lên
B. Tỷ lệ lỗi gói tin không đổi
C. Tỷ lệ gói tin giảm đi
D. Chưa thể khẳng định gì

Lưu ý: BER là tỷ lệ MỘT bit bị lỗi, do đó nếu gói tin dài ra thì chắc chắn tỷ lệ lỗi GÓI tin sẽ tăng
=> Đáp án đúng: A
Câu 15: Trong mô hình OSI, chức năng định tuyến được thực hiện ở tầng nào?
=> Tầng mạng/ Network
Câu 16: Địa chỉ Ethernet gồm bao nhiêu bit => 48 bit
Câu 17: Mô hình TCP/IP có bao nhiêu tầng: => 5 tầng
Câu 18: Những cơ chế nào giúp cho giao thức các tầng khác nhau giữa máy gửi và máy nhận trong mô hình kiến trúc phân tầng của TCP/IP có thể hoạt động với nhau nhưng không ảnh hưởng đến dữ liệu các tầng khác? (2 đáp án đúng)
A. Các tầng hiểu giao thức của nhau để phục vụ cho cho việc truyền thông độc lập
B. Mỗi tầng có giao thức độc lập hoạt động không liên quan đến nhau
C. Mỗi tầng (bên gửi) đóng gói dữ liệu tầng trên bằng việc thêm header của riêng mình và chuyển xuống tầng dưới
D. Các tầng ngang hàng (giữa máy gửi và máy nhận) sử dụng chung giao thức để trao đổi dữ liệu

A và B sai vì nó không quá độc lập nhưng các tầng cũng chẳng hiểu giao thức của nhau, nói chung là lưng chừng
=> Đáp án C và D(peer-to-peer communication) rõ ràng đúng
Câu 19: Thiết bị nào sau đây không sử dụng cho mạng LAN?
A. Cổng kết nối mạng (NIC)
B. Máy tính
C. Cáp nối
D. Modem
=> Đáp án là: Modem. thằng này liên kết mạng LAN với Internet (trung gian)
Câu 20: Cho một đường truyền sử dụng mã hóa Manchester vi sai có tốc độ truyền dữ liệu là 100.000 bit/s. Hỏi tốc độ baud của đường truyền đấy là:
Tốc độ baud là số ký hiệu tín hiệu trên giây
Thằng manchester đặc biệt ở chỗ dùng gấp đôi để biểu diễn
=> Tốc độ baud là 200 000 bauds
Câu 21: Trong các mạng được mô tả dưới đây, mạng nào kết nối dưới dạng điểm- đa điểm? (3 đáp án đúng)
A. Một điện thoại thông minh kết nối với nhiều thiết bị ngoại vi (bluetooth)
B. Các máy tính để bàn kết nối với nhau qua một switch trung gian
C. Các máy tính để bàn kết nối với nhau qua một hub trung gian
D. Các máy tính kết nối với nhau qua mạng WLAN
E. Các máy tính kết nối với nhau dưới dạng Token Ring

A (Bluetooth): Hoạt động theo mô hình Piconet, trong đó một thiết bị Master (như smartphone) có thể kết nối và quản lý dữ liệu với nhiều thiết bị Slave (tai nghe, đồng hồ, chuột) cùng một lúc.

C (Hub): Hub là thiết bị "ngu", nó không phân biệt được các máy tính. Khi một gói tin đến, Hub sẽ nhân bản và đẩy gói tin đó ra tất cả các cổng còn lại (Broadcasting), tạo thành một môi trường kết nối đa điểm.

D (WLAN): Trong mô hình hạ tầng (Infrastructure mode), Access Point (AP) đóng vai trò trạm phát trung tâm, truyền tín hiệu vô tuyến đến tất cả các thiết bị khách trong vùng phủ sóng.

B (Switch): Switch thông minh hơn Hub. Nó sử dụng bảng địa chỉ MAC để tạo ra một đường truyền Điểm - Điểm (Point-to-Point) riêng biệt giữa máy gửi và máy nhận. Dữ liệu không bị đẩy ra toàn mạng một cách đại trà.

E (Token Ring): Mặc dù về vật lý có thể cắm vào một bộ tập trung, nhưng về mặt logic, dữ liệu được truyền theo vòng tròn. Mỗi máy tính chỉ thực hiện kết nối Điểm - Điểm với máy kế tiếp trong vòng nhẫn để chuyển tiếp "thẻ bài" (token).

Khi nói đến mạng LAN, người ta mặc định dùng cáp Ethernet và Switch
Lưu ý: Nếu Switch thì không phải điểm- đa điểm mà sẽ là điểm- điểm
Câu 22: Nhược điểm của cáp quang khi so sánh với cáp đôi và cáp đồng trục là gì? (2 đáp án đúng)
A. Giá thành đắt đỏ khi sử dụng cho mạng LAN
B. Dễ hư hỏng hơn
C. Băng thông truyền tải thấp hơn
D. Có kích thước và trọng lượng lớn hơn
E. Dễ bị ảnh hưởng bởi sóng điện từ
Dễ thấy đáp án đúng là A và B, E sai vì rõ ràng quang thì sao bị ảnh hưởng bởi sóng điện từ được
Câu 23: Cho một mạng với địa chỉ IP như sau: 200.23.0.0/22. Địa chỉ nào sau đây thuộc về mạng đã cho?
A. 200.23.2.1
B. 200.23.1.1
C. 200.23.3.1
D.200.23.4.1
=> Dễ thấy D
Câu 24: Trong truyền tin sử dụng CSMA/ CA để truy cập đường truyền chia sẻ, vì sao đụng độ vẫn xảy ra dù các máy đã lắng nghe trước khi truyền?
A. Do độ trễ lan truyền
B. Do các máy có thể phát tín hiệu trên tần số khác nhau
C. Khi mạng tắc nghẽn có thể ảnh hưởng đến việc nhận diện tín hiệu truyền dữ liệu
D. Tất cả các đáp án khác đều đúng
=> Dễ thấy là A
B sai vì nếu tần số khác nhau thì đã không đụng độ, còn D sai vì tắc nghẽn không liên quan đến lắng nghe
Câu 25: Cho một mạng có đường truyền chia sẻ gồm 10 máy. Khả năng mỗi máy có nhu cầu truyền dữ liệu tại 1 thời điểm là 80%. Hãy lựa chọn kỹ thuật truy cập đường truyền phù hợp nhất trong các đáp án sau:
A. Aloha
B. Slotted Aloha
C. CSMA/ CD
D. TDMA
Lưu ý: TDMA là chia khe "thời gian" nên nếu không có gì thì các gói vẫn phải đợi đến lượt
Ok, trình bày dưới dạng liệt kê để bạn dễ dàng đưa vào tài liệu Markdown nhé:

1. Môi trường Tải thấp (Low Load)
Giao thức tối ưu: Nhóm Random Access (Aloha, CSMA/CD, CSMA/CA).

Lý do/Ưu điểm: Phản ứng tức thì với nhu cầu truyền tin, không tốn tài nguyên cho việc quản lý hoặc điều phối trung tâm.

Nhược điểm: Khi số lượng máy truyền tăng đột ngột, hiệu suất sẽ sụt giảm mạnh do tần suất đụng độ (Collision) tăng cao.

2. Môi trường Tải cao (Heavy Load)
Giao thức tối ưu: Nhóm Partitioning (TDMA, FDMA, CDMA).

Lý do/Ưu điểm: Loại bỏ hoàn toàn hiện tượng đụng độ, đảm bảo băng thông được phân chia công bằng và ổn định cho mọi thiết bị.

Nhược điểm: Độ trễ (Delay) lớn vì mỗi máy bắt buộc phải chờ đến đúng lượt hoặc khe thời gian của mình mới được phép gửi tin, kể cả khi các máy khác đang không có dữ liệu.
Câu 26: Trong mạng không dây ad-hoc,.....
A. Cần có AP
B. Mọi nút đều là AP
C. Các máy tính không cần thiết
D. AP không cần thiết

AP- Access Point, đóng vai trò như một trung tâm giúp kết nối
Mạng ad-hoc là mạng mà các thiết bị kết nối trực tiếp với nhau
=> Đáp án đúng: D
câu 27: Kỹ thuật truy nhập đường truyền nào được dùng trong chuẩn mạng LAN không dây 802.11?
Chú ý: mạng LAN nhưng không dây => CSMA/ CA
Câu 28: Trường nào trong gói tin IP được dùng để sắp xếp các phân mảnh khi truyền tin
=> Offset (Cái này dùng để sắp xếp thứ tự)
Câu 29:
Thiết bị nào sau đây đang hoạt động ở tầng liên kết dữ liệu trong mô hình tham chiếu OSI(có thể có nhiều lựa chọn)
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
Câu 30: Giả sử đường truyền dẫn từ A đến B thông qua 3 kết nối có băng thông 4Mbps, 1Mbps và 2Mbps. Nếu tất cả các liên kết chỉ phục vụ kết nối giữa A và B và độ trễ lan truyền gẫn như bằng 0 thì A cần chuyền một tệp 20MB sang B trong bao nhiêu giây?
Áp dụng nguyên lý nút thắt cổ chai => Bị giới hạn bởi 1Mbps
Vì độ trễ lan truyền ~0 nên thời gian truyền 20MB với băng thông 1Mbps sẽ là: 20.8=160 (giây)
*** Tất cả các câu còn lại đều có trong đề Giua_ky_thay_Van ***
31. B
32. D
33. A
34. D
35. D
36. Nhược điểm của chuyển mạch kênh là gì?
A. Đảm bảo chất lượng dịch vụ kém hơn chuyển mạch gói
B. Hiệu suất truyền thấp khi tỷ lệ truyền dữ liệu thấp sau khi thiết lập liên kết
C. Hiệu suất truyền thấp khi lượng dữ liệu truyền nhỏ do phải thiết lập và hủy liên kết khi truyền dữ liệu
D. Khi một thiết bị chuyển mạch bị lỗi phải bắt đầu lại quá trình thiết lập kênh truyền
E. Trễ khi chuyển mạch cao
Đáp án đúng là B,C,D
A sai là rõ
B đúng vì: Tỷ lệ truyền dữ liệu thấp ở đây có nghĩa là: "Tỷ lệ" mà Ta truyền " dữ liệu" thấp. Dễ hiểu thì là set up một cái băng thông riêng ra nhưng mà thi thoảng mới truyền ở chỗ đó => rất phí
C đúng vì truyền có tí mà set up lâu bỏ búa ra
D đúng vì như nó nói
E sai vì khi đã set up xong, trễ khi chuyển mạch sẽ thấp, (setup mọi thứ chuẩn chỉ thì sẽ khó trễ chuyển mạch)
37. B + F
38. D + F
39. B
40. 646 (Mỗi mảnh tin trừ cái cuối phải là 856 byte)