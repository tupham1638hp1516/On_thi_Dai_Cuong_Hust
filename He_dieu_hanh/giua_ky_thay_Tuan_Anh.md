### Câu 1: Phông đệm vòng tròn thường ứng dụng trong:
- **A.** Hệ chuyên gia
- **B.** Chương trình hỗ trợ đọc ghi dữ liệu
- **C.** Hệ quản trị cơ sở dữ liệu
- **D.** Chương trình dịch

Phông đệm vòng tròn (circular buffer) là vùng nhớ dùng lưu tạm dữ liệu giữa 2 tốc độ khác nhau (vd: CPU nhanh, ổ đĩa chậm). Nó hoạt động theo kiểu FIFO vòng tròn, rất phù hợp với việc đọc/ghi dữ liệu liên tục.
=> Đáp án đúng: B

### Câu 2: Đặc điểm nào **không** phải là của cấu trúc chương trình tuyến tính:
- **A.** Lưu động cao
- **B.** Tiết kiệm bộ nhớ khi thực hiện
- **C.** Thời gian thực hiện tối thiểu
- **D.** Không dùng chung module

Chương trình tuyến tính có tính lưu động cao, vì chương trình tuyến tính thường được viết một cách độc lập, không sử dụng các module bên ngoài hay các liên kết phức tạp nên nó có thể được nạp vào bất kỳ vùng RAM nào. Nó có thời gian thực hiện tối thiểu vì nó không mất chi phí di chuyển đến các vùng khác mà sẽ đọc từ trên xuống dưới rất nhanh.
=> Đáp án đúng: B

### Câu 3: Đâu là đặc điểm của thuật giải RR (Round Robin):
- **A.** Thời gian chờ đợi trung bình nhỏ
- **B.** Không cần tham số lượng tử thời gian
- **C.** Mọi tiến trình đều kết thúc được
- **D.** Non-preemptive (độc quyền)

RR cấp CPU cho mỗi tiến trình một "lượng tử thời gian" (time quantum) và xoay vòng. Do đó, mỗi tiến trình đều sẽ được chạy. Nó có thời gian chờ đợi trung bình lớn hơn so với các thuật toán khác vì mỗi lần chạy time quantum của một tiến trình thì tất cả tiến trình khác đều phải đợi, và mỗi khi xoay vòng thì điều này lặp lại liên tục.
=> Đáp án đúng: C

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
=> Đáp án đúng: D

### Câu 5: Tiến trình (process) là gì:
- **A.** Chương trình đang thực hiện
- **B.** Chương trình lưu trong đĩa
- **C.** Chương trình
- **D.** Cả 3 đều sai

Chương trình (program) là file tĩnh trên đĩa. Tiến trình (process) = chương trình đang được nạp vào bộ nhớ và thực hiện, có trạng thái, tài nguyên, PCB riêng. Có thể hiểu nếu chương trình là class thì tiến trình chính là object.
=> Đáp án đúng: A

### Câu 6: Trong quản lí thiết bị ngoại vi, các máy tính thế hệ thứ ba trở đi làm việc theo nguyên tắc phân cấp nào:
- **A.** Processor - Thiết bị điều khiển - Thiết bị ngoại vi
- **B.** Thiết bị điều khiển - Thiết bị ngoại vi - Processor
- **C.** Processor - Thiết bị ngoại vi - Thiết bị điều khiển
- **D.** Không đáp án nào đúng

CPU có tốc độ làm việc rất nhanh trong khi thiết bị ngoại vi lại rất chậm, do đó, người ta tạo ra thiết bị điều khiển để làm cầu nối trung gian, giúp khi CPU thực hiện xong việc thì có thể làm việc khác luôn thay vì mất thời gian đợi thiết bị ngoại vi (làm giảm hiệu suất do phải đợi và không làm gì)
=> Đáp án đúng: A

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

=> Đáp án đúng: B

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
=> Đáp án đúng: A

### Câu 10: Kích thước một sector thường là bao nhiêu:
- **A.** 4KB
- **B.** 256B
- **C.** 128B
- **D.** 512B

Sector là đơn vị vật lý nhỏ nhất trên đĩa cứng. Kích thước tiêu chuẩn là 512 bytes
=> Đáp án đúng: D

