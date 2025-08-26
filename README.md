🤖 Dynamic AI Agents Playground

Agents jo ham sey ziada smart — ab flight book karte, mareez ko samjhatay aur safar plan karte hain!
“They say practice makes perfect… but in our case, practice makes AGENTS! ☕😂

A small experimental playground demonstrating Dynamic Instructions for AI agents — making them context-aware, adaptive, and (almost) human-like. Use these templates to build agents that change tone, detail, and actions based on a few context fields.

🔥 Highlights

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

Minimal templates: prompts are short, modular, and testable.

Human-centered: clarity and empathy prioritized; safety for high-risk domains.

Testable: examples + tests to ensure consistent tone & behavior.
