#!/usr/bin/env python3
"""
BEDA Core Test Runner
====================

BEDA Core modülü için basit test çalıştırıcı.
pytest kullanarak tüm testleri çalıştırır ve sonuçları raporlar.

Kullanım:
    python run_tests.py
    python run_tests.py --verbose
    python run_tests.py --coverage
"""

import sys
import os
import subprocess
from pathlib import Path


def run_tests(verbose=False, coverage=False):
    """
    Testleri çalıştır ve sonuçları göster
    
    Parametreler:
        verbose (bool): Detaylı çıktı
        coverage (bool): Coverage raporu
    """
    print("🧪 BEDA Core Test Sistemi")
    print("=" * 50)
    
    # Test dizinini kontrol et
    test_dir = Path(__file__).parent / "tests"
    if not test_dir.exists():
        print("❌ Test dizini bulunamadı")
        return False
    
    # pytest komutunu hazırla
    cmd = [sys.executable, "-m", "pytest"]
    
    if verbose:
        cmd.append("-v")
    else:
        cmd.append("-q")
    
    if coverage:
        cmd.extend(["--cov=beda_core", "--cov-report=term-missing"])
    
    cmd.append(str(test_dir))
    
    try:
        print(f"🚀 Test komutu: {' '.join(cmd[2:])}")
        print("-" * 50)
        
        # Testleri çalıştır
        result = subprocess.run(cmd, capture_output=False, text=True)
        
        print("-" * 50)
        if result.returncode == 0:
            print("✅ Tüm testler başarıyla geçti!")
            return True
        else:
            print("❌ Bazı testler başarısız oldu")
            return False
            
    except FileNotFoundError:
        print("❌ pytest bulunamadı. Kurulum: pip install pytest")
        return False
    except Exception as e:
        print(f"❌ Test çalıştırma hatası: {e}")
        return False


def main():
    """Ana fonksiyon"""
    import argparse
    
    parser = argparse.ArgumentParser(description="BEDA Core Test Runner")
    parser.add_argument("-v", "--verbose", action="store_true", help="Detaylı çıktı")
    parser.add_argument("-c", "--coverage", action="store_true", help="Coverage raporu")
    
    args = parser.parse_args()
    
    success = run_tests(verbose=args.verbose, coverage=args.coverage)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()