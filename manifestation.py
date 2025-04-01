import datetime
import random

# Get current date and time
now = datetime.datetime.now()

# Ask user for intent and what they want to keep
intent = input("🪄 What is your manifestation intent? ")
keep = input("💖 What do you want to KEEP while shifting your reality? ")

# Sacred geometry options
geometry = ["Metatron’s Cube", "Flower of Life", "Merkaba", "Sri Yantra"]
chosen_geometry = random.choice(geometry)

# Affirmations
affirmations = [
    "I trust the reset, for it brings me divine alignment.",
    "I shift realities with love, power, and ease.",
    "Everything I desire is already aligning for me.",
    "I am anchored in truth and guided by Source.",
    "I allow positive change while keeping what I love."
]
chosen_affirmation = random.choice(affirmations)

# Elemental suggestions
elements = [
    "💧 Drink a glass of water charged with your intention.",
    "🔥 Light a candle and speak your desire into the flame.",
    "🌿 Hold a crystal or pine cone and infuse it with your intent.",
    "🌬️ Go outside and speak your desire into the wind."
]
element_action = random.choice(elements)

# Visualization suggestions
visualizations = [
    "🧘 Close your eyes and imagine stepping into a glowing new timeline.",
    "🌈 Picture your new reality like a movie—then step into the scene.",
    "🌌 Visualize sacred geometry forming around you as energy reshapes your world."
]
chosen_visual = random.choice(visualizations)

# Output
print("\n🌟 Manifestation Journal Entry 🌟")
print(f"Date: {now.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"\n🪄 Intent: {intent}")
print(f"💖 What I want to keep: {keep}")
print(f"🔮 Sacred Geometry Anchor: {chosen_geometry}")
print(f"\n✨ Affirmation: {chosen_affirmation}")
print(f"\n🌿 Elemental Action: {element_action}")
print(f"🧘 Visualization: {chosen_visual}")
print(f"\n📿 Reminder: Do your 3-6-9 method today — write your intent 3 times in the morning, 6 times in the afternoon, and 9 times at night.")

import random

# Add this list of frequencies and their meanings
frequencies = [
    ("174 Hz", "Reduce pain and stress; grounding"),
    ("285 Hz", "Heal tissues and organs; cellular rejuvenation"),
    ("396 Hz", "Let go of fear and guilt; root chakra activation"),
    ("417 Hz", "Facilitate change and remove negative energy"),
    ("528 Hz", "DNA repair and miracles; heart chakra alignment"),
    ("639 Hz", "Heal relationships and connect deeply"),
    ("741 Hz", "Detoxify and awaken intuition"),
    ("852 Hz", "Return to spiritual order and higher awareness"),
    ("963 Hz", "Pineal gland activation and connection to Source")
]

# Choose a random frequency
frequency, meaning = random.choice(frequencies)

# Print the suggestion
print("🎶 Frequency Suggestion: ", frequency)
print("   🌀 Use this frequency to support your manifestation: " + meaning)

# ✨ Add list of Universal Laws and focus prompts
universal_laws = [
    ("Law of Divine Oneness", "Everything is connected. Practice seeing unity in all things."),
    ("Law of Vibration", "Everything vibrates. Align your energy with your desires."),
    ("Law of Correspondence", "As above, so below. Shift your inner world to change the outer."),
    ("Law of Attraction", "Like attracts like. Focus on what you want, not what you fear."),
    ("Law of Inspired Action", "Take steps toward your desires, even small ones."),
    ("Law of Perpetual Transmutation", "Energy is always moving. You can shift any situation."),
    ("Law of Cause and Effect", "Your actions create ripples. Choose actions aligned with love."),
    ("Law of Compensation", "You are always rewarded in divine timing. Be open to receive."),
    ("Law of Relativity", "Everything is neutral until compared. Shift your perspective."),
    ("Law of Polarity", "Everything has an opposite. Use contrast to gain clarity."),
    ("Law of Rhythm", "Life has cycles. Flow with the ups and downs."),
    ("Law of Gender", "Balance the divine masculine and feminine within you.")
]

# Choose a random Universal Law
law, focus = random.choice(universal_laws)

print("\n🌀 Universal Law Focus: ", law)
print("🧭 Reflection: ", focus)
