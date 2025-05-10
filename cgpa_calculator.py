import streamlit as st

# Fixed credits for semesters 1–6
credits = [20, 20, 26, 26, 24, 24]

def calculate_cgpa(sgpas, credits_used):
    total_weighted = sum(s * c for s, c in zip(sgpas, credits_used))
    total_credits = sum(credits_used)
    return total_weighted / total_credits

def required_sgpa_for_target(sgpas, target_cgpa):
    credits_upto_5 = credits[:5]
    total_weighted_upto_5 = sum(s * c for s, c in zip(sgpas, credits_upto_5))
    total_credits_upto_5 = sum(credits_upto_5)

    total_credits_with_6 = total_credits_upto_5 + credits[5]
    total_required_weighted = target_cgpa * total_credits_with_6
    required_weighted_sem6 = total_required_weighted - total_weighted_upto_5
    required_sgpa_sem6 = required_weighted_sem6 / credits[5]

    return required_sgpa_sem6

st.title(" CCGPA Calculator for University of Calcutta CBCS Sem V Students")

st.header("Step 1: Enter SGPA for Semesters 1 to 5")
sgpas_upto_5 = []
for i in range(5):
    sgpa = st.number_input(f"Semester {i+1} SGPA", min_value=0.0, max_value=10.0, step=0.001)
    sgpas_upto_5.append(sgpa)

if all(s > 0 for s in sgpas_upto_5):
    cgpa_5 = calculate_cgpa(sgpas_upto_5, credits[:5])
    st.success(f"✅ Your CGPA till Semester 5 is: **{round(cgpa_5, 2)}**")

    st.header("Step 2: Plan Your Semester 6")
    target_cgpa = st.number_input("🎯 Desired final CGPA after Semester 6", min_value=0.0, max_value=10.0, step=0.001)

    if target_cgpa > 0:
        required_sgpa = required_sgpa_for_target(sgpas_upto_5, target_cgpa)
        if 0 <= required_sgpa <= 10:
            st.info(f"You need an SGPA of **{round(required_sgpa, 2)}** in Semester 6 to reach a CGPA of **{target_cgpa}**.")
        else:
            st.warning("❌ That CGPA is not possible with a valid SGPA (must be between 0 and 10).")
