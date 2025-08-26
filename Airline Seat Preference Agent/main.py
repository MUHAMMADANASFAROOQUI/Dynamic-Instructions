from agents import Agent, RunContextWrapper, Runner, function_tool, trace
from pydantic import BaseModel
from connection import config
import asyncio
import rich

from dotenv import load_dotenv
load_dotenv()


class Passsenger(BaseModel):
    name: str
    seat_prefrence: str
    travelling_experience: str

passsengerone = Passsenger(name="M.Anas",seat_prefrence="Any",travelling_experience="Premium")

def dynamic_instructions(ctx:RunContextWrapper[Passsenger],agent: Agent):
    if ctx.context.seat_prefrence == "Window" and ctx.context.travelling_experience == "First time":
        return "Explain window benefits, mention scenic views, reassure about flight experience."
    elif ctx.context.seat_prefrence == "Aisle" and ctx.context.travelling_experience == "Occasional":
        return "Highlight the convenience of an aisle seat for easy movement and quick access to the cabin. Reassure the traveler that it’s a comfortable choice for occasional flyers, especially if they like stretching their legs or prefer not to disturb others when moving around."
    elif ctx.context.seat_prefrence == "Middle" and ctx.context.travelling_experience == "Frequent":
        return "Acknowledge the compromise, suggest strategies, offer alternatives."
    elif ctx.context.seat_prefrence == "Any" and ctx.context.travelling_experience == "Premium":
        return"Highlight luxury options, upgrades, priority boarding."
    else:
        return "you are a helpful airline seat preference agent."

airline_booking = Agent(
    name= "Airline Booking",
    instructions= dynamic_instructions
)

async def main():
    with trace("Airline Booking Agent"):
        result = await Runner.run(
            airline_booking,
            "Can you suggest the best seat for me?",
            run_config= config,
            context= passsengerone
            )
        rich.print(result.final_output)



if __name__ == "__main__":
    asyncio.run(main())
