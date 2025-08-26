**🤖 Dynamic AI Agents Playground**

Agents jo ham sey ziada smart — ab flight book karte, mareez ko samjhatay aur safar plan karte hain!
“They say practice makes perfect… but in our case, practice makes AGENTS! ☕😂

A small experimental playground demonstrating Dynamic Instructions for AI agents — making them context-aware, adaptive, and (almost) human-like. Use these templates to build agents that change tone, detail, and actions based on a few context fields.

**🔥 Highlights**

One agent, many personalities — controlled by small structured context fields.

Focus domains: Medical consultation, Airline seat recommendations, Travel planning.

Ready-to-use prompt templates, example scripts, and a recommended prompt pattern for easy integration with any LLM/orchestration system.

✨ Exercises included
1. Medical Consultation Assistant (Intermediate)

Agent switches language by user role:

Patient → Simple, empathetic, lay language.

Medical Student → Moderate medical terms + concise explanations.

Doctor → Clinical language, terse & precise.

Example:

Patient: “Don’t worry, high BP just means pressure is a little high.”

Doctor: “Hypertension is persistently elevated arterial blood pressure.”

2. Airline Seat Preference Agent (Intermediate → Advanced)

Personalized seat guidance using:

seat_preference ∈ {window, aisle, middle, any}

travel_experience ∈ {first_time, occasional, frequent, premium}

Behavior examples:

Window + First-time → scenic views + reassurance.

Aisle + Occasional → mobility & convenience.

Middle + Frequent → survival tips + upgrade strategies.

Any + Premium → focus on luxury, upgrades & priority services.

Sample prompt (occasional + aisle):

“Highlight the convenience of an aisle seat for easy movement and quick access to the cabin. Reassure the traveler that it’s a comfortable choice for occasional flyers, especially if they like stretching their legs or prefer not to disturb others when moving around.”

3. Travel Planning Assistant (Intermediate → Advanced)

Adaptive itineraries and suggestions by trip style and traveler type:

Adventure + Solo → adrenaline activities, safety tips, budget stays.

Cultural + Family → kid-friendly museums, interactive itineraries.

Business + Executive → efficiency-first plans, lounges, fast Wi-Fi.

🧠 Design Principles

Context-first: small structured fields (role, preference, experience) control behavior.

🛠 Quick Start

Clone the repo:

git clone https://github.com/<your-org>/dynamic-ai-agents-playground.git
cd dynamic-ai-agents-playground


Create & activate a virtual environment:

# Create venv (example)
python -m venv .venv

# macOS / Linux (bash/zsh)
source .venv/bin/activate

# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# Windows (cmd)
.venv\Scripts\activate.bat


If you used a different tool (e.g., uv) or named your env folder something else, replace .venv with your env folder name and use its activation command.

Install dependencies:

pip install -r requirements.txt

🚀 Usage Examples

Example scripts (see examples/):

python examples/run_airline_demo.py     # test airline seat agent
python examples/run_medical_demo.py     # test medical role-switching agent
python examples/run_travel_demo.py      # test travel planner


Each script accepts a JSON-like context and prints the generated prompt + a sample LLM-style output. Tweak templates in prompts/ to tune tone and verbosity.

🧩 Prompt Pattern (recommended)

Use a short modular pattern that your orchestration layer can populate:

SYSTEM: You are a helpful domain-specific agent. Keep replies under 120 words unless user requests more detail.

CONTEXT: seat_preference={seat_preference}, travel_experience={travel_experience}, user_role={role}, trip_style={trip_style}

INSTRUCTION:
1. Use tone based on travel_experience:
   - first_time: extra reassurance, step-by-step guidance.
   - occasional: practical, friendly tips.
   - frequent: concise, efficiency-focused.
   - premium: highlight exclusivity & upgrades.
2. Mention seat-specific benefits/drawbacks.
3. Offer one clear action (e.g., check-in early, request upgrade, prebook lounge).
4. End with a question/invitation to modify preferences.

Minimal templates: prompts are short, modular, and testable.

Human-centered: clarity and empathy prioritized; safety for high-risk domains.

Testable: examples + tests to ensure consistent tone & behavior.

