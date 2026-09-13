"""
🛠️ TOOL DEFINITIONS & EXECUTION BACKEND
Mã nguồn chứa danh sách Tool Schemas (JSON Schema) và Execution Layer phục vụ cho MCP Server.
"""

import json
from typing import Dict, Any

# ==============================================================================
# 1. KHAI BÁO TOOL SCHEMAS CHUẨN NATIVE JSON SCHEMA (TASK 1.2)
# ==============================================================================

TOOLS_SCHEMA = [
    # Tool 1: Tra cứu đơn hàng và vị trí lưu kho
    {
        "name": "order_query",
        "description": "Tra cứu thông tin đơn hàng, vị trí lưu kho và mã vận đơn bằng mã đơn hàng. Tuyệt đối chỉ dùng tool này khi người dùng cung cấp chính xác mã đơn hàng.",
        "parameters": {
            "type": "object",
            "properties": {
                "order_id": {
                    "type": "string",
                    "description": "Mã đơn hàng cần tra cứu (ví dụ: 'DH2026001'). Tuyệt đối không tự bịa ra mã nếu người dùng không cung cấp."
                }
            },
            "required": ["order_id"]
        }
    },
    
    # --------------------------------------------------------------------------
    # Tool 2: Cập nhật trạng thái đơn hàng
    # --------------------------------------------------------------------------
    {
        "name": "update_order_status",
        "description": "Cập nhật trạng thái xử lý hoặc vận chuyển của đơn hàng. Chỉ sử dụng khi người dùng cung cấp chính xác mã đơn hàng.",
        "parameters": {
            "type": "object",
            "properties": {
                "order_id": {
                    "type": "string",
                    "description": "Mã đơn hàng cần cập nhật (ví dụ: 'DH2026001'). Tuyệt đối không tự bịa ra mã."
                },
                "status": {
                    "type": "string",
                    "description": "Trạng thái mới của đơn hàng, ví dụ: 'Đã bàn giao cho đơn vị vận chuyển'"
                }
            },
            "required": ["order_id", "status"]
        }
    }
]

# ==============================================================================
# 2. MÔ PHỎNG DỮ LIỆU & HÀM THỰC THI TOOL (EXECUTION LAYER)
# ==============================================================================

MOCK_DATABASE = {
    "DH2026001": {
        "customer_name": "Nguyễn Minh Anh",
        "product": "Máy lọc không khí",
        "quantity": 1,
        "warehouse": "Kho Hà Nội",
        "location": "Kệ A-03-12",
        "status": "Đang đóng gói",
        "tracking_number": None,
        "carrier": None
    },
    "DH2026002": {
        "customer_name": "Trần Quốc Bình",
        "product": "Robot hút bụi",
        "quantity": 1,
        "warehouse": "Kho Bình Dương",
        "location": "Khu xuất kho B-02",
        "status": "Đã xuất kho",
        "tracking_number": "VN2026002",
        "carrier": "Viettel Post"
    }
}


def execute_order_query(order_id: str) -> str:
    """Tra cứu thông tin đơn hàng theo mã đơn."""
    normalized_order_id = order_id.strip().upper()
    order = MOCK_DATABASE.get(normalized_order_id)
    if order:
        return json.dumps({
            "status": "SUCCESS",
            "order_id": normalized_order_id,
            "data": order
        }, ensure_ascii=False)
    return json.dumps({
        "status": "NOT_FOUND",
        "message": f"Không tìm thấy đơn hàng có mã '{order_id}'"
    }, ensure_ascii=False)


def execute_update_order_status(order_id: str, status: str) -> str:
    """Cập nhật trạng thái đơn hàng."""
    normalized_order_id = order_id.strip().upper()
    order = MOCK_DATABASE.get(normalized_order_id)
    if not order:
        return json.dumps({
            "status": "NOT_FOUND",
            "message": f"Không tìm thấy đơn hàng có mã '{order_id}'"
        }, ensure_ascii=False)

    order["status"] = status
    return json.dumps({
        "status": "SUCCESS",
        "order_id": normalized_order_id,
        "new_status": status,
        "message": f"Đã cập nhật đơn hàng {normalized_order_id} sang trạng thái '{status}'."
    }, ensure_ascii=False)


# Router gọi tool thực tế
TOOL_ROUTER = {
    "order_query": execute_order_query,
    "update_order_status": execute_update_order_status
}

def dispatch_tool_call(tool_name: str, arguments: Dict[str, Any]) -> str:
    """Hàm trung chuyển thực thi tool"""
    if tool_name in TOOL_ROUTER:
        try:
            return TOOL_ROUTER[tool_name](**arguments)
        except Exception as e:
            return json.dumps({"status": "EXECUTION_ERROR", "error": str(e)}, ensure_ascii=False)
    return json.dumps({"status": "UNKNOWN_TOOL", "error": f"Tool '{tool_name}' không tồn tại!"}, ensure_ascii=False)
