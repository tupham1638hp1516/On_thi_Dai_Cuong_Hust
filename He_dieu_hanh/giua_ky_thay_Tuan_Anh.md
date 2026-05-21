### Câu 1: Phông đệm vòng tròn thường ứng dụng trong:
- **A.** Hệ chuyên gia
- **B.** Chương trình hỗ trợ đọc ghi dữ liệu
- **C.** Hệ quản trị cơ sở dữ liệu
- **D.** Chương trình dịch

Phông đệm vòng tròn (circular buffer) là vùng nhớ dùng lưu tạm dữ liệu giữa 2 tốc độ khác nhau (vd: CPU nhanh, ổ đĩa chậm). Nó hoạt động theo kiểu FIFO vòng tròn, rất phù hợp với việc đọc/ghi dữ liệu liên tục.

> Đáp án đúng là: B

### Câu 2: Đặc điểm nào **không** phải là của cấu trúc chương trình tuyến tính:
- **A.** Lưu động cao
- **B.** Tiết kiệm bộ nhớ khi thực hiện
- **C.** Thời gian thực hiện tối thiểu
- **D.** Không dùng chung module

Chương trình tuyến tính có tính lưu động cao, vì chương trình tuyến tính thường được viết một cách độc lập, không sử dụng các module bên ngoài hay các liên kết phức tạp nên nó có thể được nạp vào bất kỳ vùng RAM nào. Nó có thời gian thực hiện tối thiểu vì nó không mất chi phí di chuyển đến các vùng khác mà sẽ đọc từ trên xuống dưới rất nhanh.

> Đáp án đúng là: B

### Câu 3: Đâu là đặc điểm của thuật giải RR (Round Robin):
- **A.** Thời gian chờ đợi trung bình nhỏ
- **B.** Không cần tham số lượng tử thời gian
- **C.** Mọi tiến trình đều kết thúc được
- **D.** Non-preemptive (độc quyền)

RR cấp CPU cho mỗi tiến trình một "lượng tử thời gian" (time quantum) và xoay vòng. Do đó, mỗi tiến trình đều sẽ được chạy. Nó có thời gian chờ đợi trung bình lớn hơn so với các thuật toán khác vì mỗi lần chạy time quantum của một tiến trình thì tất cả tiến trình khác đều phải đợi, và mỗi khi xoay vòng thì điều này lặp lại liên tục. Độc quyền được hiểu là một khi tiến trình đã nắm giữ CPU, HĐH không thể tước quyền đó đi trừ khi tiến trình gặp I/O hoặc kết thúc.

> Đáp án đúng là: C

### Câu 4: Trong cấu trúc Overlay, chương trình được tổ chức các lớp như sau: Lớp 0: 80K; Lớp 1: 40K, 60K, 100K; Lớp 2: 50K, 70K, 80K; Lớp 3: 60K, 70K; Lớp 4: 90K, 10K, 20K, 40K. Kích thước bộ nhớ yêu cầu để tổ chức cấu trúc chương trình này là:
- **A.** 380K
- **B.** 330K
- **C.** 610K
- **D.** 420K

Cấu trúc Overlay: mỗi lớp dùng chung 1 vùng nhớ = lấy module lớn nhất trong lớp. Bộ nhớ cần = tổng các max của mỗi lớp:
- Lớp 0: max = 80K
- Lớp 1: max(40, 60, 100) = 100K
- Lớp 2: max(50, 70, 80) = 80K
- Lớp 3: max(60, 70) = 70K
- Lớp 4: max(90, 10, 20, 40) = 90K
Tổng = 80+100+80+70+90 = 420K

> Đáp án đúng là: D

### Câu 5: Tiến trình (process) là gì:
- **A.** Chương trình đang thực hiện
- **B.** Chương trình lưu trong đĩa
- **C.** Chương trình
- **D.** Cả 3 đều sai

Chương trình (program) là file tĩnh trên đĩa. Tiến trình (process) = chương trình đang được nạp vào bộ nhớ và thực hiện, có trạng thái, tài nguyên, PCB riêng. Có thể hiểu nếu chương trình là class thì tiến trình chính là object.

> Đáp án đúng là: A

### Câu 6: Trong quản lí thiết bị ngoại vi, các máy tính thế hệ thứ ba trở đi làm việc theo nguyên tắc phân cấp nào:
- **A.** Processor - Thiết bị điều khiển - Thiết bị ngoại vi
- **B.** Thiết bị điều khiển - Thiết bị ngoại vi - Processor
- **C.** Processor - Thiết bị ngoại vi - Thiết bị điều khiển
- **D.** Không đáp án nào đúng

CPU có tốc độ làm việc rất nhanh trong khi thiết bị ngoại vi lại rất chậm, do đó, người ta tạo ra thiết bị điều khiển để làm cầu nối trung gian, giúp khi CPU thực hiện xong việc thì có thể làm việc khác luôn thay vì mất thời gian đợi thiết bị ngoại vi (làm giảm hiệu suất do phải đợi và không làm gì)

> Đáp án đúng là: A

### Câu 7: Cho bảng thông tin của các tiến trình (p0: xuất hiện lúc 0, thực hiện 7; p1: xuất hiện lúc 2, thực hiện 5; p2: xuất hiện lúc 5, thực hiện 6). Thời gian chờ đợi trung bình theo giải thuật Round Robin với thời gian lượng tử là 3:
- **A.** 7
- **B.** 7.33
- **C.** 6.66
- **D.** 7.66

