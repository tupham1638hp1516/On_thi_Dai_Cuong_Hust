1. Phân biệt rõ: Tầng (Layer) vs Thiết bị (Device)
Đúng như ông nghĩ, mọi gói tin khi đi trên mạng đều phải có đủ các tầng (từ tầng 1 đến tầng 7) để hoạt động được. Tuy nhiên, điểm khác biệt nằm ở chỗ: Thiết bị đó "thông minh" đến tầng nào?
•	Máy tính của ông (Host): Có đủ cả "lòng mề" từ tầng 1 đến tầng 7. Nó hiểu từ sợi dây cáp (L1) cho đến cái giao diện Chrome ông đang dùng (L7).
•	Switch (Thiết bị tầng 2): Nó là một thiết bị "kém thông minh" hơn máy tính. Khi một gói tin bay qua, nó chỉ đọc cái nhãn ở Tầng 2 (Địa chỉ MAC) rồi đưa ra quyết định chuyển tiếp. Nó hoàn toàn không quan tâm bên trong gói tin đó ghi địa chỉ IP là gì.
•	Router (Thiết bị tầng 3): Nó thông minh hơn Switch. Nó biết bóc cái nhãn MAC ra để đọc nhãn ở Tầng 3 (Địa chỉ IP). Dựa vào IP, nó biết gói tin này cần đi sang "xóm" khác hay mạng khác.
________________________________________
2. Tại sao một cái là LAN, một cái là "kết nối nhiều mạng"?
Ông hãy tưởng tượng cấu trúc mạng giống như hệ thống địa chỉ bưu điện trong slide trang 14 của ông:
Mạng LAN (Căn chung cư)
•	Trong một mạng LAN, tất cả các máy tính dùng chung một "đường hành lang".
•	Vì ở gần nhau, chúng ta chỉ cần gọi tên nhau (địa chỉ MAC) là nghe thấy.
•	Switch giống như cái Thang máy: Nhiệm vụ của nó là đưa ông từ tầng 1 lên tầng 10 trong cùng tòa nhà. Nó không cần biết số CMND (IP) của ông, nó chỉ cần biết ông muốn vào phòng nào (MAC).
Liên mạng - Internet (Hệ thống giao thông thành phố)
•	Internet thực chất là "Mạng của các mạng" (Network of networks). Nó gồm hàng tỷ cái mạng LAN nhỏ kết nối lại với nhau qua các hệ tự trị (AS).
•	Router giống như cái Bưu cục thành phố: Khi ông gửi thư từ Hà Nội vào Sài Gòn, cái thang máy (Switch) không thể giúp ông được. Ông phải mang thư ra bưu cục.
•	Bác bưu tá (Router) sẽ nhìn vào địa chỉ: "À, thư này gửi đến Quận 1, Sài Gòn" (Địa chỉ IP) để tìm tuyến đường tốt nhất chuyển đi.
________________________________________
3. "Mối quan hệ cộng sinh" trong thực tế
Ông không bao giờ phải chọn "Hoặc LAN hoặc WAN". Trong thực tế, chúng luôn lồng vào nhau:
1.	Trong nhà ông (LAN): Các máy tính nối với nhau qua Switch (hoặc bộ phát WiFi). Chúng nói chuyện bằng tầng 2 (MAC).
2.	Bước ra ngoài (Internet): Khi ông muốn vào Google, gói tin của ông phải đi qua Cổng mặc định (Default Gateway) - chính là cái Router nhà ông.
3.	Lúc này, Router sẽ "đóng gói" cái thư của ông vào một con tàu lớn hơn để vượt đại dương sang server của Google.
________________________________________
✅ Chốt lại cho ông dễ nhớ:
•	Tầng 2 (Data Link): Giải quyết chuyện "Hàng xóm láng giềng" trong một mạng LAN.
•	Tầng 3 (Network): Giải quyết chuyện "Đi liên tỉnh, xuyên quốc gia" giữa các mạng LAN khác nhau.

**********************************************************************************


Bước 1: Thành phố mạng (Mạng và Nút mạng)
Đầu tiên, ta tưởng tượng mạng Internet là một Đất nước khổng lồ.

Mạng (Network): Chính là các Khu phố. Mỗi khu phố có một ranh giới rõ ràng.

