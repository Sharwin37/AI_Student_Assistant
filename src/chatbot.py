# chatbot.py

from ml_model import predict_marks, predict_result

# ---------------------------------
# 💬 Chatbot Function
# ---------------------------------
def chatbot_response(query):
    query = query.lower()

    # Basic responses
    if "hello" in query or "hi" in query:
        return "Hello! I am your AI Student Assistant 😊"

    elif "improve" in query:
        return "Increase study hours, revise regularly, and focus on weak subjects."

    elif "attendance" in query:
        return "Maintain at least 75% attendance to be eligible for exams."

    elif "study plan" in query:
        return "Divide your time equally and give extra time to weak subjects."

    # ML-based prediction (🔥 important)
    elif "predict" in query:
        try:
            att = float(input("Enter attendance: "))
            hours = float(input("Enter study hours: "))
            internal = float(input("Enter internal marks: "))

            marks = predict_marks(att, hours, internal)
            result = predict_result(att, hours, internal)

            return f"Predicted Marks: {marks:.2f}, Result: {result}"
        except:
            return "Invalid input. Please try again."

    else:
        return "I can help with study tips, predictions, and planning!"
    

# ---------------------------------
# 🧪 Run Chatbot
# ---------------------------------
if __name__ == "__main__":
    print("🤖 AI Student Assistant Chatbot (type 'exit' to stop)\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Chatbot: Goodbye! 👋")
            break

        response = chatbot_response(user_input)
        print("Chatbot:", response)