import streamlit as st

# Function to generate a response based on user input
def generate_response(user_input):
    user_input = user_input.lower()  # Convert input to lowercase for easy matching

    # Compliment categories
    if "hair" in user_input:
        return "Your hair looks so healthy! It's full of life and absolutely perfect. 🌟"
    elif "smile" in user_input:
        return "Your smile is like heaven—it lights up every room you walk into. 😊"
    elif "teeth" in user_input:
        return "Your teeth are brighter than Chip Skylark's shiny teeth! 😁"
    elif "eyes" in user_input:
        return "Your eyes are deep like the ocean; I can tell I'd need a life vest in case I get lost in them. 👀✨"
    elif "body" in user_input:
        return "Are you sure you aren't a model? Because you sure have the effect of one! 💪❤️"
    elif "personality" in user_input:
        return "Your personality is bubbly and full of life. Always a pleasure to see you! ❤️"
    elif "compliment" in user_input:
        return "Ask me about your hair, smile, teeth, eyes, body, or personality for a special compliment!"
    elif "favorite animal" in user_input:
        return None  # We'll handle this separately for the corgi gif.

    # Mental health and uplifting responses
    if "sad" in user_input or "depressed" in user_input:
        return (
            "I'm really sorry you're feeling this way. Remember, it's okay to not be okay. "
            "Things will always get better. You are loved. 💖"
        )
    elif "stressed" in user_input or "anxious" in user_input or "overwhelmed" in user_input:
        return (
            "Take a deep breath. You are doing your best, and that's more than enough. "
            "Don't forget to take breaks and be kind to yourself—you deserve it. 🌈"
        )
    elif "mental health" in user_input:
        return (
            "Taking care of your mental health is so important, and I'm proud of you for recognizing that. "
            "Remember, you're not alone. It's okay to reach out for support. 🌻"
        )
    elif "cheer me up" in user_input or "motivate me" in user_input:
        return (
            "You’ve got this! Even when things feel tough, remember how capable and resilient you are. "
            "You’re amazing, and the world is lucky to have you! 🌟"
        )

    # Default response if no conditions are matched
    return (
        "🤖 Hmm, I’m not sure how to respond to that. But just so you know, you're amazing the way you are! ❤️"
    )

# Streamlit Interface
def main():
    st.title("Compliment Bot 🥰")
    st.write("Welcome to the Compliment Bot! Type something and I'll shower you with kindness. ❤️")
    
    # User input
    user_input = st.text_input("Ask me for a compliment or share how you're feeling:")

    if user_input:
        response = generate_response(user_input)

        # Handle response output
        if response:
            st.write(f"🤖 {response}")
        else:
            # Special case for favorite animal
            st.write("Here's my favorite animal:")
            st.image(
                "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExa3hrNjRvcDh3ZGNldHpzaWliZWlhdnVheWg4ZWtwcGZ3ZGtuMHRlaSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/bWS1Vh9mVkcZq/giphy.webp", 
                caption="Corgi shaking its butt 🐶"
            )

# Run the app
if __name__ == "__main__":
    main()
