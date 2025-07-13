import google.generativeai as genai
genai.configure(api_key="AIzaSyCrrGW2iK6_RPkBtm94VlQ9RGsbnwnWRrw")

def ask_gemini(prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    return response.text
# Feature 1: Career Q&A
def career_chat():
    print("\n Ask me anything about your career! (type 'exit' to stop)")
    while True:
        q = input("You: ")
        if q.lower() == 'exit':
            break
        reply = ask_gemini(q)
        print("\n Gemini says:", reply)

# Feature 2: Skill Roadmap
def learning_path():
    interest = input("\n What field are you interested in? (e.g., AI, Web Dev): ")
    roadmap_prompt = f"Suggest a learning roadmap for a college student who wants to build a career in {interest}. Include free resources."
    roadmap = ask_gemini(roadmap_prompt)
    print("\n🛣 Roadmap:\n", roadmap)

# Feature 3: Resume Feedback
def resume_review():
    print("\n📄 Paste your resume content below (text only). Type 'done' when finished:")
    lines = []
    while True:
        line = input()
        if line.lower() == 'done':
            break
        lines.append(line)
    resume_text = "\n".join(lines)
    review_prompt = f"Please review this resume and suggest improvements:\n\n{resume_text}"
    feedback = ask_gemini(review_prompt)
    print("\n✅ Feedback:\n", feedback)

# Main Menu
def main():
    while True:
        print("\n====CareerBridge Menu====")
        print("1. Career Chat with Gemini")
        print("2. Get Learning Roadmap")
        print("3. Resume Feedback")
        print("4. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            career_chat()
        elif choice == '2':
            learning_path()
        elif choice == '3':
            resume_review()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
