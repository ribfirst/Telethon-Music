import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "14547608"))
    API_HASH = os.environ.get("API_HASH", "c6c5e34f44bc5dd80dd2a4b894c7bcff")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5253002724:AAHvqxxpWE-fvmQe5F8DBvRE7OQC_6J5Um0")
    STRING_SESSION = os.environ.get("STRING_SESSION", "BAAJqZ97OoewSKWlU05svC2a6sVAGDcULGNRIVgWjzOyU7YEbLlU794K1hYPFkQC8l9Rou4r6tSO77NH0RvAMzgtDCW_gZ1l5eI-JpRQx5idYdktyNI-1Pk6hv4b57x3Cxsbw4lR3xNsDAhMdgBSwGkE7A2hhvhd17WyYa-FZlZOF1yW9bAABgld_pbHdPQVsgEkw4Y9-OEVAf1GqNiybpBOt_WugP6oqUHhv4N3hMF3md8TIbkNB4B7mpbAe0Q9eTiDvU33ChX3ZGG4qh0pZNVeHjW0Z6AFkDJ8oOOeaNKRD_N_KPO37PYKv-iz8rbShRosoZzgnckPKxhJ8V1GmyQpf0N3SgA")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Mss_Rosan_Bot")
    SUPPORT = os.environ.get("SUPPORT", "osmanigroupbot")
    CHANNEL = os.environ.get("CHANNEL", "teamosmani")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/9affea74c9eed1b4a1963.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "2135127882"))
