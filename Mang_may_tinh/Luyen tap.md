### Câu 1: Những hiện tượng nào sau đây là thách thức đặc trưng đối với tầng vật lý khi sử dụng phương tiện truyền thông không dây? (Nhiều đáp án)
- **A.** Tán xạ do gặp vật cản trên đường truyền
- **B.** Suy hao tín hiệu khi không thể xuyên qua tường (đặc biệt với sóng hồng ngoại)
- **C.** Nhiễu giao thoa do các tín hiệu trên các dải tần gần nhau chồng lấn
- **D.** Sự cố xung đột dữ liệu do hoạt động ở chế độ Song công toàn phần (Full-duplex)

> Đáp án đúng là: A, B và C

**Giải thích**: Dễ hiểu khi môi trường là không dây thì sóng khi truyền sẽ có thể bị tán xạ, va vào vật cản. Sóng cũng có thể bị suy hoa nếu nó gặp phải tường. Và vì môi trường truyền là dùng chung giữa các mạng không dây, các tín hiệu có thể bị nhiễu (va vào nhau). Đáp án D sai vì song công toàn phần là dành cho môi trường có dây, và nó không thể bị xung đột dữ liệu do môi trường truyền là dành riêng.

### Câu 2: Tại sao việc duy trì giá trị trung bình của tín hiệu ở mức 0 (loại bỏ thành phần một chiều) lại cực kỳ quan trọng trong mã hóa đường truyền? (Nhiều đáp án)
- **A.** Để tránh việc bên nhận xác định sai mức tín hiệu cơ sở (baseline wander)
- **B.** Để tiết kiệm băng thông bằng cách giảm tần số tín hiệu xuống 0
- **C.** Để cho phép truyền song song nhiều bit trên cùng một dây dẫn
- **D.** Để ngăn chặn tình trạng giải mã sai dữ liệu khi tín hiệu ở mức dương hoặc âm quá lâu

> Đáp án đúng là: A và D

**Giải thích**: Thành phần một chiều là khi tín hiệu không có sự luân phiên thay đổi mà liên tục giữ nguyên (có thể hiểu là tín hiệu toàn bit 1 hoặc toàn bit 0). Đáp án B và C thì không liên quan gì.

Ta cần biết 2 điều, thứ nhất máy sẽ không biết đâu là bit 0 hay bit 1 một cách đơn thuần, mà nó dựa vào baseline, baseline chính là giá trị tín hiệu trung bình trong thời gian gần nhất. Ví dụ truyền 0 1 0 1 với định mức 0V là bit 0, 5V là bit 1 => Ta có baseline là 2.5V, đem ra so sánh thì cứ tín hiệu 5V > 2.5V thì sẽ là bit 1, 0V < 2.5V thì sẽ là bit 0. Thứ 2, ta sử dụng baseline liên tục thay đổi thay vì một giá trị cố định là do sự suy hao tín hiệu khi truyền. Ví dụ nếu ta truyền 5V đi, nhưng do suy hao lại chỉ còn 2V, nếu đặt cố định là 2.5V thì sẽ nhận định sai, nhưng nếu lấy trung bình thì baseline lại chỉ còn 1V, vẫn đúng.

Vấn đề của thành phần một chiều là, VD: Nếu ta truyền 100 bit 1, khi đó, baseline sẽ ~4,6-4,7 V, lúc này các tín hiệu được truyền sau đó (bit 1) gặp suy hao có thể chỉ còn 4,5V, và do đó máy sẽ nhận định sai liên tục. 2 vấn đề nữa là nhiễu và biên độ an toàn, nếu mức suy hao là tương đối, tín hiệu cũng loanh quanh ở một mức suy hao nào đó, thì nhiễu có thể khiến tín hiệu đột ngột giảm hoặc tăng ở một mức nào đó, và do liên tục truyền bit 1, biên độ an toàn lúc này trở nên rất nhỏ, khoảng 4,6-4,7 so với tối đa là 5V, tức là khả năng bị lệch sẽ rất cao so với việc baseline~2,5V và tối đa là tận 5V.