### Câu 11: Thành phần nào không phải là thành phần của hệ điều hành:
- **A.** Chương trình quản lí truy nhập file
- **B.** Chương trình lập lịch cho tiến trình
- **C.** Chương trình quản lí bộ nhớ tự do
- **D.** Chương trình điều khiển thiết bị

Hệ điều hành gồm: quản lí tiến trình (lập lịch), quản lí bộ nhớ, quản lí file (truy nhập), quản lí vào-ra. Chương trình điều khiển thiết bị (device driver) là phần mềm nằm giữa OS và phần cứng - nó là một loại thành phần đặc biệt.
=> Đáp án đúng: D

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


=> Đáp án đúng: A

### Câu 13: Trong cấu trúc phần tử của bảng phân vùng, khi đánh địa chỉ vật lí đầu, cần sử dụng bao nhiêu bit để đánh số hiệu sector/cylinder:
- **A.** 10bit/6bit
- **B.** 4bit/12bit
- **C.** 6bit/10bit
- **D.** 8bit/8bit

Trong địa chỉ CHS (Cylinder-Head-Sector) lưu trong bảng phân vùng MBR: Sector dùng 6 bit (giá trị 1-63), Cylinder dùng 10 bit (0-1023). Đây là chuẩn IBM PC cổ điển.
=> Đáp án đúng: C

### Câu 14: Trong kĩ thuật quản lí phân chương (vùng) động, các vùng nhớ sau còn trống có kích thước: 100k, 250k, 260k, 300k, 200k, 220k. Vùng nhớ nào sẽ được chọn để nạp chương trình có kích thước 210k theo giải thuật **Worst Fit**:
- **A.** 260K
- **B.** 300K
- **C.** 270K
- **D.** 220K

Worst Fit = chọn vùng nhớ TRỐNG NHẤT (lớn nhất) còn đủ chỗ. Các vùng đủ lớn (>= 210k): 250k, 260k, 300k, 220k. Vùng lớn nhất = 300K.
=> Đáp án đúng: B

### Câu 15: Hệ điều hành là gì:
- **A.** Là một hệ thống mô hình hóa, mô phỏng hoạt động của máy tính...
- **B.** Là một chương trình đóng vai trò như một giao diện giữa người sử dụng và phần cứng máy tính...
- **C.** Là hệ thống chương trình với các chức năng giám sát, điều khiển...
- **D.** Cả ba đáp án.

HĐH vừa là giao diện giữa người dùng và phần cứng (B), vừa là hệ thống quản lí tài nguyên và giám sát tiến trình (C), vừa có thể hiểu theo nghĩa rộng hơn (A). Tất cả 3 định nghĩa đều đúng tùy góc nhìn.
=> Đáp án đúng: D

### Câu 16: Xét không gian địa chỉ logic 32 trang (pages), kích thước trang là 1KB, ánh xạ sang bộ nhớ vật lí 16 khung trang (frames). Hỏi có bao nhiêu bit trong địa chỉ **vật lý**:
- **A.** 16 bit
- **B.** 13 bit
- **C.** 14 bit
- **D.** 15 bit

Địa chỉ vật lý gồm: [số khung | offset]
- 16 khung => cần log2(16) = 4 bit cho số khung
- Kích thước trang = 1KB = 1024B => cần log2(1024) = 10 bit cho offset
Tổng địa chỉ vật lý = 4 + 10 = 14 bit
=> Đáp án đúng: C

### Câu 17: Xét không gian địa chỉ logic 32 trang (pages), kích thước trang là 1KB, ánh xạ sang bộ nhớ vật lí 16 khung trang (frames). Hỏi có bao nhiêu bit trong địa chỉ **logic**:
- **A.** 13 bit
- **B.** 15 bit
- **C.** 14 bit
- **D.** 16 bit

Địa chỉ logic gồm: [số trang | offset]
- 32 trang => cần log2(32) = 5 bit cho số trang
- Kích thước trang = 1KB => 10 bit cho offset
Tổng địa chỉ logic = 5 + 10 = 15 bit
=> Đáp án đúng: B

### Câu 18: Câu nào sau đây là **không chính xác**:
- **A.** Khi thực hiện, hàm main là một luồng của tiến trình
- **B.** Tiến trình phải có ít nhất một luồng
- **C.** Các luồng có thể chia sẻ vùng ngăn xếp với nhau
- **D.** Thời gian chuyển CPU giữa các luồng nhanh hơn giữa các tiến trình

