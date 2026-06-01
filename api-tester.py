import base64
import os
from anthropic import Anthropic
from dotenv import load_dotenv

#loading api key from .env file
load_dotenv()
client = Anthropic(
    api_key=os.getenv("CLAUDE_API_KEY")
)

#read and encode image to base64
with open("F:/projects/simple-sell-me/images/image2.png", "rb") as image_file:
    base64_image = base64.b64encode(image_file.read()).decode("utf-8")

#sending image and getting a structured json return


#calling model with message and getting response
response =  client.messages.create(
    model = "claude-sonnet-4-5",
    max_tokens= 2048,
    messages=[
    {
        "role":"user", 
        "content": [
            #sending text to model before image processing improves token usage and helps model understand the task better
            {
            "type":"text",
            "text": "you are a sales person selling used goods your task is to to look at product images and identify the exact title of the product including version type, maybe serial number if you can, price of the product used dont give me a range try to find the best price to sell based on the usage you can see in the image, description and category of the product. Please return the information in a structured json format with the following keys: title, price, description, category. Make sure to only return the information in the specified format and do not include any additional text or explanations."
            },
            
            {
            "type":"image",
            "source" : {
                "type": "base64", 
                "media_type": "image/png",
                "data": base64_image
            },
        }
        ]}
    ],

    tools=[
        {
            "type": "web_search_20260209",
            "name": "web_search",
            "max_uses" : 3
        }
    ],
)

print(response.content[0].text)



