# MỤC LỤC CHI TIẾT
## Chương 1. Tổng quan về mạng máy tính
1.1. Cơ bản về mạng máy tính
1.2. Giao thức mạng (Protocol)
1.3. Định nghĩa mạng LAN/WAN và các khái niệm mở rộng
1.4. Hình trạng (Topology) vật lý
1.5. Các kỹ thuật chuyển mạch và tính độ trễ
1.6. Kiến trúc phân tầng và Các mô hình tham chiếu

## Chương 2. Tầng vật lý
2.1. Tổng quan tầng vật lý
2.2. Phương tiện truyền dẫn (Transmission Media)
2.3. Mã hóa và Điều chế (Encoding & Modulation)
2.4. Dồn kênh (Multiplexing / Multiple Access)
2.5. Các chuẩn cáp/ Ethernet và Các thông số đo lường đường truyền

## Chương 3. Tầng liên kết dữ liệu
3.1. Giới thiệu về tầng liên kết dữ liệu và Địa chỉ MAC
3.2. Điều khiển truy nhập đường truyền mạng đa truy nhập
3.3. Kiểm soát lỗi
3.4. Kiểm soát luồng
3.5. Mạng cục bộ (LAN) và Chuyển tiếp dữ liệu tầng 2

## Chương 4. Tầng liên mạng
4.1. Tổng quan về tầng liên mạng
4.2. Giao thức IPv4
4.3. Cơ chế phân mảnh gói tin
4.4. Định tuyến (Routing) và Chuyển tiếp gói tin IPv4

---

# CHƯƠNG 1. TỔNG QUAN VỀ MẠNG MÁY TÍNH

## 1.1. Cơ bản về mạng máy tính

**Mạng Internet "đơn giản":**
- Trạm làm việc: PC, mobile phone
- Đường truyền: Có dây, không dây
- Phần mềm sử dụng: PC web, phone voice chat, liên quân,…
- Thiết bị kết nối mạng: Switch, Internet connect box,…
- Đơn vị cung cấp kết nối Internet (ISP)
- Đám mây Internet

**Mạng Internet đầy đủ:**
- Internet: Hệ sinh thái toàn cầu, sản phẩm nhân tạo lớn nhất
- Mạng xương sống (backbone)
- Mạng ISP
- Mạng home/ office
- Trạm làm việc
- Phần mềm ứng dụng

## 1.2. Giao thức mạng (Protocol)
*(Giao thức là "luật chơi" chung của mạng. Khái niệm "đóng/mở gói" (Encapsulation) chính là cách dữ liệu di chuyển từ trên xuống dưới trong mô hình OSI (1.6). Sự phân biệt giữa TCP (tin cậy, có ACK, có kiểm soát luồng) và UDP (nhanh, bỏ qua lỗi) sẽ giải thích tại sao ở Tầng 2 (3.3) và Tầng 3 (4.2) người ta chỉ loại bỏ gói tin lỗi mà không thèm sửa (vì để dành việc sửa lỗi đó cho TCP ở Tầng 4). Cơ chế cửa sổ trượt (3.4) cũng chính là hiện thực hóa của "quy tắc kiểm soát luồng" được nhắc đến ở đây.)*

Khuôn dạng dữ liệu, thứ tự truyền nhận, quy tắc truyền thông.
1. **Khuôn dạng dữ liệu (Data Format) & Cơ chế đóng/mở gói:**
   Giao thức quy định rõ dữ liệu phải được tổ chức và cấu trúc như thế nào khi đi qua mỗi tầng. Đơn vị dữ liệu được đóng gói theo giao thức tại mỗi tầng được gọi chung là PDU (Protocol Data Unit).
   - **Quá trình Đóng gói (Encapsulation - Phía gửi):** Dữ liệu đi từ tầng cao xuống tầng thấp. Mỗi tầng dưới sẽ coi toàn bộ khối dữ liệu từ tầng trên chuyển xuống là phần "thân" (Payload) của nó, và tiến hành dán thêm một phần "tiêu đề" (Header) chứa thông tin định danh và điều khiển của riêng tầng mình vào. Khuôn dạng dữ liệu thay đổi qua từng tầng trong mô hình TCP/IP như sau:
     - Tầng Giao vận (Transport): Thêm TCP/UDP Header vào khối Data gốc để tạo thành khuôn dạng Segment (Đoạn).
     - Tầng Mạng (Network): Bọc Segment vào một vỏ lớn hơn và thêm IP Header (chứa IP nguồn/đích), tạo thành khuôn dạng Packet (Gói tin).
     - Tầng Liên kết (Data Link): Bao bọc Packet bằng hai đầu: phần Frame Header ở trước (chứa địa chỉ MAC) và Frame Trailer ở sau (chứa mã kiểm lỗi CRC), tạo thành khuôn dạng Frame (Khung tin).
   - **Quá trình Mở gói (Decapsulation - Phía nhận):** Khi nhận dữ liệu, quy trình đi ngược từ dưới lên trên. Tại đây, mỗi tầng sẽ chỉ bóc lớp vỏ Header thuộc phạm vi quản lý của giao thức tầng mình để đọc thông tin, sau đó chuyển phần Payload "sạch" lên cho tầng cao hơn xử lý.

2. **Quy tắc truyền thông (Communication Rules & Processing):**
   Giao thức quy định cách thức mỗi bên xử lý dữ liệu để luồng giao tiếp diễn ra trơn tru và đạt được mục đích của ứng dụng. Sự khác biệt về quy tắc được thể hiện rõ nhất qua hai giao thức tầng Giao vận:
   - **Giao thức TCP (Quy tắc chặt chẽ, tin cậy):** TCP quan tâm đến việc dữ liệu có đến đích an toàn không. Nó có quy tắc kiểm tra lỗi bit bằng Checksum, tự động phát lại dữ liệu khi bị hết hạn chờ (time-out) hoặc bị lỗi. Đồng thời, TCP có các bộ luật về kiểm soát luồng (đảm bảo bên gửi không đẩy dữ liệu làm tràn bộ nhớ đệm bên nhận thông qua việc cập nhật kích thước cửa sổ - Window size) và kiểm soát tắc nghẽn mạng (thông qua các giai đoạn khởi động chậm Slow Start, tránh tắc nghẽn và hồi phục nhanh).
   - **Giao thức UDP (Quy tắc tối giản, nhanh):** Ngược lại với TCP, giao thức UDP truyền dữ liệu liên tục mà không cần thiết lập liên kết trước, không sử dụng báo nhận (ACK), không kiểm soát luồng và cũng không phát lại dữ liệu nếu có lỗi. Nếu phát hiện lỗi trên gói tin UDP, phía nhận có thể đơn giản là loại bỏ hoặc hủy gói tin đó thay vì yêu cầu gửi lại.

