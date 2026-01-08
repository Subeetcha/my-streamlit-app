import streamlit as st

# Set page config
st.set_page_config(page_title="Immunoapp", layout="centered")

# Set background color using HTML/CSS
st.markdown(
    """
    <style>
    body {
        background-color: #ADD8E6;  /* Light blue background */
    }
    .result-box {
        padding: 15px;
        margin: 10px 0;
        border-radius: 8px;
        font-size: 16px;
        font-weight: bold;
        color: white;
    }
    .normal {
        background-color: #4CAF50; /*light green*/
    }
    .abnormal {
        background-color: #ff0000; /*red*/
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🩺 Immunoapp")
st.markdown("Enter the biomarker values below:")

# Input biomarkers
cd19 = st.number_input("CD19", min_value=0.0)
cd34 = st.number_input("CD34 (cells/µL)", min_value=0.0)
anti_ccp = st.number_input("Anti-CCP (u/ml)", min_value=0.0)
rf = st.number_input("RF (u/ml)", min_value=0.0)
il6 = st.number_input("IL-6 (pg/ml)", min_value=0.0)
tnf = st.number_input("TNF-alpha (pg/ml)", min_value=0.0)
testosterone = st.number_input("Testosterone (ng/dl)", min_value=0.0)
gfap = st.number_input("GFAP (pg/ml)", min_value=0.0)

# Button to check
if st.button("Check Health Status"):
    results = []

    # Helper function to return a styled box
    def box_text(text, is_normal=True):
        box_class = "normal" if is_normal else "abnormal"
        return f'<div class="result-box {box_class}">{text}</div>'

    # CD19
    if cd19 > 500:
        results.append(box_text("CD19: Abnormal-Blood cancer risk", is_normal=False))
    else:
        results.append(box_text("CD19: Normal"))

    # CD34
    if cd34 < 50:
        results.append(box_text("CD34: Normal"))
    else:
        results.append(box_text("CD34: Abnormal-Blood cancer risk", is_normal=False))

    # Anti CCP
    if anti_ccp < 20:
        results.append(box_text("Anti-CCP: Negative"))
    elif 20 <= anti_ccp <= 39:
        results.append(box_text("Anti-CCP: Weakly Positive-RA risk", is_normal=False))
    elif 40 <= anti_ccp <= 59:
        results.append(box_text("Anti-CCP: Moderately Positive-RA risk", is_normal=False))
    else:
        results.append(box_text("Anti-CCP: High Positive-RA risk", is_normal=False))

    # RF
    if rf > 60:
        results.append(box_text("RF: Positive-RA risk", is_normal=False))
    else:
        results.append(box_text("RF: Normal"))

    # IL-6
    if il6 > 5:
        results.append(box_text("IL-6: Elevated-Osteoarthritis risk", is_normal=False))
    else:
        results.append(box_text("IL-6: Normal"))

    # TNF-alpha
    if tnf > 29.4:
        results.append(box_text("TNF-alpha: Osteoarthritis risk", is_normal=False))
    else:
        results.append(box_text("TNF-alpha: Normal"))

    # Testosterone
    if testosterone < 15 or testosterone > 70:
        results.append(box_text("Testosterone: Abnormal-PCOD risk", is_normal=False))
    else:
        results.append(box_text("Testosterone: Normal"))
    if abs(lh_fsh - 1.0) < 0.2:
        results.append(box_text("Abnormal-PCOD risk", is_normal=False))
    else 
        results.append(box_text("Normal"))
    # GFAP
    if gfap > 30:
        results.append(box_text("GFAP: Elevated-Heartstroke risk", is_normal=False))
    else:
        results.append(box_text("GFAP: Normal"))

    # Show results
    st.subheader("Results:")
    for r in results:
        st.markdown(r, unsafe_allow_html=True)

    st.warning("This app gives alerts when it is connected with the implantale chip.")


