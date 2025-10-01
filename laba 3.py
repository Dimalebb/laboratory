Students = {}
while True:
    name = input("\nВведіть ім'я студента (або 'стоп' для завершення): ")
    if name.lower() == "стоп":
        break

    try:
        grade = int(input("Введіть його оцінку (1-12): "))
        if 1 <= grade <= 12:
            Students[name] = grade
            print(f"Студента {name} додано з оцінкою {grade}")
        else:
            print("Оцінка має бути в діапазоні 1–12.")
    except ValueError:
        print("Помилка! Введіть ціле число від 1 до 12.")

print("Список студентів та їх оцінок:")
for name, grade in Students.items():
    print(f"{name}:{grade}")

if Students:
    average = sum(Students.values()) / len(Students)
    print(f"\nСередній бал по групі: {average:.2f}")

    excellent = [n for n, g in Students.items() if 10 <= g <= 12]
    good = [n for n, g in Students.items() if 7 <= g <= 9]
    weak = [n for n, g in Students.items() if 4 <= g <= 6]
    failed = [n for n, g in Students.items() if 1 <= g <= 3]

    print(f"\nКількість відмінників (10-12): {len(excellent)} Імена: {', '.join(excellent) if excellent else '-'}")
    print(f"Кількість хорошистів (7-9): {len(good)} Імена: {', '.join(good) if good else '-'}")
    print(f"Кількість відстаючих (4-6): {len(weak)} Імена: {', '.join(weak) if weak else '-'}")
    print(f"Кількість тих, хто не здав (1-3): {len(failed)} Імена: {', '.join(failed) if failed else '-'}")
else:
    print("\nНемає введених студентів.")