3. **Thứ tự truyền nhận thông điệp (Transmission Order):**
   Giao thức mạng quy định trình tự thiết lập, trao đổi và ngắt kết nối giữa các máy tính.
   - **Thứ tự thiết lập và ngắt liên kết:** Trong TCP, hai bên không thể tự tiện gửi dữ liệu ngay. Máy tính phải truyền các thông điệp bắt tay (sử dụng cờ SYN) để thống nhất thông số. Khi truyền xong, giao thức yêu cầu trình tự kết thúc bằng cách sử dụng các gói tin được thiết lập cờ FIN để báo hiệu ngắt kết nối.
   - **Sắp xếp thứ tự dữ liệu (Sequencing):** Khi một tập tin lớn bị băm nhỏ thành nhiều gói tin để truyền đi, chúng có thể đến đích lộn xộn hoặc lặp lại. Giao thức TCP có trường Sequence Number để đánh số thứ tự, giúp máy nhận tự động sắp xếp lại các mảnh (fragments) hoặc phát hiện gói tin bị trùng lặp.
   - **Trình tự gửi - đáp:**
     - Đối với giao thức HTTP (Tầng ứng dụng), thứ tự luôn bắt buộc là Trình duyệt (Client) gửi các thông điệp yêu cầu (HTTP Request) như GET, POST trước, sau đó Máy chủ (Server) mới gửi phản hồi về (HTTP Response).
     - Đối với cơ chế ARQ dừng và chờ (Stop-and-Wait), thứ tự truyền nhận bị khóa cứng: Bên gửi chỉ được phép gửi một gói tin duy nhất, sau đó phải lập tức dừng lại để chờ gói tin xác nhận (ACK) từ phía nhận gửi về rồi mới được phép truyền gói tiếp theo.

## 1.3. Định nghĩa mạng LAN/WAN và các khái niệm mở rộng
*(LAN và WAN là 2 phạm vi mạng hoàn toàn đối lập nhưng phải cộng sinh. LAN dùng địa chỉ vật lý MAC (3.1) và hoạt động dựa trên cơ chế tự học của Switch (3.5). Ngược lại, WAN (mạng diện rộng) bắt buộc phải dùng địa chỉ lô-gic IPv4 (4.2) và Router (4.4) để tìm đường đi xa. Để một gói tin từ WAN (dùng IP) có thể giao chính xác cho một máy trong LAN (chỉ hiểu MAC), bắt buộc phải có sự can thiệp của giao thức ARP - đóng vai trò "thông dịch viên" giữa hai loại địa chỉ này.)*

1. **Mạng cục bộ (LAN - Local Area Network) và cơ chế hoạt động**
   - **Bản chất:** Mạng LAN là mạng kết nối các thiết bị trong một phạm vi địa lý nhỏ (như một căn hộ, tòa nhà, văn phòng). Nó giống như một "đường hành lang" dùng chung, nơi các thiết bị ở gần nhau chỉ cần gọi tên nhau là có thể truyền tin.
   - **Định danh và Giao thức:** Trong mạng LAN, các thiết bị giao tiếp với nhau chủ yếu ở tầng Liên kết dữ liệu (Layer 2) bằng địa chỉ vật lý MAC dài 48 bit. Các môi trường LAN phải sử dụng bộ quy tắc điều khiển truy cập đường truyền (để không bị đụng độ), chẳng hạn như CSMA/CD cho mạng LAN có dây (Ethernet) hoặc CSMA/CA cho mạng LAN không dây (WLAN / Wi-Fi).
   - **Thiết bị đặc trưng:** Thiết bị hoạt động trong mạng LAN bao gồm Máy tính cá nhân, Card mạng (NIC), Dây cáp, Hub, Bridge và đặc biệt là Switch (Bộ chuyển mạch). Switch được ví như một "bác bảo vệ" hay "cái thang máy" trong tòa nhà: Nó chỉ đọc nhãn địa chỉ MAC ở Tầng 2 để chuyển gói tin đến chính xác "căn phòng" đích mà hoàn toàn không quan tâm đến địa chỉ IP bên trong.
   - *Lưu ý:* Modem không phải là thiết bị dùng bên trong mạng LAN. Vai trò của nó là trung gian để kết nối mạng LAN nội bộ ra ngoài mạng Internet.

2. **Mạng diện rộng (WAN - Wide Area Network)**
   - **Bản chất:** Mạng WAN kết nối các mạng LAN ở các khu vực địa lý cách xa nhau. Mạng Internet thực chất là một mạng WAN khổng lồ, là "mạng của các mạng" (Network of networks) được ghép lại từ hàng tỷ mạng LAN nhỏ. Đường truyền vật lý của WAN thường sử dụng đường truyền điện thoại (phonelines) hoặc kênh liên kết điểm - điểm (Point-to-Point).
   - **Định danh và Giao thức:** WAN hoạt động ở tầng Mạng (Network Layer - Layer 3), định danh vị trí các thiết bị bằng địa chỉ IP.
   - **Thiết bị đặc trưng:** Router (Bộ định tuyến) là thiết bị chủ chốt của WAN. Khác với Switch chỉ loanh quanh nội bộ, Router giống như một "bưu cục thành phố" hay "bác bưu tá" tại ngã tư đường. Nó bóc lớp vỏ Tầng 2 ra để đọc địa chỉ IP ở Tầng 3 (xem gói tin thuộc "xóm" nào, mạng nào) và tiến hành định tuyến, tìm ra tuyến đường tốt nhất để chuyển tiếp gói tin đi liên tỉnh hoặc xuyên quốc gia.

3. **Mối quan hệ cộng sinh giữa LAN và WAN**
   Trong thực tế, người ta không chọn "hoặc LAN hoặc WAN" mà chúng luôn lồng ghép vào nhau:
   - **Chuyện nội bộ (LAN):** Khi thiết bị nói chuyện trong nhà, gói tin chỉ đi qua Switch và dùng địa chỉ MAC.
   - **Bước ra thế giới (WAN):** Nếu bạn muốn truy cập Google, cái thang máy (Switch) không thể giúp bạn đi xa được. Gói tin phải đi ra Cổng mặc định (Default Gateway) - chính là chiếc Router của nhà bạn. Tại đây, Router sẽ tiếp nhận và chuyển tiếp gói tin của bạn vượt đại dương ra mạng Internet.
   - **Cơ chế liên kết (Giao thức ARP):** Để một gói tin từ ngoài mạng (định vị bằng IP) có thể giao chính xác cho một máy tính trong mạng LAN (chỉ hiểu địa chỉ MAC), thiết bị trung gian cần một giao thức gọi là ARP (Address Resolution Protocol). ARP có nhiệm vụ tìm kiếm và phân giải địa chỉ MAC khi đã biết trước địa chỉ IP.

4. **Các khái niệm mở rộng liên quan**
   - **VLAN (Virtual LAN - Mạng LAN ảo):** Là công nghệ cho phép gom nhóm các máy tính về mặt logic (theo chức năng như phòng Kế toán, Kỹ thuật) thay vì vị trí cắm dây vật lý. VLAN giúp chia nhỏ "miền quảng bá" (Broadcast Domain), qua đó giảm lưu lượng rác, tăng hiệu suất và cách ly dữ liệu để bảo mật. Để hai thiết bị ở hai VLAN khác nhau nói chuyện được với nhau, bắt buộc phải dùng đến thiết bị Tầng 3 như Router (Inter-VLAN Routing).
   - **Hệ tự trị (AS - Autonomous System):** Nếu Internet là một thành phố khổng lồ thì AS chính là một tòa nhà hoặc một khu đô thị được quản lý riêng biệt (ví dụ: một trường đại học hoặc một nhà cung cấp dịch vụ mạng - ISP). Bên trong một AS, tất cả Router đều tuân theo một chính sách định tuyến chung và dùng giao thức định tuyến nội miền (như RIP, OSPF). Để kết nối các AS này lại với nhau thành WAN/Internet, người ta sử dụng giao thức định tuyến liên miền (điển hình là BGP). Số lượng các AS không bao giờ cố định mà liên tục thay đổi trên toàn cầu tùy theo sự phát triển của hạ tầng mạng.

