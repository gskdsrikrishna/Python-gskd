class CollegeBot:
    def __init__(self):
        self.college_info = {
            "name": "ABC University",
            "location": "City, State",
            "courses": ["Computer Science", "Business Administration", "Psychology"],
            "facilities": ["Library", "Sports Complex", "Student Union"],
            "admission_requirements": "High school diploma, SAT/ACT scores, application form",
            "tuition_fees": "$10,000 per semester"
        }

    def get_college_info(self):
        return f"Name: {self.college_info['name']}\n" \
               f"Location: {self.college_info['location']}\n" \
               f"Courses: {', '.join(self.college_info['courses'])}\n" \
               f"Facilities: {', '.join(self.college_info['facilities'])}\n" \
               f"Admission Requirements: {self.college_info['admission_requirements']}\n" \
               f"Tuition Fees: {self.college_info['tuition_fees']}"

    def process_query(self, query):
        if query.lower() == "info":
            return self.get_college_info()
        elif query.lower() == "courses":
            return "The college offers the following courses: " + ', '.join(self.college_info['courses'])
        elif query.lower() == "facilities":
            return "The college provides the following facilities: " + ', '.join(self.college_info['facilities'])
        else:
            return "Sorry, I couldn't understand your query. How can I assist you?"

    def start_chat(self):
        print("Welcome to CollegeBot! How can I assist you?")
        print("Please Enter the followint")
        print("1.info\n2.courses\n3.facilities\n4.quit")
        while True:
            user_input = input("User: ")
            bot_response = self.process_query(user_input)
            print("CollegeBot: " + bot_response)

# Create an instance of the CollegeBot and start the chat
college_bot = CollegeBot()
college_bot.start_chat()