HànhViTool là một công cụ cho giáo viên NV để dễ tạo bảng Excel về hành vi của học sinh.

------------------- WINDOWS ------------------------

Cài đặt
1. Di chuyển đến thư mục "Install (Windows)"
2. Chạy file install.bat

Cách sử dụng công cụ
1. Sao chép tất cả các mục cần chuyển đổi vào file input.txt
2. Chạy file run.bat
3. Kết quả sẽ được lưu trong file output.xlsx

--------------------- MAC --------------------------

Cài đặt
1. Mở Terminal
	Nhấn Cmd + Space, gõ Terminal, rồi nhấn Enter
	Hoặc vào Applications → Utilities → Terminal
2. Di chuyển đến thư mục chứa script
	Dùng lệnh "cd" để đi đến thư mục có file script của bạn.
	Ví dụ:
		cd /Users/yourusername/path/to/folder
3. Cấp quyền chạy cho script
	Mặc định file có thể chưa có quyền thực thi. Dùng lệnh:
		chmod +x install.sh
4. Chạy script
	./install.sh

Cách sử dụng công cụ
1. Mở Terminal
	Nhấn Cmd + Space, gõ Terminal, rồi nhấn Enter
	Hoặc vào Applications → Utilities → Terminal
2. Di chuyển đến thư mục chứa script
	Dùng lệnh "cd" để đi đến thư mục có file script của bạn.
	Ví dụ:
		cd /Users/yourusername/path/to/folder
3. Chạy script (Đảm bảo bạn chưa mở file output.xlsx trong bất kỳ chương trình nào; ví dụ: Microsoft Excel)
	./run.sh
4. Kết quả sẽ được lưu trong file output.xlsx

-----------------------------------------------------

Debugging

1. PermissionError: [Errno 13] Permission denied: 'output.xlsx'
	- Bạn đang mở file output.xlsx trong một chương trình khác. Bạn cần đóng nó lại trước.
	
-----------------------------------------------------

Định dạng file input.txt

1. Mỗi mục (entry) được phân tách bằng một dòng trống.
2. Với mỗi entry, dòng đầu tiên có thể là ngày và dòng thứ hai có thể là thời gian. 
	Cả hai đều là tùy chọn. Mỗi dòng còn lại phải bắt đầu bằng (A), (B), (C) hoặc (F).
3. input.txt có thể có nhiều hơn 1 entry.

Ví dụ về một entry đơn giản:
18/4
1h40
(A) A1
(B) B1
(C) C1
(F) F1

Ví dụ về entry không có thời gian:
18/4
(A) A1
(B) B1
(C) C1
(F) F1

Ví dụ về entry thiếu một số cột:
18/4
1h40
(A) A1
(C) C1

Ví dụ về entry thiếu một số cột và sẽ tạo ra 2 dòng:
18/4
1h40
(B) B1
(B) B2
(C) C2