## 1.4. Hình trạng (Topology) vật lý
*(Hình trạng vật lý không chỉ là cách cắm dây, nó quyết định trực tiếp đến loại cáp nào được sử dụng (2.2). Ví dụ, mạng hình sao (Star) luôn đi kèm với Switch/Hub làm trung tâm (3.5). Hình trạng Bus (chung đường truyền) là nguyên nhân sâu xa dẫn đến hiện tượng "đụng độ tín hiệu" - lý do mà Tầng liên kết dữ liệu bắt buộc phải sinh ra các thuật toán lắng nghe và tránh đụng độ như CSMA/CD hay CSMA/CA (3.2).)*

1. **Định nghĩa Topology vật lý**
   - **Bản chất:** Topology vật lý mô tả cách bố trí cáp kết nối thực tế giữa các nút mạng (thiết bị mạng) với nhau.
   - **Phân biệt với Topology logic:** Trong khi Topology vật lý thiên về cách đi dây cáp, thì Topology logic lại dựa trên cách thức truyền và luân chuyển tín hiệu (ví dụ: truyền điểm-điểm hay quảng bá).

2. **Các loại Hình trạng (Topology) vật lý phổ biến**
   Dựa vào cách kết nối cáp, có 4 loại hình trạng mạng cơ bản:
   - **Hình trục (Bus Topology):** Hoạt động dựa trên việc chia sẻ một đường truyền thông tin duy nhất. Trong mạng Bus, tất cả các thiết bị mạng đều kết nối chung vào một trục và cùng lắng nghe trên một môi trường truyền tải đó.
   - **Hình sao (Star Topology):** Gắn liền với sự xuất hiện của một thiết bị trung tâm đứng ở giữa. Bất cứ khi nào các máy tính kết nối tập trung qua một Switch (Bộ chuyển mạch) hoặc Hub (Bộ chia mạng), hệ thống đó đang được triển khai dưới dạng hình sao.
   - **Hình vòng (Ring Topology):** Các thiết bị được kết nối cáp nối tiếp nhau tạo thành một vòng tròn khép kín.
   - **Hình lưới (Mesh Topology):** Là tên gọi khác của một mạng có "kết nối đầy đủ" (fully connected). Các thiết bị trong mạng lưới sẽ được kết nối chằng chịt và trực tiếp với nhiều thiết bị khác, tạo ra độ dự phòng cao.

## 1.5. Các kỹ thuật chuyển mạch và tính độ trễ
*(Trong chuyển mạch gói, dữ liệu bị băm nhỏ, mỗi gói tự đi một đường (4.4), do đó sinh ra độ trễ hàng đợi (Queue Delay) rất biến động tại các Router. Để mạng không bị "sập" do trễ hàng đợi quá cao, TCP phải sử dụng "cửa sổ tắc nghẽn" (3.4) để điều tiết lượng gói tin bơm vào mạng. Hơn nữa, trễ truyền tải và trễ lan truyền trong phần này bị phụ thuộc trực tiếp vào Băng thông và Khoảng cách cáp vật lý (đã học ở 2.5).)*

1. **Chuyển mạch kênh (Circuit Switching)**
   - **Bản chất và cách hoạt động:** Cung cấp dịch vụ truyền thông theo mô hình hướng kết nối (connection-oriented). Trước khi có thể truyền bất kỳ dữ liệu nào, hai bên bắt buộc phải dành thời gian để thiết lập một kênh truyền vật lý xuyên suốt.
   - **Đặc điểm tài nguyên:** Tài nguyên của mỗi cuộc hội thoại (băng thông) được xác định ngay trong giai đoạn thiết lập kênh và được giữ nguyên/dành riêng (không đổi) trong suốt quá trình truyền dữ liệu. Kênh truyền này chỉ được giải phóng khi một trong hai bên chủ động ngắt liên kết.
   - **Ưu điểm:** Khi liên kết đã được thiết lập xong, trễ chuyển mạch trong quá trình truyền dữ liệu sẽ rất thấp.
   - **Nhược điểm:** Hiệu suất đường truyền thấp và lãng phí: Kỹ thuật này rất lãng phí nếu tỷ lệ truyền dữ liệu thấp (đã thiết lập một băng thông riêng nhưng thỉnh thoảng mới có dữ liệu truyền qua). Đồng thời, nó cũng kém hiệu quả khi lượng dữ liệu cần truyền quá nhỏ, vì thời gian bỏ ra để thiết lập và hủy liên kết lại chiếm quá nhiều. Thiếu linh hoạt: Trong quá trình truyền, nếu một thiết bị chuyển mạch trung gian bị lỗi, mạng bắt buộc phải bắt đầu lại toàn bộ quá trình thiết lập kênh truyền từ đầu.

2. **Chuyển mạch gói (Packet Switching)**
   - **Bản chất và cách hoạt động:** Dữ liệu không được gửi đi nguyên khối mà được băm nhỏ thành các gói tin (packet), mỗi gói tin bao gồm phần dữ liệu (payload) và phần tiêu đề (header). Các thiết bị trung gian thực hiện việc định tuyến dựa trên cơ chế "lưu và chuyển tiếp" (Store and forward).
   - **Đặc điểm tài nguyên:** Khác với chuyển mạch kênh, chuyển mạch gói không dành riêng đường truyền cho ai. Tài nguyên đường truyền được chia sẻ, nghĩa là các gói tin từ nhiều phiên truyền thông và các liên kết khác nhau có thể được truyền trên cùng một đường truyền vật lý một cách đồng thời.
   - **Sự di chuyển linh hoạt (Routing):** Các gói tin đi từ một nguồn đến cùng một đích không bắt buộc phải đi qua các chặng đường giống nhau. Tùy vào tình trạng mạng, mỗi gói tin có thể tự chọn một đường đi riêng, dẫn đến việc chúng có thể đến đích lộn xộn và không theo đúng thứ tự lúc gửi.
   - **Ưu điểm:** Hiệu năng cao: Không mất thời gian để thiết lập kênh truyền ban đầu, thời gian chuyển tiếp dữ liệu ngắn hơn và mang lại hiệu suất sử dụng đường truyền tổng thể cao hơn. Quản lý thông minh: Thiết bị mạng có thể thiết lập độ ưu tiên cho từng loại gói tin khi xử lý hàng đợi (ví dụ: ưu tiên gói dữ liệu video/thoại hơn gói tải file).
   - **Nhược điểm:** : Độ trễ không ổn định. Độ trễ trong mạng chuyển mạch gói bị phụ thuộc rất lớn vào tải trọng của mạng (network load). Nếu có quá nhiều gói tin cùng chọn đi vào một đường truyền, chúng sẽ bị kẹt lại tại hàng đợi của Router, gây ra tình trạng nghẽn mạng và tăng độ trễ.

3. **4 Loại trễ (Delays) tại một nút mạng**
   Khi một gói tin đi qua bất kỳ một thiết bị mạng nào, tổng độ trễ tại nút đó sẽ bằng tổng của 4 loại trễ:
   - **Trễ xử lý (Processing Delay - d_proc):** Bị chi phối bởi tốc độ phần cứng (CPU). Đây là thời gian thiết bị tháo dỡ gói tin ra, đọc địa chỉ, kiểm tra lỗi bit, và quyết định đường đi.
   - **Trễ hàng đợi (Queuing Delay - d_queue):** Bị chi phối bởi tải trọng của mạng. Là thời gian gói tin chờ trong bộ đệm (buffer) tới lượt mình xử lý. Đây là yếu tố cốt lõi gây ra giật lag và làm biến động độ trễ.
   - **Trễ truyền tải / Trễ truyền dẫn (Transmission Delay - d_trans):** Bị chi phối bởi Băng thông và Kích thước gói tin. Là thời gian để đẩy toàn bộ các bit của gói tin vào đường cáp.
   - **Trễ lan truyền (Propagation Delay - d_prop):** Bị chi phối bởi khoảng cách vật lý. Là thời gian để tín hiệu bay từ điểm A đến điểm B.