### Câu 3: Tại sao kiến trúc TCP/IP được mô tả là có dạng "đồng hồ cát" (hourglass model)? (Nhiều đáp án)
- **A.** Vì nó cho phép tầng ứng dụng sử dụng nhiều loại giao thức khác nhau (HTTP, FTP, SMTP)
- **B.** Vì nó đảm bảo tính "trong suốt", giúp thay đổi công nghệ tầng vật lý không ảnh hưởng tầng ứng dụng
- **C.** Vì nó được thiết kế để tối ưu hóa bảo mật tại lõi mạng
- **D.** Vì giao thức IP là giao thức duy nhất và bắt buộc ở tầng mạng

> Đáp án đúng là:

### Câu 4: Một gói tin 1500B gửi qua liên kết 10 Mbps, dài 200km (2x10^8 m/s). Trễ xử lý 0.01ms, trễ hàng đợi 0.05ms. Tổng trễ nút?
- **A.** 2.26 ms
- **B.** 1.26 ms
- **C.** 2.20 ms

> Đáp án đúng là:

### Câu 5: Khi nói về thông lượng (throughput) và nút thắt cổ chai (bottleneck), phát biểu nào sau đây là chính xác? (Nhiều đáp án)
- **A.** Thông lượng luôn bằng đúng băng thông vật lý của đường truyền
- **B.** Thông lượng trung bình được tính trong một khoảng thời gian nhất định
- **C.** Nút thắt cổ chai là điểm trên đường truyền làm giới hạn thông lượng toàn hệ thống
- **D.** Nếu tốc độ gửi Rs nhỏ hơn tốc độ nhận Rc, thông lượng trung bình sẽ bị giới hạn bởi Rs

> Đáp án đúng là:

### Câu 6: Đặc điểm của truyền thông không dây (Wireless) trong tầng vật lý là gì? (Nhiều đáp án)
- **A.** Chịu ảnh hưởng lớn của môi trường dẫn đến các hiện tượng phản xạ, tán xạ và nhiễu giao thoa
- **B.** Sóng vi ba (Microwave) chỉ được sử dụng cho truyền thông vệ tinh, không dùng cho mặt đất
- **C.** Sóng hồng ngoại có tần số cao (300 GHz - 430 THz) nhưng không có khả năng xuyên tường
- **D.** Thường hoạt động ở chế độ bán song công (Half-duplex): tại một thời điểm chỉ có thể gửi hoặc nhận

> Đáp án đúng là:

### Câu 7: Đặc điểm của kiến trúc "đồng hồ cát" trong TCP/IP là gì? (Nhiều đáp án)
- **A.** Sử dụng duy nhất một giao thức liên mạng (IP) tại tầng mạng
- **B.** Cho phép tách rời việc phát triển ứng dụng tầng trên với công nghệ truyền dẫn tầng thấp

> Đáp án đúng là:

### Câu 8: Đường truyền 100 Mbps, mỗi người dùng cần 10 Mbps và hoạt động 20% thời gian. Nếu có 15 người dùng, biểu thức tính xác suất mạng bị nghẽn (> 10 người dùng đồng thời) là?
- **A.** Tổng xích-ma từ k=11 đến 15 của (C(15,k) * 0.2^k * 0.8^(15-k))
- **B.** C(15,10) * 0.2^10 * 0.8^5
- **C.** 1 - P(x < 10)

> Đáp án đúng là:

### Câu 9: Theo chuẩn EIA-232-E (RS-232), nếu khoảng cách truyền dẫn vượt quá 15m, thông số nào sau đây sẽ bị ảnh hưởng nghiêm trọng nhất theo quy chuẩn điện?
- **A.** Tốc độ truyền tin (bị giới hạn ở mức 20kbps hoặc thấp hơn)
- **B.** Số lượng chân cắm của đầu nối
- **C.** Mã hóa NRZ-L bị chuyển thành Manchester