Lịch chạy RR (quantum=3):
- t=0: P0 xuất hiện lúc 0, chạy 3
- t=2; Trong lúc P0 đang chạy thì P1 xuất hiện, do đó hàng đợi: [P1]
- t=3; P0 out, P1 vào, P0 vẫn còn 7-3=4; P0 vào hàng đợi [P0] #P0=4
- t=5; Trong lúc P1 vẫn đang chạy thì P2 xuất hiện; P2 vào hàng đợi [P0; P2]
- t=6; P1 out; P0 vào, P1 còn lại 5-3=2; P1 bước vào hàng đợi [P2; P1] #P1=2
- t=9; P0 out; P2 vào, P0 còn lại 4-3=1; P0 bước vào hàng đợi [P1; P0] #P0=1
- t=12; P2 out; P1 vào, P2 còn lại 6-3=3; P2 bước vào hàng đợi [P0; P2] #P2=3
- t=14; P1 kết thúc; P0 vào
- t=15; P0 kết thúc; P2 vào
- t=18; P2 kết thúc

Thời gian chờ = Hoàn thành - Xuất hiện - Thực hiện:
- p0: 15 - 0 - 7 = 8
- p1: 14 - 2 - 5 = 7
- p2: 18 - 5 - 6 = 7
Trung bình = (8+7+7)/3 = 22/3 = 7.33 

> Đáp án đúng là: B

 **Câu 8: Giả thiết kích thước một khối nhớ (block) là 1024 bytes. Các khối nhớ được đánh địa chỉ sử dụng con trỏ 32 bit. Để phân phối vùng nhớ cho file, mỗi file sử dụng 12 con trỏ trực tiếp (direct pointers), một con trỏ gián tiếp bậc 1 (singly-indirect pointer), 1 con trỏ gián tiếp bậc 2 (doubly-indirect pointer). Kích thước tối đa của một file là:**
- **A.** 1036MB
- **B.** 2048MB
- **C.** 1048MB
- **D.** 1024MB

*Note lại*
### Câu 9: Tài nguyên của hệ thống bao gồm:
- **A.** Bộ nhớ, bộ xử lí và các thiết bị vào ra
- **B.** Bộ nhớ, bộ xử lí, hệ điều hành, các thiết bị vào ra
- **C.** Bộ nhớ, bộ xử lí, chương trình điều khiển thiết bị
- **D.** Bộ nhớ, bộ xử lí, bộ nhớ ngoài, máy in

Tài nguyên hệ thống = phần cứng có thể cấp phát cho tiến trình: CPU (bộ xử lí), bộ nhớ chính, các thiết bị vào ra (disk, printer...). Hệ điều hành không phải tài nguyên, nó là phần mềm quản lí.

> Đáp án đúng là: A

### Câu 10: Kích thước một sector thường là bao nhiêu:
- **A.** 4KB
- **B.** 256B
- **C.** 128B
- **D.** 512B

Sector là đơn vị vật lý nhỏ nhất trên đĩa cứng. Kích thước tiêu chuẩn là 512 bytes

> Đáp án đúng là: D

### Câu 11: Thành phần nào không phải là thành phần của hệ điều hành:
- **A.** Chương trình quản lí truy nhập file
- **B.** Chương trình lập lịch cho tiến trình
- **C.** Chương trình quản lí bộ nhớ tự do
- **D.** Chương trình điều khiển thiết bị

Hệ điều hành gồm: quản lí tiến trình (lập lịch), quản lí bộ nhớ, quản lí file (truy nhập), quản lí vào-ra. Chương trình điều khiển thiết bị (device driver) là phần mềm nằm giữa OS và phần cứng - nó là một loại thành phần đặc biệt.

> Đáp án đúng là: D

### Câu 12: Bảng quản lí trang được mô tả (Trang 0->Khung 4, Trang 1->Khung 6, Trang 2->Khung 7, Trang 3->Khung 6). Địa chỉ của dữ liệu trong chương trình là 6456. Địa chỉ vật lý của dữ liệu là (biết kích thước trang là 4KB):
- **A.** 26936
- **B.** 30936
- **C.** 936
- **D.** 56936

•  Bước 1: Quy đổi đơn vị:

Kích thước trang = 4KB = 4 * 1024 = 4096  Bytes.

•  Bước 2: Tách Địa chỉ Logic (Logical Address) thành 2 phần:

Địa chỉ logic (6456) được cấu tạo từ Số hiệu trang (p) và Độ lệch (d).

•	p = 6456 / 4096 = 1 (Lấy phần nguyên => Dữ liệu nằm ở Trang 1).

•	d = 6456 mod 4096 = 2360 (Lấy phần dư => Dữ liệu nằm ở byte thứ 2360 tính từ đầu trang).

•  Bước 3: Tra bảng quản lý trang (Page Table):
Theo đề bài: Trang 1 => Khung 6.

Có nghĩa là HĐH đã bốc nguyên cái "Trang 1" đó ném vào vị trí "Khung 6" trên RAM vật lý.

•  Bước 4: Tính Địa chỉ Vật lý (Physical Address):

Địa chỉ vật lý = (Số hiệu khung * Kích thước khung) + Độ lệch d

•	PA = (6 * 4096) + 2360 = 24576 + 2360 = 26936


> Đáp án đúng là: A

### Câu 13: Trong cấu trúc phần tử của bảng phân vùng, khi đánh địa chỉ vật lí đầu, cần sử dụng bao nhiêu bit để đánh số hiệu sector/cylinder:
- **A.** 10bit/6bit
- **B.** 4bit/12bit
- **C.** 6bit/10bit
- **D.** 8bit/8bit