Nút mạng (Node/Host): Chính là các Ngôi nhà nằm bên trong khu phố đó. (Nhà có thể là PC, điện thoại, hoặc tủ lạnh thông minh).

👉 Mục tiêu của chúng ta là làm sao để bưu tá đưa thư đến đúng Ngôi nhà nằm trong đúng Khu phố.

Bước 2: Tấm thẻ địa chỉ (Địa chỉ IP)
Để bưu tá tìm được nhà, mỗi ngôi nhà phải có một tấm biển ghi số, gọi là Địa chỉ IP (ví dụ: 192.168.1.15).

Nhưng bưu tá nhìn vào dãy số đó, làm sao biết đoạn nào là tên Khu phố, đoạn nào là Số nhà?
Nên người ta quy ước, địa chỉ IP luôn bị cắt làm 2 phần:

Phần đầu là Họ (Tên Khu phố - Network ID)

Phần sau là Tên (Số nhà - Host ID)

Bước 3: Thời "Đồ đá" - Chia lô cứng nhắc (Phân lớp A, B, C)
Ngày xửa ngày xưa, người ta không có công cụ cắt đất linh hoạt, nên họ tạo ra 3 cái khuôn cắt cố định, gọi là các Lớp (Class):

Lớp A (Khu phố Khổng Lồ): Dành cho các đại gia. Họ lấy 1 số đầu làm Khu phố, 3 số sau làm Số nhà. Cứ nhìn thấy biển số bắt đầu từ 0 đến 127 là biết ngay nó thuộc Khu phố khổng lồ này.

Lớp B (Khu phố Tầm trung): Lấy 2 số đầu làm Khu, 2 số sau làm Nhà. Dấu hiệu nhận biết là số đầu từ 128 đến 191.

Lớp C (Khu phố Nhỏ): Dành cho dân thường. Họ lấy 3 số đầu làm Khu, chỉ có 1 số cuối cùng làm nhà. Dấu hiệu nhận biết là số đầu từ 192 đến 223.

👉 Nhược điểm: Kiểu chia này rất cứng nhắc. Ví dụ ông chỉ có 300 người, dùng Lớp C (chứa được 254 nhà) thì thiếu, mà dùng lớp B (chứa được 65.500 nhà) thì thừa cả đống đất bỏ hoang, rất lãng phí!

Bước 4: Thời Hiện Đại - Hàng rào di động (Mặt nạ mạng / CIDR)
Để giải quyết sự lãng phí trên, người ta phát minh ra "Cái hàng rào" (Subnet Mask hoặc CIDR).

Bây giờ, địa chỉ không còn đứng trơ trọi nữa mà luôn đi kèm một cái vạch kẻ gạch chéo. Ví dụ: 192.168.1.15 /28.

Cái /28 này chính là cái hàng rào. Nó bảo bưu tá rằng: "Hãy đếm đúng 28 bước từ trái sang phải, cắm hàng rào ở đó. Toàn bộ phần trước rào là Tên Khu phố, phần sau rào là Số nhà!"

Nhờ cái rào này, ông có thể chia lô đất to nhỏ tùy ý, cực kỳ tiết kiệm và vừa vặn.

Bước 5: Những ngôi nhà "Cấm vào" (Địa chỉ không gán được)
1. "Cổng làng" (Địa chỉ mạng - Network Address)
Đây là địa chỉ dùng để đặt tên cho cả khu phố.

Dấu hiệu: Khi ông đổi phần Tên (Số nhà/Host ID) sang nhị phân, tất cả các số đều là số 0.

Tại sao cấm: Vì nó là cái tên chung. Nếu ông gán cho một máy, bưu tá sẽ không biết là ông đang gọi cái máy đó hay đang gọi cả khu phố.

Ví dụ: 192.168.1.0/24 (8 bit cuối toàn là 0).

2. "Loa phường" (Địa chỉ quảng bá - Broadcast Address)
Đây là địa chỉ dùng để gửi tin nhắn cho tất cả mọi người trong khu.

Dấu hiệu: Khi ông đổi phần Tên (Host ID) sang nhị phân, tất cả các số đều là số 1.

Tại sao cấm: Gửi thư vào đây là tất cả máy trong mạng đều nhận được. Nếu gán cho 1 máy, hệ thống sẽ bị loạn "thông tin cá nhân" và "thông tin công cộng".

