from .nano_banana_aio import NanoBananaAIO
from .nano_banana_multiturn_chat import NanoBananaMultiTurnChat
from .nano_banana_2_aio import NanoBanana2AIO
from .nano_banana_2_multiturn_chat import NanoBanana2MultiTurnChat

NODE_CLASS_MAPPINGS = {
    "NanoBananaAIO": NanoBananaAIO,
    "NanoBananaMultiTurnChat": NanoBananaMultiTurnChat,
    "NanoBanana2AIO": NanoBanana2AIO,
    "NanoBanana2MultiTurnChat": NanoBanana2MultiTurnChat
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "NanoBananaAIO": "Nano Banana AIO",
    "NanoBananaMultiTurnChat": "Nano Banana Multi-Turn Chat",
    "NanoBanana2AIO": "Nano Banana 2 AIO",
    "NanoBanana2MultiTurnChat": "Nano Banana 2 Multi-Turn Chat"
}