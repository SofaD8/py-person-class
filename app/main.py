class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person_dict in people:
        person = Person(person_dict["name"], person_dict["age"])
        person_list.append(person)

    for i, person_dict in enumerate(people):
        if "wife" in person_dict and person_dict["wife"] is not None:
            person_list[i].wife = Person.people[person_dict["wife"]]
        elif "husband" in person_dict and person_dict["husband"] is not None:
            person_list[i].husband = Person.people[person_dict["husband"]]

    return person_list
