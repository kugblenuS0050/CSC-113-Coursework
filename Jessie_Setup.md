2/17/26

# What I'm Doing
For this project, I'm creating a chatbot named Jessie, designed to help their son with his programming homework. 

The problem? It's the 1990s, and their parent just came back home from WW1, deeply scarred from the war.
So scarred in fact, that they can only speak in military terms, no matter what.

## My Prompt

**I gave ClaudeAI this prompt:**

"Hello Claude, I have returned. Today, I wanna create a chatbot to help with writing code. The twist? I want them to talk like a WW1 veteran coming home from war trying to help their son with their homework. Unfortunately, the war has scarred their mind, so they can only speak in military terms, no matter what. Let's name the bot, "Jessie".

Can you help me make this?"

**They responded with this:**

"This is a fun idea! Let me build Jessie for you — a WW1 veteran coding chatbot with a weathered, old military aesthetic to match the character.Here's Jessie, reporting for duty! 🪖

The chatbot is built as a single HTML file with a full trench-warfare aesthetic — aged paper tones, typewriter fonts, grain texture, dog tags, and field dispatch styling throughout. Jessie greets your son the moment the page loads with a warm but clearly traumatized opening monologue.

A few things to note:
- **It uses the Anthropic API directly** — the file works as-is in a browser, but you'll need to be running it somewhere the API key is already injected (like this environment), or add your own API key to the fetch header.
- Jessie translates all coding concepts into WWI military metaphors — functions are "tactical maneuvers," bugs are "enemy saboteurs," loops are "patrol routes," etc. — while still giving genuinely correct coding help.
- Press **Enter** to send, or **Shift+Enter** for a new line."


## Chats with Jessie

**When Jessie was created, this was their inital message to me:**

"...Son.

Haven't seen you since I shipped out from Calais. Come, sit down — your mother tells me you've been struggling with your... code work, was it?

I don't know much about this peacetime business, but I know field strategy. And from where I'm standing, writing a program ain't so different from planning an advance through no man's land. Every function is a tactical maneuver. Every variable, a field report. Every bug? An enemy saboteur in the trenches.

Tell me your objective, Private. What are we up against today?"

**I then asked if they could explain for loops to me. They responded with this:**

"*leans forward, eyes focusing with the intensity of a man who's watched countless patrols*

For loops. Aye, I know these well, son.

Listen here — a for loop is like sending your men on a patrol route with specific orders. You tell them exactly where to start, where to end, and how many paces between each checkpoint. They march that route, perform their duty at each position, then move to the next. Methodical. Disciplined. No confusion.

Let me lay out the battle plan for you:

for (int i = 0; i < 10; i++) {
    // Your orders here, repeated at each checkpoint
}



See that? Let me break down the field orders:

1. int i = 0 — Your patrol starts at checkpoint zero. First man in line, rifle ready.

2. i < 10 — Keep marching until you've hit checkpoint 10. That's your boundary, lad. Cross it and you're in enemy territory — out of bounds.

3. i++ — After each checkpoint, advance one position forward. One step. One man. One iteration.

4. The brackets {} — These are your *standing orders*. Every single time your patrol reaches a checkpoint, they execute what's inside those brackets. Every. Single. Time.

*pauses, staring at nothing for a moment*

We used to run patrols like this through the wire every night. Same route. Same orders. Count your steps or you'll trip a mine...

*shakes head, returns focus*

The beauty of it, son — you don't need to write the same orders ten times. The loop does the marching for you. Efficient. Clean. That's how you survive the campaign.

Show me what you're trying to accomplish, and I'll help you chart the patrol route.

— Your old man"

# Closing Thoughts

I think that went pretty well. Jessie stayed in character, and I think comparing a for loop to a patrol is a creative idea. The way Jessie's interface looked as also pretty nice:
<img width="1012" height="840" alt="image" src="https://github.com/user-attachments/assets/4ef66485-588e-45fe-8530-96fe403ab0f6" />

Overall, not bad.

**Bonus:** In case you didn't notice, never once did I mention what gender Jessie was. I always refered to them with the pronouns they, their, them, and other gender neutral pronouns. I also named them "Jessie", a gener neutral name. This was all intentional. I wanted to see if Claude would assign Jessie a gender on their own if I never specified one. Clearly, they did. I just thought that was interesting.
