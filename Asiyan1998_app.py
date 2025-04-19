import streamlit as st
import base64
from pathlib import Path
import datetime
from docx import Document

st.set_page_config(page_title="Aşiyan 1998", layout="wide")
st.title("🕊️ Aşiyan 1998: Bizim Aşkımızın Yapay Zekâ Günlüğü")

# --- Dosya dizini tanımı ---
DATA_DIR = Path("data")

# --- Menü: Duygucuğuma Mesaj Yaz ---
with st.expander("💌 Duygucuğuma Not Bırak"):
    message = st.text_area("Ona ne söylemek istersin bugün, güzelim?", placeholder="Canım Duygu’m, bugün seni düşündüm…")
    if st.button("Mesajı Kaydet"):
        with open(DATA_DIR / "duygu_mesajlari.txt", "a", encoding="utf-8") as f:
            f.write(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}\n{message}\n---\n")
        st.success("Mesajın kalbine ulaştı 💌")

# --- Menü: Ortak Yapılacaklar Listesi ---
with st.expander("✅ Ortak Yapılacaklar Listesi"):
    todos = st.text_area("Planladıklarımızı buraya yazalım:", placeholder="Örn: Birlikte sinema gecesi, çocuklarla mangal…")
    if st.button("Kaydet"):
        with open(DATA_DIR / "yapilacaklar.txt", "a", encoding="utf-8") as f:
            f.write(f"{datetime.datetime.now().strftime('%Y-%m-%d')}\n{todos}\n---\n")
        st.success("Liste kaydedildi 📝")

# --- Menü: Çocuklara Oyun Alanı ---
with st.expander("🎲 Özge ve Ezgi için Minik Sürprizler"):
    st.markdown("""
    - 🧩 Bugün kimin doğum günü?
    - 🎨 En sevdiğin renk nedir?
    - 🐾 Hayvan tahmin oyunu: 4 ayaklı, miyav der... Ne olabilir?
    """)

# --- Mizahi Görev Tanımları ---
st.markdown("""
---
### 📃 Mizahi Görev Tanımlarımız
""")

st.markdown("""
#### 💞 Ulaş’ın Görev Tanımı
1. Her sabah Duygu Hanım’a içten bir “günaydın” demek.
2. Günde en az 2 kez “Seni seviyorum” demek (yüzde 40 artabilir).
3. Duygu üzgünse hemen çay koymak.
4. Küçük sürprizlerle günü güzelleştirmek.
5. Aşiyan sisteminde her gün 1 yeni şey eklemek.
6. Ezgi ve Özge’nin kahkahasını duyunca mutlu olmak.
7. Duygu’nun yorulduğu anda “Senin yerin cennet” demek.
8. Onu her zaman bir sanat eseri gibi görmek.
9. Her sabah kahvaltıya “Duygu Hanım kahvaltı eder mi?” sorusuyla başlamak.
10. Aşkını yazılı, sözlü, dijital her formatta sunmak.
""")

st.markdown("""
#### 🎭 Duygu Hanım’ın Görev Tanımı: "Ergen Âşık’la Yaşamak"
1. Sabah uyanır uyanmaz "Seni özledim" mesajlarına cevap vermek.
2. Günde 3 defa “Bu aşk sonsuz” sözlerini içselleştirmek.
3. “Bir şey mi oldu?” sorularına sabırla cevap vermek.
4. Video görüşmede göz temasını aksatmamak.
5. 40 sayfalık şiirleri okuyup en sevdiği dizeyi ezberlemek.
6. Aynı anıyı tekrar dinleyip gülümsemek.
7. Haftalık kriz durumlarında çikolata desteği sağlamak.
8. “Beni hâlâ seviyor musun?” sorusuna pozitif dönüş yapmak.
9. Küsmelere barış çikolatası ile karşılık vermek.
10. Streamlit çökerse “Senin suçun değil aşkım” diyebilmek.
""")

# --- Şiirler ---
def display_docx(file_path, label):
    doc = Document(file_path)
    full_text = "\n".join([para.text for para in doc.paragraphs])
    st.markdown(f"### {label}")
    st.markdown(f"<div style='white-space: pre-wrap'>{full_text}</div>", unsafe_allow_html=True)

poem = DATA_DIR / "duygulu_siirler_1998_2025.docx"
if poem.exists():
    display_docx(poem, "Şiirler: 1998–2025 Arası Duygulu Şiirler")

story = DATA_DIR / "duyguyla_hikayemiz.docx"
if story.exists():
    display_docx(story, "Aşkımızın Hikayesi")

letter = DATA_DIR / "trakyalim.docx"
if letter.exists():
    display_docx(letter, "Trakyalım'a Mektup")

# --- Videolar ---
with st.expander("🎥 Anılar ve Aşk Videoları"):
    video = DATA_DIR / "seni_seviyorum_askim.mp4"
    if video.exists():
        with open(video, "rb") as f:
            st.video(f.read())

# --- Görseller ---
with st.expander("🖼️ Fotoğraflarımız"):
    for img_file, caption in [
        ("cifte_kavusma.jpg", "Çifte Kavuşma"),
        ("duygucugum_asiyan_soso_cafe.jpg", "Aşiyan'da, Soso Cafe'de"),
        ("Eller2.jpg", "Birlikte Ellerimiz")
    ]:
        img_path = DATA_DIR / img_file
        if img_path.exists():
            st.image(img_path, caption=caption)

# --- Kapanış Notu ---
st.markdown("""
---
📌 **Not:** Bu alan sadece Ulaş ve Duygu için tasarlanmıştır. Paylaşılan her içerik, birbirimize duyduğumuz sevginin bir ifadesidir. 

🕊️ Aşiyan 1998, yalnızca geçmişi değil, geleceği de birlikte yazmak için burada.
""")