4. **RTT (Round Trip Time) và Hiệu ứng nhân lên qua các trạm (Hops)**
• Bản chất cốt lõi: Thông số RTT cho biết trễ 2 chiều giữa nút nguồn và nút đích. RTT không đơn thuần chỉ là "khoảng cách tín hiệu chạy trên dây", mà nó là tổng thời gian đo từ lúc máy nguồn bắt đầu đẩy bit ĐẦU TIÊN của gói tin đi, cho đến khi máy nguồn nhận lại trọn vẹn bit CUỐI CÙNG của gói tin xác nhận phản hồi (ACK). Bất cứ một hành động nhỏ nào tốn thời gian trên đường đi và về cũng đều được cộng dồn hết vào RTT.
•	Hiệu ứng nhân lên qua các trạm (Hop): Mạng Internet sử dụng cơ chế "Lưu và chuyển tiếp" (Store-and-Forward) nên không có con đường thẳng tắp nào nối từ máy bạn đến máy chủ. Gói tin bắt buộc phải đi qua nhiều Router trung gian.
•	Tại mỗi một Router, thiết bị phải đợi nhận xong toàn bộ gói tin, kiểm tra lỗi, xếp hàng, và đẩy ra dây truyền tiếp. Nghĩa là, toàn bộ 4 quá trình trễ ở phần 1 lại lặp lại từ đầu tại mỗi trạm trung chuyển. Càng đi qua nhiều trạm (nhiều Hops), RTT sẽ càng lớn.
> Tóm tắt lại thành công thức tổng quát của RTT: RTT = [ (Lan truyền + Truyền tải + Hàng đợi + Xử lý) x Số trạm lượt ĐI ] + [ (Lan truyền + Truyền tải + Hàng đợi + Xử lý) x Số trạm lượt VỀ ]


## 1.6. Kiến trúc phân tầng và Các mô hình tham chiếu
*(Liên kết với: Cấu trúc toàn bộ giáo trình (Chương 2, 3, 4) & Quá trình phân mảnh gói tin ở 4.3 - Tại sao: Mô hình OSI và TCP/IP là bộ xương sống của mạng máy tính, quyết định cách các chương sau được sắp xếp. Chương 2 tương ứng với Layer 1 (Physical), Chương 3 là Layer 2 (Data Link), và Chương 4 là Layer 3 (Network). Việc phân tách này giải thích tại sao Switch (Layer 2) xử lý nhanh hơn Router (Layer 3), vì Switch chỉ bóc vỏ gói tin đến lớp MAC rồi đẩy đi, trong khi Router phải bóc sâu hơn để đọc IP và thậm chí phải cắt nhỏ gói tin (phân mảnh) nếu vượt quá kích thước MTU (4.3).)*

1. **Nguyên lý phân tầng**
   - Giúp dễ thiết kế, tái sử dụng, nâng cấp. Tổ chức dữ liệu, định danh, tìm đường, kiểm soát lỗi và lưu lượng.
   - **Điểm truy cập dịch vụ (Service Access Point - SAP):** Là giao diện kết nối giữa hai tầng liền kề. SAP thể hiện tính trong suốt của kiến trúc phân tầng: tầng trên chỉ sử dụng dịch vụ của tầng dưới cung cấp mà không cần biết cách thức thực hiện.
   - **Truyền thông hướng liên kết (ví dụ: TCP) vs Hướng không liên kết (ví dụ: UDP).**
   - **Đơn vị dữ liệu giao thức (PDU)** gồm Header và Payload. Giao tiếp giữa các tầng ngang hàng và các tầng kề nhau thông qua SDU (chính là PDU của tầng trên giao xuống).

2. **Mô hình OSI và TCP/IP**
   - Mô hình OSI/ISO: 7 tầng (Application, Presentation, Session, Transport, Network, Data link, Physical).
   - Mô hình TCP/IP: 5 tầng (Application, Transport, Network, Datalink, Physical). Hạn chế của mô hình TCP/IP là vấn đề kích thước header, hoạt động trên mạng không dây và bảo mật.

3. **Định danh và Thiết bị trong TCP/IP**
   - **Layer 1 (Physical):** Hub, Repeater, Dây cáp, Modem. Chỉ khuếch đại điện/quang chứ không hiểu bit.
   - **Layer 2 (Data Link):** Switch, Bridge, NIC. Làm việc với địa chỉ MAC. Tính trễ xử lý của Switch nhỏ hơn Router vì nó chỉ bóc vỏ đến lớp 2.
   - **Layer 3 (Network):** Router, Layer-3 Switch. Làm việc với địa chỉ IP. Chức năng "định tuyến" (Routing) và phân mảnh.
   - **Layer 4 (Transport):** Làm việc với Port (Cổng).

---

# CHƯƠNG 2. TẦNG VẬT LÝ

## 2.1. Tổng quan tầng vật lý
*(Liên kết với: Kiến trúc phân tầng ở 1.6, Giới thiệu tầng Liên kết dữ liệu ở 3.1 & Chuyển tiếp Tầng 2 ở 3.5 - Tại sao: Tầng vật lý nằm ở "đáy" mô hình mạng, là "culi" vận chuyển tín hiệu điện/quang. Nó không hiểu ý nghĩa của bit dữ liệu, chỉ nhận lệnh truyền từ Tầng 2 (Liên kết dữ liệu) ở trên thả xuống. Sự ổn định của tín hiệu ở tầng này quyết định việc Frame dữ liệu có bị hỏng khi đi đến Switch ở Tầng 2 hay không, từ đó ảnh hưởng đến việc Switch có phải vứt bỏ gói tin khi tính toán mã kiểm lỗi CRC (3.5).)*

Chức năng cốt lõi của tầng vật lý là tiếp nhận các khối dữ liệu (Frame) từ tầng Liên kết dữ liệu, chuyển đổi các chuỗi dữ liệu bit (0 và 1) thành các tín hiệu vật lý (điện, quang, vô tuyến) để đẩy lên phương tiện truyền dẫn. Ở đầu nhận, thu các luồng tín hiệu này và tập hợp lại thành các bit thuần túy trước khi đẩy ngược lên.

## 2.2. Phương tiện truyền dẫn (Transmission Media)
*(Liên kết với: Các chuẩn cáp Ethernet ở 2.5, Độ suy hao ở 2.5 & Các giao thức đa truy nhập ở 3.2 - Tại sao: Môi trường truyền (Cáp đồng, Cáp quang, Vô tuyến) sở hữu các đặc tính vật lý và độ suy hao (2.5) khác nhau. Chính vì môi trường vô tuyến rất nhiễu và dễ đụng độ, người ta bắt buộc phải dùng chế độ bán song công (Half-duplex) và kỹ thuật CSMA/CA (tránh đụng độ) thay vì CSMA/CD (phát hiện đụng độ) dùng trong cáp đồng (3.2). Đồng thời, mỗi loại cáp sẽ tương ứng với một tiêu chuẩn Ethernet riêng biệt như 100BASE-T hay 100BASE-FX (2.5).)*

