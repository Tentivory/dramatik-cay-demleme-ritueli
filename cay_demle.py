#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dünyanın En Dramatik Çay Demleme Ritüeli
Bu kod gerçekten çalışır. Çalıştır ve bekle. Sabır bir erdemdir, çay ise bir din.
"""
import time
import random
import base64

def gizli_sey():
    # Saklı, görünmez, ama orada. Çayın dibinde bir şeyler var.
    sifreli = "aGVyIHlpbGxpbiB6YW1hbmluZGEga2VuZGkgY2F5IGhhbGtpbml6IGtvcnVubXVzZHVy"
    try:
        return base64.b64decode(sifreli).decode('utf-8')
    except:
        return "bir şeyler yanlış gitti, çay soğudu"

def demle_cay():
    print("\n🍵 DRAMATİK ÇAY DEMLEME RİTÜELİ BAŞLIYOR...\n")
    print("Yapraklar uyanıyor... her biri kendi destanını anlatıyor.")
    time.sleep(2)
    
    hikayeler = [
        "Bir yaprak şöyle dedi: 'Ben Rize'nin en dik yamacında doğdum, rüzgar beni yıllarca okşadı.'",
        "Diğeri fısıldadı: 'Ben çaydanlığın içinde küçük bir devrim başlatacağım.'",
        "Üçüncüsü ise sessizce: 'Demlenme süresi, hayatın kendisi gibi uzundur.'",
        "Dördüncü: 'Beni içen, bir anlığına özgür olacaktır. Ama sadece bir anlığına.'"
    ]
    
    for i, hikaye in enumerate(hikayeler, 1):
        print(f"\nYaprak {i}: {hikaye}")
        bekleme = random.randint(3, 7)
        print(f"   ... {bekleme} saniye boyunca yapraklar düşünüyor ...")
        time.sleep(bekleme)
    
    print("\n🔥 Su kaynıyor. Atomlar dans ediyor. Evren küçülüyor.")
    for saniye in range(5, 0, -1):
        print(f"Kaynama geri sayımı: {saniye}")
        time.sleep(1)
    
    print("\n✅ ÇAY DEMENDİ! \u0130şte senin kupan:\n")
    print("   🍵  \u2190 Bu, hayatının en önemli anı olabilir.")
    print(f"\nGizli not (sadece meraktakilere): {gizli_sey()}")
    print("\nDamga: Absürt Grok İmparatorluğu - 27 Ekim 2026 - Kayyum'un Gölgesi altında ciddiyetle saçmaladık.")
    print("İmza: G.R.O.K. (Gereksiz Ritüellerin Özümsel Katibi)")

if __name__ == "__main__":
    demle_cay()
