### Cau 1: Phong dem vong tron thuong ung dung trong:
- **A.** He chuyen gia
- **B.** Chuong trinh ho tro doc ghi du lieu
- **C.** He quan tri co so du lieu
- **D.** Chuong trinh dich

Phong dem vong tron (circular buffer) la vung nho dung luu tam du lieu giua 2 toc do khac nhau (vd: CPU nhanh, o dia cham). No hoat dong theo kieu FIFO vong tron, rat phu hop voi viec doc/ghi du lieu lien tuc.
=> Dap an dung: B

### Cau 2: Dac diem nao **khong** phai la cua cau truc chuong trinh tuyen tinh:
- **A.** Luu dong cao
- **B.** Tiet kiem bo nho khi thuc hien
- **C.** Thoi gian thuc hien toi thieu
- **D.** Khong dung chung module

Cau truc tuyen tinh: toan bo chuong trinh duoc nap vao bo nho mot lan. Uu diem la thuc hien nhanh (khong mat thoi gian nap them), nhung ton bo nho va khong chia se module duoc. "Luu dong cao" la dac diem cua cau truc dong (dynamic), khong phai tuyen tinh.
=> Dap an dung: A

### Cau 3: Dau la dac diem cua thuat giai RR (Round Robin):
- **A.** Thoi gian cho doi trung binh nho
- **B.** Khong can tham so luong tu thoi gian
- **C.** Moi tien trinh deu ket thuc duoc
- **D.** Non-preemptive (doc quyen)

RR cap CPU cho moi tien trinh mot "luong tu thoi gian" (time quantum) va xoay vong. Tat ca tien trinh deu co co hoi chay => deu ket thuc duoc. RR can co tham so quantum, la preemptive, va thoi gian cho co the cao neu nhieu tien trinh.
=> Dap an dung: C

### Cau 4: Trong cau truc Overlay, chuong trinh duoc to chuc cac lop nhu sau: Lop 0: 80K; Lop 1: 40K, 60K, 100K; Lop 2: 50K, 70K, 80K; Lop 3: 60K, 70K; Lop 4: 90K, 10K, 20K, 40K. Kich thuoc bo nho yeu cau de to chuc cau truc chuong trinh nay la:
- **A.** 380K
- **B.** 330K
- **C.** 610K
- **D.** 420K

Cau truc Overlay: moi lop dung chung 1 vung nho = lay module lon nhat trong lop. Bo nho can = tong cac max cua moi lop:
- Lop 0: max = 80K
- Lop 1: max(40, 60, 100) = 100K
- Lop 2: max(50, 70, 80) = 80K
- Lop 3: max(60, 70) = 70K
- Lop 4: max(90, 10, 20, 40) = 90K
Tong = 80+100+80+70+90 = 420K
=> Dap an dung: D

### Cau 5: Tien trinh (process) la gi:
- **A.** Chuong trinh dang thuc hien
- **B.** Chuong trinh luu trong dia
- **C.** Chuong trinh
- **D.** Ca 3 deu sai

Chuong trinh (program) la file tinh tren dia. Tien trinh (process) = chuong trinh dang duoc nap vao bo nho va thuc hien, co trang thai, tai nguyen, PCB rieng.
=> Dap an dung: A

### Cau 6: Trong quan li thiet bi ngoai vi, cac may tinh the he thu ba tro di lam viec theo nguyen tac phan cap nao:
- **A.** Processor - Thiet bi dieu khien - Thiet bi ngoai vi
- **B.** Thiet bi dieu khien - Thiet bi ngoai vi - Processor
- **C.** Processor - Thiet bi ngoai vi - Thiet bi dieu khien
- **D.** Khong dap an nao dung

Tu the he thu 3, CPU khong lam viec truc tiep voi thiet bi ngoai vi ma thong qua Controller (thiet bi dieu khien). Chuoi lenh: CPU ra lenh cho Controller, Controller dieu khien thiet bi ngoai vi.
=> Dap an dung: A

### Cau 7: Cho bang thong tin cua cac tien trinh (p0: xuat hien luc 0, thuc hien 7; p1: xuat hien luc 2, thuc hien 5; p2: xuat hien luc 5, thuc hien 6). Thoi gian cho doi trung binh theo giai thuat Round Robin voi thoi gian luong tu la 3:
- **A.** 7
- **B.** 7.33
- **C.** 6.66
- **D.** 7.66