1. **Môi trường Hữu tuyến (Có dây):**
   Môi trường dành riêng, mạng có thể hoạt động ở chế độ song công toàn phần (Full-duplex).
   - **Cáp xoắn đôi:** Rẻ tiền, đơn giản nhưng chống nhiễu kém.
   - **Cáp đồng trục.**
   - **Cáp quang:** Cho phép tốc độ truyền cao nhất và không bị ảnh hưởng bởi sóng điện từ, nhưng đắt đỏ và dễ gãy.
   - *Sự méo dạng xung trong cáp quang:* Cáp quang Single-mode dùng một lõi thật nhỏ để tia sáng đi thẳng, ít bị méo dạng nhất. Cáp Multimode stepped index dễ bị méo dạng nhất do tia sáng truyền zic-zac (tán xạ). Cáp Multimode graded index làm chiết suất lõi giảm dần để khắc phục sự chênh lệch thời gian.

2. **Môi trường Vô tuyến (Không dây):**
   Dùng chung môi trường không gian, sóng dễ bị ảnh hưởng bởi môi trường (tán xạ khi va cản, suy hao khi xuyên tường, nhiễu giao thoa).
   - Các thiết bị thường hoạt động ở chế độ bán song công (Half-duplex) để tránh đụng độ.
   - Các sóng sử dụng: Radio, hồng ngoại, ánh sáng, vi ba.

## 2.3. Mã hóa và Điều chế (Encoding & Modulation)
*(Liên kết với: Thông số đo lường BER ở 2.5, Tốc độ Baud/Bit ở 2.5 & Kiểm soát lỗi CRC ở 3.3 - Tại sao: Tín hiệu điện chạy trên cáp rất dễ bị "ngủ gật" (mất đồng bộ) hoặc bị lệch trục (Baseline wander - 2.5) nếu truyền chuỗi bit toàn 0 hoặc 1. Việc dùng mã Manchester hay Bipolar giúp tín hiệu tự tạo nhịp giật để đồng bộ cực kỳ chuẩn xác. Mã hóa càng tốt thì tỷ lệ lỗi bit (BER) càng giảm, từ đó giảm đáng kể gánh nặng cho Tầng 2 phía trên (phải dùng mã CRC để tính toán và vứt bỏ các khung tin bị sai lệch bit). Ngoài ra, loại mã hóa sẽ quyết định mối quan hệ giữa tốc độ Baud và Bit rate (2.5).)*

Để loại bỏ "thành phần một chiều" (DC Component) và giúp tự đồng bộ nhịp điệu.

1. **Mã hóa đường truyền (Digital-to-Digital)**
   - **Nhóm mã hóa NRZ (Non-Return to Zero):**
     - *NRZ-L (NRZ-Level):* Bit 1 mức cao, bit 0 mức thấp. Dễ mất đồng bộ khi gặp chuỗi toàn 1 hoặc toàn 0 dài.
     - *NRZ-I (NRZ-Invert / NRZ Vi sai):* Bit 1 tạo chuyển mức ở đầu chu kỳ, bit 0 giữ nguyên mức. Khắc phục được chuỗi toàn 1 nhưng vẫn mất đồng bộ với chuỗi toàn 0.
   - **Nhóm Multilevel Binary (Bipolar-AMI):** Dùng 3 mức điện áp. Bit 0 là 0V, bit 1 luân phiên đảo chiều (+/-). Tự đồng bộ tốt, không có thành phần một chiều, tối ưu băng thông.
   - **Nhóm Biphase (Manchester & Differential Manchester):**
     - *Manchester (Không vi sai):* Có sự chuyển mức ở giữa chu kỳ bit (0 là sườn âm, 1 là sườn dương). Tự đồng bộ đồng hồ tuyệt vời, tuy nhiên Baud rate phải gấp đôi Bit rate, tốn băng thông (Ethernet thường dùng).
     - *Differential Manchester:* Giữ cú giật ở giữa bit để đồng bộ. Nếu đầu chu kỳ có chuyển mức là bit 0, nối tiếp ngang sang là bit 1.
   - **Mã On-Off Keying (OOK)** dùng trong cáp quang.

2. **Điều chế (Digital-to-Analog)**
   - Kỹ thuật chuyển dữ liệu số thành tín hiệu dạng sóng liên tục: Khóa dịch biên độ (ASK), Khóa dịch pha (PSK) và Khóa dịch tần số (FSK). QAM kết hợp biên độ và pha. Điều chế mã xung (PCM) dùng lượng tử hóa để chuyển từ giọng nói sang bit số.

## 2.4. Dồn kênh (Multiplexing / Multiple Access)
*(Liên kết với: Nhóm phương pháp phân chia kênh ở 3.2 & Chuyển mạch kênh ở 1.5 - Tại sao: Dồn kênh bản chất là kỹ thuật "chia bánh" tài nguyên ở lớp vật lý (chia thời gian, chia tần số, chia mã). Ở Tầng 2 (3.2), nó được ứng dụng trực tiếp thành các phương pháp kiểm soát truy cập (TDMA, FDMA) nhằm loại bỏ hoàn toàn sự đụng độ trong môi trường tải trọng cao. Khái niệm này cũng gắn liền với cơ chế Chuyển mạch kênh (1.5), nơi mà băng thông đường truyền được chia nhỏ và dành riêng cho từng cuộc gọi điện thoại mà không ai được lấn chiếm.)*

- **TDMA (Phân chia theo thời gian):** Đường truyền chia thành khe thời gian; thiết bị chờ đến lượt mới được truyền.
- **FDMA (Phân chia theo tần số):** Dải tần số băm nhỏ thành các kênh riêng biệt, truyền đồng thời.
- **CDMA (Phân chia theo mã):** Mạng di động 3G/4G, truyền cùng lúc cùng tần số nhưng dùng mã toán học đặc trưng để lọc.

## 2.5. Các chuẩn cáp/ Ethernet và Các thông số đo lường đường truyền
*(Liên kết với: Trễ truyền tải ở 1.5, Phân mảnh MTU ở 4.3 & CSMA/CD ở 3.2 - Tại sao: Băng thông (Bandwidth) quyết định "ống nước to hay nhỏ", từ đó ảnh hưởng trực tiếp đến độ trễ truyền tải (1.5). Tỷ lệ lỗi bit (BER) càng cao (do cáp dỏm hoặc khoảng cách xa) thì xác suất hỏng cả gói tin càng lớn. Do đó, BER buộc Tầng Mạng (4.3) phải tính toán một kích thước gói tin tối đa (MTU) sao cho vừa vặn: to quá thì dễ dính lỗi BER và phải gửi lại từ đầu, nhỏ quá thì tỷ lệ Header lại chiếm phần lớn gây lãng phí băng thông thực tế (Goodput).)*

1. **Các chuẩn cáp Ethernet thông dụng (IEEE 802.3)**
   - Ethernet sử dụng CSMA/CD. Cổ điển tốc độ 10Mbps (10BASE-2, 10BASE-5).
   - Cáp xoắn đôi (có chữ "T"): 100BASE-T (Fast Ethernet - 100 Mbps), 1000BASE-T (Gigabit Ethernet - 1 Gbps, cắm RJ-45, vẫn dùng CSMA/CD).
   - Cáp quang (có chữ "F/FX"): 100BASE-F/100BASE-FX.

