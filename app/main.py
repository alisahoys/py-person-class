class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    people_instances = []

    for person in people:
        person_to_add = Person(person["name"], person["age"])
        people_instances.append(person_to_add)

    for person in people:
        current_person = Person.people[person["name"]]

        if person.get("wife"):
            current_person.wife = Person.people[person["wife"]]
        if person.get("husband"):
            current_person.husband = Person.people[person["husband"]]

    return people_instances
