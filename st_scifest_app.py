import streamlit as st
import pandas as pd
import streamlit as st

st.markdown(
    """
    <style>
    .block-container {
        background-image: url('https://static.vecteezy.com/system/resources/thumbnails/038/585/123/small_2x/ai-generated-minimalist-wave-white-background-free-photo.jpg');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        padding: 5rem 2rem;  /* Optional: Adjust padding for better visibility */
    }
    </style>
    """, unsafe_allow_html=True
)


# Load dataset
df = pd.read_csv("2and5.csv")

st.title("🎓 Pressure Profile Explorer")
st.write("Enter your weekly extracurricular and daily acadmiec hours **outside of school** to discover your pressure profile based on real student data.")

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
    if abs(hw - ec) <= 1.0:
        return "Well-Rounded Learner"
    elif ec >= 4 and hw >= 2.5:
        return "Stretched Achiever"    
    elif ec <= 1 and hw <= 1:
        return "Take-it-easy Explorer"
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
    st.metric("📊 Average Pressure Level (based on students' self reports)", f"{avg_pressure:.2f} / 5")

    profile_type = determine_profile(ec_input, hw_input)
    st.subheader(f"🧬 Your Pressure Profile: {profile_type}")

    for trait in show_traits(profile_type):
        st.markdown(f"- {trait}")

import matplotlib.pyplot as plt

# Plotting Histogram (Activity vs Pressure)

   
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




st.markdown("### 🎭 What activities do you take part in? (Pick all that apply)")
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




