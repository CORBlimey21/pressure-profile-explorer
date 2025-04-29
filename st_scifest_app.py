import streamlit as st
import pandas as pd

st.markdown(
    """
    <style>
    .block-container {
        background-image: url('https://static.vecteezy.com/system/resources/thumbnails/038/585/123/small_2x/ai-generated-minimalist-wave-white-background-free-photo.jpg');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        padding: 2rem;
        color: #000000;
    }

    h1, h2, h3 {
        color: #222222;
    }

    .stSlider label {
        font-weight: bold;
    }

    .stMetric {
        background-color: rgba(255, 255, 255, 0.7);
        border-radius: 10px;
        padding: 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)



# Load dataset
df = pd.read_csv("2and5.csv")

st.title("🎓 Pressure Profile Explorer")
st.write("Enter your weekly extracurricular and daily academic hours **outside of school** to discover your pressure profile based on real student data.")

# User input sliders with your specific limits
ec_input = st.slider("🎨 Weekly Extracurricular Hours", 0.5, 8.0, 2.0, 0.5)
hw_input = st.slider("📚 Daily Academic Hours", 0.5, 3.0, 1.5, 0.5)

if ec_input > 5.5:
    st.warning("Your hours on extracurriculars is beyond the range of the available data (5.5 hours). Results might be less accurate.")

ec_input = min(ec_input, df['ec_hours'].max())

# Filter dataset for students within ±1 hour
ec_range = (df['ec_hours'] >= ec_input - 1) & (df['ec_hours'] <= ec_input + 1)
hw_range = (df['hw_hours'] >= hw_input - 1) & (df['hw_hours'] <= hw_input + 1)
similar_students = df[ec_range & hw_range]

# Determine profile
def determine_profile(ec, hw):
    if ec <= 1 and hw <= 1:
        return "Take-it-easy Explorer"
    elif ec >= 4 and hw >= 2.5:
        return "Stretched Achiever"  
    elif abs(hw - ec) <= 1.0:
        return "Well-Rounded Learner"
    elif ec > hw:
        return "Activity Adventurer"
    elif hw > ec:
        return "Academic Driver"
    else:
        return "Well-Rounded Learner"

# Traits for display
def show_traits(profile_type):
    traits = {
        "Stretched Achiever": [
            "🎯 Aim for top grades",
            "📅 Participate in many demanding activities",
            "⚠️ Often report stress"
        ],
        "Take-it-easy Explorer": [
            "😌 Low homework and activity load",
            "🌱 Enjoy life without pressure",
            "🎨 Tend to explore interests casually"
        ],
        "Activity Adventurer": [
            "🎭 Prefer extracurriculars and hobbies",
            "🎸 Trade off study time for passions"
        ],
        "Academic Driver": [
            "📖 Strong academic focus",
            "📈 May feel academic pressure"
        ],
        "Well-Rounded Learner": [
            "🔄 Balanced routine",
            "🙂 Moderate pressure levels"
        ]
    }
    return traits.get(profile_type, [])

if similar_students.empty:
    st.warning("No similar students found. Try different values.")
else:
    avg_pressure = similar_students['pressure'].mean()
    profile_type = determine_profile(ec_input, hw_input)
    st.subheader(f"🧬 Your Pressure Profile: {profile_type}")

    for trait in show_traits(profile_type):
        st.markdown(f"- {trait}")


st.subheader("Some wellbeing tips based on your profile:")
# Provide tailored advice based on the profile type        
if profile_type == "Stretched Achiever":
    st.write("⚠️ You might be feeling **higher pressure** than your peers. Consider balancing your commitments.")
    st.write("Take regular breaks, and try using time management tools like the Pomodoro technique. You might also consider delegating tasks or saying 'no' to extra commitments when possible. Your mental health is as important as your success.")
elif profile_type == "Take-it-easy Explorer":
    st.write("✅ You seem to have a **relaxed schedule**. This is great for your well-being!")
    st.write("While it's fantastic to have less pressure, make sure to keep exploring new activities or skills that excite you. Sometimes it helps to set small goals to push yourself, even if it's just in your hobbies, to avoid stagnation and maintain motivation.")
elif profile_type == "Activity Adventurer":
    st.write("🎨 You are actively engaged in extracurriculars, which is fantastic for personal growth!")
    st.write("It’s awesome that you’re following your passions, but be mindful not to burn out. Try to set aside time for relaxation or schoolwork. Keep a balanced routine so you don’t sacrifice academic progress for fun. Avoiding cramming and downtime are important too!")
elif profile_type == "Academic Driver":
    st.write("📚 Your focus on academics is commendable, but ensure to take breaks for your mental health.")
    st.write("Consider practicing mindfulness techniques like deep breathing or meditation to reduce stress. Regular exercise can also help clear your mind and improve focus. Don’t forget to make time for activities that recharge you, whether it’s a hobby or spending time with friends.")
elif profile_type == "Well-Rounded Learner":
    st.write("🌟 You maintain a balanced approach, which is key to sustainable success!")
    st.write("Keep up the good work! Continue to explore new interests and maintain a healthy balance between academics and extracurriculars. Regularly check in with yourself to ensure you’re not overcommitting. Remember, it’s okay to take breaks and prioritize your well-being.")



st.markdown("### 🎭 What activities do you take part in? (Pick all that apply)")
st.write("This will help you compare your predicted pressure from your time commitments with the predicted pressure from your activities.")

with st.expander("Select your activities"):
    activity_options = {
        "Academic (Chess, Debating etc)": 3.0,
        "Artistic (Painting, Drawing etc)": 2.0,
        "Drama/Acting (Dance, Performance etc)": 1.5,
        "Music (Instrument, Choir etc)": 3.33,
        "Solo Sports (Tennis, Rowing etc)": 2.66,
        "Team Sports (Hurling, Soccer etc)": 2.37
    }

    selected_activities = []
    for activity in activity_options:
        if st.checkbox(activity):
            selected_activities.append(activity)

# Activity Pressure Comparison – runs independently of student match
# 📌 Activity Pressure Comparison Section
if selected_activities:
    # Calculate average pressure score for selected activities
    activity_scores = [activity_options[act] for act in selected_activities]
    estimated_activity_pressure = sum(activity_scores) / len(activity_scores)

    # Use fallback average pressure if no match was found
    baseline_pressure = avg_pressure if not similar_students.empty else 2.5
    pressure_difference = estimated_activity_pressure - baseline_pressure

    st.subheader("🔍 Activity Type vs Time-Based Pressure")
    st.write(f"🎛️ Estimated Pressure from Your Activities: **{estimated_activity_pressure:.2f} / 5**")

    # Compare and give feedback
    if pressure_difference > 0.5:
        st.error("⚠️ Your selected activities indicate **higher stress potential** than your time-based profile.")
        st.markdown("You might be juggling demanding activities like academic competitions or serious music commitments.")
    elif pressure_difference < -0.5:
        st.success("✅ Your activities seem **less intense** than peers with similar schedules.")
        st.markdown("You're likely engaging in more relaxing or enjoyable activities.")
    else:
        st.info("📘 Your activity choices align with your estimated pressure.")
        st.markdown("This suggests you're feeling roughly what most students with your time commitments feel.")


import matplotlib.pyplot as plt



   
    # Create a 'profile' column in the DataFrame based on the student data
df['profile'] = df.apply(lambda row: determine_profile(row['ec_hours'], row['hw_hours']), axis=1)

# Plot pie chart with adjustments
profile_counts = df['profile'].value_counts()

# Plot pie chart with adjustments
fig, ax = plt.subplots(figsize=(8, 8))  # Increase figure size
ax.pie(profile_counts, 
       labels=profile_counts.index, 
       autopct='%1.1f%%', 
       startangle=90, 
       colors=['skyblue', 'lightgreen', 'lightcoral', 'gold', 'lightskyblue'],
       pctdistance=0.70,  # Move percentage text further from the center
       labeldistance=1.1,  # Move labels further out
       wedgeprops={'edgecolor': 'black', 'linewidth': 1})  # Add border to wedges

# Title
ax.set_title("Distribution of Student Profiles")

# Display the chart
st.pyplot(fig)








