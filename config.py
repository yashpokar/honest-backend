class Config:
	SECRET_KEY = b'K"[A]8K"z+-L?=7TvE@M@kL,0[Gii$ojelI&JRql#$wZ:gEX$j@ev4BEmv^(Hqi'
	DEBUG = False
	ALLOWED_ORIGINS = ''


class LocalConfig(Config):
	DEBUG = True

	MONGO_URI = 'mongodb://localhost:27017/honest'
	MONGO_COLLECTION_NAME = 'outlets'
	ALLOWED_ORIGINS = '*'
