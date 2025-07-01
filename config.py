import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class Config:
    """Base configuration"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'quickoo-secret-key-2024-uk-service'

    # Flask settings
    FLASK_APP = 'app.py'
    FLASK_ENV = os.environ.get('FLASK_ENV') or 'production'
    DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'

    # Security
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'

    # Mail settings (for production email functionality)
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.gmail.com'
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 587)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'True').lower() == 'true'
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER') or 'noreply@quickoo.co.uk'

    # Company settings
    COMPANY_NAME = 'Quickoo PVT LTD'
    COMPANY_EMAIL = 'info@quickoo.co.uk'
    COMPANY_PHONE = '+44 20 3576 1617'
    COMPANY_ADDRESS = '450 bath road, Longford, London,Heathrow, UB70EB'

    # SEO settings
    SEO_TITLE = 'Quickoo - Premium Car Service UK'
    SEO_DESCRIPTION = 'Premium car service provider in UK. Professional chauffeur services, airport transfers, and luxury transportation.'
    SEO_KEYWORDS = 'car service, chauffeur, UK, airport transfer, luxury transport, London'


class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    FLASK_ENV = 'development'


class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    FLASK_ENV = 'production'

    # Additional production security settings
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_NAME = 'quickoo_session'
    PERMANENT_SESSION_LIFETIME = 3600  # 1 hour


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': ProductionConfig
}