2. **Các thông số đo lường Đường truyền**
   - **Băng thông (Bandwidth):** Độ rộng tối đa của "đường ống" / dải tần số.
   - **Thông lượng (Throughput):** Lượng dữ liệu thực tế trung bình truyền được. Bị ảnh hưởng bởi "Nút thắt cổ chai" (Bottleneck) - thông lượng toàn tuyến bị giới hạn bởi đoạn chậm nhất.
   - **Baud rate vs Bit rate:** Baud là tốc độ thay đổi tín hiệu. Bit rate là lượng dữ liệu gửi được. (Ví dụ: Manchester thì Baud = 2 × Bit rate; mã đa mức như 16-PSK thì Bit rate = Baud rate × 4).
   - **Tỉ lệ lỗi bit (BER):** Xác suất để MỘT bit bị lỗi. Kích thước gói tin MTU càng lớn, xác suất lỗi cả gói càng tăng ().
   - **Độ suy hao (Attenuation):** Sự giảm sút tín hiệu trên đường dây/không gian.
   - **Thành phần một chiều (DC Component) & Baseline Wander:** Mức điện áp cơ sở bị lệch nếu truyền quá nhiều bit giống nhau, dẫn tới đọc sai dữ liệu. Cần phải luôn duy trì giá trị trung bình tín hiệu ở mức 0.

---

# CHƯƠNG 3. TẦNG LIÊN KẾT DỮ LIỆU

## 3.1. Giới thiệu về tầng liên kết dữ liệu và Địa chỉ MAC
*(Liên kết với: Định nghĩa LAN/WAN ở 1.3, Địa chỉ IPv4 ở 4.2 & Bảng địa chỉ MAC ở 3.5 - Tại sao: Nếu IPv4 (4.2) là "địa chỉ nhà" (dùng để tìm đường liên tỉnh), thì MAC là "Căn cước công dân" gắn chết trên card mạng (NIC) dùng để giao tiếp nội bộ trong LAN (1.3). Bảng MAC của Switch (3.5) cũng hoàn toàn dựa vào việc đọc địa chỉ MAC nguồn/đích này để chuyển mạch gói. Giao thức ARP đóng vai trò là "nhân viên tra cứu", giúp máy tính đổi từ IP sang MAC khi gói tin đã về đến khu vực mạng nội bộ nhưng chưa biết phải gửi cho card mạng nào.)*

1. **Bản chất của Địa chỉ MAC (Media Access Control)**
   - **Định vị:** Tầng 2, định danh duy nhất giao diện mạng (NIC). Kích thước 48 bit (6 cặp hexa).
   - **Hình thức truyền thông:**
     - *Unicast:* Gửi Điểm - Điểm.
     - *Broadcast:* Gửi quảng bá cho tất cả LAN (địa chỉ FF-FF-FF-FF-FF-FF).
     - *Multicast:* Gửi một nhóm máy tính.

2. **Giao thức và Thiết bị**
   - **Giao thức ARP:** Khi biết IP mà chưa biết MAC, máy sẽ phát Broadcast để hỏi MAC.
   - **Switch (Bộ chuyển mạch):** Thiết bị Tầng 2, chuyển tiếp dữ liệu dựa trên bảng MAC bằng cơ chế tự học.

## 3.2. Điều khiển truy nhập đường truyền mạng đa truy nhập
*(Liên kết với: Dồn kênh ở 2.4, Phương tiện vô tuyến/hữu tuyến ở 2.2 & Cấu trúc mạng LAN ở 1.3 - Tại sao: Vì mạng LAN thường có kiến trúc chia sẻ chung đường truyền (như Bus topology - 1.4), nên khi hai máy cùng "gào" lên, tín hiệu sẽ va vào nhau (đụng độ). Kỹ thuật CSMA/CD được sinh ra chuyên biệt để xử lý đụng độ trên cáp đồng (Ethernet), trong khi CSMA/CA sinh ra để né tránh đụng độ trên sóng Wi-Fi vô tuyến (2.2). Nếu mạng quá đông đúc, các phương pháp ngẫu nhiên này sẽ thất bại, lúc đó mạng buộc phải chuyển sang dùng phương pháp Phân chia kênh (TDMA, FDMA - kế thừa từ Dồn kênh 2.4) hoặc dùng Thẻ bài (Token Passing) để xếp hàng tuần tự.)*

Giải quyết sự cố đụng độ (Collision) khi nhiều thiết bị truyền cùng lúc trên đường truyền chung.
1. **Nhóm phương pháp Điều khiển ngẫu nhiên (Random Access)**
   Tối ưu cho môi trường Tải thấp.
   - **ALOHA:** Pure ALOHA (ngẫu nhiên hoàn toàn, đụng độ cao), Slotted ALOHA (đồng bộ khe thời gian, giảm đụng độ).
   - **CSMA/CD:** Dùng cho mạng có dây Ethernet. Cảm nhận sóng mang có phát hiện đụng độ ngay trong lúc truyền, phát tín hiệu JAM báo toàn mạng rồi chờ.
   - **CSMA/CA:** Dùng cho mạng không dây Wi-Fi. Cảm nhận sóng mang để chủ động tránh đụng độ (vì không thể vừa phát vừa nghe), nhưng đụng độ vẫn có thể xảy ra do trễ lan truyền.

2. **Nhóm phương pháp Phân chia kênh (Partitioning)**
   Tối ưu mạng Tải trọng cao (TDMA, FDMA, CDMA). Đảm bảo công bằng, loại bỏ hoàn toàn đụng độ, nhưng độ trễ cao do thiết bị phải chờ đến đúng lượt/khe thời gian mới được truyền.

3. **Nhóm phương pháp Luân phiên (Token Passing)**
   Dùng một thẻ bài (Token) rỗi luân chuyển tuần tự. Tránh đụng độ và có thể thiết lập mức độ ưu tiên truyền dữ liệu.

## 3.3. Kiểm soát lỗi
*(Liên kết với: Giao thức TCP/UDP ở 1.2, Mã hóa tín hiệu ở 2.3 & Đặc tính IPv4 ở 4.2 - Tại sao: Tầng 2 dùng mã CRC (mạnh nhất) để rà quét toàn bộ khung tin xem trong quá trình đi qua Tầng vật lý (2.3) có bị nhiễu lật bit nào không. Một quy tắc thiết kế cực kỳ quan trọng của TCP/IP: Tầng 2, Tầng 3 (IP) và UDP không bao giờ tự "sửa" lỗi bit, chúng chỉ kiểm tra (bằng Checksum hoặc CRC), nếu thấy sai sẽ thẳng tay VỨT BỎ gói tin. Mọi trách nhiệm khắc phục sự cố (Yêu cầu gửi lại gói bị vứt - ARQ) đều được đẩy lên cho giao thức TCP ở Tầng 4 (1.2) giải quyết để tiết kiệm tài nguyên cho các Router trung gian.)*

Nguyên lý chung: Thêm thông tin dư thừa.
1. **Mã Parity (Chẵn/Lẻ):** Thêm 1 bit để tổng số bit 1 là chẵn hoặc lẻ. Yếu điểm là chỉ phát hiện lỗi bit đơn, dễ bị lừa bởi lỗi triệt tiêu (chẵn bit bị lỗi).
2. **Mã Checksum (Tổng kiểm tra):** Cộng các khối dữ liệu, đảo bit làm checksum. Phát hiện tốt hơn nhưng vẫn có thể bị lừa bởi lỗi triệt tiêu bù trừ. IP dùng Checksum kiểm tra Header, TCP/UDP kiểm tra toàn bộ.
3. **Mã CRC (Kiểm tra dư thừa vòng):** Mạnh nhất, dùng phép chia nhị phân đa thức sinh G. Phát hiện nhiều lỗi nhất và nhạy cảm nhất, được đính ở Frame Trailer Tầng 2.