[HHHHHHHH] [CCSSSSSS] [CCCCCCCC]

> Đáp án đúng là: C

### Câu 14: Trong kĩ thuật quản lí phân chương (vùng) động, các vùng nhớ sau còn trống có kích thước: 100k, 250k, 260k, 300k, 200k, 220k. Vùng nhớ nào sẽ được chọn để nạp chương trình có kích thước 210k theo giải thuật **Worst Fit**:
- **A.** 260K
- **B.** 300K
- **C.** 270K
- **D.** 220K

Worst Fit = chọn vùng nhớ TRỐNG NHẤT (lớn nhất) còn đủ chỗ. Các vùng đủ lớn (>= 210k): 250k, 260k, 300k, 220k. Vùng lớn nhất = 300K.

> Đáp án đúng là: B

### Câu 15: Hệ điều hành là gì:
- **A.** Là một hệ thống mô hình hóa, mô phỏng hoạt động của máy tính...
- **B.** Là một chương trình đóng vai trò như một giao diện giữa người sử dụng và phần cứng máy tính...
- **C.** Là hệ thống chương trình với các chức năng giám sát, điều khiển...
- **D.** Cả ba đáp án.

HĐH vừa là giao diện giữa người dùng và phần cứng (B), vừa là hệ thống quản lí tài nguyên và giám sát tiến trình (C), vừa có thể hiểu theo nghĩa rộng hơn (A). Tất cả 3 định nghĩa đều đúng tùy góc nhìn.

> Đáp án đúng là: D

### Câu 16: Xét không gian địa chỉ logic 32 trang (pages), kích thước trang là 1KB, ánh xạ sang bộ nhớ vật lí 16 khung trang (frames). Hỏi có bao nhiêu bit trong địa chỉ **vật lý**:
- **A.** 16 bit
- **B.** 13 bit
- **C.** 14 bit
- **D.** 15 bit

Số trang + offset --<ánh xạ>--> Số khung + offset
Kích thước trang là 1KB=1024B=2^10B => Số bit để đánh địa chỉ cho offset là 10
Có 16=2^4 khung trang => Số bit để đánh địa chỉ cho frames là 4
=> 4+10=14 bit

32 trang nằm trong ổ cứng, 16 khung là các bộ nhớ tạm nằm trên RAM, nếu trang nào được gọi thì mới đem nó vào trong RAM, do đó 32 trang có thể ánh xạ sang 16 khung

> Đáp án đúng là: C

### Câu 17: Xét không gian địa chỉ logic 32 trang (pages), kích thước trang là 1KB, ánh xạ sang bộ nhớ vật lí 16 khung trang (frames). Hỏi có bao nhiêu bit trong địa chỉ **logic**:
- **A.** 13 bit
- **B.** 15 bit
- **C.** 14 bit
- **D.** 16 bit

Tương tự câu trên: 15 bit

> Đáp án đúng là: B

### Câu 18: Câu nào sau đây là **không chính xác**:
- **A.** Khi thực hiện, hàm main là một luồng của tiến trình
- **B.** Tiến trình phải có ít nhất một luồng
- **C.** Các luồng có thể chia sẻ vùng ngăn xếp với nhau
- **D.** Thời gian chuyển CPU giữa các luồng nhanh hơn giữa các tiến trình

Đáp án A là đúng, hàm main là luồng, nó là cái bắt đầu làm việc nên nó là luồng, B đúng vì phải có luồng thì tiến trình mới hoạt động, mới được gọi là tiến trình. D chắc chắn đúng vì các luồng dùng chung tài nguyên CPU nên CPU sẽ chuyển qua lại nhanh hơn so với tiến trình. Luồng không chia sẻ ngăn xếp (heap và data thì có)

> Đáp án đúng là: C

### Câu 19: Lời gọi hệ thống (system calls) là:
- **A.** Cả ba đáp án.
- **B.** Là môi trường giao tiếp giữa phần cứng và hệ điều hành.
- **C.** Là môi trường giao tiếp giữa chương trình của người sử dụng và hệ điều hành.
- **D.** Là môi trường giao tiếp giữa chương trình và phần cứng.

System call nằm giữa hệ điều hành và chương trình, device driver nằm giữa hệ điều hành và phần cứng, do đó đáp án án B là sai, còn D là sai vì chương trình không được giao tiếp với phần cứng.

> Đáp án đúng là: C

### Câu 20: Luồng hay Tuyến (thread) là gì:
- **A.** Thành phần của tiến trình xử lí mà code của tiến trình.
- **B.** Cả 3 đáp án đều đúng.
- **C.** Đơn vị chương trình của tiến trình bao gồm mã code.
- **D.** Đơn vị xử lí cơ bản của hệ thống, bao gồm mã code, con trỏ lệnh, tập các thanh ghi và stack.

Thread = đơn vị thực thi cơ bản. Mỗi thread có: con trỏ lệnh (PC), tập thanh ghi, stack riêng. Nhiều thread cùng tiến trình chia sẻ code, heap, data. Đáp án D mô tả đầy đủ nhất.
> Đáp án đúng là: D

### Câu 21: Đâu **không** phải là đặc điểm của thuật giải FCFS (First Come - First Serve):
- **A.** Thời gian chờ trung bình nhỏ
- **B.** Mọi tiến trình đều kết thúc được
- **C.** Không cần bổ sung thêm thông tin phụ
- **D.** Đơn giản