Ví dụ: 192.168.1.255/24 (8 bit cuối toàn là 1).

3. "Gương soi" (Địa chỉ Loopback)
Đây là địa chỉ để máy tính tự nói chuyện với chính nó (tự kiểm tra phần cứng/phần mềm của mình).

Dấu hiệu: Bất kỳ địa chỉ nào bắt đầu bằng số 127. (Phổ biến nhất là 127.0.0.1).

Tại sao cấm: Vì đây là địa chỉ "nội tâm". Ông không thể dùng địa chỉ này để đi ra ngoài làm quen với các máy tính khác được.

4. "Họp nhóm" (Địa chỉ Multicast)
Đây là địa chỉ dành riêng cho một nhóm máy tính cùng nhận một luồng dữ liệu (như xem truyền hình trực tuyến).

Dấu hiệu: Các địa chỉ thuộc Lớp D (Số đầu tiên nằm trong khoảng 224 đến 239).

Tại sao cấm: Nó không dành cho cá nhân (Unicast). Nó dành cho hội nhóm.

5. "Phòng thí nghiệm" (Địa chỉ dự phòng/Lớp E)
Đây là các địa chỉ mà các nhà khoa học giữ lại để nghiên cứu, chưa cho phép dùng rộng rãi.

Dấu hiệu: Các địa chỉ bắt đầu từ 240 đến 255.

********************************************************************************

1. Kẻ lười biếng: NRZ (Cách ngây thơ nhất)
Đây là cách ông sẽ nghĩ ra đầu tiên khi chơi trò này:
•	Nhịp 1 (Tùng): Muốn gửi số 1 => Giơ cờ lên cao.
•	Nhịp 2 (Tùng): Muốn gửi số 0 => Hạ cờ xuống thấp.
Tưởng tượng thực tế:
Ông muốn gửi chuỗi 00000000. Ông hạ cờ xuống. Người bên kia đếm: Nhịp 1 thấy cờ hạ (số 0), Nhịp 2 thấy cờ hạ (số 0)... Đến nhịp thứ 5 thì người kia lóa mắt, chớp mắt một cái, rơi mất một nhịp trống. Thế là họ đếm thiếu mất một số 0.
👉 Tóm lại: NRZ quá êm đềm, không có sự thay đổi liên tục nên người nhận rất dễ bị "lệch nhịp" (mất đồng bộ) nếu có quá nhiều số 0 hoặc số 1 đứng cạnh nhau.
________________________________________
2. Kẻ tăng động: Manchester (Cách chống ngủ gật)
Vì NRZ hay làm người ta ngủ gật, Manchester đặt ra một luật thép: Bất chấp gửi số gì, CỨ ĐÚNG GIỮA NHỊP TRỐNG LÀ PHẢI VẪY CỜ MỘT CÁI!
Sự "thay đổi" chính là thông điệp:
•	Muốn gửi số 1: Đầu nhịp cờ ở dưới, đến đúng giữa nhịp giật mạnh cờ đưa LÊN TRÊN. (Luôn luôn đi LÊN).
•	Muốn gửi số 0: Đầu nhịp cờ ở trên, đến đúng giữa nhịp giật mạnh cờ kéo XUỐNG DƯỚI. (Luôn luôn đi XUỐNG).
Tưởng tượng thực tế:
Dù ông gửi 0000 hay 1111, thì cứ mỗi một giây người bên kia đều thấy ông vẫy cờ giật lên hoặc giật xuống. Mắt họ cứ nhìn theo lá cờ là họ tự đếm được nhịp thời gian mà không cần nghe tiếng trống nữa.
👉 Tóm lại: Rất an toàn, cực kỳ đồng bộ. Nhưng... thằng vẫy cờ vã mồ hôi hột (trong mạng gọi là Tốn gấp đôi băng thông) vì gửi 1 bit mà phải làm tới 2 động tác.
________________________________________
3. Kẻ khôn ngoan: Bipolar AMI (Cách đi hai chân)
Thấy Manchester mệt quá, AMI nghĩ ra một cách thông minh hơn, sử dụng hai lá cờ Xanh và Đỏ.
Nó chia làm 2 trường hợp rất nhàn:
•	Muốn gửi số 0: Đứng im, giấu cờ đi (Mức 0). Rất tiết kiệm sức!
•	Muốn gửi số 1: Giơ cờ lên. Nhưng luật là phải luân phiên màu cờ giống như người đi hai chân:
o	Thấy số 1 đầu tiên: Giơ cờ Xanh (+).
o	Thấy số 1 tiếp theo: Bắt buộc phải giơ cờ Đỏ (-).
o	Thấy số 1 tiếp nữa: Lại quay về cờ Xanh (+).
Tưởng tượng thực tế:
Nếu ông gửi chuỗi 11111, người bên kia sẽ thấy cờ Xanh - Đỏ - Xanh - Đỏ liên tục. Sự thay đổi màu sắc này giúp họ tỉnh ngủ và đếm nhịp cực chuẩn mà ông lại không bị mệt như thằng Manchester.
👉 Tóm lại: Cứ thấy đồ thị nằm im ru ở vạch số 0 thì đó là bit 0. Cứ thấy nó nhảy chồm chồm lúc trên lúc dưới, thì mỗi cú nhảy đó là một bit 1.