**Xử lý lỗi TCP/IP:** IP và UDP không tự sửa lỗi, nếu thấy sai sẽ loại bỏ gói. TCP tự "sửa" bằng cơ chế Yêu cầu phát lại tự động (ARQ) khi không nhận được ACK (do Time-out hoặc có Duplicate ACKs).

## 3.4. Kiểm soát luồng (Sliding Window / Cửa sổ trượt)
*(Liên kết với: Trễ hàng đợi ở 1.5, Kỹ thuật chuyển mạch gói ở 1.5 & Giao thức TCP ở 1.2 - Tại sao: Kỹ thuật chuyển mạch gói (1.5) đẩy mọi gói tin đi chung trên mạng, khiến các Router rất dễ bị quá tải bộ nhớ đệm (gây ra Trễ hàng đợi cực cao). Cửa sổ trượt của TCP không chỉ giúp máy gửi truyền nhanh hơn (không phải chờ ACK từng gói) mà còn liên tục theo dõi tình hình tắc nghẽn (Congestion Window) và thông báo tràn bộ đệm (Receive Window = 0). Nhờ cửa sổ trượt, TCP có thể chủ động "bóp bớt" lượng dữ liệu xả vào đường truyền, cứu các Router khỏi tình cảnh sập mạng do kẹt xe.)*

- **Mục tiêu:** Ngăn trạm gửi đẩy dữ liệu làm quá tải bộ nhớ đệm (buffer) của trạm nhận.
- **Cơ chế Cửa sổ trượt (Sliding Window):** Cho phép máy gửi truyền liên tục nhiều gói tin mà không cần chờ ACK cho từng gói, tiết kiệm thời gian hơn nhiều so với cơ chế Dừng-và-Chờ.
- **Ứng dụng trong TCP:**
  - *Kiểm soát luồng:* Dùng trường Receive Window do bên nhận báo. Khi Window = 0, máy gửi ngưng truyền.
  - *Sửa lỗi (ARQ):* Cửa sổ sẽ "trượt" tịnh tiến khi có ACK. Phát lại các gói tin nằm trong cửa sổ bị mất (thuật toán Go-Back-N / Selective Reject).
  - *Kiểm soát tắc nghẽn (Congestion Control):* TCP tự tính Congestion Window, bắt đầu cực nhỏ (Khởi động chậm), tăng dần (Tránh tắc nghẽn). Nếu có Time-out hoặc đứt quãng, sẽ lập tức giảm cửa sổ (Hồi phục nhanh).

## 3.5. Mạng cục bộ (LAN) và Chuyển tiếp dữ liệu tầng 2
*(Liên kết với: Bảng định tuyến Tầng 3 ở 4.4, Thiết bị Switch ở 1.3 & Giao thức ARP ở 3.1 - Tại sao: Switch hoạt động dựa vào "Bảng MAC" được xây dựng qua cơ chế Tự học (Self-learning) bằng cách nhìn vào địa chỉ MAC nguồn. Điều này cực kỳ đối lập với Router ở Tầng 3 (4.4) - Router không tự học mà dùng Bảng định tuyến phức tạp (Routing Table) được tính toán bằng các thuật toán như OSPF. Khi máy tính muốn phát ARP để tìm MAC (3.1), nó sẽ gửi một gói tin Broadcast toàn bit 1 (FF:FF:FF:FF:FF:FF), và Switch buộc phải nhân bản gói tin đó đẩy ra toàn bộ các cổng (trừ cổng gốc) để cả mạng đều nghe thấy.)*

1. **Bảng địa chỉ MAC và Cơ chế tự học (Self-learning)**
   - Ban đầu Bảng MAC trống rỗng. Switch "học" liên tục qua địa chỉ nguồn của khung tin mới đi vào cổng.
   - Switch có thể nhận biết sự thay đổi cổng nếu cáp bị cắm sang cổng khác, và có cơ chế hết hạn (Aging TTL) tự động xóa bản ghi nếu máy tính không hoạt động sau một thời gian.

2. **Cơ chế Chuyển mạch (Switching/Forwarding)**
   - Khi đã biết đích: Chuyển tiếp chính xác (Forwarding) nếu địa chỉ MAC đích đã có trong bảng, chỉ mở lối ra đúng một cổng.
   - Chế độ Store-and-Forward: Switch tiếp nhận toàn bộ khung, kiểm tra lỗi CRC xong xuôi rồi mới chuyển tiếp.

3. **Cơ chế Broadcast và Unknown Unicast**
   - *Broadcast:* Khi MAC đích là FF-FF-FF-FF-FF-FF, chuyển khung tin ra mọi cổng trừ cổng nhận vào.
   - *Unknown Unicast:* Địa chỉ MAC đích cụ thể nhưng chưa có trong bảng, Switch áp dụng nguyên tắc thà gửi nhầm hơn bỏ sót: cũng quảng bá khung tin đó ra tất cả các cổng để tìm máy đích.

---

# CHƯƠNG 4. TẦNG LIÊN MẠNG

## 4.1. Tổng quan về tầng liên mạng
*(Liên kết với: Mạng diện rộng WAN ở 1.3 & Mô hình OSI ở 1.6 - Tại sao: Tầng liên mạng (Layer 3) là "bộ não chỉ đường" của toàn bộ Internet. Nếu Tầng 2 (LAN) chỉ là câu chuyện giao tiếp trong xóm làng nhỏ bé, thì Tầng 3 chịu trách nhiệm kết nối hàng triệu xóm làng đó lại với nhau thành WAN. Nhiệm vụ tối thượng của nó là gán địa chỉ logic (IP) và tìm con đường ngắn nhất, rẻ nhất (Định tuyến) thông qua các Router để đi xuyên quốc gia.)*

Chức năng: Định tuyến (Routing), Chuyển tiếp (Forwarding), Định địa chỉ (Addressing), Đóng gói (Encapsulating), Đảm bảo QoS.
Các giao thức: IP, ICMP, Giao thức định tuyến (RIP, OSPF, BGP).

## 4.2. Giao thức IPv4
*(Liên kết với: Bảng chuyển tiếp (Forwarding Table) ở 4.4, Địa chỉ MAC ở 3.1 & Cơ chế chia mạng VLAN ở 1.3 - Tại sao: IPv4 là một cấu trúc địa chỉ phân cấp (chia làm phần Họ/Network và phần Tên/Host), giống hệt như Tên đường và Số nhà. Cấu trúc phân cấp này rất tuyệt vời vì nó giúp Router ở 4.4 có thể tóm gọn hàng ngàn máy tính vào chung một bảng định tuyến (Routing Aggregation) thay vì phải nhớ từng máy. Kỹ thuật chia mạng con (Subnetting / CIDR) cũng chính là nền tảng để người ta quy hoạch và cô lập các dải IP riêng biệt khi thiết lập các mạng LAN ảo (VLAN - 1.3). Trái ngược lại, địa chỉ MAC (3.1) là địa chỉ phẳng (chỉ là dãy số ngẫu nhiên), nên không thể dùng để định tuyến đi xa được.)*