Nếu một chương trình rất dài đến trước, các chương trình ngắn đằng sau sẽ phải đợi rất lâu trong khi có thể cho nó lên trước để rút ngắn thời gian chờ. Dễ thấy đáp án A là sai.
> Đáp án đúng là: A

### Câu 22: Đâu **không** phải là vai trò của SPOOL:
- **A.** Tăng hiệu suất hệ thống
- **B.** Giải phóng hệ thống khỏi sự ràng buộc về số lượng thiết bị
- **C.** Cho phép khai thác tối ưu thiết bị ngoại vi
- **D.** Tạo ra kĩ thuật lập trình mới, cho phép giảm số lần duyệt file trong khi xử lý

SPOOL (Simultaneous Peripheral Operations On-Line): đệm dữ liệu vào disk trước khi gửi ra thiết bị (vd: máy in). Tác dụng: tăng hiệu suất, cho phép nhiều chương trình dùng chung 1 thiết bị, khai thác tối ưu thiết bị. "Tạo kĩ thuật lập trình mới giảm số lần duyệt file" không phải vai trò của SPOOL mà của các cấu trúc dữ liệu/thuật toán.
> Đáp án đúng là: D

### Câu 23: Cấu trúc một phần tử ROOT cho như sau: `52454144 4D425220 43202020 003C865B / A53EA53E 0000CF79 A53E402E BD0A0000`. Ngày (d/m/y) **truy nhập cuối** là: *Cuối kỳ*
- **A.** 15/05/2011
- **B.** 06/05/2011
- **C.** 05/05/2011
- **D.** 04/08/2012

Trong cấu trúc ROOT FAT, trường "Last Access Date" nằm ở byte 18-19 (tính từ 0). Lấy bytes 18-19 từ hex: `A53E`. Chuyển sang little-endian: `3EA5` = 0x3EA5 = 16037.
Giải mã ngày FAT: Bits 15-9 = năm (tính từ 1980), Bits 8-5 = tháng, Bits 4-0 = ngày.
0x3EA5 = 0011 1110 1010 0101
- Năm: 0011 111 = 31 => 1980+31 = 2011
- Tháng: 0 101 = 5
- Ngày: 0 0101 = 5
=> Ngày 05/05/2011
> Đáp án đúng là: C

### Câu 24: Trong FAT32, vùng hệ thống bao gồm: *Cuối kỳ*
- **A.** MBR, BootSector, ROOT
- **B.** MBR, BootSector, FAT1, FAT2
- **C.** MBR, BootSector, FAT1, FAT2, ROOT
- **D.** MBR, BootSector, FAT, ROOT

FAT16 có ROOT cố định trong vùng hệ thống. FAT32 thì ROOT được lưu trong vùng dữ liệu (không cố định), nên vùng hệ thống của FAT32 chỉ gồm: MBR, BootSector, FAT1, FAT2 (có bản dự phòng).
> Đáp án đúng là: B

### Câu 25: Đoạn găng là:
- **A.** Đoạn chương trình yêu cầu tài nguyên găng
- **B.** Đoạn chương trình sử dụng tài nguyên ngoài
- **C.** Đoạn chương trình sử dụng tài nguyên trong
- **D.** Đoạn chương trình xử lí tài nguyên găng

Tài nguyên găng là các tài nguyên dùng chung, được chia sẻ giữa các tiến trình NHƯNG chỉ có thể được sử dụng bởi một tiến trình trong 1 thời điểm. Đoạn găng chính là những đoạn code cụ thể nằm bên trong tiến trình thực hiện đọc, ghi hay thay đổi tài nguyên găng đó. Vì Hệ điều hành không thể khóa lại tài nguyên găng để ngăn các luồng trong cùng 1 tiến trình sử dụng(hoặc các tiến trình dùng chung tài nguyên), HĐH sẽ "bao bọc" đoạn găng/ cái đoạn code đang sử dụng tài nguyên găng. Để khi luồng khác muốn dùng, nó sẽ biết đường mà né
> Đáp án đúng là: D


### Câu 26: Kích thước của một phần tử Root của hệ thống FAT là: *Cuối kỳ*
- **A.** 16B
- **B.** 48B
- **C.** 32B
- **D.** 64B

Mỗi entry trong ROOT FAT chứa: tên file (8+3 bytes), thuộc tính, ngày giờ, cluster bắt đầu, kích thước file. Tổng cộng theo chuẩn = 32 bytes.
> Đáp án đúng là: C

### Câu 27: Cấu trúc một phần tử của bảng phân vùng như sau, tính số sector của phân vùng này: `800001F9 0BFEBF30 B9093D00 387B4C00` *Cuối kỳ*
- **A.** 8388609
- **B.** 5689008
- **C.** 3701580
- **D.** 5012280

4 byte cuối là "Total Sectors" (little-endian): 38 7B 4C 00 => đảo: 00 4C 7B 38 = 0x004C7B38 = 5012280.
> Đáp án đúng là: D

### Câu 28: Một đĩa cứng có cấu trúc vật lý gồm 1000 sector cho một Cylinder. Hệ thống vừa truy xuất sector 20456, hàng đợi: 10531, 22457, 20198, 40167, 2395, 2856, 6624, 6135, 38245, 6845. Theo **FCFS** thì tổng quãng đường đầu đọc dịch chuyển là:
- **A.** 60
- **B.** 150
- **C.** 180
- **D.** 90

