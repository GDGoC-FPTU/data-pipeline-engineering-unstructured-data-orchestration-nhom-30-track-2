from pydantic import BaseModel, Field

# ==========================================
# ROLE 1: LEAD DATA ARCHITECT
# ==========================================

class UnifiedDocument(BaseModel):
    """
    Hệ thống cần 6 trường thông tin chuẩn (document_id, source_type, author, category, content, timestamp). 
    TODO: Khai báo các trường với kiểu dữ liệu str ở dưới.
    """
    document_id: str = Field(..., description="Mã định danh duy nhất của tài liệu")
    source_type: str = Field(..., description="Nguồn gốc tài liệu (ví dụ: PDF, Web, API)")
    author: str = Field(..., description="Tác giả hoặc đơn vị khởi tạo")
    category: str = Field(..., description="Phân loại nội dung")
    content: str = Field(..., description="Nội dung chi tiết của tài liệu")
    timestamp: str = Field(..., description="Thời gian tạo hoặc cập nhật (định dạng chuỗi)")
