# main.py

from ml_model import predict_marks, predict_result
from clustering import get_clusters
from search import generate_study_plan, smart_study_plan
from chatbot import chatbot_response

# ---------------------------------
# 🎯 Main Menu
# ---------------------------------
def main():
    print("🎓 AI Student Assistant System\n")

    while True:
        print("\nChoose an option:")
        print("1. Predict Marks & Result")
        print("2. View Student Clusters")
        print("3. Generate Study Plan")
        print("4. Chatbot")
        print("5. Exit")

        choice = input("Enter choice: ")

        # -------------------------------
        # 1. Prediction
        # -------------------------------
        if choice == "1":
            att = float(input("Enter attendance: "))
            hours = float(input("Enter study hours: "))
            internal = float(input("Enter internal marks: "))

            marks = predict_marks(att, hours, internal)
            result = predict_result(att, hours, internal)

            print(f"\nPredicted Marks: {round(marks,2)}")
            print(f"Result: {result}")

        # -------------------------------
        # 2. Clustering
        # -------------------------------
        elif choice == "2":
            clusters = get_clusters()
            print("\nStudent Clusters:")
            print(clusters)

        # -------------------------------
        # 3. Study Plan
        # -------------------------------
        elif choice == "3":
            hours = int(input("Enter total study hours: "))
            weak = input("Enter weak subject (Math/AI/Physics): ")

            plan = smart_study_plan(hours, weak)
            print("\nStudy Plan:")
            print(plan)

        # -------------------------------
        # 4. Chatbot
        # -------------------------------
        elif choice == "4":
            print("\n🤖 Chatbot (type 'exit' to return)\n")

            while True:
                user_input = input("You: ")

                if user_input.lower() == "exit":
                    break

                response = chatbot_response(user_input)
                print("Bot:", response)

        # -------------------------------
        # Exit
        # -------------------------------
        elif choice == "5":
            print("Goodbye 👋")
            break

        else:
            print("Invalid choice. Try again.")


# Run program
if __name__ == "__main__":
    main()