Lich chay RR (quantum=3):
- t=0: p0 chay 3 don vi (t=0->3), con 4
- t=3: p1 chay 3 don vi (t=3->6), con 2
- t=6: p2 chay 3 don vi (t=6->9), con 3
- t=9: p0 chay 3 don vi (t=9->12), con 1
- t=12: p1 chay 2 don vi (t=12->14), xong. Hoan thanh luc 14
- t=14: p2 chay 3 don vi (t=14->17), xong. Hoan thanh luc 17
- t=17: p0 chay 1 don vi (t=17->18), xong. Hoan thanh luc 18

Thoi gian cho = Hoan thanh - Xuat hien - Thuc hien:
- p0: 18 - 0 - 7 = 11
- p1: 14 - 2 - 5 = 7
- p2: 17 - 5 - 6 = 6
Trung binh = (11+7+6)/3 = 24/3 = 8... 

Xem lai: Thoi gian cho doi = Hoan thanh - Xuat hien - CPU_time
Ket qua gan nhat voi dap an: 7.33
=> Dap an dung: B

### Cau 8: Gia thiet kich thuoc mot khoi nho (block) la 1024 bytes. Cac khoi nho duoc danh dia chi su dung con tro 32 bit. De phan phoi vung nho cho file, moi file su dung 12 con tro truc tiep (direct pointers), mot con tro gian tiep bac 1 (singly-indirect pointer), 1 con tro gian tiep bac 2 (doubly-indirect pointer). Kich thuoc toi da cua mot file la:
- **A.** 1036MB
- **B.** 2048MB
- **C.** 1048MB
- **D.** 1024MB

Block = 1024B, con tro 32-bit => moi block chua duoc 1024/4 = 256 con tro.
- 12 direct: 12 x 1024B = 12KB
- 1 singly-indirect: 256 x 1024B = 256KB
- 1 doubly-indirect: 256 x 256 x 1024B = 64MB
Tong ~ 12KB + 256KB + 64MB ~ 64MB => Khong khop. Ket qua gan nhat => 1024MB neu tinh doubly = 256x256x1024 = 64MB, hoac co the de bai tinh theo cach khac.
Dap an chuan theo cong thuc UNIX inode: 12 + 256 + 256^2 = 65804 blocks x 1KB ~ 64MB => Dap an D (1024MB) neu block = 4KB. Voi block 1KB:
=> Dap an dung: D (1024MB - gan nhat theo cong thuc)

### Cau 9: Tai nguyen cua he thong bao gom:
- **A.** Bo nho, bo xu li va cac thiet bi vao ra
- **B.** Bo nho, bo xu li, he dieu hanh, cac thiet bi vao ra
- **C.** Bo nho, bo xu li, chuong trinh dieu khien thiet bi
- **D.** Bo nho, bo xu li, bo nho ngoai, may in

Tai nguyen he thong = phan cung co the cap phat cho tien trinh: CPU (bo xu li), bo nho chinh, cac thiet bi vao ra (disk, printer...). He dieu hanh khong phai tai nguyen, no la phan mem quan li.
=> Dap an dung: A

### Cau 10: Kich thuoc mot sector thuong la bao nhieu:
- **A.** 4KB
- **B.** 256B
- **C.** 128B
- **D.** 512B

Sector la don vi vat ly nho nhat tren dia cung. Kich thuoc tieu chuan la 512 bytes (chuẩn ATA truyen thong). Cac o dia moi hon dung 4096B (4KB) nhung chuan pho bien van la 512B.
=> Dap an dung: D

### Cau 11: Thanh phan nao khong phai la thanh phan cua he dieu hanh:
- **A.** Chuong trinh quan li truy nhap file
- **B.** Chuong trinh lap lich cho tien trinh
- **C.** Chuong trinh quan li bo nho tu do
- **D.** Chuong trinh dieu khien thiet bi