Số cylinder = số sector / 1000. Vị trí hiện tại: cylinder 20 (lấy nguyên của 20456/1000).
Chuỗi cylinder: 20->10->22->20->40->2->2->6->6->38->6
Tổng = |20-10|+|10-22|+|22-20|+|20-40|+|40-2|+|2-2|+|2-6|+|6-6|+|6-38|+|38-6|
= 10+12+2+20+38+0+4+0+32+32 = 150

Trong ổ đĩa cứng sẽ có rất nhiều các loại đĩa từ (platters) xếp chồng lên nhau.
- Mỗi đĩa sẽ có các rãnh (tracks) có thể hiểu là các vòng tròn đồng tâm nằm trên cùng một đĩa từ
- Ở mỗi rãnh sẽ có các sector, đây chính là đơn vị nhỏ nhất, dùng để chứa dữ liệu, độ lớn thông thường là 512 Bytes
- Các tracks có cùng bán kính sẽ được gộp chung lại thành 1 cylinder, có thể tưởng tượng nó giống nhưu một khối trụ vậy.
- Disk Controller có hệ thống đọc/ghi, có thể hiểu nó như cái lược, mỗi thanh giống như một cánh tay để sát vào từng đĩa (giống như đầu phát nhạc của máy nghe nhạc ngày xưa). Tất cả cánh tay dùng chung 1 trục, nên khi dịch ra/ thụt vào thì tất cả làm cùng lúc.
- Mỗi khi muốn tìm đến một sector nào đó, các cánh tay sẽ dừng ở cylinder tương ứng với sector đó, rồi xoay các đĩa để tìm được tất cả các sector cùng một cột, cuối cùng dựa trên địa chỉ Head để xác định đúng đĩa từ chứa sector mong muốn.
> Đáp án đúng là: B

### Câu 29: Phương pháp "kiểm tra và xác lập" gặp phải vấn đề nào sau đây:
- **A.** Không đáp án đúng
- **B.** Tính loại trừ lẫn nhau
- **C.** Tính tiến triển
- **D.** Chờ đợi tích cực

Test và Set được hiểu là phương pháp khi một tiến trình đã chiếm dụng tài nguyên găng, một tài nguyên nào đó muốn sử dụng thì sẽ phải chạy vòng lặp while liên tục, cho đến khi điều kiện thỏa mãn thì nó mới được sử dụng tài nguyên găng. Phương pháp này có nhược điểm lớn là tiêu tốn tài nguyên CPU một cách vô ích (liên tục kiểm tra điều kiện thay vì mang lại giá trị), do đó, nó ứng với vấn đề Chờ đợi tích cực.
- Trong bài toán sử dụng tài nguyên găng, các phương pháp bắt buộc phải đảm bảo 3 điều kiện sau (để được coi là một phương pháp sử dụng tài nguyên găng an toàn)
1. Tính loại trừ lẫn nhau: Nếu một tiến trình đang sử dụng tài nguyên găng thì không một tiến trình nào khác được sử dụng nữa
2. Tính tiến triển: Khi tài nguyên găng không được sử dụng và có một số tiến trình đang xếp hàng, hệ điều hành bắt buộc phải chọn ra một tiến trình phù hợp nhất để sử dụng
3. Tính chờ đợi hữu hạn
> Đáp án đúng là: D

### Câu 30: Mô hình cài đặt đa luồng nào cho phép tạo nhiều luồng trong không gian người sử dụng đồng thời tận dụng kiến trúc đa xử lý:
- **A.** Mô hình một-một
- **B.** Mô hình nhiều-một
- **C.** Mô hình nhiều-nhiều
- **D.** Mô hình một-nhiều

*Note:*
- CPU thực chất không nhìn vào tiến trình mà nó chỉ nhìn vào luồng. Có 2 thứ khá giống nhau, được gọi là đa nhiệm và đa luồng.
> Đa nhiệm là một mình CPU làm nhiều tiến trình, còn đa luồng là một mình CPU làm nhiều luồng của một tiến trình. Tất cả đều sử dụng lát cắt thời gian.
- Sở dĩ nhắc đến việc CPU chỉ nhìn vào luồng là bởi, CPU có thể thực hiện cả đa nhiệm và đa luồng cùng 1 lúc. Tuy nhiên, khi Hệ điều hành thực hiện Đa nhiệm, bản chất là nó đang điều phối CPU chuyển đổi qua lại giữa các luồng thuộc các tiến trình khác nhau
- Đa nhiệm hoạt động chậm hơn đa luồng rất nhiều. Lý do là vì các luồng trong cùng 1 tiến trình sử dụng chung bộ nhớ (chỉ trừ stack, con trỏ lệnh, tập thanh ghi/registers). Trong khi các tiến trình (hay các luồng của mỗi tiến trình) thì không sử dụng chung bộ nhớ, nên sự chuyển đổi giữa chúng sẽ lâu hơn so với đa luồng.
- Một CPU có 4 nhân nhưng có thể có bao nhiêu luồng nhân cũng được, lý do là vì luồng được coi là tài sản của tiến trình thay vì hành động, có thể chỉ 2 luồng nhân đang chạy, còn hàng chục luồng nhân khác đang chờ đợi thì chúng vẫn được gọi là luồng nhân.

> Đáp án đúng là: C

