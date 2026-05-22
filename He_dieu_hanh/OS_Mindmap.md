graph TD
    %% BẢN ĐỒ 1: TỪ Ổ CỨNG LÊN RAM (SỰ HÌNH THÀNH TIẾN TRÌNH)
    subgraph BanDo1 ["BẢN ĐỒ 1: TỪ Ổ CỨNG LÊN RAM"]
        P_File["[Chương trình / Program]<br/>(Cục file tĩnh .exe trên ổ cứng)"]
        LTS["(Bộ điều phối dài hạn<br/>Long-term Scheduler)"]
        Process["[Tiến trình / Process]<br/>(Thực thể sống, sở hữu tài nguyên)"]
        
        P_File -->|"Được HĐH nạp lên RAM thông qua"| LTS
        LTS --> Process
        
        Process -->|"HĐH cấp phát và chia làm 4 khu vực"| MemoryAreas
        
        subgraph MemoryAreas ["Các vùng nhớ của Tiến trình"]
            direction LR
            Code["[Vùng Code]<br/>Chứa mã lệnh máy<br/>(Chỉ đọc, bị xóa nếu chật)"]
            Data["[Vùng Data]<br/>Chứa biến toàn cục"]
            Heap["[Vùng Heap]<br/>Cấp phát động<br/>(Hay bị Swap nhất)"]
            Stack["[Vùng Stack]<br/>Chứa biến cục bộ<br/>(Ít bị đuổi)"]
        end
    end

    %% BẢN ĐỒ 2: GIẢI PHẪU BÊN TRONG TIẾN TRÌNH
    subgraph BanDo2 ["BẢN ĐỒ 2: GIẢI PHẪU BÊN TRONG TIẾN TRÌNH"]
        OS2["[Hệ Điều Hành]"]
        PCB["[PCB - Process Control Block]<br/>(ID, Trạng thái, PC, Thanh ghi...)"]
        Thread["[Luồng / Thread]<br/>(Đơn vị thực thi cơ bản nhất)"]
        
        OS2 -->|"Quản lý qua cấu trúc dữ liệu"| PCB
        PCB -->|"Thực thể mượn CPU thực sự là"| Thread
        
        Thread -->|"Các Luồng cùng Tiến trình chia sẻ"| SharedResources
        subgraph SharedResources ["Tài nguyên dùng chung (Đổi Luồng nhanh)"]
            direction LR
            S_Code["Code"]
            S_Data["Data"]
            S_Heap["Heap"]
            S_Files["Files"]
        end
        
        Thread -->|"Giữ riêng"| PrivateResources
        subgraph PrivateResources ["Tài nguyên giữ riêng"]
            direction LR
            P_Stack["Stack"]
            P_PC["PC (Con trỏ lệnh)"]
            P_Regs["Tập thanh ghi"]
        end
        
        Thread --> UserThread["[Luồng User]<br/>Nhanh, tự quản lý<br/>(Đụng I/O là chết chùm)"]
        Thread --> KernelThread["[Luồng Nhân]<br/>HĐH trực tiếp tạo,<br/>quản lý và nhét vào CPU"]
        
        UserThread -->|"HĐH cung cấp cầu nối"| Upcall["[Cơ chế Upcall]"]
        Upcall -->|"Ném cho phần mềm"| TempKernelThread["[Luồng Nhân tạm thời]<br/>Để gán cho Luồng User khác chạy"]
    end

    %% BẢN ĐỒ 3: LỚP VỎ BẢO VỆ VÀ SYSTEM CALL
    subgraph BanDo3 ["BẢN ĐỒ 3: LỚP VỎ BẢO VỆ VÀ LỜI GỌI HỆ THỐNG"]
        RunningUserThread["[Luồng đang chạy ở User Mode]<br/>(Bị cấm tự làm I/O)"]
        SysCall["[System Call - Lời gọi hệ thống]<br/>(Môi trường giao tiếp Ứng dụng & HĐH)"]
        Trap["[Ngắt Mềm / Trap]"]
        KernelMode["[Kernel Mode]"]
        Hardware["[Phần cứng vật lý]"]
        
        RunningUserThread -->|"Bắt buộc phải mượn tay HĐH thông qua"| SysCall
        SysCall -->|"Sinh ra tín hiệu"| Trap
        Trap -->|"CPU lập tức chuyển sang"| KernelMode
        KernelMode -->|"HĐH ra lệnh qua Device Driver điều khiển"| Hardware
    end

    %% BẢN ĐỒ 4: VÒNG ĐỜI VÀ SCHEDULING
    subgraph BanDo4 ["BẢN ĐỒ 4: VÒNG ĐỜI VÀ GIAO THÔNG CPU"]
        State_NEW["[Trạng thái NEW]"]
        State_READY["[Trạng thái READY]<br/>(Chỉ thiếu CPU)"]
        State_RUNNING["[Trạng thái RUNNING]<br/>(Đang chiếm CPU)"]
        State_WAITING["[Trạng thái WAITING]"]
        State_TERMINATED["[Trạng thái TERMINATED]"]
        STS["(Bộ điều phối ngắn hạn<br/>CPU Scheduler)"]
        ContextSwitch["[Context Switch]<br/>(CPU lãng phí thời gian idle)"]
        
        State_NEW -->|"Chờ LTS xếp chỗ vào RAM"| State_READY
        State_READY -->|"Được STS chọn luồng nhân đẩy vào"| State_RUNNING
        
        State_RUNNING -->|"Con đường 1: Gọi System Call đợi I/O"| State_WAITING
        State_WAITING -->|"I/O xong, sinh Ngắt ngoài"| State_READY
        
        State_RUNNING -->|"Con đường 2: Hết lượng tử thời gian / Bị cướp"| State_READY
        
        State_RUNNING -->|"Con đường 3: Chạy xong lệnh cuối"| State_TERMINATED
        
        State_RUNNING -.->|"Chuyển trạng thái"| ContextSwitch
        ContextSwitch -.-> State_READY
    end

    %% BẢN ĐỒ 5: CÁC THUẬT TOÁN ĐIỀU PHỐI
    subgraph BanDo5 ["BẢN ĐỒ 5: BỘ ĐIỀU PHỐI CPU"]
        Queue["Hàng đợi [READY]"]
        Preemptive["Nguyên tắc Không độc quyền (Preemptive)<br/>(HĐH được quyền cướp CPU)"]
        NonPreemptive["Nguyên tắc Độc quyền (Non-preemptive)<br/>(HĐH không được cướp CPU)"]
        
        Queue --> Preemptive
        Queue --> NonPreemptive
        
        Preemptive --> RR["[RR - Round Robin]<br/>Cắt lát thời gian. Công bằng nhất"]
        Preemptive --> SRTF["[SRTF]<br/>Thời gian CÒN LẠI ngắn nhất thì cướp"]
        
        NonPreemptive --> FCFS["[FCFS]<br/>Đến trước chạy trước"]
        NonPreemptive --> SJF["[SJF]<br/>Ngắn nhất chạy trước, tối ưu thời gian chờ"]
    end

    %% BẢN ĐỒ 6: BẾ TẮC VÀ ĐỒ THỊ TÀI NGUYÊN
    subgraph BanDo6 ["BẢN ĐỒ 6: BẾ TẮC (DEADLOCK)"]
        MultiTask["Các Luồng chạy đa nhiệm"]
        Coffman["(Hội tụ 4 điều kiện Coffman:<br/>Loại trừ tương hỗ, Giữ và chờ,<br/>Không chiếm đoạt, Chờ đợi vòng tròn)"]
        Deadlock["[BẾ TẮC - DEADLOCK]"]
        
        MultiTask -->|"Tranh chấp tài nguyên găng"| Coffman
        Coffman --> Deadlock
        
        RAG["[Đồ thị RAG]"]
        Proc_Req["Pi --> Rj (Cung yêu cầu)"]
        Res_Alloc["Rj --> Pi (Cung sử dụng)"]
        Cycle["(Tạo VÒNG KHÉP KÍN + Tài nguyên 1 đơn vị)"]
        
        RAG --> Proc_Req
        RAG --> Res_Alloc
        Proc_Req & Res_Alloc --> Cycle
        Cycle -->|"CHẮC CHẮN"| Deadlock
        
        Banker["(Thuật toán Banker - Phòng tránh)"]
        Banker -->|"Giả lập cấp phát"| CheckSafe
        CheckSafe{"Trạng thái An toàn<br/>(Safe state)?"}
        CheckSafe -->|"Có lối thoát"| CấpThật["Mới cấp thật"]
        CheckSafe -->|"Không an toàn"| Đợi["Bắt tiến trình đợi"]
        
        Semaphore["[Semaphore S]"]
        Semaphore -->|"Hàm Wait(S)"| TruVe["Trừ vé, hết vé thì ngủ"]
        Semaphore -->|"Hàm Signal(S)"| TraVe["Trả vé, đánh thức"]
        
        Deadlock -.->|"HĐH xây trạm kiểm duyệt"| Banker
        MultiTask -.->|"Kiểm soát giao thông"| Semaphore
    end

    %% Mối liên kết giữa các bản đồ
    Process -.-> PCB
    Thread -.-> RunningUserThread
    State_RUNNING -.-> MultiTask
    STS -.-> Queue