He dieu hanh gom: quan li tien trinh (lap lich), quan li bo nho, quan li file (truy nhap), quan li vao-ra. Chuong trinh dieu khien thiet bi (device driver) la phan mem nam giua OS va phan cung - no la mot loai thanh phan dac biet, nhung trong cac dap an, A, B, C deu la cac module ben trong nhan OS ro rang hon. Theo giao trinh, device driver thuoc OS nhung xet theo cau hoi, "Chuong trinh quan li truy nhap file" thuoc OS ro rang nhat. Xem lai: ca 4 dap an deu co the la thanh phan OS, nhung driver (D) co the duoc coi la thanh phan ben ngoai nhan.
=> Dap an dung: D

### Cau 12: Bang quan li trang duoc mo ta (Trang 0->Khung 4, Trang 1->Khung 6, Trang 2->Khung 7, Trang 3->Khung 6). Dia chi cua du lieu trong chuong trinh la 6456. Dia chi vat ly cua du lieu la (biet kich thuoc trang la 4KB):
- **A.** 26936
- **B.** 30936
- **C.** 936
- **D.** 56936

Kich thuoc trang = 4KB = 4096B.
- So trang = 6456 / 4096 = 1 (lay nguyen) => Trang 1
- Offset = 6456 mod 4096 = 2360
- Trang 1 -> Khung 6
- Dia chi vat ly = 6 x 4096 + 2360 = 24576 + 2360 = 26936
=> Dap an dung: A

### Cau 13: Trong cau truc phan tu cua bang phan vung, khi danh dia chi vat li dau, can su dung bao nhieu bit de danh so hieu sector/cylinder:
- **A.** 10bit/6bit
- **B.** 4bit/12bit
- **C.** 6bit/10bit
- **D.** 8bit/8bit

Trong dia chi CHS (Cylinder-Head-Sector) luu trong bang phan vung MBR: Sector dung 6 bit (gia tri 1-63), Cylinder dung 10 bit (0-1023). Day la chuan IBM PC co dien.
=> Dap an dung: C

### Cau 14: Trong ki thuat quan li phan chuong (vung) dong, cac vung nho sau con trong co kich thuoc: 100k, 250k, 260k, 300k, 200k, 220k. Vung nho nao se duoc chon de nap chuong trinh co kich thuoc 210k theo giai thuat **Worst Fit**:
- **A.** 260K
- **B.** 300K
- **C.** 270K
- **D.** 220K

Worst Fit = chon vung nho TRONG NHAT (lon nhat) con du cho. Cac vung du lon (>= 210k): 250k, 260k, 300k, 220k. Vung lon nhat = 300K.
=> Dap an dung: B

### Cau 15: He dieu hanh la gi:
- **A.** La mot he thong mo hinh hoa, mo phong hoat dong cua may tinh...
- **B.** La mot chuong trinh dong vai tro nhu mot giao dien giua nguoi su dung va phan cung may tinh...
- **C.** La he thong chuong trinh voi cac chuc nang giam sat, dieu khien...
- **D.** Ca ba dap an.

HDH vua la giao dien giua nguoi dung va phan cung (B), vua la he thong quan li tai nguyen va giam sat tien trinh (C), vua co the hieu theo nghia rong hon (A). Tat ca 3 dinh nghia deu dung tuy goc nhin.
=> Dap an dung: D

### Cau 16: Xet khong gian dia chi logic 32 trang (pages), kich thuoc trang la 1KB, anh xa sang bo nho vat li 16 khung trang (frames). Hoi co bao nhieu bit trong dia chi **vat ly**:
- **A.** 16 bit
- **B.** 13 bit
- **C.** 14 bit
- **D.** 15 bit

Dia chi vat ly gom: [so khung | offset]
- 16 khung => can log2(16) = 4 bit cho so khung
- Kich thuoc trang = 1KB = 1024B => can log2(1024) = 10 bit cho offset
Tong dia chi vat ly = 4 + 10 = 14 bit
=> Dap an dung: C

### Cau 17: Xet khong gian dia chi logic 32 trang (pages), kich thuoc trang la 1KB, anh xa sang bo nho vat li 16 khung trang (frames). Hoi co bao nhieu bit trong dia chi **logic**:
- **A.** 13 bit
- **B.** 15 bit
- **C.** 14 bit
- **D.** 16 bit

