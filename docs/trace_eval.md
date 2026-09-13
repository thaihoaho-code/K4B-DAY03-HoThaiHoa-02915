# 📊 BÁO CÁO THU HOẠCH NGHIỆM THU BÀI LAB 3 (BƯỚC 3 — SUBMISSION ARTIFACT)

> **Họ và Tên Học viên:** Hồ Thái Hòa
> **Mã Sinh Viên / Mã Học viên:** 2A202602915
> **Chủ đề Lựa chọn:** 3.2: Trợ lý Đơn hàng & Kho vận (Supply Chain Agent)  

---

## 1. BẢNG CHẤM ĐIỂM AGENTIC FIT SCORING MATRIX (ĐÁNH GIÁ CHỦ ĐỀ)

| Tiêu chí Đánh giá | Mức độ (1 - 5) | Giải trình chi tiết lý do chọn điểm |
| :--- | :---: | :--- |
| **1. Multi-step Reasoning** | 3 / 5 | Một yêu cầu có thể bao gồm nhiều bước: xác định đơn hàng -> tra cứu mã vận đơn -> lấy trạng thái từ đơn vị vận chuyển -> kiểm tra vị trí hàng trong kho -> đối chiếu thông tin -> trả kết quả hoặc cập nhật trạng thái. Tuy nhiên với case này, quy trình tương đối rõ và không quá phức tạp. |
| **2. Tool Interaction** | 5 / 5 | Agent cần tương tác với OMS/WMS, database kho, API đơn vị vận chuyển, ERP hoặc MCP Server để đọc và cập nhật dữ liệu. Một yêu cầu có thể gọi nhiều tool khác nhau. |
| **3. Dynamic Decision** | 4 / 5 | Có. Ví dụ: nếu vận đơn chưa được tạo thì kiểm tra trạng thái đóng gói; nếu trạng thái giữa WMS và carrier không khớp thì cần kiểm tra hoặc báo bất thường. |
| **4. Long Horizon Goal** | 2 / 5 | Phần lớn chức năng sẽ hoàn thành trong thời gian ngắn. Ví dụ như: "đơn hàng tới đâu rồi?", Agent chưa cần duy trì mục tiêu qua nhiều giờ/ngày, trừ khi bổ sung chức năng chủ động theo dõi đơn hàng hoặc xử lý sự cố đến khi hoàn tất. |
| **TỔNG ĐIỂM AGENTIC FIT** | **14 / 20** | *Nếu tổng điểm > 12/20: Bài toán rất phù hợp triển khai Agentic System.* |

---

## 2. TRÍCH XUẤT KẾT QUẢ WATERFALL TRACE LOG (SAU KHI CHẠY TEST SUITE TRÊN API THẬT)

> ⚠️ **YÊU CẦU NGHIỆM THU:** Mở tệp `.env` điền `GEMINI_API_KEY` (hoặc `OPENAI_API_KEY`) để kết nối LLM thật trước khi thực thi `python src/app.py --all`. Bài nộp chỉ dùng Mock Offline Provider sẽ không đạt điểm nghiệm thực tế.

Dán 1 đoạn trích xuất log tiêu biểu từ file `docs/trace_waterfall.json` sinh ra từ phản hồi LLM API thật:

```json
[
  {
    "step": 1,
    "query": "chuyển trạng thái đang hàng DH2026002 sang Hủy, và tra thông tin đơn hàng DH2026001",
    "action_type": "TOOL_EXECUTION",
    "tool_name": "update_order_status",
    "arguments": {
      "order_id": "DH2026002",
      "status": "Hủy"
    },
    "observation": {
      "status": "SUCCESS",
      "order_id": "DH2026002",
      "new_status": "Hủy",
      "message": "Đã cập nhật đơn hàng DH2026002 sang trạng thái 'Hủy'."
    },
    "latency_ms": 5505.37
  },
  {
    "step": 2,
    "query": "chuyển trạng thái đang hàng DH2026002 sang Hủy, và tra thông tin đơn hàng DH2026001",
    "action_type": "TOOL_EXECUTION",
    "tool_name": "order_query",
    "arguments": {
      "order_id": "DH2026001"
    },
    "observation": {
      "status": "SUCCESS",
      "order_id": "DH2026001",
      "data": {
        "customer_name": "Nguyễn Minh Anh",
        "product": "Máy lọc không khí",
        "quantity": 1,
        "warehouse": "Kho Hà Nội",
        "location": "Kệ A-03-12",
        "status": "Đang đóng gói",
        "tracking_number": null,
        "carrier": null
      }
    },
    "latency_ms": 1394.3
  },
  {
    "step": 3,
    "query": "chuyển trạng thái đang hàng DH2026002 sang Hủy, và tra thông tin đơn hàng DH2026001",
    "action_type": "FINAL_ANSWER",
    "thought": "OpenAI phản hồi trực tiếp bằng văn bản (không cần gọi công cụ).",
    "output": "Đã hoàn thành tất cả nhiệm vụ yêu cầu. \n\n1. Trạng thái của đơn hàng DH2026002 đã được cập nhật thành 'Hủy'.\n2. Thông tin đơn hàng DH2026001 như sau:\n   - Khách hàng: Nguyễn Minh Anh\n   - Sản phẩm: Máy lọc không khí (SL: 1)\n   - Trạng thái: Đang đóng gói\n   - Vị trí: Kệ A-03-12 tại Kho Hà Nội\n   - Mã vận đơn: chưa có\n   - Đơn vị vận chuyển: chưa phân công\n\nNếu cần hỗ trợ thêm, hãy cho tôi biết!",
    "latency_ms": 2369.09
  }
]
```

---

## 3. TỔNG KẾT KẾT QUẢ NGHIỆM THU & NỘP BÀI

- [x] Đã điền API Key thật trong `.env` và xác nhận Agent chạy mượt mà trên LLM API thật (Gemini/OpenAI).
- **Tổng số Test Cases đã chạy thành công:** 5 / 5 test cases.
- **Số lượt gọi Tool qua MCP Server chính xác:** 4 / 4 lượt.
- **Kết quả đẩy Repo nộp bài:** [x] Đã Commit và Push mã nguồn thành công lên GitHub cá nhân.

---

> ✅ **HOÀN TẤT NỘP BÀI:** Sao chép đường link GitHub Repository cá nhân của bạn và dán vào ô nộp bài trên hệ thống LMS VLearn để hoàn tất Bài Lab 3!
