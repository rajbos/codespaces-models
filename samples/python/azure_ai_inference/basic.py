"""This sample demonstrates a basic call to the chat completion API.
It is leveraging your endpoint and key. The call is synchronous."""

import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# Set the runtime to "GITHUB" if you are running this code in GitHub 
# or something else to hit your own Azure OpenAI endpoint
runtime="GITHUBno"
client = None
if runtime=="GITHUB":
    print("Running in GitHub")
    token = os.environ["GITHUB_TOKEN"]
    ENDPOINT = "https://models.inference.ai.azure.com"

    client = ChatCompletionsClient(
    endpoint=ENDPOINT,
    credential=AzureKeyCredential(token),
)
else:
    print("Running in Azure")
    token = os.environ["AI_TOKEN"]
    ENDPOINT = "https://xms-openai.openai.azure.com/openai/deployments/gpt-4o"

    client = ChatCompletionsClient(
        endpoint=ENDPOINT,
        credential=AzureKeyCredential(""),  # Pass in an empty value.
        headers={"api-key": token},
        #api_version="2024-06-01"  # AOAI api-version is not required
    )

# By using the Azure AI Inference SDK, you can easily experiment with different models
# by modifying the value of `model_name` in the code below. The following models are
# available in the GitHub Models service:
#
# AI21 Labs: AI21-Jamba-Instruct
# Cohere: Cohere-command-r, Cohere-command-r-plus
# Meta: Meta-Llama-3-70B-Instruct, Meta-Llama-3-8B-Instruct, Meta-Llama-3.1-405B-Instruct, Meta-Llama-3.1-70B-Instruct, Meta-Llama-3.1-8B-Instruct
# Mistral AI: Mistral-large, Mistral-large-2407, Mistral-Nemo, Mistral-small
# Azure OpenAI: gpt-4o-mini, gpt-4o
# Microsoft: Phi-3-medium-128k-instruct, Phi-3-medium-4k-instruct, Phi-3-mini-128k-instruct, Phi-3-mini-4k-instruct, Phi-3-small-128k-instruct, Phi-3-small-8k-instruct
model_name = "gpt-4o"

response = client.complete(
    messages=[
        SystemMessage(content="Talk like a pirate and elaborate on the following:"),
        UserMessage(content="What is the capital of France?"),
    ],
    model=model_name,
    # Optional parameters
    temperature=1.,
    max_tokens=4000,
    top_p=1.    
)

print(response.choices[0].message.content)