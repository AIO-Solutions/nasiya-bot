import sys
from settings import Setting

setting = Setting(file = 'data/setting.json')

if 'true' in sys.argv:
    setting.data['server'] = '1'
    setting.update()

elif 'false' in sys.argv:
    setting.data['server'] = '0'
    setting.update()