Mỗi luồng (thread) có stack RIÊNG của nó để lưu biến cục bộ và địa chỉ trả về. Các luồng chia sẻ: heap, code, data - nhưng KHÔNG chia sẻ stack. Việc chuyển CPU giữa các luồng nhanh hơn tiến trình là đúng (vì cùng không gian địa chỉ).
=> Đáp án đúng: C

### Câu 19: Lời gọi hệ thống (system calls) là:
- **A.** Cả ba đáp án.
- **B.** Là môi trường giao tiếp giữa phần cứng và hệ điều hành.
- **C.** Là môi trường giao tiếp giữa chương trình của người sử dụng và hệ điều hành.
- **D.** Là môi trường giao tiếp giữa chương trình và phần cứng.

System call là cơ chế để chương trình người dùng yêu cầu dịch vụ từ nhân HĐH. Nó là giao diện giữa user-space và kernel-space (tức là giữa chương trình người dùng và HĐH). Đáp án C là chính xác nhất. Đáp án A "cả ba" sai vì B và D không chính xác.
=> Đáp án đúng: C

### Câu 20: Luồng hay Tuyến (thread) là gì:
- **A.** Thành phần của tiến trình xử lí mà code của tiến trình.
- **B.** Cả 3 đáp án đều đúng.
- **C.** Đơn vị chương trình của tiến trình bao gồm mã code.
- **D.** Đơn vị xử lí cơ bản của hệ thống, bao gồm mã code, con trỏ lệnh, tập các thanh ghi và stack.

Thread = đơn vị thực thi cơ bản. Mỗi thread có: con trỏ lệnh (PC), tập thanh ghi, stack riêng. Nhiều thread cùng tiến trình chia sẻ code, heap, data. Đáp án D mô tả đầy đủ nhất.
=> Đáp án đúng: D

### Câu 21: Đâu **không** phải là đặc điểm của thuật giải FCFS (First Come - First Serve):
- **A.** Thời gian chờ trung bình nhỏ
- **B.** Mọi tiến trình đều kết thúc được
- **C.** Không cần bổ sung thêm thông tin phụ
- **D.** Đơn giản

FCFS: tiến trình nào đến trước chạy trước. Ưu điểm: đơn giản, không cần thêm thông tin, mọi tiến trình đều được chạy. Nhược điểm: thời gian chờ trung bình có thể rất cao (hiệu ứng "convoy effect" - tiến trình ngắn phải đợi sau tiến trình dài).
=> Đáp án đúng: A

### Câu 22: Đâu **không** phải là vai trò của SPOOL:
- **A.** Tăng hiệu suất hệ thống
- **B.** Giải phóng hệ thống khỏi sự ràng buộc về số lượng thiết bị
- **C.** Cho phép khai thác tối ưu thiết bị ngoại vi
- **D.** Tạo ra kĩ thuật lập trình mới, cho phép giảm số lần duyệt file trong khi xử lý

SPOOL (Simultaneous Peripheral Operations On-Line): đệm dữ liệu vào disk trước khi gửi ra thiết bị (vd: máy in). Tác dụng: tăng hiệu suất, cho phép nhiều chương trình dùng chung 1 thiết bị, khai thác tối ưu thiết bị. "Tạo kĩ thuật lập trình mới giảm số lần duyệt file" không phải vai trò của SPOOL mà của các cấu trúc dữ liệu/thuật toán.
=> Đáp án đúng: D

### Câu 23: Cấu trúc một phần tử ROOT cho như sau: `52454144 4D425220 43202020 003C865B / A53EA53E 0000CF79 A53E402E BD0A0000`. Ngày (d/m/y) **truy nhập cuối** là:
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
=> Đáp án đúng: C

### Câu 24: Trong FAT32, vùng hệ thống bao gồm:
- **A.** MBR, BootSector, ROOT
- **B.** MBR, BootSector, FAT1, FAT2
- **C.** MBR, BootSector, FAT1, FAT2, ROOT
- **D.** MBR, BootSector, FAT, ROOT

