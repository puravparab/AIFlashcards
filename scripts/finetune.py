import json

# Open the JSON file in read mode
with open('../examples/flashcard.txt', 'r') as file:
	# Parse the JSON data from the file
	data = json.load(file)
	for qa in data:
		json = {}
		json["messages"] = []

		json["messages"].append({
			"role": "system", 
			"content": "You are an assistant that creates flashcards"
		})
		json["messages"].append({
			"role": "user", 
			"content": qa["A"]
		})
		json["messages"].append({
			"role": "assistant", 
			"content": str(qa)
		})
		print(json)