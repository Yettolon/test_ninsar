import random
from django.core.management.base import BaseCommand
from api.models import ResultEntry


class Command(BaseCommand):
    help = "Добавляет тестовые данные в базу с очисткой старых"

    def handle(self, *args, **kwargs):
        competitions = ["SpringCup", "AutumnCup", "WinterCup", "SummerCup"]
        scenarios = ["easy", "medium", "hard"]
        commands = ["Alpha", "Bravo", "Charlie", "Delta", "Echo"]
        users = [
            "Ivan",
            "Anna",
            "Peter",
            "John",
            "Olga",
            "Mike",
            "Sophia",
            "Dmitry",
            "Laura",
            "Tom",
            "admin",
        ]

        # Удаление старых записей
        self.stdout.write("Очищаем старые данные")
        ResultEntry.objects.all().delete()

        records = []
        for i in range(10000):
            competition = random.choice(competitions)
            scenario = random.choice(scenarios)
            command_name = random.choice(commands)
            false_start = random.choice([False, False, False, True])
            flight_time = round(random.uniform(20, 200), 2)

            # Создаем для Ивана
            if i < 50:
                user_name = "Ivan"
                command_name = "Alpha"
                competition = "SpringCup"
                scenario = "easy"
                false_start = False
                flight_time = round(random.uniform(30, 80), 2)
            else:
                user_name = random.choice(users)

            record = ResultEntry(
                competition=competition,
                room_id=f"room_{random.randint(1, 100)}",
                command_name=command_name,
                user_name=user_name,
                scenario=scenario,
                flight_time=flight_time,
                false_start=false_start,
            )
            records.append(record)

        self.stdout.write("Запись в базу")
        ResultEntry.objects.bulk_create(records, batch_size=1000)

        self.stdout.write(self.style.SUCCESS("Задачи успешно созданы"))