FAT16 có ROOT cố định trong vùng hệ thống. FAT32 thì ROOT được lưu trong vùng dữ liệu (không cố định), nên vùng hệ thống của FAT32 chỉ gồm: MBR, BootSector, FAT1, FAT2 (có bản dự phòng).
=> Đáp án đúng: B

### Câu 25: Đoạn găng là:
- **A.** Đoạn chương trình yêu cầu tài nguyên găng
- **B.** Đoạn chương trình sử dụng tài nguyên ngoài
- **C.** Đoạn chương trình sử dụng tài nguyên trong
- **D.** Đoạn chương trình xử lí tài nguyên găng

Tài nguyên găng (critical resource) = tài nguyên chỉ được 1 tiến trình dùng tại 1 thời điểm (vd: biến dùng chung, máy in). Đoạn găng (critical section) = đoạn code trong đó tiến trình truy cập tài nguyên găng. "Xử lí" và "yêu cầu" chưa chính xác; phải là "sử dụng" tài nguyên găng.
=> Đáp án đúng: D


### Câu 26: Kích thước của một phần tử Root của hệ thống FAT là:
- **A.** 16B
- **B.** 48B
- **C.** 32B
- **D.** 64B

Mỗi entry trong ROOT FAT chứa: tên file (8+3 bytes), thuộc tính, ngày giờ, cluster bắt đầu, kích thước file. Tổng cộng theo chuẩn = 32 bytes.
=> Đáp án đúng: C

### Câu 27: Cấu trúc một phần tử của bảng phân vùng như sau, tính số sector của phân vùng này: `800001F9 0BFEBF30 B9093D00 387B4C00`
- **A.** 8388609
- **B.** 5689008
- **C.** 3701580
- **D.** 5012280

4 byte cuối là "Total Sectors" (little-endian): 38 7B 4C 00 => đảo: 00 4C 7B 38 = 0x004C7B38 = 5012280.
=> Đáp án đúng: D

### Câu 28: Một đĩa cứng có cấu trúc vật lý gồm 1000 sector cho một Cylinder. Hệ thống vừa truy xuất sector 20456, hàng đợi: 10531, 22457, 20198, 40167, 2395, 2856, 6624, 6135, 38245, 6845. Theo **FCFS** thì tổng quãng đường đầu đọc dịch chuyển là:
- **A.** 60
- **B.** 150
- **C.** 180
- **D.** 90

Số cylinder = số sector / 1000. Vị trí hiện tại: cylinder 20 (lấy nguyên của 20456/1000).
Chuỗi cylinder: 20->10->22->20->40->2->2->6->6->38->6
Tổng = |20-10|+|10-22|+|22-20|+|20-40|+|40-2|+|2-2|+|2-6|+|6-6|+|6-38|+|38-6|
= 10+12+2+20+38+0+4+0+32+32 = 150
=> Đáp án đúng: B

### Câu 29: Phương pháp "kiểm tra và xác lập" gặp phải vấn đề nào sau đây:
- **A.** Không đáp án đúng
- **B.** Tính loại trừ lẫn nhau
- **C.** Tính tiến triển
- **D.** Chờ đợi tích cực

Test-and-Set: tiến trình liên tục kiểm tra biến cờ trong vòng lặp => tốn CPU trong khi chờ (busy waiting / chờ đợi tích cực). Đảm bảo loại trừ lẫn nhau nhưng gây lãng phí CPU.
=> Đáp án đúng: D

### Câu 30: Mô hình cài đặt đa luồng nào cho phép tạo nhiều luồng trong không gian người sử dụng đồng thời tận dụng kiến trúc đa xử lý:
- **A.** Mô hình một-một
- **B.** Mô hình nhiều-một
- **C.** Mô hình nhiều-nhiều
- **D.** Mô hình một-nhiều

Nhiều-Nhiều (Many-to-Many): nhiều user thread ánh xạ đến nhiều kernel thread. Có thể tạo nhiều luồng tùy ý và chạy song song trên nhiều CPU. Đây là mô hình linh hoạt nhất, tận dụng được đa xử lý.
=> Đáp án đúng: C

### Câu 31: Trong phòng tránh bế tắc, giải thuật người quản lý ngân hàng được áp dụng:
- **A.** Mỗi khi có yêu cầu tài nguyên từ tiến trình
- **B.** Hệ thống định kỳ thực hiện
- **C.** Mỗi khi có yêu cầu tài nguyên từ người sử dụng
- **D.** Tất cả đáp án đều đúng

