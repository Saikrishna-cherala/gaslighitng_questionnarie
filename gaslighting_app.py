import streamlit as st
import json
import datetime

# --- PAGE CONFIG ---
st.set_page_config(page_title="Gaslighting Impact Assessment", layout="wide")

# --- ADAPTIVE CUSTOM STYLES ---
# Using native CSS variables so it looks perfect in BOTH Light and Dark modes
st.markdown("""
    <style>
    /* Add a subtle box around each question that adapts to the theme */
    div[data-testid="stRadio"] {
        background-color: var(--secondary-background-color);
        padding: 15px 25px;
        border-radius: 10px;
        border: 1px solid rgba(128, 128, 128, 0.2);
        margin-bottom: 10px;
    }
    
    /* Ensure section headers match the theme text color */
    .section-header {
        font-family: 'Helvetica', sans-serif;
        color: var(--text-color);
        border-bottom: 2px solid var(--text-color);
        padding-bottom: 5px;
        margin-top: 40px;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- FULL DATASET (All 50 Questions) ---
SECTIONS = [
    {
        "title": "Section 1: Memory & Reality Distortion",
        "questions": [
            "How often do you doubt your own memory of specific events after talking to this person?",
            "Do you feel the need to record conversations or write down details to prove what happened?",
            "How frequently does this person tell you that you imagined or made up a situation?",
            "Do you find yourself questioning your own sanity or mental stability?",
            "How often do you walk away from a conversation feeling more confused than when you started?",
            "Does this person deny saying things that you clearly remember them saying?",
            "Do you feel like you are losing your mind in the context of this relationship?",
            "How often do you search for external evidence to validate your own feelings?",
            "Do you feel like you have to lawyer your way through conversations to stay grounded?",
            "How often do you doubt your ability to perceive the truth?",
        ]
    },
    {
        "title": "Section 2: Self-Esteem & Decision Making",
        "questions": [
            "Do you feel like you were a much more confident person before this relationship?",
            "How often do you feel like you cannot do anything right in their eyes?",
            "Do you find it difficult to make simple decisions without their input?",
            "How often do you apologize to this person, even when you are not sure what you did wrong?",
            "Do you feel too sensitive or dramatic because they tell you so?",
            "How often do you feel inadequate or not good enough?",
            "Do you second-guess your instincts about other people because of this person's influence?",
            "How frequently do you feel like you are walking on eggshells around them?",
            "Do you feel like your successes are minimized or ignored by this person?",
            "How often do you feel like you have lost your sense of self-identity?",
        ]
    },
    {
        "title": "Section 3: Social Isolation & External Validation",
        "questions": [
            "Do you hide details of your relationship from friends or family to avoid their judgment?",
            "Has this person suggested that your friends or family are against you or untrustworthy?",
            "Do you feel isolated from people who used to be close to you?",
            "How often does this person tell you that no one else will ever love or support you?",
            "Do you worry that if you told others the truth, they would not believe you?",
            "Does this person tell you that other people think you are crazy or difficult?",
            "Do you avoid social gatherings because you are afraid of how this person will react?",
            "Have you stopped pursuing hobbies or interests because this person mocked them?",
            "Do you feel like this person is the only one who truly understands you?",
            "How often do you feel like you have to manage this person's mood to keep the peace?",
        ]
    },
    {
        "title": "Section 4: Behavioural Adaptation",
        "questions": [
            "Do you lie to this person about small things just to avoid a conflict?",
            "How often do you rehearse what you are going to say to them in your head?",
            "Do you find yourself making excuses for their behaviour to others?",
            "How often do you withhold your true opinion because it is not worth the fight?",
            "Do you feel a sense of dread when you know you have to interact with them?",
            "How often do you check your phone obsessively for their messages?",
            "Do you feel a sense of relief when they are not around?",
            "Have you noticed physical symptoms (headaches, stomach aches) before seeing them?",
            "How often do you try to fix yourself to satisfy their complaints?",
            "Do you feel like you are constantly waiting for the other shoe to drop?",
        ]
    },
    {
        "title": "Section 5: The Narcissistic Loop",
        "questions": [
            "Does this person treat you like you are special one moment and worthless the next?",
            "Do they bring up your past mistakes to win current arguments?",
            "How often do they claim they are the real victim when you confront them?",
            "Does this person use your deepest insecurities against you during fights?",
            "Do you feel like the rules in the relationship change constantly?",
            "How often does this person give you the silent treatment as punishment?",
            "Do you feel like you are responsible for this person's happiness or anger?",
            "Does this person dismiss your feelings as irrational or crazy?",
            "Do you feel like you are stuck in a loop of the same argument that never gets resolved?",
            "How often do you feel hopeless about the relationship ever improving?",
        ]
    }
]

RESPONSE_OPTIONS = ["0 — Never", "1 — Rarely", "2 — Sometimes", "3 — Often", "4 — Very Often"]

# --- SIDEBAR (Project Metadata) ---
with st.sidebar:
    st.title("Project Details")
    st.write("**Researcher:** Sai Krishna")
    st.write("**Degree:** M.Tech")
    st.write("**Guide:** Dr. Rashmi Achla Minz")
    st.divider()
    st.info("This framework evaluates the emotional impact connected to multimodal gaslighting detection (audio and text analysis).")

# --- MAIN UI ---
st.title("Emotional Impact Questionnaire")
st.info("Gaslighting Pattern Detected. Please complete this assessment for your research record.")

# Sample snippet
st.warning("**🔍 Flagged Dialogue:** 'You are imagining things again. I never said that. You always twist my words.'")

responses = []
section_scores_dict = {}

# Generate All 50 Questions
for sec in SECTIONS:
    st.markdown(f"<h2 class='section-header'>{sec['icon']} {sec['title']}</h2>", unsafe_allow_html=True)
    
    sec_responses = []
    for i, q in enumerate(sec['questions']):
        # horizontal=True ensures the 0-4 options are in one single line
        choice = st.radio(
            f"**Q{i+1}:** {q}", 
            RESPONSE_OPTIONS, 
            index=None, 
            key=f"{sec['title']}_{i}",
            horizontal=True 
        )
        responses.append(choice)
        sec_responses.append(choice)
        
    section_scores_dict[sec['title']] = sec_responses

st.divider()

# --- RESULTS CALCULATION ---
if st.button("Submit & Calculate Results", type="primary", use_container_width=True):
    if None in responses:
        st.error("Please answer all 50 questions before submitting.")
    else:
        # Convert choice strings to integers for the total score
        scores = [int(r.split(" ")[0]) for r in responses]
        total = sum(scores)
        
        # Results Section
        st.balloons()
        st.header(f"Total Impact Score: {total} / 200")
        
        # Determine Severity Band
        if total <= 50:
            st.success("🟢 **Low Impact:** Suggests healthy boundaries or very occasional conflict.")
            severity = "Low Impact"
        elif total <= 100:
            st.warning("🟡 **Moderate Impact:** Indicates a high risk of psychological manipulation.")
            severity = "Moderate Impact"
        elif total <= 150:
            st.error("🟠 **High Impact:** Significant evidence of gaslighting. Possible Narcissistic Victim Syndrome.")
            severity = "High Impact"
        else:
            st.error("🔴 **Severe Impact:** Deep psychological impact. Immediate intervention or therapy strongly recommended.")
            severity = "Severe Impact"

        # Display Section Breakdown
        st.subheader("Score Breakdown by Section")
        for sec_title, sec_resps in section_scores_dict.items():
            sec_total = sum([int(r.split(" ")[0]) for r in sec_resps])
            st.write(f"**{sec_title}:** {sec_total} / 40")
            st.progress(sec_total / 40)

        # Data export for research records
        result_json = {
            "user": "Sai Krishna",
            "total_score": total,
            "max_score": 200,
            "severity_band": severity,
            "timestamp": str(datetime.datetime.now()),
            "status": "Verified"
        }
        st.download_button("Download Research Report (JSON)", json.dumps(result_json, indent=4), "questionnaire_results.json")