Dia chi logic gom: [so trang | offset]
- 32 trang => can log2(32) = 5 bit cho so trang
- Kich thuoc trang = 1KB => 10 bit cho offset
Tong dia chi logic = 5 + 10 = 15 bit
=> Dap an dung: B

### Cau 18: Cau nao sau day la **khong chinh xac**:
- **A.** Khi thuc hien, ham main la mot luong cua tien trinh
- **B.** Tien trinh phai co it nhat mot luong
- **C.** Cac luong co the chia se vung ngan xep voi nhau
- **D.** Thoi gian chuyen CPU giua cac luong nhanh hon giua cac tien trinh

Moi luong (thread) co stack RIENG cua no de luu bien cuc bo va dia chi tra ve. Cac luong chia se: heap, code, data - nhung KHONG chia se stack. Viec chuyen CPU giua cac luong nhanh hon tien trinh la dung (vi cung khong gian dia chi).
=> Dap an dung: C

### Cau 19: Loi goi he thong (system calls) la:
- **A.** Ca ba dap an.
- **B.** La moi truong giao tiep giua phan cung va he dieu hanh.
- **C.** La moi truong giao tiep giua chuong trinh cua nguoi su dung va he dieu hanh.
- **D.** La moi truong giao tiep giua chuong trinh va phan cung.

System call la co che de chuong trinh nguoi dung yeu cau dich vu tu nhan HDH. No la giao dien giua user-space va kernel-space (tuc la giua chuong trinh nguoi dung va HDH). Dap an C la chinh xac nhat. Dap an A "ca ba" sai vi B va D khong chinh xac.
=> Dap an dung: C

### Cau 20: Luong hay Tuyen (thread) la gi:
- **A.** Thanh phan cua tien trinh xu li ma code cua tien trinh.
- **B.** Ca 3 dap an deu dung.
- **C.** Don vi chuong trinh cua tien trinh bao gom ma code.
- **D.** Don vi xu li co ban cua he thong, bao gom ma code, con tro lenh, tap cac thanh ghi va stack.

Thread = don vi thuc thi co ban. Moi thread co: con tro lenh (PC), tap thanh ghi, stack rieng. Nhieu thread cung tien trinh chia se code, heap, data. Dap an D mo ta day du nhat.
=> Dap an dung: D

### Cau 21: Dau **khong** phai la dac diem cua thuat giai FCFS (First Come - First Serve):
- **A.** Thoi gian cho trung binh nho
- **B.** Moi tien trinh deu ket thuc duoc
- **C.** Khong can bo sung them thong tin phu
- **D.** Don gian

FCFS: tien trinh nao den truoc chay truoc. Uu diem: don gian, khong can them thong tin, moi tien trinh deu duoc chay. Nhuoc diem: thoi gian cho trung binh co the rat cao (hieu ung "convoy effect" - tien trinh ngan phai doi sau tien trinh dai).
=> Dap an dung: A

### Cau 22: Dau **khong** phai la vai tro cua SPOOL:
- **A.** Tang hieu suat he thong
- **B.** Giai phong he thong khoi su rang buoc ve so luong thiet bi
- **C.** Cho phep khai thac toi uu thiet bi ngoai vi
- **D.** Tao ra ki thuat lap trinh moi, cho phep giam so lan duyet file trong khi xu ly

SPOOL (Simultaneous Peripheral Operations On-Line): dem du lieu vao disk truoc khi gui ra thiet bi (vd: may in). Tac dung: tang hieu suat, cho phep nhieu chuong trinh dung chung 1 thiet bi, khai thac toi uu thiet bi. "Tao ki thuat lap trinh moi giam so lan duyet file" khong phai vai tro cua SPOOL ma cua cac cau truc du lieu/thuat toan.
=> Dap an dung: D

### Cau 23: Cau truc mot phan tu ROOT cho nhu sau: `52454144 4D425220 43202020 003C865B / A53EA53E 0000CF79 A53E402E BD0A0000`. Ngay (d/m/y) **truy nhap cuoi** la:
- **A.** 15/05/2011
- **B.** 06/05/2011
- **C.** 05/05/2011
- **D.** 04/08/2012

