from agents import Agent, RunContextWrapper, Runner, function_tool, trace
from pydantic import BaseModel
from connection import config
import asyncio

from dotenv import load_dotenv
load_dotenv()


class User(BaseModel):
    name: str
    user_type: str

userone = User(name="M.Anas",user_type="Patient")

def dynamic_instructions(ctx:RunContextWrapper[User],agent : Agent):
    if ctx.context.user_type == "Patient":
        return "Use simple, non-technical language. Explain medical terms in everyday words. Be empathetic and reassuring."
    elif ctx.context.user_type == "Medical Student":
        return "Use moderate medical terminology with explanations. Include learning opportunities."
    elif ctx.context.user_type == "Doctor":
        return "Use full medical terminology, abbreviations, and clinical language. Be concise and professional."
    else:
        return "you are a helpful medical consultation agent."

medical_consul = Agent(
    name= "Medical_consul",
    instructions= f"you are helpful medical consultation agent {dynamic_instructions}"
)

async def main():
    with trace("Medical Consultant"):
        result = await Runner.run(
            medical_consul,
            "i am feeling drowsy and fatigue what measures should i take?",
            run_config= config,
            context= userone
            )
        print(result.final_output)



if __name__ == "__main__":
    asyncio.run(main())