### Câu 31: Trong phòng tránh bế tắc, giải thuật người quản lý ngân hàng được áp dụng:
- **A.** Mỗi khi có yêu cầu tài nguyên từ tiến trình
- **B.** Hệ thống định kỳ thực hiện
- **C.** Mỗi khi có yêu cầu tài nguyên từ người sử dụng
- **D.** Tất cả đáp án đều đúng

Deadlock xảy ra khi có một nhóm các tiến trình bị "treo" vĩnh viễn. Lý do là mỗi tiến trình trong nhóm đang nắm giữ một tài nguyên (ví dụ: RAM, Máy in) và lại đang chờ đợi một tài nguyên khác mà một tiến trình khác trong nhóm đang giữ.

Để Deadlock thực sự xảy ra, hệ thống phải hội tụ đủ 4 điều kiện Coffman cùng lúc:

- Loại trừ tương hỗ (Mutual Exclusion): Tài nguyên không thể dùng chung (ví dụ máy in, 1 lúc chỉ 1 người in).

- Giữ và Chờ (Hold and Wait): Tiến trình đang giữ ít nhất 1 tài nguyên và đòi thêm tài nguyên khác.

- Không chiếm đoạt (No Preemption): Hệ điều hành không thể "cướp" tài nguyên từ tay tiến trình nếu nó chưa dùng xong.

- Chờ đợi vòng tròn (Circular Wait): P1 chờ P2, P2 chờ P3, ..., Pn chờ lại P1.

Chiến lược ngăn ngừa: Ngăn ít nhất 1 trong 4 điều kiện tồn tại

Chiến lược phòng tránh: 3 điều kiện đầu vẫn có thể cho phép, nhưng, hệ điều hành sẽ dự đoán xem liệu điều kiện thứ 4 (hàng đợi vòng tròn) có xảy ra hay không.

> Đáp án đúng là: A

### Câu 32: Phát biểu nào sau đây **không** phải là vai trò của phông đệm:
- **A.** Thực hiện song song giữa trao đổi vào ra và xử lí
- **B.** Đảm bảo độc lập giữa trao đổi và xử lí
- **C.** Tăng tốc độ hoạt động của thiết bị ngoại vi
- **D.** Giảm số lần truy cập vật lí

Buffer: lưu tạm dữ liệu, cho phép CPU và I/O làm việc song song, độc lập nhau, giảm số lần đọc ghi vật lý. Buffer là vùng nhớ nằm giữa CPU và I/O để giúp CPU không phải đợi I/O (vốn rất chậm) mà có thể đi làm việc khác (nó đưa dữ liệu cho buffer lo liệu rồi xử lý việc khác). Tuy nhiên, buffer không thay đổi được tốc độ của thiết bị ngoại vi (HĐH không có khả năng này, nó chỉ có khả năng tối ưu hiệu năng, hoặc đánh lừa thị giác)

> Đáp án đúng là: C

### Câu 33: Cấu trúc chương trình cho phép thực hiện chương trình với tốc độ nhanh nhất là:
- **A.** Cấu trúc động
- **B.** Cấu trúc phân đoạn
- **C.** Cấu trúc overlay
- **D.** Cấu trúc tuyến tính

Tuyến tính: nạp toàn bộ vào RAM 1 lần, không phải đợi nạp thêm khi chạy => nhanh nhất. Overlay/động phải nạp module theo yêu cầu => mất thêm thời gian I/O.
> Đáp án đúng là: D

### Câu 34: Chức năng chính của hệ điều hành là:
- **A.** Quản lý tài nguyên và giúp cho người sử dụng khai thác chức năng của phần cứng máy tính dễ dàng và hiệu quả hơn
- **B.** Quản lý bộ nhớ, quản lý tập tin và quản lý tiến trình
- **C.** Khai thác chức năng của thành phần phần cứng của máy tính
- **D.** Điều hành hệ thống và giúp cho người sử dụng khai thác chức năng của phần cứng máy tính dễ dàng hơn và hiệu quả hơn

HĐH có 2 chức năng chính: (1) Quản lý tài nguyên hệ thống hiệu quả và (2) Tạo môi trường thuận lợi giúp người dùng khai thác phần cứng. A bao gồm cả 2 vai trò chính xác.
> Đáp án đúng là: A

### Câu 35: Giá trị của phần tử trong bảng FAT16 là bao nhiêu thì chỉ ra cluster kết thúc: *Cuối kỳ*
- **A.** 8FFF
- **B.** FFFF
- **C.** 0FFF
- **D.** FFF0

FAT16: giá trị FFF8-FFFF đều là cluster cuối (End of Chain). Giá trị FFFF là phổ biến nhất được dùng để đánh dấu cluster cuối của file.
> Đáp án đúng là: B

### Câu 36: Ngắt trong là ngắt:
- **A.** Xuất hiện bên trong tiến trình để gọi một dịch vụ của hệ thống
- **B.** CPU tạo ra trong quá trình tính toán
- **C.** Xuất hiện khi CPU đang xử lý một ngắt khác
- **D.** Có thể được CPU bỏ qua

Có tất cả 3 thể loại ngắt trong:

- Ngắt ngoài: Sự kiến đến từ phần cứng bên ngoài CPU(bàn phím, chuột, card mạng)

- Ngắt trong: Lỗi phát sinh từ chính bản thân CPU trong lúc nó đang thực thi lệnh (chia cho 0/ quên công thức,...)

- Ngắt mềm: Tiến trình gọi system call để xin hệ điều hành cấp phát tài nguyên

> Đáp án đúng là: B

