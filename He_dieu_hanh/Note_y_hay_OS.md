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

1. Chân lý về Tiến trình (Process) và Luồng (Thread)
Đây là sự phân ly vĩ đại nhất của Khoa học máy tính, tách biệt giữa "Tài sản" và "Hành động".

Tiến trình (Cái Vỏ / Công ty): Là đơn vị Sở hữu tài nguyên. Nó là một "thùng chứa" được Hệ điều hành (OS) nạp từ ổ cứng lên RAM, chia làm 4 khu (Code, Data, Heap, Stack). Tiến trình không tự chạy, nó chỉ đứng yên và giữ tài nguyên.

Luồng (Thực thể / Nhân viên): Là đơn vị Lập lịch và Thực thi. CPU chỉ nhìn thấy Luồng, không nhìn thấy Tiến trình. Mọi luồng trong cùng một tiến trình dùng chung 100% không gian bộ nhớ (Code, Data, Heap), chỉ giữ lại đồ dùng cá nhân là Stack (Ngăn xếp biến cục bộ) và Thanh ghi (Registers, Con trỏ lệnh).

2. Sự thật về Đa nhiệm (Multitasking) và Đa luồng (Multithreading)
Cả hai đều dùng chung một kỹ thuật: Cắt lát thời gian (Time-slicing / Round Robin) để tạo ảo giác chạy song song trên CPU có ít nhân. Điểm "chí mạng" là sự khác biệt về cái giá phải trả:

Chuyển đổi Đa luồng (Nhẹ như lông hồng): Chuyển đổi giữa 2 luồng của CÙNG 1 tiến trình. OS chỉ việc tráo đổi bộ Thanh ghi và Stack. Cực kỳ nhanh.

Chuyển đổi Đa nhiệm (Nặng như tảng đá): Chuyển đổi giữa 2 luồng của 2 Tiến trình KHÁC NHAU. OS bắt buộc phải gỡ toàn bộ bảng đồ không gian bộ nhớ (Page Table), xóa bộ đệm (TLB) để dọn dẹp sạch sẽ mặt bàn làm việc rồi mới nạp không gian của tiến trình mới vào. Tốn cực nhiều chu kỳ CPU.

3. Vén màn Luồng Nhân (Kernel Thread) và Luồng User (User Thread)
Đây là cuộc chiến về quyền lực giữa Phần cứng (OS) và Phần mềm (Ứng dụng).

Luồng Nhân (Quyền lực tuyệt đối): Là thực thể do OS trực tiếp tạo ra, quản lý và nhét vào nhân CPU. Chậm tạo ra, tốn bộ nhớ RAM để quản lý, nhưng ổn định. OS nắm quyền sinh sát bằng cách đổi trạng thái của nó: Running (Đang chạy), Ready (Sẵn sàng xếp hàng), Waiting/Blocked (Bị khóa chờ I/O).

Luồng User (Cú lừa của phần mềm): Là một cấu trúc dữ liệu mỏng nhẹ do thư viện phần mềm (Trưởng phòng) tự đẻ ra trên RAM. OS hoàn toàn mù tịt về sự tồn tại của nó. Phần mềm tự dùng lát cắt thời gian để luân chuyển các Luồng User chạy trên lưng một Luồng Nhân duy nhất. Cực nhanh, nhưng có một "Tử huyệt" chí mạng.

4. "Tử huyệt I/O" và Sự bất lực của Không gian Người dùng
Khi phần mềm đang tự lập lịch cắt lát thời gian, nó chỉ làm được việc đó khi đang ở Không gian Người dùng (User Space) và nắm quyền điều khiển CPU.

Cú vượt biên chí mạng: Khi một Luồng User gọi lệnh I/O (ví dụ gõ phím), nó tạo ra một System Call. Nó mang theo cái Luồng Nhân chui tọt vào Không gian Lõi (Kernel Space).

Sự bất lực: OS khóa chặt cái Luồng Nhân đó lại vì phải chờ bàn phím. Lúc này, cái đồng hồ cắt lát thời gian của phần mềm nằm ở User Space bị tê liệt hoàn toàn (vì nó mất Luồng Nhân, mất CPU để chạy code đòi lại luồng). Toàn bộ các Luồng User khác đang chờ đều bị "chết chùm" (Móm toàn tập).

