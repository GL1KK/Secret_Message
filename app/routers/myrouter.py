from fastapi import APIRouter, HTTPException
from uuid import uuid4

class Router:
    def __init__(self):
        self.router = APIRouter()
        self.all_sms = {}
        self.__setup_routers()
    def __setup_routers(self):
        self.router.post("/post_sms")(self.post_sms)
        self.router.get("/sms/{sms_id}")(self.get_sms)
    async def post_sms(self, name: str, sms: str):
        sms_id = str(uuid4())
        self.all_sms[sms_id] = {
            "name": name,
            "sms": sms,
        }
        return f"http://127.0.0.1:8000/sms/{sms_id}"
    async def get_sms(self, sms_id: str):
        try:
            return self.all_sms.pop(sms_id)
        except KeyError:
            raise HTTPException(status_code=404, detail="Сообщение уже было открыто!")