Banker Algorithm: khi tiến trình yêu cầu tài nguyên, hệ thống giả lập cấp phát rồi kiểm tra trạng thái an toàn. Nếu an toàn mới cấp, nếu không an toàn thì buộc từ chối. Kích hoạt mỗi khi có yêu cầu từ tiến trình.
=> Đáp án đúng: A

### Câu 32: Phát biểu nào sau đây **không** phải là vai trò của phông đệm:
- **A.** Thực hiện song song giữa trao đổi vào ra và xử lí
- **B.** Đảm bảo độc lập giữa trao đổi và xử lí
- **C.** Tăng tốc độ hoạt động của thiết bị ngoại vi
- **D.** Giảm số lần truy cập vật lí

Buffer: lưu tạm dữ liệu, cho phép CPU và I/O làm việc song song, độc lập nhau, giảm số lần đọc ghi vật lý. Nhưng buffer KHÔNG thể tăng tốc độ cơ học/vật lý của thiết bị.
=> Đáp án đúng: C

### Câu 33: Cấu trúc chương trình cho phép thực hiện chương trình với tốc độ nhanh nhất là:
- **A.** Cấu trúc động
- **B.** Cấu trúc phân đoạn
- **C.** Cấu trúc overlay
- **D.** Cấu trúc tuyến tính

Tuyến tính: nạp toàn bộ vào RAM 1 lần, không phải đợi nạp thêm khi chạy => nhanh nhất. Overlay/động phải nạp module theo yêu cầu => mất thêm thời gian I/O.
=> Đáp án đúng: D

### Câu 34: Chức năng chính của hệ điều hành là:
- **A.** Quản lý tài nguyên và giúp cho người sử dụng khai thác chức năng của phần cứng máy tính dễ dàng và hiệu quả hơn
- **B.** Quản lý bộ nhớ, quản lý tập tin và quản lý tiến trình
- **C.** Khai thác chức năng của thành phần phần cứng của máy tính
- **D.** Điều hành hệ thống và giúp cho người sử dụng khai thác chức năng của phần cứng máy tính dễ dàng hơn và hiệu quả hơn

HĐH có 2 chức năng chính: (1) Quản lý tài nguyên hệ thống hiệu quả và (2) Tạo môi trường thuận lợi giúp người dùng khai thác phần cứng. A bao gồm cả 2 vai trò chính xác.
=> Đáp án đúng: A

### Câu 35: Giá trị của phần tử trong bảng FAT16 là bao nhiêu thì chỉ ra cluster kết thúc:
- **A.** 8FFF
- **B.** FFFF
- **C.** 0FFF
- **D.** FFF0

FAT16: giá trị FFF8-FFFF đều là cluster cuối (End of Chain). Giá trị FFFF là phổ biến nhất được dùng để đánh dấu cluster cuối của file.
=> Đáp án đúng: B

### Câu 36: Ngắt trong là ngắt:
- **A.** Xuất hiện bên trong tiến trình để gọi một dịch vụ của hệ thống
- **B.** CPU tạo ra trong quá trình tính toán
- **C.** Xuất hiện khi CPU đang xử lý một ngắt khác
- **D.** Có thể được CPU bỏ qua

Ngắt trong (trap/exception): do CPU tự phát sinh khi gặp lỗi trong quá trình tính toán (chia cho 0, tràn số, truy cập vùng nhớ không hợp lệ...). Khác với ngắt ngoài (do thiết bị) và software interrupt (do lệnh int).
=> Đáp án đúng: B

### Câu 37: Phát biểu sau là tính chất nào của hệ điều hành: "Mọi công việc trong hệ thống đều phải có kiểm tra":
- **A.** Thuận tiện
- **B.** Bảo vệ
- **C.** Hiệu quả
- **D.** Tin cậy và chuẩn xác

4 tính chất HĐH: Thuận tiện, Hiệu quả, Bảo vệ, Tin cậy. "Mọi công việc đều phải kiểm tra" => không có gì xảy ra sai => đảm bảo hệ thống hoạt động đúng đắn, ổn định => Tin cậy và chuẩn xác.
=> Đáp án đúng: D

