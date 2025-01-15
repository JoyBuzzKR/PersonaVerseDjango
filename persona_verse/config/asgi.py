"""
ASGI config for persona_verse project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os
import asyncio
import django
from django.core.asgi import get_asgi_application

from common.setup import init_mongo

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

# Beanie 초기화 호출
# 비동기로 호출 (가능한 한 번만 실행)
# asyncio.run(init_mongo())

application = get_asgi_application()

loop = asyncio.get_event_loop()
loop.create_task(init_mongo())