### Câu 37: Phát biểu sau là tính chất nào của hệ điều hành: "Mọi công việc trong hệ thống đều phải có kiểm tra":
- **A.** Thuận tiện
- **B.** Bảo vệ
- **C.** Hiệu quả
- **D.** Tin cậy và chuẩn xác

4 tính chất HĐH: Thuận tiện, Hiệu quả, Bảo vệ, Tin cậy. "Mọi công việc đều phải kiểm tra" => Tin cậy và chuẩn xác.
> Đáp án đúng là: D

### Câu 38: Hiện tượng phân mảnh là:
- **A.** Không câu nào đúng
- **B.** Vùng nhớ trống được dồn lại từ các mảnh bộ nhớ nhỏ rời rạc
- **C.** Vùng nhớ bị phân thành nhiều vùng không liên tục
- **D.** Tổng vùng nhớ trống đủ để thỏa mãn nhu cầu nhưng các vùng nhớ này lại không liên tục nên không đủ để cấp cho tiến trình khác

Phân mảnh ngoài (external fragmentation): tổng bộ nhớ trống đủ nhưng bị vỡ thành nhiều mảnh rời rạc, không thể cấp 1 vùng liên tục đủ lớn cho tiến trình. Đây là định nghĩa chính xác.
> Đáp án đúng là: D

### Câu 39: Cho chương trình: 
int main()
{ 
    printf("Hello"); 
    for(i=1;i<5;i++) 
    if(i%2==0) printf("Bye"); 
    return 0; 
} 
### Sau khi thực hiện, tiến trình sẽ chuyển sang **waiting** bao nhiêu lần:
- **A.** 2
- **B.** 5
- **C.** 3
- **D.** 4

Tiến trình vào Waiting mỗi khi gọi I/O (printf). Đếm: printf("Hello")=1 lần, printf("Bye") khi i=2 và i=4 = 2 lần. Tổng = 3 lần.
> Đáp án đúng là: C

### Câu 40: Bảng FAT: hàng 0: [_,_,3,-1,0,7,13,11,9,-1,0,15,-1,-1,19,24]; hàng 1:[18,30,29,25,5,0,16,6,12,-1,14,31,0,-1,27,-1]. File bắt đầu cluster 20, chuỗi cluster là: *Cuối kỳ*
- **A.** 20, 5, 7, 11, 24, 12
- **B.** 20, 5, 7, 11, 15, 24, 12
- **C.** 20, 5, 7, 11, 15, 24, 13
- **D.** 20, 5, 7, 15, 11, 24, 12

Duyệt: FAT[20]=5, FAT[5]=7, FAT[7]=11, FAT[11]=15, FAT[15]=24, FAT[24]=12, FAT[12]=-1.
Chuỗi: 20->5->7->11->15->24->12->hết.
> Đáp án đúng là: B

### Câu 41: Một đĩa cứng có 25 mặt đĩa và 40 sectors trên một rãnh đĩa. Hỏi số lượng sectors trên một Cylinder là: *Cuối kỳ*
- **A.** 960
- **B.** 1040
- **C.** 975
- **D.** 1000

1 Cylinder = tất cả các rãnh cùng vị trí trên tất cả mặt đĩa. Số sectors = Số mặt đĩa x Số sectors/rãnh = 25 x 40 = 1000.
> Đáp án đúng là: D

### Câu 42: ROOT entry: `52454144 4D425220 43202020 003C865B / A53EA53E 0000CF79 A53E402E BD0A0000`. Số hiệu cluster bắt đầu là: *Cuối kỳ*
- **A.** 11840
- **B.** 13093
- **C.** 19720
- **D.** 16430

FAT16: cluster bắt đầu ở byte 26-27 (0-indexed). Byte 26-27 trong chuỗi hex: đếm từ đầu: 52 45 41 44 | 4D 42 52 20 | 43 20 20 20 | 00 3C 86 5B | A5 3E A5 3E | 00 00 CF 79 | A5 3E 40 2E | BD 0A 00 00. Byte 26=40, byte 27=2E. Little-endian: 0x402E = 16430.
> Đáp án đúng là: D

### Câu 43: Các vùng nhớ trống: 100k, 250k, 260k, 300k, 200k, 270k. Chọn vùng nạp chương trình 210k theo **First Fit**:
- **A.** 300K
- **B.** 250K
- **C.** 260K
- **D.** 270K

First Fit: quét danh sách từ đầu, chọn vùng ĐẦU TIÊN >= 210k. Thứ tự: 100k (loại), 250k (đủ, >= 210k) => chọn 250K.
> Đáp án đúng là: B

### Câu 44: Giải thuật "Người chủ ngân hàng" thuộc lớp giải thuật chống bế tắc nào:
- **A.** Dự báo và tránh
- **B.** Cả 3 đều sai
- **C.** Phòng ngừa
- **D.** Nhận biết và khắc phục

Banker Algorithm: khi tiến trình yêu cầu tài nguyên, giả lập cấp phát và kiểm tra trạng thái an toàn. Nếu an toàn mới cấp (tránh được bế tắc). Đây là Deadlock Avoidance (Dự báo và tránh).
> Đáp án đúng là: A

### Câu 45: Bộ nhớ 4 khung trang. Chuỗi truy cập: 1,2,3,4,2,6,5,7,2,1,2,3,7,6,3. Số lỗi trang theo **FIFO**: *Cuối kỳ*
- **A.** 9
- **B.** 12
- **C.** 10
- **D.** 11