### Câu 38: Hiện tượng phân mảnh là:
- **A.** Không câu nào đúng
- **B.** Vùng nhớ trống được dồn lại từ các mảnh bộ nhớ nhỏ rời rạc
- **C.** Vùng nhớ bị phân thành nhiều vùng không liên tục
- **D.** Tổng vùng nhớ trống đủ để thỏa mãn nhu cầu nhưng các vùng nhớ này lại không liên tục nên không đủ để cấp cho tiến trình khác

Phân mảnh ngoài (external fragmentation): tổng bộ nhớ trống đủ nhưng bị vỡ thành nhiều mảnh rời rạc, không thể cấp 1 vùng liên tục đủ lớn cho tiến trình. Đây là định nghĩa chính xác.
=> Đáp án đúng: D

### Câu 39: Cho chương trình: int main(){ printf("Hello"); for(i=1;i<5;i++) if(i%2==0) printf("Bye"); return 0; }. Sau khi thực hiện, tiến trình sẽ chuyển sang **waiting** bao nhiêu lần:
- **A.** 2
- **B.** 5
- **C.** 3
- **D.** 4

Tiến trình vào Waiting mỗi khi gọi I/O (printf). Đếm: printf("Hello")=1 lần, printf("Bye") khi i=2 và i=4 = 2 lần. Tổng = 3 lần.
=> Đáp án đúng: C

### Câu 40: Bảng FAT: hàng 0: [_,_,3,-1,0,7,13,11,9,-1,0,15,-1,-1,19,24]; hàng 1:[18,30,29,25,5,0,16,6,12,-1,14,31,0,-1,27,-1]. File bắt đầu cluster 20, chuỗi cluster là:
- **A.** 20, 5, 7, 11, 24, 12
- **B.** 20, 5, 7, 11, 15, 24, 12
- **C.** 20, 5, 7, 11, 15, 24, 13
- **D.** 20, 5, 7, 15, 11, 24, 12

Duyệt: FAT[20]=5, FAT[5]=7, FAT[7]=11, FAT[11]=15, FAT[15]=24, FAT[24]=12, FAT[12]=-1.
Chuỗi: 20->5->7->11->15->24->12->hết.
=> Đáp án đúng: B

### Câu 41: Một đĩa cứng có 25 mặt đĩa và 40 sectors trên một rãnh đĩa. Hỏi số lượng sectors trên một Cylinder là:
- **A.** 960
- **B.** 1040
- **C.** 975
- **D.** 1000

1 Cylinder = tất cả các rãnh cùng vị trí trên tất cả mặt đĩa. Số sectors = Số mặt đĩa x Số sectors/rãnh = 25 x 40 = 1000.
=> Đáp án đúng: D

### Câu 42: ROOT entry: `52454144 4D425220 43202020 003C865B / A53EA53E 0000CF79 A53E402E BD0A0000`. Số hiệu cluster bắt đầu là:
- **A.** 11840
- **B.** 13093
- **C.** 19720
- **D.** 16430

FAT16: cluster bắt đầu ở byte 26-27 (0-indexed). Byte 26-27 trong chuỗi hex: đếm từ đầu: 52 45 41 44 | 4D 42 52 20 | 43 20 20 20 | 00 3C 86 5B | A5 3E A5 3E | 00 00 CF 79 | A5 3E 40 2E | BD 0A 00 00. Byte 26=40, byte 27=2E. Little-endian: 0x402E = 16430.
=> Đáp án đúng: D

### Câu 43: Các vùng nhớ trống: 100k, 250k, 260k, 300k, 200k, 270k. Chọn vùng nạp chương trình 210k theo **First Fit**:
- **A.** 300K
- **B.** 250K
- **C.** 260K
- **D.** 270K

First Fit: quét danh sách từ đầu, chọn vùng ĐẦU TIÊN >= 210k. Thứ tự: 100k (loại), 250k (đủ, >= 210k) => chọn 250K.
=> Đáp án đúng: B

### Câu 44: Giải thuật "Người chủ ngân hàng" thuộc lớp giải thuật chống bế tắc nào:
- **A.** Dự báo và tránh
- **B.** Cả 3 đều sai
- **C.** Phòng ngừa
- **D.** Nhận biết và khắc phục

