import streamlit as st
import pandas as pd
import re
import joblib
from urllib.parse import urlparse


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="PhishGuard AI",
    page_icon="🛡️",
    layout="wide"
)
st.markdown("""
<style>

.main-title {
    font-size: 42px;
    font-weight: 700;
    text-align: center;
    margin-bottom: 5px;
}

.sub-title {
    text-align: center;
    font-size: 18px;
    color: #666;
    margin-bottom: 30px;
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# LOAD MODEL
# ==========================================

model = joblib.load("phishing_model.pkl")


def extract_features(url):

    original_url = url.strip()

    if not original_url.startswith(("http://", "https://")):
        url_for_parsing = "http://" + original_url
    else:
        url_for_parsing = original_url

    parsed = urlparse(url_for_parsing)

    domain = parsed.netloc.lower().split(":")[0]
    clean_domain = domain.replace("www.", "")

    # IP address
    ip_pattern = r"(\d{1,3}\.){3}\d{1,3}"
    has_ip = int(bool(re.fullmatch(ip_pattern, clean_domain)))

    # URL features
    url_length = len(original_url)
    num_dots = clean_domain.count(".")
    num_hyphens = clean_domain.count("-")

    # Special characters
    num_special_chars = sum(
        not c.isalnum() and c not in ".-"
        for c in original_url
    )

    # HTTPS
    has_https = int(original_url.startswith("https://"))

    # Domain length
    domain_length = len(clean_domain)

    # Subdomains
    num_subdomains = max(0, len(clean_domain.split(".")) - 2)

    # @ symbol
    has_at_symbol = int("@" in original_url)

    # Redirect count
    redirect_count = max(
        0,
        original_url.count("//") - 1
    )

    features = pd.DataFrame([{
        "url_length": url_length,
        "num_dots": num_dots,
        "num_hyphens": num_hyphens,
        "num_special_chars": num_special_chars,
        "has_ip": has_ip,
        "has_https": has_https,
        "domain_length": domain_length,
        "num_subdomains": num_subdomains,
        "has_at_symbol": has_at_symbol,
        "redirect_count": redirect_count
    }])

    return features

# ==========================================
# HEADER
# ==========================================

st.markdown(
    '<div class="main-title">🛡️ PhishGuard AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">'
    'AI-Powered Phishing Website Detection System'
    '</div>',
    unsafe_allow_html=True
)

st.write(
    "Enter a website URL and analyze its "
    "characteristics using our Machine Learning model."
)

st.divider()


# ==========================================
# URL INPUT
# ==========================================

st.subheader("🌐 Website Security Analysis")

url = st.text_input(
    "Enter Website URL",
    placeholder="example.com"
)


# ==========================================
# ANALYZE BUTTON
# ==========================================

if st.button(
    "🔍 Analyze Website",
    use_container_width=True
):

    if not url.strip() or "." not in url.strip():

        st.warning(
            "⚠️ Please enter a valid website URL."
        )

    else:

        features = extract_features(url)

        prediction = model.predict(features)[0]

        # Probability if available
        if hasattr(model, "predict_proba"):
            probabilities = model.predict_proba(features)[0]

            phishing_probability = (
                probabilities[1] * 100
            )

            legitimate_probability = (
                probabilities[0] * 100
            )

        else:
            phishing_probability = 0
            legitimate_probability = 0


        st.divider()

        st.subheader("📊 Analysis Result")


       # ==================================
        # RESULT DISPLAY
        # ==================================

        if prediction == 1:

            st.error(
                "🚨 Potential Phishing Website"
            )

            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "🛑 Phishing Probability",
                    f"{phishing_probability:.2f}%"
                )

            with col2:
                st.metric(
                    "✅ Legitimate Probability",
                    f"{legitimate_probability:.2f}%"
                )

            st.warning(
                "⚠️ This URL contains characteristics "
                "associated with phishing websites."
            )

        else:

            st.success(
                "✅ Appears Legitimate"
            )

            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "🛑 Phishing Probability",
                    f"{phishing_probability:.2f}%"
                )

            with col2:
                st.metric(
                    "✅ Legitimate Probability",
                    f"{legitimate_probability:.2f}%"
                )

            st.info(
                "ℹ️ No major phishing characteristics "
                "were detected in this URL."
            )

        

        # ==================================
        # FEATURE DETAILS
        # ==================================

        with st.expander(
            "🔎 View Extracted Features"
        ):

            st.dataframe(
                features,
                use_container_width=True
            )


# ==========================================
# PROJECT INFORMATION
# ==========================================

st.divider()

st.subheader("📌 About PhishGuard AI")

st.write(
    "PhishGuard AI is an academic cybersecurity "
    "project that uses a Random Forest Machine "
    "Learning classifier to identify potentially "
    "phishing websites."
)

col1, col2, col3 = st.columns(3)

with col1:

    st.info(
        "🤖 Machine Learning\n\n"
        "Random Forest Classifier"
    )

with col2:

    st.info(
        "📊 Dataset\n\n"
        "4,374 website records"
    )

with col3:

    st.info(
        "🎯 Accuracy\n\n"
        "91.43% on test data"
    )

st.caption(
    "Academic Project • PhishGuard AI"
)