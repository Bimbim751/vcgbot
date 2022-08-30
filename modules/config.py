import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}
aiohttpsession = aiohttp.ClientSession()

API_ID = int(getenv("API_ID", "12655083"))
API_HASH = getenv("API_HASH", "ed0c564a2c3bc6b2a3b355cf4556498a")
BOT_TOKEN = getenv("BOT_TOKEN", "5297319132:AAFW5Tbb9EhrXAMiFKeEJz8GkCOmaeyehrI")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
STRING_SESSION = getenv("STRING_SESSION", "AQBap_R0o7igk0vVRTTNh6jwSRLtD5XOLnGgplBMqFX3hMbrONCnamsqjGqeLyOXWlnx-j_2YmNBh_sFaDk8t9hjoGW4XUPkFaf17pGnw89_hfSuo7Pooze3ya80YAeggi2hJ_DujY5UVmL_Wo3Qzrv1YlV7j0dzV6RaBadbqyhHGDyB1NHjkfYKPrLPpO7Q0Z7ye3533Gq1rrVY-iGiKbQjGlN0iEs9-XklsZSJN1bkNyYy-3EdafnNd8PfybvJU1NVXzm5HPGjamVtMdssx7RTsUOlF554C2iXzCH5Ifd8mVxu_4pqwZ-9_Yhcu59wtIg8YBK7mlw55cZVT47NxYDWAAAAAUmiCkMA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! $ .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5530323523 1965477321").split()))
