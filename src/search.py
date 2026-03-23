# search.py

# ---------------------------------
# 🧠 Basic Study Plan (Equal Division)
# ---------------------------------
def generate_study_plan(total_hours):
    subjects = ["Math", "AI", "Physics"]

    hours_per_subject = total_hours / len(subjects)

    plan = {}
    for subject in subjects:
        plan[subject] = round(hours_per_subject, 2)

    return plan


# ---------------------------------
# 🔍 Smart Study Plan (Priority-based)
# ---------------------------------
def smart_study_plan(total_hours, weak_subject):
    subjects = ["Math", "AI", "Physics"]

    base_hours = total_hours / len(subjects)

    plan = {}
    for subject in subjects:
        plan[subject] = base_hours

    # Give extra weight to weak subject
    if weak_subject in subjects:
        extra = total_hours * 0.2  # 20% extra focus
        plan[weak_subject] += extra

        # Reduce from others
        reduction = extra / (len(subjects) - 1)
        for subject in subjects:
            if subject != weak_subject:
                plan[subject] -= reduction

    # Round values
    for subject in plan:
        plan[subject] = round(plan[subject], 2)

    return plan


# ---------------------------------
# 🧪 Testing
# ---------------------------------
if __name__ == "__main__":
    print("Basic Study Plan (2 hours):")
    print(generate_study_plan(2))

    print("\nSmart Study Plan (2 hours, weak in AI):")
    print(smart_study_plan(2, "AI"))