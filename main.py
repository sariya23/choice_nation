class Profile:
    def __init__(self, name):  # конструктор
        self.name = name
        self.data = []
        self.file_name = str(self.name)
        self.f = open(self.file_name + '.txt', 'w+')
        self.f.writelines(self.name)
        self.f.close()

    def write_data(self, arr):  # записать данные
        self.data.extend(arr)

    def delete_data(self, deleted_item):  # удалить данные
        del self.data[self.data.index(deleted_item)]

    def print_info(self):  # просмотреть информацию
        print(self.name, self.data)


a = Profile('Nikita')
b = Profile('MAx')






