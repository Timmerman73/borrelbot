import random
import datetime

SPECIAL_LOCATION_CHANCE = 0.25
#How far in the future should the bot pick a date
DAYDELTA = 7



def get_host():
    with open("hosts.txt","r") as file:
        return random.choice(list(map(str.strip,file.readlines())))
    
def get_location():
    if random.random() < SPECIAL_LOCATION_CHANCE:
        with open("locations.txt","r") as file:
            return random.choice(file.readlines())
    else:
        return "Geen speciale locatie"
    

def get_date():
    today = datetime.date.today()
    random_date = today + datetime.timedelta(days=random.randint(0, DAYDELTA-1))
    return random_date
    



def main():
    host,location,date = get_host(),get_location(),get_date()
    print(f"Borrel bij {host} op {date}. Met als locatie {location}")

if __name__ == "__main__":
    main()