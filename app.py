import streamlit as st
from PIL import Image
import tempfile
from pathlib import Path
from yolov7_infer import run_detection

st.set_page_config(page_title="Threat Detection", layout="centered")

st.title("🛡️ YOLOv7 Threat Detection")
st.caption("Upload an image. We’ll scan it for threats like knives 🔪 and guns using my custom YOLOv7 model!")

uploaded = st.file_uploader("📁 Upload an image", type=["jpg", "jpeg", "png"])

if uploaded:
    img = Image.open(uploaded)
    st.image(img, caption="Uploaded Image", use_container_width=True)

    if st.button("🔍 Detect Threat"):
        with st.spinner("Analyzing for potential threats..."):
            with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as tmp:
                img.save(tmp.name)
                output_path, labels, count = run_detection(Path(tmp.name))

            st.success(f"✅ Detection complete! Found {count} threat{'s' if count != 1 else ''}.")
            if count > 0:
                st.write("### Detected Classes:")
                st.write(", ".join(set(labels)))
            st.image(output_path, caption="Detection Result", use_container_width=True)
