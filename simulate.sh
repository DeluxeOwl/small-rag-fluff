#!/bin/bash

# Define the API endpoint
API_ENDPOINT="http://localhost:8000"

# Define example paragraphs to send in POST requests
declare -a paragraphs=(
    "The Renaissance, a period of cultural, artistic, political, and economic rebirth following the Middle Ages, transformed Europe between the 14th and 17th centuries. It marked the transition from the medieval period to the modern age, as a revival of classical learning and wisdom after the long period of cultural stagnation and decline known as the Dark Ages."
    "Originating in Florence, Italy, in the late 13th century, the Renaissance played a pivotal role in reshaping thought, art, and life across Europe. Its influence spread across the continent, bringing a renewed focus on humanism, a philosophy that emphasized the value and agency of human beings, individually and collectively."
    "Art and science flourished as the Renaissance saw the emergence of figures like Leonardo da Vinci and Michelangelo, who not only contributed to the visual arts but also made significant advances in anatomy, astronomy, and physics. This period also witnessed the invention of the printing press by Johannes Gutenberg, which revolutionized the spread of knowledge."
    "Politically, the Renaissance contributed to the rise of nation-states in place of the feudal system and paved the way for the modern sovereign state. It also fostered an environment where the questioning of traditional authority figures and institutions became more commonplace, setting the stage for the Reformation and the Enlightenment."
    "However, the Renaissance was not without its challenges and contradictions. It was a time of great inequality and upheaval, as the newfound emphasis on individual achievement and wealth often exacerbated social divides, and the era was marked by numerous wars, including the Italian Wars. Additionally, while the Renaissance spread throughout Europe, it did so unevenly, with some regions experiencing more profound changes than others."
)

# Loop through the paragraphs and send them as POST requests
for i in "${!paragraphs[@]}"; do
  curl -X 'POST' \
    "${API_ENDPOINT}/paragraphs" \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -d "{\"text\":\"${paragraphs[$i]}\"}"
  echo "" # New line for readability
done

echo ""
echo "Query response:"

# Send a POST request to query the database
curl -X 'POST' \
  "${API_ENDPOINT}/query" \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d "{\"query\":\"where did the renaissance start?\"}"
echo "" # New line for readability