class Equipment:
    def __init__(self, equipment_id, name, quantity):
        self.equipment_id = equipment_id
        self.name = name
        self.quantity = quantity

    def update_quantity(self, quantity):
        self.quantity = quantity


class Experiment:
    def __init__(self, experiment_id, name, description):
        self.experiment_id = experiment_id
        self.name = name
        self.description = description
        self.documentation = []

    def add_documentation(self, document):
        self.documentation.append(document)


class Laboratory:
    def __init__(self, lab_id, name):
        self.lab_id = lab_id
        self.name = name
        self.equipment = []
        self.experiments = []

    def add_equipment(self, equipment):
        self.equipment.append(equipment)

    def add_experiment(self, experiment):
        self.experiments.append(experiment)


class LaboratoryManagementSystem:
    def __init__(self):
        self.laboratories = []

    def create_laboratory(self, lab_id, name):
        lab = Laboratory(lab_id, name)
        self.laboratories.append(lab)
        return lab

    def find_laboratory(self, lab_id):
        for lab in self.laboratories:
            if lab.lab_id == lab_id:
                return lab
        return None


# Creating the Laboratory Management System instance
lms = LaboratoryManagementSystem()

# Creating laboratories
lab1 = lms.create_laboratory(1, "Chemistry Laboratory")
lab2 = lms.create_laboratory(2, "Physics Laboratory")

# Creating equipment
equipment1 = Equipment(1, "Microscope", 5)
equipment2 = Equipment(2, "Bunsen Burner", 3)
equipment3 = Equipment(3, "Spectrophotometer", 2)

# Adding equipment to laboratories
lab1.add_equipment(equipment1)
lab1.add_equipment(equipment2)
lab2.add_equipment(equipment3)

# Updating equipment quantity
equipment1.update_quantity(4)

# Creating experiments
experiment1 = Experiment(1, "Chemical Reactions", "Study of chemical reactions")
experiment2 = Experiment(2, "Electric Circuits", "Study of electric circuits")

# Adding experiments to laboratories
lab1.add_experiment(experiment1)
lab2.add_experiment(experiment2)

# Adding documentation to experiments
experiment1.add_documentation("Procedure document")
experiment1.add_documentation("Results document")

# Accessing laboratory information and equipment
for lab in [lab1, lab2]:
    print("Laboratory ID:", lab.lab_id)
    print("Laboratory Name:", lab.name)
    print("Equipment:")
    for equipment in lab.equipment:
        print("Equipment ID:", equipment.equipment_id)
        print("Equipment Name:", equipment.name)
        print("Quantity:", equipment.quantity)
        print()

# Accessing experiment information and documentation
for experiment in [experiment1, experiment2]:
    print("Experiment ID:", experiment.experiment_id)
    print("Experiment Name:", experiment.name)
    print("Experiment Description:", experiment.description)
    print("Documentation:", experiment.documentation)
    print()

# Searching for a laboratory
searched_lab_id = 2
searched_lab = lms.find_laboratory(searched_lab_id)

if searched_lab:
    print("Laboratory found:")
    print("Laboratory ID:", searched_lab.lab_id)
    print("Laboratory Name:", searched_lab.name)
else:
    print("Laboratory not found.")