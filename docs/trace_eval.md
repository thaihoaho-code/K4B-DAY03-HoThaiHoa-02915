# 📊 BÁO CÁO THU HOẠCH NGHIỆM THU BÀI LAB 3 (BƯỚC 3 — SUBMISSION ARTIFACT)

> **Họ và Tên Học viên:** Hồ Thái Hòa
> **Mã Sinh Viên / Mã Học viên:** 2A202602915
> **Chủ đề Lựa chọn:** 3.2: Trợ lý Đơn hàng & Kho vận (Supply Chain Agent)  

---

## 1. BẢNG CHẤM ĐIỂM AGENTIC FIT SCORING MATRIX (ĐÁNH GIÁ CHỦ ĐỀ)

| Tiêu chí Đánh giá | Mức độ (1 - 5) | Giải trình chi tiết lý do chọn điểm |
| :--- | :---:  :--- |
| **1. Multi-step Reasoning** | 3 / 5 | Một yêu cầu có thể bao gồm nhiều bước: xác định đơn hàng -> tra cứu mã vận đơn -> lấy trạng thái từ đơn vị vận chuyển -> kiểm tra vị trí hàng trong kho -> đối chiếu thông tin -> trả kết quả hoặc cập nhật trạng thái. Tuy nhiên với case này, quy trình tương đối rõ và không quá phức tạp|
| **2. Tool Interaction** | 5 / 5 | Agent cần tương tác với OMS/WMS, database kho, API đơn vị vận chuyển, ERP hoặc MCP Server để đọc và cập nhật dữ liệu. Một yêu cầu có thể gọi nhiều tool khác nhau |
| **3. Dynamic Decision** | 4 / 5 | Có. Ví dụ: nếu vận đơn chưa được tạo thì kiểm tra trạng thái đóng gói, nếu trạng thái giữa WMS và carrier không khớp thì cần kiểm tra hoặc báo bất thường. |
| **4. Long Horizon Goal** | 2 / 5 | Phần lớn chức năng sẽ hoàn thành trong thời gian ngắn. Ví dụ như: "đơn hàng tới đâu rồi?", Agent chưa cần duy trì mục tiêu qua nhiều giờ/ngày, trừ khi bổ sung chức năng chủ động theo dõi đơn hàng hoặc xử lý sự cố đến khi hoàn tất. |
| **TỔNG ĐIỂM AGENTIC FIT** | **14 / 20** | *Nếu tổng điểm > 12/20: Bài toán rất phù hợp triển khai Agentic System.* |
|
---

## 2. TRÍCH XUẤT KẾT QUẢ WATERFALL TRACE LOG (SAU KHI CHẠY TEST SUITE TRÊN API THẬT)

> ⚠️ **YÊU CẦU NGHIỆM THU:** Mở tệp `.env` điền `GEMINI_API_KEY` (hoặc `OPENAI_API_KEY`) để kết nối LLM thật trước khi thực thi `python src/app.py --all`. Bài nộp chỉ dùng Mock Offline Provider sẽ không đạt điểm nghiệm thực tế.

Dán 1 đoạn trích xuất log tiêu biểu từ file `docs/trace_waterfall.json` sinh ra từ phản hồi LLM API thật:

```json
[
  {
    "step": 1,
    "query": "Kiểm tra đơn hàng DH2026002 đang ở đâu",
    "action_type": "TOOL_EXECUTION",
    "tool_name": "order_query",
    "arguments": {
      "order_id": "DH2026002"
    },
    "observation": {
      "status": "SUCCESS",
      "order_id": "DH2026002",
      "data": {
        "customer_name": "Trần Quốc Bình",
        "product": "Robot hút bụi",
        "quantity": 1,
        "warehouse": "Kho Bình Dương",
        "location": "Khu xuất kho B-02",
        "status": "Đã xuất kho",
        "tracking_number": "VN2026002",
        "carrier": "Viettel Post"
      }
    },
    "latency_ms": 1508.63
  },
  {
    "step": 2,
    "query": "Kiểm tra đơn hàng DH2026002 đang ở đâu",
    "action_type": "FINAL_ANSWER",
    "thought": "Tổng hợp kết quả từ MCP Server thành công.",
    "output": "Thông tin đơn hàng DH2026002: Khách hàng Trần Quốc Bình, sản phẩm Robot hút bụi (SL: 1), trạng thái Đã xuất kho, vị trí Khu xuất kho B-02 tại Kho Bình Dương, mã vận đơn VN2026002, đơn vị vận chuyển Viettel Post.",
    "latency_ms": 10.0
  }
]
```

---

## 3. TỔNG KẾT KẾT QUẢ NGHIỆM THU & NỘP BÀI

- [x] Đã điền API Key thật trong `.env` và xác nhận Agent chạy mượt mà trên LLM API thật (Gemini/OpenAI).
- **Tổng số Test Cases đã chạy thành công:** 5 / 5 test cases.
- **Số lượt gọi Tool qua MCP Server chính xác:** 3 / 3 lượt.
- **Kết quả đẩy Repo nộp bài:** [x] Đã Commit và Push mã nguồn thành công lên GitHub cá nhân.

---

> ✅ **HOÀN TẤT NỘP BÀI:** Sao chép đường link GitHub Repository cá nhân của bạn và dán vào ô nộp bài trên hệ thống LMS VLearn để hoàn tất Bài Lab 3!
