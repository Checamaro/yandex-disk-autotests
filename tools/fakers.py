from faker import Faker

faker = Faker()


def random_folder():
    return f"test_folder_{faker.random_int()}"