1. **Đặc điểm và Cấu trúc**
   - Hướng không liên kết, truyền theo datagram (best effort), có trách nhiệm loại bỏ lỗi header thay vì tự sửa. Xử lý lặp vòng vô tận bằng trường TTL (Time-To-Live).
   - IP hoạt động ở Tầng 3 (định danh thiết bị). Cổng (Port) hoạt động ở Tầng 4 (định danh tiến trình/phần mềm).
   - **Cấu trúc 32-bit:** Gồm phần Họ (Network ID) và phần Tên (Host ID). Thường biểu diễn dạng thập phân (ví dụ: 192.168.1.1).
   - **Định địa chỉ Cổ điển (Classful):** Lớp A (0-127), Lớp B (128-191), Lớp C (192-223). Dễ gây lãng phí.
   - **Định địa chỉ CIDR (Mặt nạ mạng / Subnet Mask):** Dùng `/số_bit_mạng` (ví dụ /24). Khắc phục lãng phí địa chỉ bằng cách dùng hàng rào bit di động. Cấp phát bằng IP tĩnh (Static) hoặc tự động (DHCP).

2. **Các dạng địa chỉ đặc biệt**
   - *Địa chỉ mạng ("Cổng làng"):* Host ID toàn 0 (Không được gán cho máy).
   - *Địa chỉ Broadcast ("Loa phường"):* Host ID toàn 1.
   - *Địa chỉ Loopback ("Gương soi"):* Bắt đầu bằng 127 (Tự kiểm tra chính mình).
   - *Địa chỉ Multicast ("Họp nhóm"):* Lớp D (224-239).
   - *Dải IP Private (IP nội bộ):* 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16. Không thể định tuyến công khai trên Internet.

3. **Cách chia Host (Subnetting)**
   - Số thiết bị tối đa = (với n là số bit dành cho Host). Phải trừ đi 2 để chừa ra Địa chỉ mạng và Broadcast.

## 4.3. Cơ chế phân mảnh gói tin
*(Liên kết với: Thông số MTU và Lỗi bit BER ở 2.5, Trễ truyền tải ở 1.5 & Lỗi gói tin Tầng 2 ở 3.3 - Tại sao: Sự phân mảnh là minh chứng rõ nhất cho việc Tầng mạng phải nhượng bộ Tầng vật lý. Kích thước tối đa của gói tin (MTU) bị giới hạn hoàn toàn bởi đặc tính của cáp truyền và tỷ lệ lỗi BER (2.5). Nếu một Router nhận được gói IP quá to so với khả năng chứa của cáp ở cổng lối ra, nó bắt buộc phải "chặt" gói tin đó thành nhiều mảnh (Fragment). Quá trình chặt nhỏ này làm tăng độ trễ xử lý (1.5) của Router, và nếu một mảnh vỡ bị dính lỗi CRC ở Tầng 2 (3.3), toàn bộ gói IP gốc sẽ hỏng và TCP phải gửi lại cả khối từ đầu.)*

1. **MTU (Maximum Transmission Unit)**
   - Là kích thước tối đa của gói tin trên đường truyền.
   - MTU quá lớn dễ tăng xác suất lỗi bit và lãng phí truyền lại; MTU quá nhỏ làm giảm Goodput vì Header chiếm dụng nhiều.
   - Khi gói IP truyền tới có kích thước lớn hơn MTU của đường truyền đầu ra, Router phải tiến hành phân mảnh (Fragment).

2. **Cơ cấu phân mảnh trên IP Header**
   - *Identifier:* Dấu hiệu nhận biết các mảnh vỡ riêng lẻ thuộc cùng một gói gốc.
   - *Flag:* Cờ báo hiệu còn mảnh nào đằng sau hay không (đã là mảnh cuối chưa).
   - *Fragment Offset:* Vị trí của mảnh đó trong gói gốc để đích đến có thể hợp mảnh (Reassembly).

3. **Quy tắc cụm 8 Byte và tính toán Offset**
   - Tải trọng mỗi mảnh vỡ (ngoại trừ mảnh cuối cùng) BẮT BUỘC là con số chia hết cho 8.
   - *Ví dụ tính kích thước:* Payload 1200 byte phân mảnh làm 3 đoạn với Offset lần lượt là 0, 69, 138.
     - Mảnh 1 (Offset 0): Byte 0 đến byte 551 (do mảnh sau bắt đầu từ 69x8=552) -> Kích thước 552 byte.
     - Mảnh 2 (Offset 69): Byte 552 đến 1103 (mảnh sau từ 138x8=1104) -> Kích thước 552 byte.
     - Mảnh 3 (Offset 138): 1200 - 552 - 552 = 96 byte.

## 4.4. Định tuyến (Routing) và Chuyển tiếp gói tin IPv4
*(Liên kết với: Kỹ thuật chuyển mạch gói ở 1.5, Hệ tự trị (AS) ở 1.3 & Chuyển tiếp nội bộ LAN ở 3.5 - Tại sao: Khác với Switch ở LAN (3.5) chỉ cần nhìn bảng MAC để gạt cổng là xong, Định tuyến (Routing) là bài toán vĩ mô của mạng WAN. Vì áp dụng cơ chế chuyển mạch gói (1.5), mạng liên tục biến động, một sợi cáp đứt có thể làm thay đổi mọi thứ. Do đó, các Router phải liên tục chạy các thuật toán toán học phức tạp (Bellman-Ford cho RIP, Dijkstra cho OSPF) để vẽ lại bản đồ mạng và cập nhật Bảng định tuyến. Ở quy mô cao hơn, giao thức BGP được dùng để định tuyến các gói tin bay xuyên qua các Hệ tự trị (AS - 1.3) toàn cầu.)*

1. **Bảng chuyển tiếp (Forwarding Table / Bảng định tuyến)**
   - Là "biển chỉ đường" gồm: Địa chỉ mạng đích (kèm Subnet Mask), Trạm kế tiếp (Next-hop) và Cổng giao tiếp.
   - **Quy tắc "Longest matching" (Khớp tiền tố dài nhất):** Khi IP đích khớp nhiều dòng (nhiều tuyến đường) trong bảng, dòng nào chi tiết nhất (mặt nạ mạng / dài nhất) sẽ được ưu tiên chọn. Nếu không tìm thấy, router hủy bỏ và báo lỗi.
   - **Kết hợp đường đi (Routing Aggregation):** Gộp nhiều mạng nhỏ thành mạng lớn dùng CIDR để giảm bớt số bản ghi trong Bảng định tuyến.

2. **Định tuyến (Routing)**
   - Quá trình tìm đường đi độc lập. Các gói tin đi từ nguồn đến đích có thể đi qua các chặng (next-hop) khác nhau tùy tình trạng mạng, dẫn tới đến đích không theo thứ tự.
   - *Bộ định tuyến (Router):* Thiết bị Tầng 3. Bóc lớp vỏ Tầng 2 để đọc IP, kết nối các mạng LAN lại thành WAN.

3. **Giao thức và Thuật toán tìm đường (Chi phí Min)**
   - **RIP (Distance-vector):** Dùng thuật toán Bellman-Ford để tính chi phí bằng số bước nhảy (Hop Count, max 15 hops). Cập nhật đồn thổi cục bộ, tốc độ hội tụ chậm khi mạng đứt dây.
   - **OSPF (Link-state):** Dùng thuật toán Dijkstra (Shortest Path First). Tính chi phí dựa trên băng thông đường truyền (nhanh thì rẻ). Mỗi router có một bản đồ GPS toàn mạng, tốc độ hội tụ siêu nhanh.
   - **BGP:** Giao thức định tuyến liên miền để kết nối giữa các Hệ tự trị (AS).