****************************************************************************************
1. Bản chất cốt lõi của RTT (Cái bạn đã rút ra)
RTT không chỉ là "khoảng cách tín hiệu chạy trên dây". RTT là tổng thời gian đo từ lúc máy nguồn bắt đầu đẩy bit ĐẦU TIÊN của gói tin đi, cho đến khi máy nguồn nhận lại trọn vẹn bit CUỐI CÙNG của gói tin phản hồi (ACK). Trong suốt quãng đường đi và về đó, gói tin phải dừng lại, xử lý, chờ đợi, và bất cứ một hành động nhỏ nào tốn thời gian cũng đều bị cộng dồn hết vào RTT.

2. Bốn loại "kiếp nạn" tốn thời gian trên đường đi (Cái tôi giải thích)
Tại nguồn, tại đích, và tại mỗi trạm trung chuyển (Router) mà gói tin đi qua, nó đều phải chịu 4 loại độ trễ (Delay) sau:

Trễ lan truyền (Propagation Delay): Do Khoảng cách vật lý. Tín hiệu (quang/điện/vô tuyến) cần thời gian để bay từ điểm A đến điểm B. (Giống như thời gian xe chạy trên đường).

Trễ truyền tải (Transmission Delay): Do Băng thông và Kích thước gói tin. Là thời gian cần thiết để thiết bị đẩy "TOÀN BỘ" các bit của gói tin đó vào đường truyền cáp. (Giống như thời gian xả nước qua một đường ống to hay nhỏ).

Trễ hàng đợi (Queuing Delay): Do Tải của mạng. Nếu mạng đang tắc nghẽn, router bận rộn, gói tin phải nằm chờ trong bộ nhớ đệm (buffer) tới lượt mình. Đây là yếu tố gây giật lag và làm RTT biến động mạnh nhất. (Giống như thời gian xếp hàng ở trạm thu phí).

Trễ xử lý (Processing Delay): Do Tốc độ phần cứng (CPU) của router hoặc nút đích. Là thời gian thiết bị tháo gói tin ra, đọc địa chỉ, kiểm tra lỗi bit, và quyết định đường đi tiếp theo. (Giống như thời gian nhân viên cầm vé lên xem và quét mã vạch).

3. Hiệu ứng nhân lên (Số Hop)
Mạng Internet dùng cơ chế "Lưu và chuyển tiếp" (Store-and-Forward). Nghĩa là không có con đường thẳng tắp nào từ máy bạn đến máy chủ. Gói tin phải đi qua nhiều Router (các nút chuyển tiếp).

Tại MỖI MỘT Router, toàn bộ 4 quá trình trên (nhận xong toàn bộ -> kiểm tra -> xếp hàng -> đẩy toàn bộ ra dây -> chạy trên dây) lại lặp lại từ đầu. Càng qua nhiều trạm, RTT càng lớn.

Tóm tắt bằng công thức:

RTT = [ (Lan truyền + Truyền tải + Hàng đợi + Xử lý) x Số trạm lượt ĐI ]

CỘNG VỚI > [ (Lan truyền + Truyền tải + Hàng đợi + Xử lý) x Số trạm lượt VỀ ]

1. Nhóm Mạng có dây (Ethernet - Chuẩn IEEE 802.3)

