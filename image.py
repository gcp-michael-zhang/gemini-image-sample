from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO

client = genai.Client(vertexai=True,project="zhmichael-demo",location="global")

prompt = (
    "Create a picture of a nano banana dish in a fancy restaurant with a Gemini theme"
)
contents = [
    types.Content(
      role="user",
      parts=[
        types.Part.from_text(text="""Create a picture of a nano banana dish in a fancy restaurant with a Gemini theme""")
      ]
    )
  ]

generate_content_config = types.GenerateContentConfig(
    temperature = 1,
    top_p = 0.95,
    max_output_tokens = 32768,
    response_modalities = ["TEXT", "IMAGE"],
    safety_settings = [types.SafetySetting(
      category="HARM_CATEGORY_HATE_SPEECH",
      threshold="OFF"
    ),types.SafetySetting(
      category="HARM_CATEGORY_DANGEROUS_CONTENT",
      threshold="OFF"
    ),types.SafetySetting(
      category="HARM_CATEGORY_SEXUALLY_EXPLICIT",
      threshold="OFF"
    ),types.SafetySetting(
      category="HARM_CATEGORY_HARASSMENT",
      threshold="OFF"
    )],
  )


response = client.models.generate_content(
    model="gemini-2.5-flash-image-preview",
    contents=contents,
    config = generate_content_config,
)

for part in response.candidates[0].content.parts:
    if part.text is not None:
        print(part.text)
    elif part.inline_data is not None:
        image = Image.open(BytesIO(part.inline_data.data))
        image.save("generated_image.png")