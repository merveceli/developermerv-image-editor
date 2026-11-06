<img width="2048" height="1152" alt="image_20261106_115415" src="https://github.com/user-attachments/assets/f4e6b051-9350-4d9e-873b-896a0c9ac6fd" />🎨 developermerv-image-editor
<p align="center">
<img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/by-developermerv-FF6B00?style=for-the-badge" />
<img src="banner.png" width="100%" />
</p>

Fotoğraflara tek komutla filtre, boyutlandırma ve developermerv imzası ekleyen hafif editör

✨ Özellikler
🖋️ Sağ alta turuncu developermerv watermark
⚫ Siyah-beyaz, blur, keskinleştirme, parlaklık filtreleri
📱 Instagram için 1080px yeniden boyutlandırma
🚀 Pillow ile, düşük PC dostu
🚀 Kullanım
pip install Pillow
# İmza ekle
python main.py foto.jpg --watermark
# Siyah beyaz + imza
python main.py foto.jpg --filter bw --watermark
# Instagram boyutu
python main.py foto.jpg --resize 1080 --watermark
📸 Örnek
Önce: foto.jpg → Sonra: edited_foto.jpg (sağ altta developermerv imzası)

by developermerv
Made with ❤️ by @developermerv!