> Đáp án đúng là:

### Câu 10: Khi so sánh giữa các loại sợi quang, nhận định nào sau đây là chính xác về mặt kỹ thuật? (Nhiều đáp án)
- **A.** Trong sợi Multimode graded index, chiết suất của lõi giảm dần từ trong ra ngoài giúp các tia sáng truyền theo đường cong và giảm méo dạng xung
- **B.** Sợi Multimode stepped index dễ bị méo dạng xung nhất vì các tia sáng truyền theo nhiều đường khác nhau và đến đích tại các thời điểm khác nhau
- **C.** Sợi quang Single-mode có xung nhận được hội tụ tốt và ít bị méo dạng nhất do tia sáng truyền song song với trục lõi
- **D.** Cáp quang Single-mode có hệ số khúc xạ thay đổi nhiều hơn so với Multimode để tăng tốc độ truyền

> Đáp án đúng là:

### Câu 11: Một gói tin được gửi từ A lúc t=0 và nhận được phản hồi từ B lúc t=40ms. Nếu thời gian xử lý tại B là 5ms, trễ lan truyền một chiều (từ A đến B) lý thuyết là bao nhiêu (giả sử trễ truyền tin không đáng kể)?
- **A.** 17.5 ms
- **B.** 20 ms
- **C.** 35 ms

> Đáp án đúng là:

### Câu 12: Một gói tin L=1000 bits truyền từ A qua một Router rồi đến B. Các liên kết đều có R=1Mbps. Bỏ qua d_proc, d_prop và d_queue. Tổng trễ để gói tin đi từ A đến B là bao nhiêu? (Lưu ý cơ chế Store and Forward)
- **A.** 2 ms
- **B.** 1 ms
- **C.** 1.5 ms

> Đáp án đúng là:

### Câu 13: Khi nói về chuẩn EIA-232-E (RS-232), nhận định nào sau đây phản ánh chính xác các quy định về mặt kỹ thuật của nó? (Nhiều đáp án)
- **A.** Đặc điểm Điện quy định mức điện áp cho bit 1 là -3V và bit 0 là +3V
- **B.** Đặc điểm Thủ tục quy định hình dạng vật lý của giắc cắm là 25 chân hoặc 15 chân
- **C.** Đặc điểm Chức năng phân loại các dây dẫn thành 4 nhóm: dữ liệu, điều khiển, đồng bộ và nối đất
- **D.** Tốc độ truyền tin bị giới hạn ở 20kbps cho khoảng cách dưới 15m

> Đáp án đúng là:

### Câu 14: Tại sao mã Manchester được sử dụng rộng rãi trong mạng Ethernet thay vì các mã NRZ? (Nhiều đáp án)
- **A.** Vì nó chỉ sử dụng 2 mức điện áp thay vì 3 mức như mã AMI
- **B.** Vì nó không có thành phần một chiều (DC component), giúp tín hiệu ổn định hơn
- **C.** Vì nó luôn có sự chuyển mức ở giữa mỗi bit, cung cấp cơ chế tự đồng bộ đồng hồ giữa bên gửi và bên nhận
- **D.** Vì nó sử dụng băng thông đường truyền hiệu quả hơn mã NRZ (tốc độ dữ liệu bằng tốc độ tín hiệu)

> Đáp án đúng là:

### Câu 15: Các thông số đặc trưng cho khả năng truyền dẫn của đường truyền vật lý bao gồm những gì? (Nhiều đáp án)
- **A.** Độ suy hao: mức suy giảm tín hiệu khi truyền
- **B.** Băng tần (Bandwidth): Độ rộng tần số tín hiệu có thể truyền đi
- **C.** Số lượng nút mạng tối đa kết nối vào đường truyền
- **D.** Tỉ lệ lỗi bit (BER - Bit Error Rate)

> Đáp án đúng là:

### Câu 16: Một gói tin Ethernet tại Switch có tổng kích thước là 1526 bytes, trong đó Header tầng Liên kết dữ liệu chiếm 26 bytes. Tính hiệu suất truyền tải payload của gói tin này tại tầng Liên kết.
- **A.** 98.3%
- **B.** 96.5%
- **C.** 94.1%

> Đáp án đúng là:

### Câu 17: Đặc điểm của kỹ thuật chuyển mạch gói (Packet Switching) là gì? (Nhiều đáp án)
- **A.** Các gói tin có thể tới đích theo các đường khác nhau và không đúng thứ tự
- **B.** Thiết bị chuyển mạch thực hiện cơ chế "lưu và chuyển tiếp" (store and forward)
- **C.** Tài nguyên đường truyền được dành riêng cho từng kết nối
- **D.** Dữ liệu được chia thành các gói tin có phần tiêu đề (header) và dữ liệu (payload)

> Đáp án đúng là:

### Câu 18: Các thành phần cơ bản của một hệ thống mạng Internet "đơn giản" bao gồm những gì? (Nhiều đáp án)
- **A.** Đường truyền (có dây, không dây)
- **B.** Đơn vị cung cấp kết nối Internet (ISP)
- **C.** Thiết bị kết nối mạng (switch, Internet connect box)
- **D.** Trạm làm việc (PC, mobile phone)

> Đáp án đúng là:

### Câu 19: Xét một đường truyền có băng thông giới hạn ở mức 10 MHz. Nếu sử dụng mã hóa Manchester, tốc độ truyền dữ liệu tối đa lý thuyết mà hệ thống đạt được là bao nhiêu (giả sử mỗi đơn vị tín hiệu chiếm toàn bộ băng thông sẵn có)?
- **A.** 20 Mbps
- **B.** 10 Mbps
- **C.** 5 Mbps

> Đáp án đúng là:

### Câu 20: Nhận định nào sau đây đúng khi so sánh Topology vật lý và Topology logic? (Nhiều đáp án)
- **A.** Topology logic luôn luôn trùng khớp với Topology vật lý trong mọi trường hợp
- **B.** Topology vật lý dựa trên cách bố trí cáp kết nối thực tế
- **C.** Topology logic dựa trên cách thức truyền tín hiệu (ví dụ: điểm-điểm, quảng bá)

> Đáp án đúng là:

### Câu 21: Tại sao phía nhận phải thực hiện quá trình ngược lại với Encapsulation (tháo dỡ gói tin)? (Nhiều đáp án)
- **A.** Để xử lý dữ liệu dựa trên các tham số trong tiêu đề mà phía gửi đã thiết lập tại tầng tương ứng
- **B.** Để thay đổi nội dung Payload nhằm phù hợp với giao thức của tầng trên
- **C.** Để tách bỏ phần tiêu đề (Header) trước khi chuyển phần dữ liệu (Payload) lên cho tầng trên cao hơn

> Đáp án đúng là:

### Câu 22: Một ứng dụng gửi khối dữ liệu 1000 bytes. Qua tầng Giao vận thêm 20B header, tầng Mạng thêm 20B header và tầng Liên kết dữ liệu thêm 14B header. Hiệu suất truyền dẫn (H) tại tầng Liên kết dữ liệu là bao nhiêu?
- **A.** ~94.8%
- **B.** 90.0%
- **C.** 96.2%

> Đáp án đúng là:

### Câu 23: Giả sử trễ tháo dỡ và kiểm tra tiêu đề tại mỗi tầng là 2 micro giây. So sánh trễ xử lý (d_proc) lý thuyết giữa một Switch (tầng 2) và một Router (tầng 3) khi nhận một gói tin.
- **A.** Router có d_proc lớn hơn Switch khoảng 2 micro giây (do xử lý thêm tầng Mạng)
- **B.** Switch có d_proc lớn hơn Router
- **C.** Cả hai có d_proc bằng nhau vì đều là thiết bị trung gian

> Đáp án đúng là:

### Câu 24: Trong kiến trúc phân tầng TCP/IP, nút mạng Switch trung gian thường triển khai các tầng nào? (Nhiều đáp án)
- **A.** Tầng Mạng (Network)
- **B.** Tầng Liên kết dữ liệu (Data link)
- **C.** Tầng Vật lý (Physical)
- **D.** Tầng Giao vận (Transport)

> Đáp án đúng là:

### Câu 25: Về các phương pháp mã hóa đường truyền NRZ (Non-Return to Zero), phát biểu nào sau đây đúng? (Nhiều đáp án)
- **A.** NRZ-I gặp vấn đề mất đồng bộ khi gặp chuỗi toàn bit 1 liên tiếp
- **B.** NRZ-I là phương pháp điều chế vi sai, trong đó bit 1 tương ứng với việc có chuyển mức ở đầu thời gian bit
- **C.** NRZ-L ưu việt hơn NRZ-I vì nó không phụ thuộc vào cực của tín hiệu
- **D.** Cả NRZ-L và NRZ-I đều gặp vấn đề mất đồng bộ khi truyền một chuỗi dài các bit 0 liên tiếp

> Đáp án đúng là:

### Câu 26: Dựa trên các phương tiện vật lý, đường truyền được phân thành những loại chính nào? (Nhiều đáp án)
- **A.** Vô tuyến (sóng radio, viba, sóng hồng ngoại...)
- **B.** Đường truyền logic (kênh ảo)
- **C.** Hữu tuyến (cáp xoắn, cáp đồng trục, cáp quang...)

> Đáp án đúng là:

### Câu 27: Các loại hình trạng (topology) vật lý phổ biến dựa trên cách kết nối cáp giữa các nút mạng là gì? (Nhiều đáp án)
- **A.** Bus (Trục dẫn)
- **B.** Ring (Vòng)
- **C.** Star (Hình sao)
- **D.** Mesh (Lưới)

> Đáp án đúng là:

### Câu 28: Một hệ thống truyền thông sử dụng kỹ thuật điều chế pha có 16 trạng thái pha khác nhau (16-PSK). Nếu tốc độ điều chế (Baud rate) đo được là 2400 Baud, tốc độ dữ liệu (Bit rate) thực tế của hệ thống là bao nhiêu?
- **A.** 2400 bps
- **B.** 4800 bps
- **C.** 9600 bps

> Đáp án đúng là:

### Câu 29: Tính trễ truyền tin (transmission delay) cho một gói tin kích thước L = 800 bits qua đường truyền có băng thông R = 1 Mbps.
- **A.** 0.8 ms
- **B.** 1.8 ms

> Đáp án đúng là:

### Câu 30: Khi một gói tin đi qua các thiết bị mạng, nhận định nào sau đây về việc sử dụng định danh là đúng? (Nhiều đáp án)
- **A.** Router sử dụng địa chỉ IP để xác định đường đi trong mạng liên mạng
- **B.** Switch sử dụng địa chỉ MAC (Physical address) để quyết định cổng ra cho gói tin
- **C.** Switch sử dụng địa chỉ IP để lọc các gói tin broadcast
- **D.** Router chỉ cần địa chỉ MAC là đủ để chuyển tiếp gói tin đi toàn cầu

> Đáp án đúng là:

### Câu 31: Một modem sử dụng kỹ thuật điều chế 8-PSK (khóa dịch pha với 8 trạng thái pha khác nhau). Nếu tốc độ dữ liệu yêu cầu là 9600 bps, tốc độ điều chế (Baud rate) cần thiết là bao nhiêu?
- **A.** 3200 Baud
- **B.** 9600 Baud
- **C.** 4800 Baud

> Đáp án đúng là:

### Câu 32: Cho chuỗi bit 1100. Khi phân tích dạng sóng của mã NRZ-I (Non-Return to Zero Invert) so với NRZ-L, nhận định nào sau đây là đúng? (Giả sử mức điện áp ban đầu trước khi truyền bit đầu tiên là mức thấp). (Nhiều đáp án)
- **A.** NRZ-I sẽ có 4 lần chuyển mức cho chuỗi 1100 này
- **B.** Trong mã NRZ-I, tại hai bit 0 cuối cùng, mức điện áp sẽ giữ nguyên không thay đổi so với mức của bit trước đó
- **C.** Trong mã NRZ-L, mức điện áp sẽ thay đổi ở giữa thời gian của mỗi bit 1
- **D.** Trong mã NRZ-I, tín hiệu sẽ thực hiện chuyển mức (từ thấp lên cao hoặc ngược lại) tại thời điểm bắt đầu của cả bit 1 thứ nhất và bit 1 thứ hai

> Đáp án đúng là:

### Câu 33: Một đường truyền có khả năng truyền tín hiệu trong dải tần số từ 300 Hz đến 3400 Hz. Băng tần (độ rộng băng thông tần số) của đường truyền này là bao nhiêu?
- **A.** 3100 Hz
- **B.** 3700 Hz
- **C.** 3400 Hz

> Đáp án đúng là:

### Câu 34: Trong quá trình đóng gói dữ liệu (Encapsulation) tại bên gửi, khẳng định nào sau đây là đúng? (Nhiều đáp án)
- **A.** Tầng dưới coi toàn bộ PDU của tầng trên chuyển xuống là phần Payload của nó
- **B.** Việc đóng gói chỉ xảy ra tại các nút mạng trung gian như Router hoặc Switch
- **C.** Mỗi tầng thêm vào một Header chứa thông tin định danh và điều khiển phục vụ cho tầng đồng cấp bên nhận
- **D.** Quá trình đóng gói làm giảm kích thước thực tế của dữ liệu truyền trên đường dây

> Đáp án đúng là:

### Câu 35: Phân tích dạng sóng Manchester (không vi sai) cho chuỗi bit 0101. Đặc điểm nào sau đây xuất hiện trong tín hiệu? (Nhiều đáp án)
- **A.** Giữa hai bit 1 liên tiếp (tại ranh giới bit) chắc chắn không có sự chuyển mức nào [2].
- **B.** Bit 0 được biểu diễn bằng sườn âm (từ cao xuống thấp) và bit 1 là sườn dương (từ thấp lên cao) [2].
- **C.** Tại mỗi bit đều có một sự chuyển mức (transition) chính xác ở giữa chu kỳ bit [2].

> Đáp án đúng là:

### Câu 36: Hệ thống mạng Ethernet sử dụng mã hóa Manchester để truyền dữ liệu với tốc độ 10 Mbps. Tốc độ điều chế (tốc độ tín hiệu - Baud rate) thực tế trên đường truyền là bao nhiêu?
- **A.** 20 Mbaud
- **B.** 10 Mbaud
- **C.** 5 Mbaud

> Đáp án đúng là:

### Câu 37: Trước khi bị thay thế bởi cáp quang, một hệ thống cáp đồng trục có khả năng truyền đồng thời tối đa bao nhiêu cuộc gọi điện thoại đường dài?
- **A.** 10,000 cuộc gọi
- **B.** 1,000 cuộc gọi
- **C.** 5,000 cuộc gọi

> Đáp án đúng là:

### Câu 38: Tại sao đơn vị truyền dẫn tối đa (MTU) không nên quá lớn hoặc quá nhỏ? (Nhiều đáp án)
- **A.** MTU nhỏ giúp giảm tỉ lệ gói tin bị lỗi bit
- **B.** MTU quá nhỏ làm giảm hiệu suất truyền do tỉ lệ phần tiêu đề chiếm dụng cao
- **C.** MTU lớn giúp giảm thời gian trễ hàng đợi tại các router
- **D.** MTU quá lớn làm tăng xác suất gói tin bị lỗi bit và phải truyền lại nhiều dữ liệu hơn

> Đáp án đúng là: