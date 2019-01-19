from honest import create_app
from flask_script import Manager
from config import LocalConfig

app = create_app(LocalConfig)
manager = Manager(app)

if __name__ == '__main__':
	manager.run()
