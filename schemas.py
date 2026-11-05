from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field, EmailStr


class UserBase(BaseModel):
    username: str = Field(min_length=1, max_length=50)
    email: EmailStr = Field(max_length=120)

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    image_file: str | None
    image_path: str


class PostBase(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    content: str = Field(min_length=1)


class PostCreate(PostBase):
    user_id: int  # TEMPORARY


class PostResponse(PostBase):
    # 允许 Pydantic 从对象属性（如 ORM 模型实例）读取字段，构建并校验响应模型。
    # 默认 from_attributes=False，Pydantic 接收字典等映射数据来构建模型，例如 {"title": "标题", ...}，不会自动读取普通对象的属性。
    # 设置为 True 后，就可以直接传入 ORM 实例，Pydantic 会从 post.title、post.id 等属性中提取字段，再进行校验。
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int
    date_posted: datetime
    author: UserResponse