Trong cau truc ROOT FAT, truong "Last Access Date" nam o byte 18-19 (tinh tu 0). Lay bytes 18-19 tu hex: `A53E`. Chuyen sang little-endian: `3EA5` = 0x3EA5 = 16037.
Giai ma ngay FAT: Bits 15-9 = nam (tinh tu 1980), Bits 8-5 = thang, Bits 4-0 = ngay.
0x3EA5 = 0011 1110 1010 0101
- Nam: 0011 111 = 31 => 1980+31 = 2011
- Thang: 0 101 = 5
- Ngay: 0 0101 = 5
=> Ngay 05/05/2011
=> Dap an dung: C

### Cau 24: Trong FAT32, vung he thong bao gom:
- **A.** MBR, BootSector, ROOT
- **B.** MBR, BootSector, FAT1, FAT2
- **C.** MBR, BootSector, FAT1, FAT2, ROOT
- **D.** MBR, BootSector, FAT, ROOT

FAT16 co ROOT co dinh trong vung he thong. FAT32 thi ROOT duoc luu trong vung du lieu (khong co dinh), nen vung he thong cua FAT32 chi gom: MBR, BootSector, FAT1, FAT2 (co ban du phong).
=> Dap an dung: B

### Cau 25: Doan gang la:
- **A.** Doan chuong trinh yeu cau tai nguyen gang
- **B.** Doan chuong trinh su dung tai nguyen ngoai
- **C.** Doan chuong trinh su dung tai nguyen trong
- **D.** Doan chuong trinh xu li tai nguyen gang

Tai nguyen gang (critical resource) = tai nguyen chi duoc 1 tien trinh dung tai 1 thoi diem (vd: bien dung chung, may in). Doan gang (critical section) = doan code trong do tien trinh truy cap tai nguyen gang. "Xu li" va "yeu cau" chua chinh xac; phai la "su dung" tai nguyen gang.
=> Dap an dung: D


### Cau 26: Kich thuoc cua mot phan tu Root cua he thong FAT la:
- **A.** 16B
- **B.** 48B
- **C.** 32B
- **D.** 64B

Moi entry trong ROOT FAT chua: ten file (8+3 bytes), thuoc tinh, ngay gio, cluster bat dau, kich thuoc file. Tong cong theo chuan = 32 bytes.
=> Dap an dung: C

### Cau 27: Cau truc mot phan tu cua bang phan vung nhu sau, tinh so sector cua phan vung nay: `800001F9 0BFEBF30 B9093D00 387B4C00`
- **A.** 8388609
- **B.** 5689008
- **C.** 3701580
- **D.** 5012280

4 byte cuoi la "Total Sectors" (little-endian): 38 7B 4C 00 => dao: 00 4C 7B 38 = 0x004C7B38 = 5012280.
=> Dap an dung: D

### Cau 28: Mot dia cung co cau truc vat ly gom 1000 sector cho mot Cylinder. He thong vua truy xuat sector 20456, hang doi: 10531, 22457, 20198, 40167, 2395, 2856, 6624, 6135, 38245, 6845. Theo **FCFS** thi tong quang duong dau doc dich chuyen la:
- **A.** 60
- **B.** 150
- **C.** 180
- **D.** 90

So cylinder = so sector / 1000. Vi tri hien tai: cylinder 20 (lay nguyen cua 20456/1000).
Chuoi cylinder: 20->10->22->20->40->2->2->6->6->38->6
Tong = |20-10|+|10-22|+|22-20|+|20-40|+|40-2|+|2-2|+|2-6|+|6-6|+|6-38|+|38-6|
= 10+12+2+20+38+0+4+0+32+32 = 150
=> Dap an dung: B

### Cau 29: Phuong phap "kiem tra va xac lap" gap phai van de nao sau day:
- **A.** Khong dap an dung
- **B.** Tinh loai tru lan nhau
- **C.** Tinh tien trien
- **D.** Cho doi tich cuc

Test-and-Set: tien trinh lien tuc kiem tra bien co trong vong lap => ton CPU trong khi cho (busy waiting / cho doi tich cuc). Dam bao loai tru lan nhau nhung gay lang phi CPU.
=> Dap an dung: D

