import store_address_generator
import store_id_generator
import store_name_generator
import store_type_generator

class DataGenerator:
    def __init__(self, storeName_file, si_file, gu_file):   # 객체 생성
        self.store_id_gen = store_id_generator.StoreIDGenerator()
        self.store_name_gen = store_name_generator.StoreNameGenerator()
        self.store_address_gen = store_address_generator.StoreAddressGenerator(si_file, gu_file)
        self.store_type_gen = store_type_generator.storeTypeGenerator(storeName_file)

    def generate_data(self, count):
        data = []
        for _ in range(count):
            id = self.store_id_gen.generate_id()
            type = self.store_type_gen.generate_type()
            address = self.store_address_gen.generate_address()
            gu = self.store_address_gen.gu
            name = self.store_name_gen.generate_name(type,gu)
            data.append((id, name, type, address))
        return data