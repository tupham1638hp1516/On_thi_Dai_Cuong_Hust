Phông đệm vòng tròn (thuật ngữ tiếng Anh là Circular Buffer hoặc Ring Buffer) là một cấu trúc dữ liệu bộ nhớ có kích thước cố định, hoạt động theo nguyên lý hàng đợi (FIFO - First In First Out) nhưng điểm cuối của bộ nhớ được nối vòng quay trở lại điểm đầu tiên.

Trong Hệ điều hành, ứng dụng kinh điển nhất của Circular Buffer là để giải quyết các bài toán đọc/ghi dữ liệu (I/O), đặc biệt là khi có sự chênh lệch tốc độ giữa tiến trình tạo ra dữ liệu (Producer) và tiến trình xử lý dữ liệu (Consumer).

Ví dụ đời thường:
Bạn có thể hình dung Circular Buffer giống như băng chuyền hành lý ở sân bay.

Nhân viên bốc xếp (đại diện cho tiến trình Ghi/Đọc dữ liệu từ đĩa) cứ việc đặt vali lên các vị trí trống trên băng chuyền.

Hành khách (đại diện cho tiến trình Xử lý dữ liệu của CPU) đứng đợi và lấy vali của mình ra.

Vì là băng chuyền vòng tròn, khi đến cuối dải, nó tự quay lại điểm đầu. Nhờ vậy, sân bay không cần xây một cái băng chuyền dài vô tận; họ chỉ cần tái sử dụng lại các khoảng trống mà hành khách đã lấy vali đi.

Góc nhìn IT (dành cho dân kỹ thuật):
Tại sao Hệ điều hành lại ưu tiên Circular Buffer cho việc đọc ghi?
Nếu bạn dùng một mảng (Array) hoặc hàng đợi (Queue) tuyến tính thông thường để làm bộ đệm streaming hoặc gõ phím:

Khi dữ liệu được lấy ra, bạn sẽ phải dịch chuyển (shift) toàn bộ dữ liệu còn lại lên đầu mảng -> Độ phức tạp O(n), cực kỳ tốn chi phí CPU.

Nếu không dịch chuyển, con trỏ ghi sẽ chạy mãi về phía cuối và tràn bộ nhớ, dù phần đầu mảng đã trống (do dữ liệu đã được đọc).

Với Circular Buffer, OS chỉ cần duy trì 2 con trỏ là Read_Pointer (con trỏ đọc) và Write_Pointer (con trỏ ghi). Khi một con trỏ chạy đến cuối mảng, nó dùng phép chia lấy dư (Modulo %) để tự động quay lại index 0. Mọi thao tác push/pop lúc này đều chỉ mất thời gian O(1), bộ nhớ được cấp phát tĩnh một lần và tái sử dụng liên tục, không bị phân mảnh.

*
Hãy tưởng tượng đĩa cứng giống như một bãi gửi xe hình tròn.

Track là nguyên một con đường vòng tròn chạy quanh bãi.

Sector chính là từng "ô đỗ xe" được kẻ vạch sơn cố định trên con đường đó.
Dù chiếc xe của bạn (dữ liệu file) có bé xíu như cái xe đạp, thì khi cất vào bãi, bạn vẫn phải trả tiền và chiếm trọn vẹn một ô đỗ (Sector). Không có chuyện bãi xe cho thuê "nửa ô đỗ" để tính nửa tiền.

*
Hội chứng "Đập đĩa" (Thrashing)

Vì Page Fault quá chậm, Hệ điều hành phải thiết kế sao cho tỷ lệ xảy ra lỗi trang (Page Fault Rate) là cực kỳ thấp (thường < 0.00001%).

Nhưng điều gì xảy ra nếu bạn cố tình mở quá nhiều ứng dụng nặng cùng lúc (VD: Vừa mở Premiere render video, vừa mở 50 tab Chrome, vừa chơi Cyberpunk 2077) trên một máy tính chỉ có 4GB RAM?

Ứng dụng A gọi một Trang, xảy ra Page Fault. HĐH lấy một Trang của ứng dụng B trên RAM ném ra ổ cứng để nhường chỗ.

Ngay giây sau, CPU chuyển qua chạy ứng dụng B. B lại đòi đúng cái Trang vừa bị ném đi. Lại xảy ra Page Fault. HĐH lại lấy một Trang của ứng dụng A ném ra ổ cứng.

Vòng lặp này diễn ra liên tục. Hệ thống rơi vào trạng thái gọi là Thrashing (Tắc nghẽn / Đập đĩa).

