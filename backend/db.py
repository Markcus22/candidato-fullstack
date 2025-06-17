from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = "mongodb://root:6PaoFsr77wzl@57.129.59.106:27017/?authSource=admin"
client = AsyncIOMotorClient(MONGO_URI)
db = client["C11"]