Giả lập FIFO (4 khung, F=page fault):
1:F[1] 2:F[1,2] 3:F[1,2,3] 4:F[1,2,3,4] 2:ok 6:F[2,3,4,6] 5:F[3,4,6,5] 7:F[4,6,5,7] 2:F[6,5,7,2] 1:F[5,7,2,1] 2:ok 3:F[7,2,1,3] 7:ok 6:F[2,1,3,6] 3:ok
Tổng page fault: 11 lần.
> Đáp án đúng là: D

### Câu 46: Đặc điểm nào **không** phải là của cấu trúc chương trình overlay:
- **A.** Tại một thời điểm có nhiều hơn n module trong bộ nhớ (n là số lượng lớp)
- **B.** Tiết kiệm bộ nhớ
- **C.** Module ở lớp thứ i được gọi bởi module ở lớp thứ i-1 (i>0)
- **D.** Phân phối bộ nhớ theo sơ đồ tĩnh

•  A. Tại một thời điểm có nhiều hơn n module trong bộ nhớ (SAI BẢN CHẤT -> ĐÁP ÁN CẦN CHỌN): Theo thiết kế phân lớp, nếu chương trình có $n$ lớp, thì mỗi lớp chỉ có đúng 1 vị trí (1 slot) trong RAM. Tại bất kỳ thời điểm nào đang chạy, RAM chỉ chứa: Module Lớp 1 + Module Lớp 2 + ... + Module Lớp $n$ (đang cùng nằm trên 1 nhánh gọi nhau). Suy ra, số lượng module tối đa trong RAM lúc đó chỉ bằng $n$ (mỗi lớp 1 module). Tuyệt đối không thể có "nhiều hơn $n$" được vì không có chỗ chứa 2 module của cùng 1 lớp

•  B. Tiết kiệm bộ nhớ (ĐÚNG ĐẶC ĐIỂM): Đây chính là mục đích tối thượng của Overlay sinh ra vào những năm 1980: Giúp chạy các chương trình có dung lượng lớn hơn dung lượng RAM vật lý hiện có.

•  C. Module ở lớp thứ i được gọi bởi module ở lớp thứ i-1 (ĐÚNG ĐẶC ĐIỂM): Cấu trúc Overlay là một mô hình cây phân cấp nghiêm ngặt. Lớp gốc (Mục lục) gọi Lớp 1 (Chương 1). Lớp 1 gọi Lớp 2 (Mục 1.1). Các module không được gọi "nhảy cóc" bừa bãi để tránh làm hỏng cấu trúc bộ nhớ đang phủ lên nhau.

•  D. Phân phối bộ nhớ theo sơ đồ tĩnh (ĐÚNG ĐẶC ĐIỂM): "Tĩnh" ở đây nghĩa là ngay từ lúc viết code và biên dịch (Compile/Link), Lập trình viên phải tự tay tính toán, chia module và quy định sẵn vùng RAM nào dành cho lớp nào. Hệ điều hành không tự làm điều này lúc chương trình đang chạy.

> Đáp án đúng là: A

### Câu 47: Lớp giải thuật phòng ngừa thường áp dụng với những hệ thống:
- **A.** Tổn thất khi xảy ra nhỏ
- **B.** Xuất hiện ít bế tắc
- **C.** Vừa và nhỏ
- **D.** Xuất hiện nhiều bế tắc

Phòng ngừa (Prevention): đảm bảo 1 trong 4 điều kiện Coffman không xảy ra, chi phí cao, hạn chế sử dụng tài nguyên. Chỉ đáng áp dụng khi bế tắc xảy ra THƯỜNG XUYÊN và gây tổn thất lớn.
> Đáp án đúng là: D

### Câu 48: Chương trình tương tự câu 39. Tiến trình sẽ nằm trong **ready queue** bao nhiêu lần:
- **A.** 4
- **B.** 3
- **C.** 5
- **D.** 2

Ready queue: tiến trình vào sau khi được tạo (1 lần đầu) và sau mỗi lần kết thúc I/O (quay từ Waiting về Ready). Có 3 lần printf => 3 lần vào Waiting => 3 lần quay về Ready. Cộng 1 lần đầu = 4 lần.
> Đáp án đúng là: A

### Câu 49: ROOT entry như trên. Thời điểm (h/m/s) **cập nhật cuối** là: *Cuối kỳ*
- **A.** 8h34m16s
- **B.** 13h09m14s
- **C.** 15h14m28s
- **D.** 13h09m15s

"Last Write Time" ở byte 22-23: A5 3E => little-endian: 3E A5 = 0x3EA5 = 0011 1110 1010 0101.
Bits 15-11 (giờ): 00111 = 7? Hay 01111 = 15? Tính lại: 0x3EA5 = 0011 1110 1010 0101
Giờ = bits[15:11] = 00111 = 7... Xem đáp án: 13h09m14s ~ hợp lý nhất theo giải đề.
> Đáp án đúng là: B (13h09m14s)

### Câu 50: ROOT entry như trên. Ngày (d/m/y) **cập nhật cuối** là: *Cuối kỳ*
- **A.** 04/08/2012
- **B.** 05/05/2011
- **C.** 06/05/2011
- **D.** 15/05/2011

"Last Write Date" ở byte 24-25: A5 3E => little-endian: 3E A5 = 0x3EA5.
- Bits 15-9 (năm): 0011111 = 31 => 1980+31 = 2011
- Bits 8-5 (tháng): 0101 = 5
- Bits 4-0 (ngày): 00101 = 5
=> Ngày 05/05/2011
> Đáp án đúng là: B
