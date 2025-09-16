PROJECT_ID="<Your Project ID>"
LOCATION_ID="global"
API_ENDPOINT="aiplatform.googleapis.com"
MODEL_ID="gemini-2.5-flash-image-preview"
GENERATE_CONTENT_API="generateContent"

curl \
-X POST \
-H "Content-Type: application/json" \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
"https://${API_ENDPOINT}/v1/projects/${PROJECT_ID}/locations/${LOCATION_ID}/publishers/google/models/${MODEL_ID}:${GENERATE_CONTENT_API}" \
-d '{
    "contents": {
      "role": "USER",
      "parts": { "text": "Create a tutorial explaining how to make a peanut butter and jelly sandwich in three easy steps."},
    },
    "generation_config": {
      "response_modalities": ["TEXT", "IMAGE"],
     },
     "safetySettings": {
      "method": "PROBABILITY",
      "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
      "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
  }' \
  | grep -o '"data": "[^"]*"' \
  | cut -d'"' -f4 \
  | base64 --decode > gemini-native-image.png