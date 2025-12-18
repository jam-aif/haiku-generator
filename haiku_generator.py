import os
from openai import OpenAI

def get_openai_client():
    """Initialize OpenAI client"""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY must be set in environment variables")

    return OpenAI(api_key=api_key)

def generate_haiku(theme: str, season: str, mood: str, keywords: str = "") -> str:
    """Generate a haiku using OpenAI API"""
    client = get_openai_client()

    # Build the prompt
    keywords_text = f" incorporating these keywords: {keywords}" if keywords else ""

    prompt = f"""Create a traditional haiku (5-7-5 syllable pattern) with the following specifications:
- Theme: {theme}
- Season: {season}
- Mood: {mood}
{keywords_text}

The haiku should follow the traditional 5-7-5 syllable structure and capture the essence of the specified theme, season, and mood. Return only the haiku text, with each line separated by a newline character.

Example format:
Cherry blossoms fall
Gentle breeze carries petals
Spring's fleeting beauty"""

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a master haiku poet. Create beautiful, traditional haikus that follow the 5-7-5 syllable pattern exactly."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=100,
            temperature=0.8
        )

        haiku = response.choices[0].message.content.strip()
        return haiku

    except Exception as e:
        print(f"Error generating haiku: {e}")
        raise Exception(f"Failed to generate haiku: {str(e)}")