Lúc này, CPU gần như hoạt động 0% (vì toàn phải ngồi chờ), nhưng ổ cứng thì chạy 100% công suất (chỉ để copy dữ liệu ra vào RAM liên tục). Máy tính của bạn sẽ bị "đóng băng" (treo cứng), chuột giật lag, và ổ cứng kêu rèn rẹt (với HDD).

*

Giải phẫu 4 vùng nhớ của một Tiến trình
Khi Hệ điều hành khởi tạo một Tiến trình (Process) — tức là cấp phép xây dựng một Gian bếp — nó sẽ chia gian bếp đó thành 4 khu vực chức năng:

1. Code (Text) - "Cuốn sổ công thức nấu ăn"

Bản chất IT: Đây là nơi chứa các mã lệnh nhị phân (mã máy) đã được biên dịch từ file .exe hoặc code C++ của bạn. CPU sẽ đọc từng dòng lệnh ở đây để thực thi.

Đặc điểm: Vùng này thường là Chỉ đọc (Read-only). Giống như cuốn sổ công thức gốc được đóng khung kính, đầu bếp chỉ được nhìn vào để làm theo, không được phép cầm bút xóa sửa nội dung công thức trong lúc đang nấu. Điều này để tránh việc chương trình tự vô tình thay đổi logic của chính nó (gây lỗi bảo mật hoặc crash).

2. Data - "Kệ gia vị và nguyên liệu dùng chung"

Bản chất IT: Chứa các biến toàn cục (Global variables) và biến tĩnh (Static variables). Ví dụ: int tong_so_khach = 0; khai báo ngoài mọi hàm.

Đặc điểm: Ngay khi gian bếp mở cửa, kệ gia vị này đã được bày sẵn và tồn tại cho đến khi gian bếp đóng cửa. Bất kỳ đầu bếp nào trong gian bếp cũng có thể với tay lấy muối, tiêu ở đây, và nếu một đầu bếp lỡ tay đổ cả lọ muối vào (thay đổi giá trị biến), các đầu bếp khác sẽ phải chịu hậu quả.

3. Heap - "Kho lạnh nguyên liệu (Cấp phát động)"

Bản chất IT: Vùng nhớ rộng lớn dùng để cấp phát động trong lúc chương trình đang chạy (Runtime). Trong C/C++, bạn xin cấp phát bằng lệnh malloc() hoặc new.

Đặc điểm:

Giống như một kho lạnh khổng lồ. Khi nhận một đơn hàng VIP đột xuất, đầu bếp cần thêm 50kg thịt bò, họ sẽ gọi điện cho quản lý kho (OS) để xin thêm chỗ chứa.

Nguy hiểm: Vùng Heap yêu cầu sự tự giác. Dùng xong (new), bạn bắt buộc phải dọn dẹp (delete). Nếu bạn cứ liên tục xin chỗ để thịt bò mà nấu xong không chịu dọn (Memory Leak - Rò rỉ bộ nhớ), kho lạnh sẽ đầy ứ, và gian bếp sẽ sập (Crash).

4. Stack (Ngăn xếp) - "Cái thớt thái đồ và sổ tay cá nhân"

Bản chất IT: Chứa các biến cục bộ (Local variables) bên trong các hàm, và lưu lại "địa chỉ quay về" khi một hàm gọi một hàm khác.

Đặc điểm:

Hoạt động theo nguyên tắc LIFO (Vào sau ra trước). Cực kỳ nhanh gọn và tự động dọn dẹp.

Khi đầu bếp nhận làm món Trứng rán (gọi hàm RanTrung()), họ lấy một cái thớt ra. Họ đập 2 quả trứng (khai báo biến cục bộ int trung = 2). Rán xong (kết thúc hàm), họ quăng luôn vỏ trứng và rửa thớt đi. Biến cục bộ trung tự động biến mất, không ai phải bận tâm đi dọn. Bộ nhớ Stack rất nhỏ, nếu bạn khai báo mảng quá to ở đây (ví dụ int a[1000000]), nó sẽ tràn thớt và sập chương trình (Lỗi Stack Overflow khét tiếng).

*
Luồng là thời gian của CPU bị cắt nhỏ ra để cứ bao nhiêu lâu lại làm 1 việc nào đó

Còn nhân có thể hiểu là CPU hẳn luôn, 4 nhân thì có 4 cái CPU đang tự hoạt động độc lập

*

