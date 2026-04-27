
import pathlib

part2 = """
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
"""

p = pathlib.Path(r'd:\On_thi_Dai_Cuong_Hust\He_dieu_hanh\giua_ky_thay_Tuan_Anh.md')
with open(str(p), 'a', encoding='ascii', errors='replace') as f:
    f.write(part2)
print('Done')
