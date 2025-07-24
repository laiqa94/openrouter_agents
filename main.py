
from agents import Agent, Runner,OpenAIChatCompletionsModel,AsyncOpenAI , RunConfig
import os
from dotenv import load_dotenv

load_dotenv()

openrouterkey = os.getenv("OPENROUTER_API_KEY")


client = AsyncOpenAI(

    api_key= "openrouter_api_key",
    base_url="https://openrouter.ai/api/v1" #Open router based url remain constant
)

model= OpenAIChatCompletionsModel(

    openai_client= client,
    model= "google/gemini-2.0-flash-001"
)

config = RunConfig(
    model=model,
    model_provider=client,
    trace_id=True
)


#Create Agent

agent = Agent(
    name= "Writer Agent",
    instructions="You are a writer agent.Generate some articles , poems and essay"
)


#Run the agent
response = Runner.run_sync(

    agent,
    input="Write essay on Agentic AI with OPENAI SDK",
    run_config=config
)

print(response.final_output)