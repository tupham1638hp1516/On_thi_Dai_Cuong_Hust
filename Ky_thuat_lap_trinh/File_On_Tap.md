### 1. Chọn phát biểu ĐÚNG về hàm có tham số ngầm định trong C++

a. Khi hàm có tham số ngầm định có prototype, thì giá trị ngầm định trong định nghĩa hàm có ý nghĩa cao hơn giá trị định nghĩa trong prototype.

b. Khi đa năng hóa toán tử không được dùng tham số có giá trị ngầm định. 

c. Tham số ngầm định của hàm có thể nằm ở  vị trí bất kỳ trong hàm có danh sách tham số nhiều hơn các tham số ngầm định.

d. Tất cả các phát biểu trên đều sai.

- Đáp án A sai là vì: Prototype là nguyên mẫu hàm được đặt ở đầu file hoặc file (.h), còn định nghĩa hàm lại là phần thân hàm thực tế nằm ở phía dưới, chứa code xử lý bên trong. Quy tắc được đưa ra là: Trình biên dịch chỉ cho khai báo giá trị ngầm định MỘT LẦN DUY NHẤT, và thường sẽ là prototype. Nếu khai báo ở định nghĩa hàm thì thậm chí còn bị báo lỗi, nên không thể nào có ý nghĩa cao hơn được.

- Đáp án B đúng là vì: Quy tắc được đưa ra là: Cấm sử dụng tham số ngầm định khi đa năng hóa toán tử. Một toán tử yêu cầu nghiêm ngặt về số ngôi, nhưng nếu như dùng tham số ngầm định, khi viết code có thể bỏ đi một số ngôi, gây nhầm lẫn và khó hiểu.

- VD:

ToaDo operator+(ToaDo b = ToaDo(0, 0)); 

Hàm main:

ToaDo diemA(3, 4);

ToaDo ketQua = diemA + ;/ "diemA +" nhìn trông rất phản cảm, khi đọc code sẽ gây khó hiểu, nên C/C++ cấm luôn.

- Đáp án C sai là vì: Thêm một quy tắc nữa là: Tất cả các tham số ngầm định bắt buộc phải nằm ở phía cuối cùng bên phải của danh sách. Lý do là vì nếu viết ở đầu danh sách, trình biên dịch sẽ rất lú:

- VD:

void ThongTin(int tuoi = 20, string ten, double chieuCao);

Hàm main:

ThongTin("Tu", 1.75); // Bạn muốn bỏ qua tuổi để lấy mặc định là 20

Khi trình biên dịch nhìn vào, nó sẽ không hiểu tại sao "Tu" là kiểu chuỗi nhưng nhưng tham số đầu tiên lại đòi hỏi kiểu int, nó sẽ không hiểu được ta đang muốn bỏ qua tham số đầu tiên.

> Đáp án đúng là: B

### Câu 2: Trong những phát biểu sau đây về sử dụng các khoảng trắng trong phong cách lập trình, phát biểu nào ĐÚNG? 

a. Sử dụng tab thay cho space để căn lề (indentation)

b. Sử dụng khoảng trắng để mã nguồn dễ đọc 

c. Không nên sử dụng tính năng tự động căn lề của trình soạn thảo 

d. Không cần phải căn lề do việc căn lề không làm thay đổi việc biên dịch 
chương  trình 

Cốt lõi của việc sử dụng khoảng trắng là để cho mã nguồn dễ đọc, khi trình biên dịch bắt đầu biên dịch, nó sẽ nén toàn bộ code lại, xóa mọi dấu cách, tab, xuống dòng. Do đó, mục đích quan trọng nhất của việc sử dụng khoảng trắng là để cho mã nguồn dễ đọc.

- Đáp án A sai là vì ở mỗi máy tính khác nhau thì sẽ có quy định khác nhau:

Đối với dấu cách (spaces): Ở bất kỳ máy tính nào, bất kỳ phần mềm nào, 1 dấu cách luôn có độ rộng bằng đúng 1 ký tự, ký tự spaces là bất biến.

Đối với phím Tab: Độ rộng của 1 phím tab là không cố định. Trên máy cá nhân thì có thể được cố định ở 1 Tab = 4 dấu cách, nhưng khi đẩy lên github thì có thể phần mềm cố định 1 Tab = 8 dấu cách. Mà khi đó thì mã nguồn sẽ khó đọc, đối nghịch với mục đích cốt lõi.

- Đáp án B đúng.

- Đáp án C là sai vì: 
