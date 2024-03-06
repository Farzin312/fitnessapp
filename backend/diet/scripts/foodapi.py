import requests
import os
from ..models import UserFoodItem
from dotenv import load_dotenv

load_dotenv()

def add_all_food_items_from_api():
    api_url = 'https://api.nal.usda.gov/fdc/v1/foods/search'

    api_key = os.getenv('API_KEY')

    params = {
        'api_key': api_key,
        'pageSize': 200,    
        'pageNumber': 1
    }

    while True:
        response = requests.get(api_url, params=params)

        if response.status_code == 200:
            data = response.json()
            for food in data['foods']:
                if food.get('servingSizeUnit') == 'g':
                    nutrients = {nutrient['nutrientName']: nutrient.get('value', 0) for nutrient in food['foodNutrients']}
                    food_item, created = UserFoodItem.objects.get_or_create(
                        name=food['description'],
                        defaults={
                            'calories': nutrients.get('Energy', 0),
                            'fat': nutrients.get('Total lipid (fat)', 0),
                            'carbs': nutrients.get('Carbohydrate, by difference', 0),
                            'protein': nutrients.get('Protein', 0),
                            'serving_size': food.get('servingSize', 0)
                        }
                    )
                    if created:
                        print(f"Added: {food_item}")
                    else:
                        print(f"Updated: {food_item}")

            if data['currentPage'] < data['totalPages']:
                params['pageNumber'] += 1
            else:
                break
        else:
            print(f"Failed to fetch data: {response.status_code}")
            break


add_all_food_items_from_api()
