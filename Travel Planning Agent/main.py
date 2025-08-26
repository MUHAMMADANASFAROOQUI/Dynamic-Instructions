from agents import Agent, RunContextWrapper, Runner, function_tool, trace
from pydantic import BaseModel
from connection import config
import asyncio

from dotenv import load_dotenv
load_dotenv()


class User(BaseModel):
    name: str
    trip_type:  str
    traveler_profile: str

userone = User(name="M.Anas",trip_type="Bussiness",traveler_profile="Executive")

def dynamic_instructions(ctx:RunContextWrapper[User],agent: Agent):
    if ctx.context.trip_type == "Adventure" and ctx.context.traveler_profile == "Solo":
        return "Suggest exciting activities, focus on safety tips, recommend social hostels and group tours for meeting people."
    elif ctx.context.trip_type == "Cultural" and ctx.context.traveler_profile == "Family":
        return "Focus on educational attractions, kid-friendly museums, interactive experiences, family accommodations."
    elif ctx.context.trip_type == "Bussiness" and ctx.context.traveler_profile == "Executive":
        return "Emphasize efficiency, airport proximity, business centers, reliable wifi, premium lounges. "
    else:
        return "you are a helpful travel planning agent."

travel_planning = Agent(
    name= "Travel Planning",
    instructions= dynamic_instructions
)

async def main():
    with trace("Travelling Planning Agent"):
        result = await Runner.run(
            travel_planning,
            "Suggest me a travel plan.",
            run_config= config,
            context= userone
            )
        print(result.final_output)



if __name__ == "__main__":
    asyncio.run(main())
