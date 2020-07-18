from decouple import config


USER = config('USER')
PASS = config('PASS')
DATABASE = config('DATABASE')

CONN_STRING = f"mongodb://{USER}:{PASS}@research.dynaptics.xyz/{DATABASE}"