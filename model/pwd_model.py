from sqlalchemy import Column, BigInteger, Integer, String

from .base_model import BaseModel


class PwdModel(BaseModel):
    __tablename__ = "t_pwd"

    email = Column(String(255), nullable=True, comment="邮箱")

    platform = Column(String(255), nullable=True, comment="平台")
    account = Column(String(255), nullable=True, comment="账号")
    password = Column(String(500), comment="密码")
    sort = Column(Integer, default=0, nullable=True, comment="排序")
    remark = Column(String(1000), comment="备注")

    def json(self):
        print()
        return {
            "id": self.id,
            "email": self.email,

            "platform": self.platform,
            "account": self.account,
            "password": self.password,

            "sort": self.sort,
            "remark": self.remark,
            "create_time": self.create_time.strftime("%Y-%m-%d"),
        }
