# myapp/services.py
import os
import motor.motor_asyncio
from beanie import init_beanie
from django.conf import settings

# Beanie 모델이 들어있는 파일을 import
from persona_mbti.models import MyBeanieDocument

# 전역에서 한번만 초기화하기 위한 장치
_beanie_initialized = False

async def init_mongo():
    """
    비동기 컨텍스트 안에서 MongoDB & Beanie 초기화를 진행
    """
    global _beanie_initialized
    if _beanie_initialized:
        return  # 이미 초기화가 되어 있다면 재실행 방지

    # 1) Motor 클라이언트 생성
    client = motor.motor_asyncio.AsyncIOMotorClient(
        f"mongodb+srv://{os.getenv("MONGODB_USER")}:{os.getenv("MONGODB_PASSWORD")}@{os.getenv("MONGODB_HOST")}"
    )

    # 2) 데이터베이스 선택
    db = client[os.getenv("MONGODB_DATABASE_NAME")]

    # 3) Beanie 초기화 (등록할 Document 리스트)
    await init_beanie(database=db, document_models=[MyBeanieDocument])

    _beanie_initialized = True