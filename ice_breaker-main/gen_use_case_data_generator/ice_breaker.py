import os 
from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

if __name__ == '__main__':
    print("Hello Langchain")
    print(os.environ['OPENAI_API_KEY'])

information = """Pichai Sundararajan (born June 10, 1972[3][4][5]), better known as Sundar Pichai (/ˈsʊndɑːr pɪˈtʃaɪ/), is an Indian-American business executive. He is the chief executive officer (CEO) of Alphabet Inc. and its subsidiary Google.[6]

Pichai began his career as a materials engineer. Following a short stint at the management consulting firm McKinsey & Co., Pichai joined Google in 2004,[7] where he led the product management and innovation efforts for a suite of Google's client software products, including Google Chrome and ChromeOS, as well as being largely responsible for Google Drive. In addition, he went on to oversee the development of other applications such as Gmail and Google Maps. In 2010, Pichai also announced the open-sourcing of the new video codec VP8 by Google and introduced the new video format, WebM. The Chromebook was released in 2012. In 2013, Pichai added Android to the list of Google products that he oversaw.

Pichai was selected to become the next CEO of Google on August 10, 2015, after previously being appointed Product Chief by CEO Larry Page. On October 24, 2015, he stepped into the new position at the completion of the formation of Alphabet Inc., the new holding company for the Google company family. He was appointed to the Alphabet Board of Directors in 2017.[8]

Pichai was included in Time's annual list of the 100 most influential people in 2016[9] and 2020.[10]
"""
summary_template = """
given the information {information} about a person from i want you to create:
1. a short summary
2. two interesting facts about them
"""

summary_prompt_template = PromptTemplate(input_variables="information", template=summary_template)

llm = ChatOpenAI(temperature=0,model_name = "gpt-3.5-turbo")

chain = LLMChain(ll=llm, prompt = summary_prompt_template)

print (chain.run(information= information))

