
import streamlit as st

st.set_page_config(page_title="Simpson Strong-Tie Outreach Generator", layout="centered")

st.title("📬 Simpson Strong-Tie Sales Outreach Generator")

# Input fields
project_name = st.text_input("Project Name", "MFH Fischeln-Südwest")
units = st.number_input("Number of Units", value=160)
structure = st.selectbox("Structure Type", ["Concrete and Timber", "Concrete Only", "Steel Frame"])
stories = st.selectbox("Building Height", ["1–2 Story", "3–4 Story", "5+ Story"])
timeframe = st.text_input("Construction Timeline", "2024–2026")

# Button to generate
if st.button("Generate Outreach Assets"):
    # Generate dynamic text content
    email = f"""
Subject: Structural Solutions for {project_name}

Hi [Engineer Name],

With {units} units planned across {stories} buildings, this project is ideal for applying Simpson Strong-Tie systems to simplify code compliance and improve build speed.

✅ Anchors: AT-HP® or SET-XP® for ledger-to-slab or post-installed hold-downs
✅ Framing: ZMAX® joist hangers, rafter ties, post bases
✅ Lateral: Strong-Rod™ for uplift tie-down, Strong-Wall® for narrow bracing segments

Can we set up a short review with your engineering team next week?

Best,  
[Your Name] – Simpson Strong-Tie
"""

    call_script = f"""
Intro: Calling about the {project_name} project – I understand it features {stories.lower()} buildings with a {structure} structure.

Pitch:
- For foundation: use AT-HP® adhesive anchors for fast, compliant post-installs.
- For tie-downs: Strong-Rod™ system ensures continuity from roof to slab.
- For lateral: Strong-Wall® simplifies narrow wall bracing, especially where there are large windows.

CTA: Can we review the connector plan or do a quick technical alignment session next week?
"""

    # Output results
    st.subheader("📧 Generated Email")
    st.code(email, language="markdown")

    st.subheader("📞 Generated Call Script")
    st.code(call_script, language="markdown")