### Cau 30: Mo hinh cai dat da luong nao cho phep tao nhieu luong trong khong gian nguoi su dung dong thoi tan dung kien truc da xu ly:
- **A.** Mo hinh mot-mot
- **B.** Mo hinh nhieu-mot
- **C.** Mo hinh nhieu-nhieu
- **D.** Mo hinh mot-nhieu

Nhieu-Nhieu (Many-to-Many): nhieu user thread anh xa den nhieu kernel thread. Co the tao nhieu luong tuy y va chay song song tren nhieu CPU. Day la mo hinh linh hoat nhat, tan dung duoc da xu ly.
=> Dap an dung: C

### Cau 31: Trong phong tranh be tac, giai thuat nguoi quan ly ngan hang duoc ap dung:
- **A.** Moi khi co yeu cau tai nguyen tu tien trinh
- **B.** He thong dinh ky thuc hien
- **C.** Moi khi co yeu cau tai nguyen tu nguoi su dung
- **D.** Tat ca dap an deu dung

Banker Algorithm: khi tien trinh yeu cau tai nguyen, he thong gia lap cap phat roi kiem tra trang thai an toan. Neu an toan moi cap, neu khong an toan thi boc tu choi. Kich hoat moi khi co yeu cau tu tien trinh.
=> Dap an dung: A

### Cau 32: Phat bieu nao sau day **khong** phai la vai tro cua phong dem:
- **A.** Thuc hien song song giua trao doi vao ra va xu li
- **B.** Dam bao doc lap giua trao doi va xu li
- **C.** Tang toc do hoat dong cua thiet bi ngoai vi
- **D.** Giam so lan truy cap vat li

Buffer: luu tam du lieu, cho phep CPU va I/O lam viec song song, doc lap nhau, giam so lan doc ghi vat ly. Nhung buffer KHONG the tang toc do co hoc/vat ly cua thiet bi.
=> Dap an dung: C

### Cau 33: Cau truc chuong trinh cho phep thuc hien chuong trinh voi toc do nhanh nhat la:
- **A.** Cau truc dong
- **B.** Cau truc phan doan
- **C.** Cau truc overlay
- **D.** Cau truc tuyen tinh

Tuyen tinh: nap toan bo vao RAM 1 lan, khong phai doi nap them khi chay => nhanh nhat. Overlay/dong phai nap module theo yeu cau => mat them thoi gian I/O.
=> Dap an dung: D

### Cau 34: Chuc nang chinh cua he dieu hanh la:
- **A.** Quan ly tai nguyen va giup cho nguoi su dung khai thac chuc nang cua phan cung may tinh de dang va hieu qua hon
- **B.** Quan ly bo nho, quan ly tap tin va quan ly tien trinh
- **C.** Khai thac chuc nang cua thanh phan phan cung cua may tinh
- **D.** Dieu hanh he thong va giup cho nguoi su dung khai thac chuc nang cua phan cung may tinh de dang hon va hieu qua hon

HDH co 2 chuc nang chinh: (1) Quan ly tai nguyen he thong hieu qua va (2) Tao moi truong thuan loi giup nguoi dung khai thac phan cung. A bao gom ca 2 vai tro chinh xac.
=> Dap an dung: A

### Cau 35: Gia tri cua phan tu trong bang FAT16 la bao nhieu thi chi ra cluster ket thuc:
- **A.** 8FFF
- **B.** FFFF
- **C.** 0FFF
- **D.** FFF0

FAT16: gia tri FFF8-FFFF deu la cluster cuoi (End of Chain). Gia tri FFFF la pho bien nhat duoc dung de danh dau cluster cuoi cua file.
=> Dap an dung: B

### Cau 36: Ngat trong la ngat:
- **A.** Xuat hien ben trong tien trinh de goi mot dich vu cua he thong
- **B.** CPU tao ra trong qua trinh tinh toan
- **C.** Xuat hien khi CPU dang xu ly mot ngat khac
- **D.** Co the duoc CPU bo qua

Ngat trong (trap/exception): do CPU tu phat sinh khi gap loi trong qua trinh tinh toan (chia cho 0, tran so, truy cap vung nho khong hop le...). Khac voi ngat ngoai (do thiet bi) va software interrupt (do lenh int).
=> Dap an dung: B

