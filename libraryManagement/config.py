class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://neondb_owner:npg_oIWq9NdM8cPT@ep-curly-glitter-a1xhzvfn-pooler.ap-southeast-1.aws.neon.tech/neondb?sslmode=require' 
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'thisisSecretKey'
    JWT_TOKEN_LOCATION = 'cookies'
    JWT_ACCESS_COOKIE_PATH = '/'
    JWT_COOKIE_CSRF_PROTECT = False
    JWT_SECRET_KEY = 'thisisSecretKey'