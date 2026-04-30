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