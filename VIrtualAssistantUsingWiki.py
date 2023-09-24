import wikipedia
import wolframalpha

class VirtualAssistant:
    def __init__(self):
        self.wikipedia_api_key = '05701db866357f54699722dc81d0025f'
        self.wolframalpha_app_id = 'YOUR_WOLFRAM_ALPHA_APP_ID'
        
    def search_wikipedia(self, query):
        wikipedia.set_lang("en")  # Set the Wikipedia language (e.g., 'en' for English)
        try:
            page = wikipedia.page(query)
            summary = wikipedia.summary(query)
            return page.title, summary, page.url
        except wikipedia.exceptions.PageError:
            return None
        except wikipedia.exceptions.DisambiguationError as e:
            options = e.options[:5]  # Limit to first 5 options
            return f"Multiple results found. Which one are you looking for?\n{', '.join(options)}"

    def query_wolfram_alpha(self, query):
        client = wolframalpha.Client(self.wolframalpha_app_id)
        res = client.query(query)
        if res['@success'] == 'false':
            return "Sorry, I couldn't find any information."
        else:
            result = ""
            for pod in res.pods:
                if pod.title == "Result":
                    result = pod.text
                    break
            return result

    def get_information(self, query):
        wikipedia_result = self.search_wikipedia(query)
        if wikipedia_result is not None:
            title, summary, url = wikipedia_result
            print(f"Wikipedia:\nTitle: {title}\nSummary: {summary}\nURL: {url}")
        else:
            wolfram_alpha_result = self.query_wolfram_alpha(query)
            print("Wolfram Alpha:\n" + wolfram_alpha_result)

    def start_assistant(self):
        print("Welcome to the Virtual Assistant!")
        while True:
            user_input = input("User: ")
            if user_input.lower() == "exit":
                break
            self.get_information(user_input)

# Create an instance of the VirtualAssistant and start the conversation
assistant = VirtualAssistant()
assistant.start_assistant()