import glob

replacements = {
    "1. İslamiyet Öncesi Türk Tarihi": "1. İslamiyet Öncesi",
    "2. İlk Türk İslam Devletleri": "2. İlk Türk İslam Dev.",
    "3. Anadolu (Türkiye) Selçuklu Devleti": "3. Anadolu Selçuklu",
    "4. Osmanlı Devleti Kültür ve Medeniyeti": "4. Osmanlı Kültür",
    "5. Osmanlı Devleti Kuruluş Dönemi (1299 - 1453)": "5. Osmanlı Kuruluş",
    "6. Osmanlı Devleti Yükselme Dönemi (1453 - 1595)": "6. Osmanlı Yükselme",
    "7. XVII. Yüzyılda Osmanlı Devleti (Duraklama Dönemi) (1595 - 1699)": "7. Osmanlı Duraklama",
    "8. XVIII. Yüzyılda Osmanlı Devleti (Gerileme Dönemi) (1699 - 1792)": "8. Osmanlı Gerileme",
    "9. XIX. Yüzyılda Osmanlı Devleti (Dağılma Dönemi) (1792 - 1922)": "9. Osmanlı Dağılma",
    "10. XX. Yüzyıl Başlarında Osmanlı Devleti": "10. XX. Yy Osmanlı",
    "11. Millî Mücadele Hazırlık Dönemi": "11. M. Mücadele Hazırlık",
    "12. I. TBMM Dönemi ve Gelişmeleri (1920 - 1923)": "12. I. TBMM Dönemi",
    "13. Millî Mücadele Muharebeler Dönemi": "13. Muharebeler Dönemi",
    "14. Atatürk'ün Hayatı": "14. Atatürk'ün Hayatı",
    "15. Atatürk Dönemi İç Politika": "15. İç Politika",
    "16. Atatürk İlkeleri": "16. Atatürk İlkeleri",
    "17. Atatürk İnkılapları": "17. Atatürk İnkılapları",
    "18. Atatürk Dönemi Türk Dış Politikası": "18. Türk Dış Politikası",
    "19. Cumhuriyet Dönemi Kültür ve Medeniyeti": "19. Cumhuriyet Kültürü",
    "20. XX. Yüzyıl Başlarında Dünya (1918 - 1939)": "20. XX. Yy Dünya",
    "21. II. Dünya Savaşı (1939 - 1945)": "21. II. Dünya Savaşı",
    "22. Soğuk Savaş Dönemi (1947 - 1990)": "22. Soğuk Savaş",
    "23. Yumuşama Dönemi (1961 - 1990)": "23. Yumuşama Dönemi",
    "24. Küreselleşen Dünya (1990 - 2026)": "24. Küreselleşen Dünya"
}

files = ['index.html'] + glob.glob('unitler/*.html')

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    for old, new in replacements.items():
        content = content.replace(f">{old}<", f">{new}<")
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Shortened nav items")
