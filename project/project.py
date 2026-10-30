from rich.console import Console
from rich.table import Table
import questionary
import json
import sys
from datetime import datetime
import random


v_d = ["saturday", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday"]
console = Console()



def main():
    swimmers = load_swimmers()
    while True:
        choice = questionary.select(
            "Choice",
            choices=["Add swimmer", "Show swimmers", "Mark paid", "Show unpaid", "Exit"],
        ).ask()

        if choice == "Add swimmer":
            while True:
                name = input("Name: ")
                if not name:
                        print("Name cannot be empty")
                        continue
                break

            while True:
                try:
                    age = int(input("Age: "))
                    if age > 60 or age < 3 :
                        print("age out of Valid range\nThe age range is from 3 to 60 years old.")
                        continue  
                except (ValueError, TypeError):
                    print("age must be numbers!")
                    continue
                break

               
            day = questionary.select("Day:", choices=v_d).ask()


            while True:
                time = input("Traning Time: ")
                try:
                    datetime.strptime(time, "%H:%M")
                except ValueError:
                    print("Time must be HH:MM")
                    continue
                break


            try:
                add_swimmer(swimmers, name, age, day, time)
                save_swimmers(swimmers)
            except ValueError as e:
                console.print(f"[red]{e}[/red]")
            after_finish()

        elif choice == "Show swimmers":
            table_swimmers(swimmers)
            after_finish()

        elif choice == "Mark paid":
            table_swimmers(swimmers)
            raw_id = questionary.text("Swimmer ID:").ask()
            try:
                mark_paid(swimmers, int(raw_id))
                save_swimmers(swimmers)
            except (ValueError, TypeError):
                console.print("[red]Invalid ID or swimmer not found[/red]")
            after_finish()

        elif choice == "Show unpaid":
            table_swimmers(unpaid_swimmers(swimmers))
            after_finish()

        elif choice == "Exit" or choice is None:
            print("Thanks for using our system :)")
            break



def load_swimmers(filename="swimmers.json"):
    
    try:
        with open(filename, "r") as f:
            s_data = json.load(f)
            return s_data
    except FileNotFoundError :
        return []
    except json.JSONDecodeError:
        return []



def save_swimmers(swimmers, filename="swimmers.json"):
    try:
        with open(filename, "w") as f:
            json.dump(swimmers, f, indent=4)
    except OSError:
     print("Could not save swimmers. Is the file open in another program?")



def add_swimmer(swimmers, name, age, training_day, training_time):
    
    
    existing_ids = {s["id"] for s in swimmers}
    
    while True:
        new_id = random.randint(1000, 9999)
        if not new_id in existing_ids:
            break
    n_swimmer = {
        "name":name,
        "age":age,
        "training_day": training_day,
        "training_time":training_time,
        "id":new_id,
        "paid": False
    }
    swimmers.append(n_swimmer)
    return n_swimmer
    
    
def table_swimmers(swimmers):
    if not swimmers:
       return console.print("there is no swimmers")
    table = Table(title= "swimmers")
    table.add_column("ID", style="cyan")
    table.add_column("Name")
    table.add_column("Age", justify="right")
    table.add_column("Day")
    table.add_column("Time")
    table.add_column("Paid")


    for swimmer in swimmers:
        table.add_row(
            str(swimmer["id"]),
            swimmer["name"],
            str(swimmer["age"]),
            swimmer["training_day"],
            swimmer["training_time"],
            "[green]Paid[/green]" if swimmer["paid"] else "[red]Not paid[/red]",
            )
    console.print(table)



def mark_paid(swimmers, swimmer_id):
    for swimmer in swimmers:
        if swimmer["id"] == swimmer_id:
            swimmer["paid"] = True
            return swimmer
    raise ValueError("Swimmer not found")


def unpaid_swimmers(swimmers):
    unpaid_list = []
    for swimmer in swimmers:
        if swimmer["paid"] == False:
            unpaid_list.append(swimmer)

    return unpaid_list

def after_finish():
    choice = questionary.select("Do you want to do something else?  ", choices = ["Yes", "No"], ).ask()
    if choice == "No":
        sys.exit("Thanks for useing our system :) ")
        

if __name__ == "__main__":
    main()