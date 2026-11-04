import streamlit as st
import streamlit.components.v1 as components

st.markdown("""
<style>
#MainMenu {display:none;}
footer {display:none;}
header {display:none;}
.stDeployButton {display:none;}
[data-testid="stToolbar"] {display:none;}
[data-testid="stDecoration"] {display:none;}
.viewerBadge_container__1QSob {display:none;}
</style>
""", unsafe_allow_html=True)

st.set_page_config(
    page_title="Text Repeater | Beginner_Coder",
    page_icon="🔁",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------- DESIGN ----------
st.markdown("""
<style>
@import url('https://googleapis.com');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}
.stApp {
    background:
      radial-gradient(circle at 15% 5%, rgba(0,145,255,.16), transparent 30%),
      radial-gradient(circle at 90% 25%, rgba(0,70,160,.12), transparent 28%),
      #050914;
    color: #edf6ff;
}
header {visibility: hidden;}
footer {visibility: hidden;}
.block-container {
    max-width: 1120px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}
.hero {
    text-align: center;
    padding: 28px 18px 20px;
    border: 1px solid rgba(56,189,248,.24);
    border-radius: 22px;
    background: linear-gradient(135deg, rgba(9,26,48,.94), rgba(5,12,27,.92));
    box-shadow: 0 0 35px rgba(0,145,255,.09);
    margin-bottom: 24px;
}
.hero h1 {
    color: #eaf7ff;
    font-size: clamp(2rem, 5vw, 3.2rem);
    font-weight: 800;
    letter-spacing: 2px;
    margin: 0;
}
.hero h1 span { color: #38bdf8; }
.hero p {
    color: #9bb8d2;
    margin: 10px 0 0;
}
.section-card {
    background: rgba(10,22,40,.82);
    border: 1px solid rgba(56,189,248,.19);
    border-radius: 17px;
    padding: 18px;
    margin-bottom: 12px;
}
.small-label {
    color: #7dd3fc;
    font-size: .82rem;
    font-weight: 700;
    letter-spacing: 1.2px;
    text-transform: uppercase;
    margin-bottom: 6px;
    margin-top: 10px;
}
div[data-testid="stTextArea"] textarea,
div[data-testid="stTextInput"] input,
div[data-testid="stNumberInput"] input,
div[data-testid="stSelectbox"] div[data-baseweb="select"] {
    background: #081629 !important;
    color: #f1f8ff !important;
    border: 1px solid #17466c !important;
    border-radius: 11px !important;
}
div[data-testid="stTextArea"] textarea:focus,
div[data-testid="stTextInput"] input:focus {
    border-color: #38bdf8 !important;
    box-shadow: 0 0 0 1px #38bdf8 !important;
}
.stButton > button, .stDownloadButton > button {
    width: 100%;
    border: 1px solid #168bd0;
    border-radius: 11px;
    min-height: 44px;
    color: white;
    font-weight: 700;
    background: linear-gradient(100deg, #075a9d, #078dcc);
    transition: .2s ease;
}
.stButton > button:hover, .stDownloadButton > button:hover {
    border-color: #7dd3fc;
    box-shadow: 0 0 18px rgba(14,165,233,.35);
    color: white;
}
div[data-testid="stMetric"] {
    background: #091a2e;
    border: 1px solid #17466c;
    border-radius: 13px;
    padding: 14px;
}
div[data-testid="stMetricLabel"] { color: #9bb8d2; }
div[data-testid="stMetricValue"] { color: #7dd3fc; }
hr { border-color: rgba(56,189,248,.2); }
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown("""
<div class="hero">
  <h1>TEXT <span>REPEATER</span></h1>
  <p>Repeat text instantly. Customize it. Copy it. Download it.</p>
</div>
""", unsafe_allow_html=True)

# Initialize Session States safely
if "input_text_val" not in st.session_state:
    st.session_state.input_text_val = ""
if "generated_text" not in st.session_state:
    st.session_state.generated_text = ""
if "generated_count" not in st.session_state:
    st.session_state.generated_count = 0

left, right = st.columns([1.05, 0.95], gap="large")

with left:
    st.markdown('<div class="small-label">01 / Your text</div>', unsafe_allow_html=True)
    source_text = st.text_area(
        "Enter text",
        value=st.session_state.input_text_val,
        placeholder="Type or paste your text here...",
        height=140,
        label_visibility="collapsed"
    )
    st.caption(f"Input characters: {len(source_text):,}")

    st.markdown('<div class="small-label">02 / Repeat settings</div>', unsafe_allow_html=True)
    repeat_count = st.number_input(
        "How many times should it repeat?",
        min_value=1,
        max_value=5000,
        value=10,
        step=1
    )
    
    # Text Case Formatting
    st.markdown('<div class="small-label">🔠 Text Case Transformation</div>', unsafe_allow_html=True)
    case_choice = st.selectbox(
        "Change text case style",
        ["Keep Original (No change)", "UPPERCASE", "lowercase", "Capitalize Each Word"]
    )

with right:
    st.markdown('<div class="small-label">03 / Customize output</div>', unsafe_allow_html=True)
    separator_choice = st.selectbox(
        "Separator between repetitions",
        ["New line", "Space", "Comma + space", "No separator", "Custom"]
    )
    custom_separator = ""
    if separator_choice == "Custom":
        custom_separator = st.text_input(
            "Custom separator",
            placeholder="For example:  |  or  ***"
        )

    prefix = st.text_input("Prefix (optional)", placeholder="Add before every repetition")
    suffix = st.text_input("Suffix (optional)", placeholder="Add after every repetition")
    
    # Numbering Toggle
    st.markdown('<div class="small-label">🔢 Indexing Options</div>', unsafe_allow_html=True)
    add_numbering = st.checkbox("Add numbering (e.g., 1. Text, 2. Text)")

st.divider()

# FIXED LINE: Columns are assigned with explicit layout configuration
generate_col, clear_col = st.columns(2)
with generate_col:
    generate = st.button("⚡ GENERATE TEXT", use_container_width=True)
with clear_col:
    clear = st.button("↻ CLEAR", use_container_width=True)

# Fixed Clear Processing
if clear:
    st.session_state.input_text_val = ""
    st.session_state.generated_text = ""
    st.session_state.generated_count = 0
    st.rerun()

if generate:
    if not source_text:
        st.warning("Please enter some text first.")
    else:
        st.session_state.input_text_val = source_text
        
        # Apply Case Transformation
        modified_text = source_text
        if case_choice == "UPPERCASE":
            modified_text = source_text.upper()
        elif case_choice == "lowercase":
            modified_text = source_text.lower()
        elif case_choice == "Capitalize Each Word":
            modified_text = source_text.title()

        separators = {
            "New line": "\n",
            "Space": " ",
            "Comma + space": ", ",
            "No separator": "",
            "Custom": custom_separator
        }
        separator = separators[separator_choice]
        
        items_list = []
        for i in range(1, int(repeat_count) + 1):
            num_prefix = f"{i}. " if add_numbering else ""
            one_piece = f"{num_prefix}{prefix}{modified_text}{suffix}"
            items_list.append(one_piece)

        full_output = separator.join(items_list)
        
        if len(full_output) > 2_000_000:
            st.error("This output would be larger than 2 million characters. Reduce the repeat count or input text.")
        else:
            st.session_state.generated_text = full_output
            st.session_state.generated_count = int(repeat_count)
            st.success("Your text has been generated!")

# ---------- RESULTS ----------
if st.session_state.generated_text:
    result = st.session_state.generated_text
    st.markdown("## ✨ Generated result")

    m1, m2, m3 = st.columns(3)
    m1.metric("Repetitions", f"{st.session_state.generated_count:,}")
    m2.metric("Characters", f"{len(result):,}")
    m3.metric("Words", f"{len(result.split()):,}")

    st.markdown('<div class="small-label">Your output</div>', unsafe_allow_html=True)
    st.text_area(
        "Generated text",
        value=result,
        height=260,
        label_visibility="collapsed"
    )
    
    # --- JS CLIPBOARD COPY ACTION ---
    safe_text = result.replace("\\", "\\\\").replace("`", "\\`").replace("$", "\\$")
    copy_html = f"""
    <button id="copy-btn" style="
        width: 100%;
        border: 1px solid #17bd72;
        border-radius: 11px;
        min-height: 44px;
        color: white;
        font-weight: 700;
        background: linear-gradient(100deg, #0e8f54, #12b569);
        cursor: pointer;
        font-size: 14px;
        font-family: 'Inter', sans-serif;
        letter-spacing: 1px;
        transition: .2s ease;
        margin-bottom: 12px;
    ">📋 COPY TO CLIPBOARD</button>

    <script>
    document.getElementById('copy-btn').addEventListener('click', function() {{
        const textToCopy = `{safe_text}`;
        navigator.clipboard.writeText(textToCopy).then(function() {{
            const btn = document.getElementById('copy-btn');
            btn.innerText = '✅ COPIED SUCCESSFULLY!';
            btn.style.background = '#1480b8';
            btn.style.borderColor = '#38bdf8';
            setTimeout(function() {{
                btn.innerText = '📋 COPY TO CLIPBOARD';
                btn.style.background = 'linear-gradient(100deg, #0e8f54, #12b569)';
                btn.style.borderColor = '#17bd72';
            }}, 1800);
        }}).catch(function(err) {{
            alert('Error copying text: ', err);
        }});
    }});
    </script>
    """
    components.html(copy_html, height=58)

    st.download_button(
        "⬇️ DOWNLOAD TEXT FILE",
        data=result.encode("utf-8"),
        file_name="repeated_text.txt",
        mime="text/plain",
        use_container_width=True
    )

st.markdown("""
<div style="text-align:center; padding:28px 0 4px; color:#6485a4;">
  <div style="color:#38bdf8;font-weight:700;letter-spacing:2px;">BEGINNER_CODER</div>
  <div style="font-size:12px;margin-top:6px;">A simple tool. A clean result.</div>
</div>
""", unsafe_allow_html=True)
