import csv
import os

DIR = os.path.dirname(os.path.abspath(__file__))
CLASSES = os.path.join(DIR, "classes.txt")
DATA_CLASSES = []
DATA_PARAMS = [
    'title',
    'title.title',
    'title.subtitle',
    'subject',
    'subject.theme',
    'source',
    'source.location',
    'description',
    'description.type_programming',
    'description.requirements',
    'description.educational_objective',
    'description.keyword',
    'description.program_objective',
    'description.general',
    'description.building'
]

with open(CLASSES, "r") as f:
    DATA_CLASSES = [line.strip() for line in f.readlines()]


def data_keys_to_csv():
    result = ["id"]
    i = 0
    for i, key in enumerate(DATA_PARAMS):
        if i+1 < len(DATA_PARAMS) and DATA_PARAMS[i+1].startswith(key + "."):
            continue
        result.append(key)
        
    return result


def get_value_by_key(data, key):
    keys = key.split('.')
    value = data
    for k in keys:
        if isinstance(value, dict) and k in value:
            value = value[k]
        else:
            value = ''
            break
    return value


def save_data_to_csv(id_list, table, filename, keys):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(keys)
        for id in id_list:
            try:
                data = table.get(id)
                row = [id] + [get_value_by_key(data, key) for key in keys[1:]]
                writer.writerow(row)
            except KeyError:
                pass

def save_categories_data_to_csv(id_list, table, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["id", "category", "confidence"])
        for id in id_list:
            try:
                data = table.get(id)
                for c_key, value in data.items():
                    row = [id, c_key, value]
                    writer.writerow(row)
            except KeyError:
                pass


def read_csv_to_hash_table(filename, table):
    data_model = {
        'title': {'title': '', 'subtitle': ''},
        'subject': {'theme': ''},
        'source': {'location': ''},
        'description': {
            'type_programming': '', 'requirements': '', 'educational_objective': '',
            'keyword': '', 'program_objective': '',
            'general': '', 'building': ''
        }
    }

    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data = data_model.copy()
            id_value = row['id']
            data['title']['title'] = row['title.title']
            data['title']['subtitle'] = row['title.subtitle']
            data['subject']['theme'] = row['subject.theme']
            data['source']['location'] = row['source.location']
            data['description']['type_programming'] = row['description.type_programming']
            data['description']['requirements'] = row['description.requirements']
            data['description']['educational_objective'] = row['description.educational_objective']
            data['description']['keyword'] = row['description.keyword']
            data['description']['program_objective'] = row['description.program_objective']
            data['description']['general'] = row['description.general']
            data['description']['building'] = row['description.building']
            table.put(id_value, data)
    
    return table






class HashTable:
    def __init__(self, initial_size=10, load_factor=0.8):
        self.size = initial_size
        self.load_factor = load_factor
        self.threshold = int(self.size * self.load_factor)
        self.table = [[] for _ in range(self.size)]
        self.count = 0

    def _hash(self, key):
        return hash(key) % self.size

    def _resize(self):
        self.size *= 2
        self.threshold = int(self.size * self.load_factor)
        new_table = [[] for _ in range(self.size)]
        for bucket in self.table:
            for key, value in bucket:
                new_index = self._hash(key)
                new_table[new_index].append((key, value))
        self.table = new_table

    def put(self, key, value):
        index = self._hash(key)
        bucket = self.table[index]
        for i, (existing_key, existing_value) in enumerate(bucket):
            if existing_key == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
        self.count += 1
        if self.count > self.threshold:
            self._resize()

    def get(self, key):
        index = self._hash(key)
        bucket = self.table[index]
        for existing_key, existing_value in bucket:
            if existing_key == key:
                return existing_value
        raise KeyError("Key not found in hash table.")

    def remove(self, key):
        index = self._hash(key)
        bucket = self.table[index]
        for i, (existing_key, existing_value) in enumerate(bucket):
            if existing_key == key:
                del bucket[i]
                self.count -= 1
                return
        raise KeyError("Key not found in hash table.")