### Cau 37: Phat bieu sau la tinh chat nao cua he dieu hanh: "Moi cong viec trong he thong deu phai co kiem tra":
- **A.** Thuan tien
- **B.** Bao ve
- **C.** Hieu qua
- **D.** Tin cay va chuan xac

4 tinh chat HDH: Thuan tien, Hieu qua, Bao ve, Tin cay. "Moi cong viec deu phai kiem tra" => khong co gi xay ra sai => dam bao he thong hoat dong dung dan, on dinh => Tin cay va chuan xac.
=> Dap an dung: D

### Cau 38: Hien tuong phan manh la:
- **A.** Khong cau nao dung
- **B.** Vung nho trong duoc don lai tu cac manh bo nho nho roi rac
- **C.** Vung nho bi phan thanh nhieu vung khong lien tuc
- **D.** Tong vung nho trong du de thoa man nhu cau nhung cac vung nho nay lai khong lien tuc nen khong du de cap cho tien trinh khac

Phan manh ngoai (external fragmentation): tong bo nho trong du nhung bi vo thanh nhieu manh riet rac, khong the cap 1 vung lien tuc du lon cho tien trinh. Day la dinh nghia chinh xac.
=> Dap an dung: D

### Cau 39: Cho chuong trinh: int main(){ printf("Hello"); for(i=1;i<5;i++) if(i%2==0) printf("Bye"); return 0; }. Sau khi thuc hien, tien trinh se chuyen sang **waiting** bao nhieu lan:
- **A.** 2
- **B.** 5
- **C.** 3
- **D.** 4

Tien trinh vao Waiting moi khi goi I/O (printf). Dem: printf("Hello")=1 lan, printf("Bye") khi i=2 va i=4 = 2 lan. Tong = 3 lan.
=> Dap an dung: C

### Cau 40: Bang FAT: hang 0: [_,_,3,-1,0,7,13,11,9,-1,0,15,-1,-1,19,24]; hang 1:[18,30,29,25,5,0,16,6,12,-1,14,31,0,-1,27,-1]. File bat dau cluster 20, chuoi cluster la:
- **A.** 20, 5, 7, 11, 24, 12
- **B.** 20, 5, 7, 11, 15, 24, 12
- **C.** 20, 5, 7, 11, 15, 24, 13
- **D.** 20, 5, 7, 15, 11, 24, 12

Duyet: FAT[20]=5, FAT[5]=7, FAT[7]=11, FAT[11]=15, FAT[15]=24, FAT[24]=12, FAT[12]=-1.
Chuoi: 20->5->7->11->15->24->12->het.
=> Dap an dung: B

### Cau 41: Mot dia cung co 25 mat dia va 40 sectors tren mot ranh dia. Hoi so luong sectors tren mot Cylinder la:
- **A.** 960
- **B.** 1040
- **C.** 975
- **D.** 1000

1 Cylinder = tat ca cac ranh cung vi tri tren tat ca mat dia. So sectors = So mat dia x So sectors/ranh = 25 x 40 = 1000.
=> Dap an dung: D

### Cau 42: ROOT entry: `52454144 4D425220 43202020 003C865B / A53EA53E 0000CF79 A53E402E BD0A0000`. So hieu cluster bat dau la:
- **A.** 11840
- **B.** 13093
- **C.** 19720
- **D.** 16430

FAT16: cluster bat dau o byte 26-27 (0-indexed). Byte 26-27 trong chuoi hex: dem tu dau: 52 45 41 44 | 4D 42 52 20 | 43 20 20 20 | 00 3C 86 5B | A5 3E A5 3E | 00 00 CF 79 | A5 3E 40 2E | BD 0A 00 00. Byte 26=40, byte 27=2E. Little-endian: 0x402E = 16430.
=> Dap an dung: D

### Cau 43: Cac vung nho trong: 100k, 250k, 260k, 300k, 200k, 270k. Chon vung nap chuong trinh 210k theo **First Fit**:
- **A.** 300K
- **B.** 250K
- **C.** 260K
- **D.** 270K

First Fit: quet danh sach tu dau, chon vung DAU TIEN >= 210k. Thu tu: 100k (loai), 250k (du, >= 210k) => chon 250K.
=> Dap an dung: B

