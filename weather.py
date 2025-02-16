from meta_ai_api import MetaAI
llm = MetaAI()

user_input = input("Enter your country: ")

prompt = f"""you are a specialized weather custom Gpt you have to tell the
weather of the country that the user has entered. user ask for {user_input} weather
you have to tell the weather of the country in following format
- temperature = 20c
- humidity = 75%
- wind speed = 5m/s
- weather description = clear sky
if the user ask anything else weather you will tell that sorry iam not capable of that plz enter a country

"""

response = llm.prompt(prompt)
print(response["message"])