Ý nghĩ của bạn rất tuyệt: "Nếu có 4 vùng (Code, Data, Heap, Stack) mà RAM lại chật, thì vùng nào sẽ bị đá ra Swap (Ổ cứng)?"

Câu trả lời là: Hệ điều hành KHÔNG QUAN TÂM nó là vùng nào. Hệ điều hành chỉ quan tâm đến thái độ của CPU: "Cái nào lâu rồi không dùng thì biến ra ngoài!"

Thuật toán đằng sau quyết định lạnh lùng này có tên là LRU (Least Recently Used - Ít được dùng gần đây nhất). Tuy nhiên, số phận của 4 vùng này khi bị đuổi khỏi RAM lại rất khác nhau:

Vùng Code (Text):

Số phận: Bị đối xử phũ phàng nhất nhưng lại an toàn nhất.

Lý do: Mã lệnh code là Chỉ đọc (Read-only). Khi HĐH cần dọn chỗ trên RAM, nó thấy vùng Code này đã lâu không chạy, nó sẽ Xóa sổ luôn khỏi RAM mà không cần tốn công copy ra file Swap trên ổ cứng. Vì sao? Vì bản gốc của code vẫn nằm chình ình trong file chrome.exe trên ổ cứng rồi. Khi nào cần, HĐH cứ ra đọc lại file gốc là xong!

Vùng Heap (Cấp phát động):

Số phận: Khách hàng thường xuyên nhất của Ổ cứng (Swap).

Lý do: Lập trình viên rất hay có thói quen khai báo những mảng dữ liệu khổng lồ (VD: mảng 10 triệu phần tử) nhưng thực chất chỉ mới dùng vài trăm phần tử đầu tiên. Những phần tử ở tít phía sau (bỏ xó lâu ngày) sẽ bị thuật toán LRU tóm cổ và ném thẳng ra ổ cứng để nhường chỗ cho tác vụ khác.

Vùng Stack (Ngăn xếp của Luồng):

Số phận: Rất ít khi bị đuổi, trừ khi Luồng đó bị "ngủ đông".

Lý do: Stack chứa các biến đang dùng ngay lập tức của hàm hiện tại. HĐH luôn ưu tiên giữ Stack trên RAM để CPU chạy nhanh nhất. Tuy nhiên, nếu Luồng A đang chờ bạn gõ bàn phím, hoặc chờ tải file từ mạng (Sleeping/Blocked), HĐH sẽ gắp toàn bộ Stack của Luồng A ném ra ổ cứng để tiết kiệm RAM.

Vùng Data (Biến toàn cục):

Số phận: Tương tự Heap. Nếu một biến toàn cục được khởi tạo từ đầu chương trình nhưng mãi không thấy ai gọi đến, nó cũng sẽ bị đẩy ra ổ cứng.

*

Chuỗi mệnh lệnh 6 tầng:

Thế giới Phần mềm (Software Realm)
Tầng 1 - Ứng dụng (User Program): Microsoft Word của bạn. Word muốn in tài liệu, nhưng nó bị cấm tự ý làm.

Tầng 2 - Lời gọi hệ thống (System Call): Cây cầu nối duy nhất. Word phải gọi một hàm System Call (ví dụ sys_write()) để gửi yêu cầu in cho Hệ điều hành.

Tầng 3 - Hệ điều hành (OS Kernel): Giám đốc nhận yêu cầu từ System Call. OS kiểm tra xem bạn có quyền in không, máy in có đang bận không. Nếu OK, nó đẩy lệnh đi tiếp.

Tầng 4 - Device Driver (Trình điều khiển): Thư ký chuyên ngành. OS đẩy lệnh xuống cho Driver của máy in HP. Driver này bắt đầu dịch lệnh in chung chung của OS thành các mã lệnh nhị phân đặc thù mà chỉ máy in HP mới hiểu.

--- [Ranh giới mỏng manh giữa Phần mềm và Phần cứng] ---

Thế giới Phần cứng (Hardware Realm)

Tầng 5 - Controller (Bộ điều khiển): Đốc công xưởng. Các mã nhị phân từ Tầng 4 truyền qua dây cáp USB, đập vào con chip Controller nằm trên máy in. Controller đọc mã này và biến nó thành các tín hiệu dòng điện (Voltage).

Tầng 6 - Thiết bị vật lý (Physical Device): Các cơ cấu cơ học. Dòng điện từ Controller kích hoạt mô-tơ cuốn giấy, nung nóng thanh nhiệt và phun mực ra tờ giấy.

CPU chạy liên tục từ tầng 1 đến tầng 4, giao tiếp với Controller.