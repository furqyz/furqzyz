import glob

replacements = {
    "1. İslamiyet Öncesi": "1. İslamiyet Öncesi Türk Tarihi",
    "2. İlk Türk İslam Dev.": "2. İlk Türk İslam Devletleri",
    "3. Anadolu Selçuklu": "3. Anadolu (Türkiye) Selçuklu Devleti",
    "4. Osmanlı Kültür": "4. Osmanlı Devleti Kültür ve Medeniyeti",
    "5. Osmanlı Kuruluş": "5. Osmanlı Devleti Kuruluş Dönemi (1299 - 1453)",
    "6. Osmanlı Yükselme": "6. Osmanlı Devleti Yükselme Dönemi (1453 - 1595)",
    "7. Osmanlı Duraklama": "7. XVII. Yüzyılda Osmanlı Devleti (Duraklama Dönemi) (1595 - 1699)",
    "8. Osmanlı Gerileme": "8. XVIII. Yüzyılda Osmanlı Devleti (Gerileme Dönemi) (1699 - 1792)",
    "9. Osmanlı Dağılma": "9. XIX. Yüzyılda Osmanlı Devleti (Dağılma Dönemi) (1792 - 1922)",
    "10. XX. Yy Osmanlı": "10. XX. Yüzyıl Başlarında Osmanlı Devleti",
    "11. M. Mücadele Hazırlık": "11. Millî Mücadele Hazırlık Dönemi",
    "12. I. TBMM Dönemi": "12. I. TBMM Dönemi ve Gelişmeleri (1920 - 1923)",
    "13. Muharebeler Dönemi": "13. Millî Mücadele Muharebeler Dönemi",
    "15. İç Politika": "15. Atatürk Dönemi İç Politika",
    "18. Türk Dış Politikası": "18. Atatürk Dönemi Türk Dış Politikası",
    "19. Cumhuriyet Kültürü": "19. Cumhuriyet Dönemi Kültür ve Medeniyeti",
    "20. XX. Yy Dünya": "20. XX. Yüzyıl Başlarında Dünya (1918 - 1939)",
    "22. Soğuk Savaş": "22. Soğuk Savaş Dönemi"
}

files = ['index.html'] + glob.glob('unitler/*.html')

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    for short, long in replacements.items():
        content = content.replace(f">{short}<", f">{long}<")
        
    # Also fix the sidebar height class
    # from max-h-[85vh] back to something smaller like max-h-[60vh] or a fixed pixel value
    content = content.replace('max-h-[85vh]', 'max-h-[60vh]')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Reverted nav items and updated height")