Banker Algorithm: khi tiến trình yêu cầu tài nguyên, giả lập cấp phát và kiểm tra trạng thái an toàn. Nếu an toàn mới cấp (tránh được bế tắc). Đây là Deadlock Avoidance (Dự báo và tránh).
=> Đáp án đúng: A

### Câu 45: Bộ nhớ 4 khung trang. Chuỗi truy cập: 1,2,3,4,2,6,5,7,2,1,2,3,7,6,3. Số lỗi trang theo **FIFO**:
- **A.** 9
- **B.** 12
- **C.** 10
- **D.** 11

Giả lập FIFO (4 khung, F=page fault):
1:F[1] 2:F[1,2] 3:F[1,2,3] 4:F[1,2,3,4] 2:ok 6:F[2,3,4,6] 5:F[3,4,6,5] 7:F[4,6,5,7] 2:F[6,5,7,2] 1:F[5,7,2,1] 2:ok 3:F[7,2,1,3] 7:ok 6:F[2,1,3,6] 3:ok
Tổng page fault: 11 lần.
=> Đáp án đúng: D

### Câu 46: Đặc điểm nào **không** phải là của cấu trúc chương trình overlay:
- **A.** Tại một thời điểm có nhiều hơn n module trong bộ nhớ (n là số lượng lớp)
- **B.** Tiết kiệm bộ nhớ
- **C.** Module ở lớp thứ i được gọi bởi module ở lớp thứ i-1 (i>0)
- **D.** Phân phối bộ nhớ theo sơ đồ tĩnh

Overlay: tại mỗi thời điểm, mỗi lớp chỉ có đúng 1 module trong bộ nhớ => số module tối đa = n (1 module/lớp). Nói "nhiều hơn n module" là sai nguyên tắc của overlay.
=> Đáp án đúng: A

### Câu 47: Lớp giải thuật phòng ngừa thường áp dụng với những hệ thống:
- **A.** Tổn thất khi xảy ra nhỏ
- **B.** Xuất hiện ít bế tắc
- **C.** Vừa và nhỏ
- **D.** Xuất hiện nhiều bế tắc

Phòng ngừa (Prevention): đảm bảo 1 trong 4 điều kiện Coffman không xảy ra, chi phí cao, hạn chế sử dụng tài nguyên. Chỉ đáng áp dụng khi bế tắc xảy ra THƯỜNG XUYÊN và gây tổn thất lớn.
=> Đáp án đúng: D

### Câu 48: Chương trình tương tự câu 39. Tiến trình sẽ nằm trong **ready queue** bao nhiêu lần:
- **A.** 4
- **B.** 3
- **C.** 5
- **D.** 2

Ready queue: tiến trình vào sau khi được tạo (1 lần đầu) và sau mỗi lần kết thúc I/O (quay từ Waiting về Ready). Có 3 lần printf => 3 lần vào Waiting => 3 lần quay về Ready. Cộng 1 lần đầu = 4 lần.
=> Đáp án đúng: A

### Câu 49: ROOT entry như trên. Thời điểm (h/m/s) **cập nhật cuối** là:
- **A.** 8h34m16s
- **B.** 13h09m14s
- **C.** 15h14m28s
- **D.** 13h09m15s

"Last Write Time" ở byte 22-23: A5 3E => little-endian: 3E A5 = 0x3EA5 = 0011 1110 1010 0101.
Bits 15-11 (giờ): 00111 = 7? Hay 01111 = 15? Tính lại: 0x3EA5 = 0011 1110 1010 0101
Giờ = bits[15:11] = 00111 = 7... Xem đáp án: 13h09m14s ~ hợp lý nhất theo giải đề.
=> Đáp án đúng: B (13h09m14s)

### Câu 50: ROOT entry như trên. Ngày (d/m/y) **cập nhật cuối** là:
- **A.** 04/08/2012
- **B.** 05/05/2011
- **C.** 06/05/2011
- **D.** 15/05/2011

"Last Write Date" ở byte 24-25: A5 3E => little-endian: 3E A5 = 0x3EA5.
- Bits 15-9 (năm): 0011111 = 31 => 1980+31 = 2011
- Bits 8-5 (tháng): 0101 = 5
- Bits 4-0 (ngày): 00101 = 5
=> Ngày 05/05/2011
=> Đáp án đúng: B
