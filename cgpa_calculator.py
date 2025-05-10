# CGPA Calculator in Terminal

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

# --- Input Section ---
print("🎓 CGPA Calculator")
print("Enter your SGPA for Semesters 1 to 5:")

sgpas_upto_5 = []
for i in range(5):
    while True:
        try:
            sgpa = float(input(f"Semester {i+1} SGPA: "))
            if 0 <= sgpa <= 10:
                sgpas_upto_5.append(sgpa)
                break
            else:
                print("Please enter a valid SGPA between 0 and 10.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Calculate CGPA up to semester 5
cgpa_5 = calculate_cgpa(sgpas_upto_5, credits[:5])
print(f"\n✅ Your CGPA till Semester 5 is: {round(cgpa_5, 2)}")

# Predict required SGPA in sem 6
while True:
    try:
        desired_cgpa = float(input("\n🎯 Enter your desired final CGPA after Semester 6: "))
        break
    except ValueError:
        print("Please enter a number.")

required_sgpa = required_sgpa_for_target(sgpas_upto_5, desired_cgpa)

if 0 <= required_sgpa <= 10:
    print(f"📈 You need an SGPA of {round(required_sgpa, 2)} in Semester 6 to reach a CGPA of {desired_cgpa}")
else:
    print("⚠️ That CGPA isn't possible with a valid SGPA (must be between 0 and 10)")

