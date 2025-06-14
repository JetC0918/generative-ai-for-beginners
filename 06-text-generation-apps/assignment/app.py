import os 
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

model = "gpt-4.1-nano"
prompt = "Complete the following: Once upon a time there was a"
messages = [{"role": "user", "content": prompt}]


client = OpenAI()

# completion = client.chat.completions.create(model = model, messages = messages)

# # print response
# print(completion.choices[0].message.content)

def create_recipt(model):
    no_recipes = input("No of recipes (for example, 5): ")

    ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")
    filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

    prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
    messages = [{"role": "user", "content": prompt}]

    response = client.chat.completions.create(model = model, messages = messages)

    recipe = response.choices[0].message.content
    
    print(recipe)
    return recipe
     

def create_shopping_list(model,recipe):
    old_prompt_result = recipe
    prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

    new_prompt = f" {prompt} {old_prompt_result}"
    messages =[{'role':'user', 'content': new_prompt}]
    responses =  client.chat.completions.create(model = model, messages = messages, max_tokens=1200)


    # print response
    print("Shopping list:")
    print(responses.choices[0].message.content)
    
def study_buddy(model):
    sys_prompt = "You are a python expert with years of Python programming experience"
    
    prompt = "Suggestt how to be a pro like you for a beginner"


    messages =[{'role':'system', 'content': sys_prompt}, {'role':'user', 'content':prompt}]
    responses =  client.chat.completions.create(model = model, messages = messages, max_tokens=1200)


    # print response 
    print(responses.choices[0].message.content)
    
def history_bot(model):
    sys_prompt = "You are a actor who can play a certain historical character and able to answer all the question about the charaacter life and times"
    prompt = "Robin Hood, tell me about yourself in 3 sentence, use reply in style of the character"


    messages =[{'role':'system', 'content': sys_prompt}, {'role':'user', 'content':prompt}]
    responses =  client.chat.completions.create(model = model, messages = messages, max_tokens=1200)


    # print response 
    print(responses.choices[0].message.content)
    

def app():
    model = "gpt-4.1-nano"
    
    print("Choose an option:")
    print("1. Create Recipe")
    print("2. Create Shopping List (requires a recipe)")
    print("3. Python Study Buddy")
    print("4. History Bot")
    
    choice = input("Enter option number (1-4): ").strip() 
    
    if choice == "1":
        recipe = create_recipt(model)
        create_list = input("Do you want to create a shopping list based on your recipes (yes/no): ").lower()
        if create_list == 'yes':
            create_shopping_list 

    elif choice == "2":
        print("You need to run 'Create Recipe' first to get the recipe content.")
    elif choice == "3":
        study_buddy(model)
    elif choice == "4":
        history_bot(model)
    else:
        print("Invalid choice. Please enter 1-4.")

if __name__ == "__main__":
    app()