5. Giải pháp Tối thượng: Mô hình Nhiều-Nhiều và Upcall
Để không bị Crash RAM vì đẻ quá nhiều Luồng Nhân (như mô hình 1-1), và không bị chết chùm (như mô hình N-1), thế giới dùng mô hình lai (N-M).

Phần mềm đẻ ra hàng vạn Luồng User, nhưng chỉ xin OS cấp một số lượng Luồng Nhân vừa đủ (thường bằng số nhân CPU vật lý).

Upcall (Đòi nợ thẻ): Khi một Luồng Nhân bị OS khóa dưới Kernel vì I/O, OS thừa biết phần mềm bên trên đang thiếu nhân lực. OS lập tức tạo ra một Luồng Nhân mới tinh (Tạm thời) và gọi điện (Upcall) ném lên cho phần mềm. Phần mềm lấy thẻ mới này gắn cho một Luồng User khác để tiếp tục duy trì tiến độ chạy song song mà không bị nghẽn. Khi I/O xong, OS thu hồi lại cái thẻ tạm đó.

Hãy tưởng tượng Hệ điều hành là một tòa nhà an ninh cao cấp. Các đoạn code thông thường của bạn chạy ở sảnh ngoài (User Space). Nhưng phần cứng (RAM, Ổ cứng, Card mạng, CPU đa luồng...) là kho bạc nằm trong khu vực VIP (Kernel Space). Tiến trình không thể tự tiện đẩy cửa vào kho bạc. Nó bắt buộc phải qua quầy lễ tân để xin giấy phép. Cái hành động "xin giấy phép" đó chính là System Call (Lời gọi hệ thống).

Dưới đây là danh sách phân loại toàn bộ các tác vụ theo chuẩn hàn lâm (Silberschatz):

🟢 Những việc KHÔNG CẦN System Call (Chỉ chạy ở User Mode)
Tất cả những gì tiến trình/luồng làm việc trực tiếp trên vùng nhớ CPU và RAM đã được cấp phát riêng cho nó thì không cần gọi Kernel.

Tính toán toán học, logic: Cộng trừ nhân chia (a + b), vòng lặp (for, while), câu lệnh điều kiện (if/else).

Tính toán con trỏ (Pointer arithmetic): Di chuyển con trỏ trong mảng dữ liệu.

Gọi hàm nội bộ (Function Calls): Các hàm do bạn tự viết gọi qua lại lẫn nhau trong cùng một chương trình.

Gán biến: int x = 10;

Tóm lại: Code chỉ thao tác với Data và Logic thuần túy trong không gian của nó thì cực kỳ nhanh vì không phải "xin phép" ai cả.

🔴 "Tất cả" những việc BẮT BUỘC tạo System Call
Bất cứ khi nào tiến trình muốn vượt ra ngoài không gian cá nhân của nó để "đụng" vào tài nguyên hệ thống, nó phải tạo System Call. Theo lý thuyết Hệ điều hành, chúng được chia thành 5 nhóm cốt lõi:

1. Quản lý tiến trình (Process Control):

Tạo một tiến trình/luồng mới (VD: fork() trong Linux).

Kết thúc một tiến trình (VD: exit()).

Tạm dừng, ép tiến trình khác chờ (VD: wait()).

Cấp phát hoặc giải phóng bộ nhớ động mới (xin thêm RAM).

2. Quản lý File (File Management):

Mọi thao tác I/O với ổ cứng: Mở file (open()), Đọc file (read()), Ghi file (write()), Đóng file (close()).

3. Quản lý Thiết bị (Device Management):

Yêu cầu quyền truy cập vào bàn phím, màn hình, máy in, hoặc card đồ họa.

Ví dụ: Khi bạn muốn in một dòng chữ ra màn hình console, phần cứng màn hình do Kernel quản lý, nên phải có System Call.

4. Bảo trì thông tin hệ thống (Information Maintenance):

Xin hệ thống cấp cho giờ/ngày tháng hiện tại.

Hỏi xem ID của tiến trình hiện tại là gì (getpid()).

5. Giao tiếp (Communication - IPC):

Gửi dữ liệu qua mạng (tạo Sockets để kết nối mạng internet).

Giao tiếp giữa các tiến trình với nhau (Shared Memory, Pipes, Message Passing).