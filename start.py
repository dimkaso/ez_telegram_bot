import asyncio

# Функция для асинхронного запуска main.py
async def run_main_py():
    process = await asyncio.create_subprocess_exec(
        "python", "main file path",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()  # Ожидаем завершения
    if stdout:
        print(f"Output from main.py: {stdout.decode()}")
    if stderr:
        print(f"Error from main.py: {stderr.decode()}")

# Функция для асинхронного запуска bot.py
async def run_bot_py():
    process = await asyncio.create_subprocess_exec(
        "python", "file path , bot.py",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()  # Ожидаем завершения
    if stdout:
        print(f"Output from bot.py: {stdout.decode()}")
    if stderr:
        print(f"Error from bot.py: {stderr.decode()}")

# Основная функция для запуска обоих файлов параллельно
async def main():
    await asyncio.gather(
        run_main_py(),
        run_bot_py()
    )

if __name__ == "__main__":
    # Запуск асинхронной функции
    asyncio.run(main())
