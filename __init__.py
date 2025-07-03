"""
BEDA Core - Modüler Yapay Zeka Motoru
====================================

BEDA Core, yeniden kullanılabilir AI bileşenleri sağlayan merkezi bir Python modülüdür.
Diğer projelere pip paketi gibi entegre edilebilir ve merkezi olarak güncellenebilir.

Özellikler:
- HuggingFace benzeri gelişmiş NLP işleme
- Redis destekli cache sistemi 
- Güvenlik ve loglama araçları
- Modüler mimari ile kolay entegrasyon

Kurulum:
    pip install git+https://replit.com/@username/beda-core-engine

Kullanım:
    from beda_core.ai.advanced_nlp import AdvancedNLPProcessor
    from beda_core.cache.redis_client import RedisCache
    from beda_core.helpers.logger import get_logger
    
    # AI işlemcisini başlat
    nlp = AdvancedNLPProcessor()
    result = nlp.comprehensive_analysis("Merhaba dünya!")
    
    # Cache sistemi
    cache = RedisCache()
    cache.set("key", "value", ttl=300)
    
    # Loglama sistemi
    logger = get_logger("MyApp")
    logger.info("Uygulama başlatıldı")

Lisans: MIT
Sürüm: 1.0.0
"""

__version__ = "1.0.0"
__author__ = "BEDA AI Team"
__license__ = "MIT"

# Core modül importları
from .ai.advanced_nlp import AdvancedNLPProcessor
from .cache import RedisCache
from .helpers.logger import get_logger
from .config.settings import BEDAConfig

# Kolay erişim için ana sınıflar
__all__ = [
    "AdvancedNLPProcessor",
    "RedisCache", 
    "get_logger",
    "BEDAConfig",
    "__version__"
]

# Modül başlatma mesajı
def _initialize_beda_core():
    """BEDA Core modülü başlatma fonksiyonu"""
    try:
        logger = get_logger("BEDA.Core")
        logger.info(f"BEDA Core v{__version__} başlatıldı")
        logger.info("Modüler AI motoru hazır")
        return True
    except Exception as e:
        print(f"BEDA Core başlatma hatası: {e}")
        return False

# Modül yüklendiğinde otomatik başlatma
_initialize_beda_core()