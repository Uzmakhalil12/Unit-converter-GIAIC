import streamlit as st
import random

# List of Growth Mindset Challenges
challenges = [
    "Try something new today that you've never done before.",
    "Write down three things you learned from a mistake.",
    "Spend 10 minutes reading about a topic you find difficult.",
    "Compliment someone on their effort rather than their talent.",
    "Practice gratitude by writing down three things you're thankful for.",
    "Turn a failure into a lesson – reflect on what you can improve.",
    "Push yourself outside your comfort zone today.",
    "Encourage someone else to keep going despite difficulties."
]

# List of Motivational Quotes
quotes = [
    "Success is not final, failure is not fatal: it is the courage to continue that counts. _ Winston Churchill",
    "Your only limit is your mind.",
    "Dream big and dare to fail. _ Norman Vaughan",
    "Difficulties in life are intended to make us better, not bitter.",
    "A positive attitude can really make dreams come true.",
    "It does not matter how slowly you go as long as you do not stop. _ Confucius",
    "Growth and comfort do not coexist. _ Ginni Rometty",
    "Believe you can and youre halfway there. _ Theodore Roosevelt"
]

# Select a random challenge and quote
daily_challenge = random.choice(challenges)
daily_quote = random.choice(quotes)

# Streamlit App UI
st.title("🌱 Growth Mindset Challenge")
st.subheader("🚀 Today's Challenge:")
st.write(f"{daily_challenge}")

st.subheader("💡 Motivational Quote:")
st.write(f"{daily_quote}")

# Progress tracking
if "completed_challenges" not in st.session_state:
    st.session_state.completed_challenges = 0

if st.button("✅ I Completed This Challenge!"):
    st.session_state.completed_challenges += 1
    st.success(f"Great job! You've completed {st.session_state.completed_challenges} challenges.")

# Display progress
st.sidebar.title("📊 Your Progress")
st.sidebar.write(f"Challenges Completed: *{st.session_state.completed_challenges}*")

# Save the script
script_path = "/mnt/data/growth_mindset_app.py"
with open(script_path, "w") as file:
    file.write("""
import streamlit as st
import random

challenges = [
    "Try something new today that you've never done before.",
    "Write down three things you learned from a mistake.",
    "Spend 10 minutes reading about a topic you find difficult.",
    "Compliment someone on their effort rather than their talent.",
    "Practice gratitude by writing down three things you're thankful for.",
    "Turn a failure into a lesson – reflect on what you can improve.",
    "Push yourself outside your comfort zone today.",
    "Encourage someone else to keep going despite difficulties."
]

quotes = [
    "Success is not final, failure is not fatal: it is the courage to continue that counts. _ Winston Churchill",
    "Your only limit is your mind.",
    "Dream big and dare to fail. _ Norman Vaughan",
    "Difficulties in life are intended to make us better, not bitter.",
    "A positive attitude can really make dreams come true.",
    "It does not matter how slowly you go as long as you do not stop. _ Confucius",
    "Growth and comfort do not coexist. _ Ginni Rometty",
    "Believe you can and youre halfway there. _ Theodore Roosevelt"
]

daily_challenge = random.choice(challenges)
daily_quote = random.choice(quotes)

st.title("🌱 Growth Mindset Challenge")
st.subheader("🚀 Today's Challenge:")
st.write(f"*{daily_challenge}*")

st.subheader("💡 Motivational Quote:")
st.write(f"{daily_quote}")

if "completed_challenges" not in st.session_state:
    st.session_state.completed_challenges = 0

if st.button("✅ I Completed This Challenge!"):
    st.session_state.completed_challenges += 1
    st.success(f"Great job! You've completed {st.session_state.completed_challenges} challenges.")

st.sidebar.title("📊 Your Progress")
st.sidebar.write(f"Challenges Completed: *{st.session_state.completed_challenges}*")
""")

# Return the file path
script_path