Ethernet (Tiêu chuẩn/Cổ điển): 10 Mbps

Fast Ethernet (Ethernet Tốc độ cao): 100 Mbps

Gigabit Ethernet: 1 Gbps (hoặc 1000 Mbps)

10-Gigabit Ethernet: 10 Gbps

100-Gigabit Ethernet: 100 Gbps

2. Nhóm Mạng không dây (Wi-Fi - Chuẩn IEEE 802.11)

Chuẩn 802.11b: 11 Mbps (Thế hệ Wi-Fi đời đầu)

Chuẩn 802.11a và 802.11g: 54 Mbps (Con số 54 Mbps bạn thấy ở câu trước chính là chuẩn này!)

Chuẩn 802.11n (Wi-Fi 4): Tối đa khoảng 600 Mbps

Chuẩn 802.11ac (Wi-Fi 5): Xấp xỉ 6.9 Gbps (lý thuyết)

Chuẩn 802.11ax (Wi-Fi 6): Xấp xỉ 9.6 Gbps (lý thuyết)

3. Nhóm Viễn thông & Mạng diện rộng (WAN)

Modem quay số (Dial-up): 56 Kbps (Cực kỳ chậm, đơn vị chỉ là Kilo-bit)

Kênh thuê riêng T1 (Chuẩn Mỹ/Nhật): 1.544 Mbps

Kênh thuê riêng E1 (Chuẩn Châu Âu/Việt Nam hay dùng): 2.048 Mbps

***********************************************************************************************

Mô tả quy trình Đóng gói (Encapsulation) và Mở gói (Decapsulation) dữ liệu giữa hai máy tính thông qua mô hình OSI 7 tầng.

Bạn có thể hình dung nó giống như quy trình đóng một món quà vào nhiều lớp hộp chồng lên nhau trước khi gửi đi:

1. Phía gửi (Bên trái - Encapsulation): Mũi tên đi xuống
Dữ liệu đi từ tầng cao nhất xuống tầng thấp nhất, mỗi tầng sẽ "dán" thêm một lớp nhãn điều khiển:

Tầng Application, Presentation, Session: Xuất phát điểm là khối dữ liệu gốc, được gọi chung là Data.

Tầng Transport: Dán thêm một lớp TCP Header vào đầu khối Data. Đơn vị dữ liệu lúc này gọi là Segment (Đoạn dữ liệu).

Tầng Network: Tiếp tục bọc lớp Segment đó vào một lớp vỏ lớn hơn và dán thêm IP Header (chứa địa chỉ IP). Đơn vị dữ liệu lúc này gọi là Packet (Gói tin).

Tầng Data Link: Bao bọc Packet bằng hai đầu: phía trước là Frame Header (chứa địa chỉ MAC) và phía sau là Frame Trailer (chứa mã kiểm lỗi CRC/FCS). Đơn vị dữ liệu lúc này gọi là Frame (Khung tin).

Tầng Physical: Chuyển toàn bộ Frame thành một chuỗi các ký hiệu Bits (010100...) để chạy trên dây cáp hoặc sóng Wi-Fi.

2. Phía nhận (Bên phải - Decapsulation): Mũi tên đi lên
Dữ liệu đi từ tầng thấp lên tầng cao, máy nhận thực hiện quy trình "bóc vỏ" ngược lại:

Tầng Physical: Nhận các luồng điện/quang và tập hợp lại thành các Bits.

Tầng Data Link: Bóc lớp vỏ Header/Trailer để lấy ra Packet bên trong (sau khi đã kiểm tra CRC ở Trailer).

Tầng Network: Bóc tiếp lớp IP Header để lấy ra Segment.

Tầng Transport: Bóc lớp TCP Header để lấy lại khối Data ban đầu.

Các tầng trên: Tiếp nhận dữ liệu sạch để hiển thị lên ứng dụng cho người dùng.

******************************************************************************

Trong mạng máy tính, Hop Count (Số bước nhảy) là đơn vị đo khoảng cách giữa các thiết bị dựa trên số lượng Router mà gói tin phải đi qua để đến được đích.

Để dễ hình dung, bạn hãy coi mỗi Router giống như một "trạm trung chuyển" trên đường đi.

