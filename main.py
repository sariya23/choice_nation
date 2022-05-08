class Profile:
    def __init__(self, name):  # конструктор
        self.name = name
        self.data = []
        self.data_string = ''
        self.file_name = str(self.name)
        self.f = open(self.file_name + '.txt', 'w+', encoding='utf-8')
        self.f.writelines(self.name + '\n')

    def write_data(self, arr):  # записать данные
        self.data.extend(arr)
        self.data_string = ''
        
        for i in self.data:
            self.data_string += str(i)
        self.f.writelines(self.data_string + '\n')
        
    def delete_data(self, deleted_item):  # удалить данные
        del self.data[self.data.index(deleted_item)]

    def print_info(self):  # просмотреть информацию
        print(self.name, self.data)