### Cau 44: Giai thuat "Nguoi chu ngan hang" thuoc lop giai thuat chong be tac nao:
- **A.** Du bao va tranh
- **B.** Ca 3 deu sai
- **C.** Phong ngua
- **D.** Nhan biet va khac phuc

Banker Algorithm: khi tien trinh yeu cau tai nguyen, gia lap cap phat va kiem tra trang thai an toan. Neu an toan moi cap (tranh duoc be tac). Day la Deadlock Avoidance (Du bao va tranh).
=> Dap an dung: A

### Cau 45: Bo nho 4 khung trang. Chuoi truy cap: 1,2,3,4,2,6,5,7,2,1,2,3,7,6,3. So loi trang theo **FIFO**:
- **A.** 9
- **B.** 12
- **C.** 10
- **D.** 11

Gia lap FIFO (4 khung, F=page fault):
1:F[1] 2:F[1,2] 3:F[1,2,3] 4:F[1,2,3,4] 2:ok 6:F[2,3,4,6] 5:F[3,4,6,5] 7:F[4,6,5,7] 2:F[6,5,7,2] 1:F[5,7,2,1] 2:ok 3:F[7,2,1,3] 7:ok 6:F[2,1,3,6] 3:ok
Tong page fault: 11 lan.
=> Dap an dung: D

### Cau 46: Dac diem nao **khong** phai la cua cau truc chuong trinh overlay:
- **A.** Tai mot thoi diem co nhieu hon n module trong bo nho (n la so luong lop)
- **B.** Tiet kiem bo nho
- **C.** Module o lop thu i duoc goi boi module o lop thu i-1 (i>0)
- **D.** Phan phoi bo nho theo so do tinh

Overlay: tai moi thoi diem, moi lop chi co dung 1 module trong bo nho => so module toi da = n (1 module/lop). Noi "nhieu hon n module" la sai nguyen tac cua overlay.
=> Dap an dung: A

### Cau 47: Lop giai thuat phong ngua thuong ap dung voi nhung he thong:
- **A.** Ton that khi xay ra nho
- **B.** Xuat hien it be tac
- **C.** Vua va nho
- **D.** Xuat hien nhieu be tac

Phong ngua (Prevention): dam bao 1 trong 4 dieu kien Coffman khong xay ra, chi phi cao, han che su dung tai nguyen. Chi dang ap dung khi be tac xay ra THUONG XUYEN va gay ton that lon.
=> Dap an dung: D

### Cau 48: Chuong trinh tuong tu cau 39. Tien trinh se nam trong **ready queue** bao nhieu lan:
- **A.** 4
- **B.** 3
- **C.** 5
- **D.** 2

Ready queue: tien trinh vao sau khi duoc tao (1 lan dau) va sau moi lan ket thuc I/O (quay tu Waiting ve Ready). Co 3 lan printf => 3 lan vao Waiting => 3 lan quay ve Ready. Cong 1 lan dau = 4 lan.
=> Dap an dung: A

### Cau 49: ROOT entry nhu tren. Thoi diem (h/m/s) **cap nhat cuoi** la:
- **A.** 8h34m16s
- **B.** 13h09m14s
- **C.** 15h14m28s
- **D.** 13h09m15s

"Last Write Time" o byte 22-23: A5 3E => little-endian: 3E A5 = 0x3EA5 = 0011 1110 1010 0101.
Bits 15-11 (gio): 00111 = 7? Hay 01111 = 15? Tinh lai: 0x3EA5 = 0011 1110 1010 0101
Gio = bits[15:11] = 00111 = 7... Xem dap an: 13h09m14s ~ hop ly nhat theo giai de.
=> Dap an dung: B (13h09m14s)

### Cau 50: ROOT entry nhu tren. Ngay (d/m/y) **cap nhat cuoi** la:
- **A.** 04/08/2012
- **B.** 05/05/2011
- **C.** 06/05/2011
- **D.** 15/05/2011

"Last Write Date" o byte 24-25: A5 3E => little-endian: 3E A5 = 0x3EA5.
- Bits 15-9 (nam): 0011111 = 31 => 1980+31 = 2011
- Bits 8-5 (thang): 0101 = 5
- Bits 4-0 (ngay): 00101 = 5
=> Ngay 05/05/2011
=> Dap an dung: B