1. Cách tính Hop Count
Hop: Mỗi khi một gói tin đi qua một Router, số bước nhảy sẽ tăng lên 1.

Ví dụ: Nếu gói tin đi từ Máy A qua Router 1, đến Router 2 rồi mới tới Máy B:

Khoảng cách từ Máy A đến Máy B được tính là 2 hops.

2. Vai trò của Hop Count trong định tuyến (RIP)
Giao thức RIP sử dụng Hop Count làm Metric (thước đo) để chọn đường đi tốt nhất:

Nguyên tắc: Đường nào có ít Hop Count hơn, RIP sẽ coi đó là đường ngắn hơn và ưu tiên gửi dữ liệu qua đó.

Hạn chế của RIP: Nó chỉ quan tâm đến "số trạm", không quan tâm đến "tốc độ".

Ví dụ: Một đường đi qua 2 Router nhưng băng thông cực thấp (vài Kbps) vẫn được RIP ưu tiên hơn một đường đi qua 3 Router nhưng có băng thông cực cao (vài Gbps).

3. Những con số "tử thần" cần nhớ
Trong giao thức RIP, có hai quy tắc về con số mà bạn bắt buộc phải nhớ để làm bài trắc nghiệm:

Tối đa 15 hops: Một gói tin chỉ được phép đi qua tối đa 15 Router trung gian.

Số 16 (Infinite): Nếu Hop Count đạt đến mức 16, RIP sẽ coi như đích đến đó là không thể tới được (Unreachable) và sẽ hủy gói tin. Đây là cơ chế để ngăn chặn việc gói tin chạy vòng quanh mạng vô tận khi có lỗi định tuyến (Routing Loop).

Tóm lại:

1 Router = 1 Hop.

Càng ít Hop = Đường càng ngắn (theo logic của RIP).

Max 15 Hops, đến số 16 là vứt gói tin.

********************************************************************************************
OSPF là gì?
OSPF (Open Shortest Path First) là một giao thức định tuyến thuộc nhóm Link-State (Trạng thái liên kết). Nếu giao thức RIP chúng ta vừa học giống như việc bạn đi đường và hỏi thăm người dân xung quanh (Distance-Vector), thì OSPF giống như việc mỗi Router đều sở hữu một bản đồ GPS toàn diện của cả mạng lưới.
Đặc điểm cốt lõi của OSPF:
•	Xây dựng bản đồ (Link-State Database): Thay vì chỉ biết hướng đi và số bước nhảy như RIP, mỗi Router OSPF sẽ gửi các bản tin LSA (Link State Advertisement) để thông báo cho toàn mạng biết: "Tôi đang kết nối với ai và tốc độ đường truyền đó là bao nhiêu".
•	Thuật toán Dijkstra: Khi đã có bản đồ trong tay, Router sử dụng thuật toán Dijkstra (Shortest Path First - SPF) để tự tính toán đường đi "rẻ" nhất (ngắn nhất về mặt chi phí) từ nó đến mọi điểm trong mạng.
•	Hội tụ nhanh: Khi có một đường link bị đứt, OSPF cập nhật thông tin gần như ngay lập tức cho toàn mạng, nhanh hơn nhiều so với việc chờ đợi cập nhật định kỳ của RIP.
________________________________________
Tại sao lại có công thức Cost = Reference Bandwith / Interface bandwith
Trong kỹ thuật mạng, chúng ta luôn muốn dữ liệu đi qua những con đường nhanh hơn (băng thông lớn hơn). Để máy tính hiểu được điều này, OSPF chuyển đổi "tốc độ" thành một con số gọi là Cost (Chi phí).
1. Nguyên lý tỉ lệ nghịch
Công thức này được thiết kế dựa trên logic: Tốc độ càng cao thì cái giá phải trả (Cost) càng rẻ.
•	Nếu đường truyền rất nhanh (ví dụ 100 Mbps), chi phí chỉ là 1.
•	Nếu đường truyền chậm (ví dụ 10 Mbps), chi phí tăng lên thành 10.
Router sẽ cộng dồn Cost của tất cả các đoạn mạng trên một lộ trình. Lộ trình nào có Tổng Cost thấp nhất sẽ được chọn làm đường chính thức.
2. Ý nghĩa của Reference Bandwidth (Băng thông tham chiếu)
Đây là một "thước đo" chung để tất cả các Router trong mạng có cùng một hệ quy chiếu khi tính toán.
•	Tại sao là 100 Mbps? Khi OSPF ra đời, 100 Mbps (Fast Ethernet) là đỉnh cao của công nghệ lúc bấy giờ, nên người ta chọn nó làm mốc chuẩn (10^8 bps).
•	Hạn chế: Vì mốc chuẩn chỉ là 100 Mbps, nên hiện nay các đường truyền 1 Gbps, 10 Gbps hay 100 Gbps đều bị tính ra Cost = 1 (do 100/1000 = 0.1, mà chi phí tối thiểu phải là 1). Để giải quyết, các kỹ sư thường phải chỉnh lại reference-bandwidth lên mức 10^5 hoặc 10^6 trong thực tế.
Tóm lại:
•	OSPF là dùng bản đồ và thuật toán để tìm đường.
•	Công thức Cost dùng để biến "tốc độ vật lý" thành một "con số logic" để Router so sánh và ưu tiên những đường truyền tốc độ cao.
 
 ********
 1. Parity (Kiểm tra Chẵn lẻ): "Người đếm số"
Đây là cách đơn giản nhất, giống như bạn gửi một thùng táo và kèm theo một mảnh giấy ghi: "Số quả táo trong thùng là số CHẴN".
•	Cách làm: Bạn đếm số bit 1 trong dữ liệu. Nếu bạn chọn hệ "Chẵn" (Even Parity), mà dữ liệu có 3 bit 1, bạn thêm 1 bit 1 nữa vào cuối để tổng là 4 (số chẵn).
•	Khi hàng đến: Bên nhận mở thùng, đếm số táo.
o	Nếu thấy 3 quả (số lẻ) => "Biết ngay là có đứa ăn vụng hoặc rơi mất một quả rồi!" (Phát hiện lỗi).
•	Điểm yếu: Nếu dọc đường rơi mất 2 quả táo. Bên nhận đếm lại vẫn thấy là số chẵn => "À, vẫn chẵn, chắc là đủ!" => Bị lừa! (Không phát hiện được lỗi kép).
________________________________________
2. Checksum (Tổng kiểm tra): "Người cân khối lượng"
Thay vì đếm từng quả, giờ bạn chia táo vào các túi nhỏ và cân tổng khối lượng.
•	Cách làm: Bạn chia chuỗi bit dài thành các khúc bằng nhau (ví dụ mỗi khúc 8 bit hoặc 16 bit). Bạn cộng tất cả các khúc này lại thành một con số tổng (Checksum).
•	Khi hàng đến: Bên nhận cũng đem các khúc đó ra cộng lại y hệt.
o	Nếu kết quả cộng khác với con số bạn gửi kèm => Hàng lỗi.
•	Điểm yếu: Nếu một túi táo bị mất 1kg, nhưng túi khác lại bị nhét thêm 1kg đá vào. Tổng khối lượng không đổi => Bị lừa tiếp! (Lỗi triệt tiêu nhau).
________________________________________
3. CRC (Kiểm tra dư thừa vòng): "Máy quét mã vạch thần thánh"
Đây là "trùm cuối" và cũng là thứ bạn thấy khó nhằn nhất vì nó dùng toán học (phép chia đa thức). Hãy tưởng tượng nó như một cái Mã vạch (Barcode) cực kỳ thông minh.
•	Cách làm (Từ gốc): Thay vì cộng (phép cộng dễ bị đánh lừa), người ta dùng phép chia. Bạn lấy toàn bộ dữ liệu (một con số khổng lồ) chia cho một "con số bí mật" (Đa thức sinh). Cái số dư còn lại chính là mã CRC.
•	Tại sao nó mạnh? Phép chia nhị phân (XOR) rất nhạy cảm. Chỉ cần bạn đổi đúng 1 bit ở bất cứ đâu, số dư sẽ nhảy sang một con số hoàn toàn khác ngay lập tức. Nó gần như không thể bị "lừa" bởi các lỗi triệt tiêu như Checksum.
•	Khi hàng đến: Bên nhận lấy toàn bộ đống dữ liệu đó chia lại cho "con số bí mật" kia. Nếu số dư bằng đúng mã CRC bạn gửi => Hàng chuẩn 99.9999%.


