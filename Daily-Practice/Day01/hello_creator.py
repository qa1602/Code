from datetime import datetime
import random
import os
from colorama import Fore, Style, init

init(autoreset=True)

class HelloCreator:
    def __init__(self):
        self.quotes = {
            "coding": [
                "Talk is cheap. Show me the code. – Linus Torvalds",
                "Code today, create tomorrow.",
                "First, solve the problem. Then, write the code."
            ],
            "life": [
                "Không ai giỏi ngay từ đầu, quan trọng là kiên trì.",
                "Learning never exhausts the mind.",
                "Hãy sống như thể bạn sẽ chết ngày mai. Hãy học như thể bạn sẽ sống mãi mãi."
            ],
            "motivation": [
                "GitHub streak xanh lá đẹp hơn cả cỏ 🌱.",
                "Debugging là một nghệ thuật 🎨.",
                "Dream big, start small, act now."
            ]
        }
        self.log_file = "hello_log.txt"
    
    def greeting(self):
        hour = datetime.now().hour
        if 5 <= hour < 12:
            return "Chúc bạn một buổi sáng nhiều năng lượng! ☀️"
        elif 12 <= hour < 18:
            return "Chúc bạn một buổi chiều làm việc hiệu quả! 💻"
        elif 18 <= hour < 22:
            return "Chúc bạn một buổi tối thư giãn! 🌙"
        else:
            return "Chúc bạn một đêm ngon giấc! 🌌"
        
    def random_quote(self, category=None):
        if category and category in self.quotes:
            return random.choice(self.quotes[category])
        else:
            all_quotes = sum(self.quotes.values(), [])
            return random.choice(all_quotes)
        
    def log_message(self, message):
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(f"{datetime.now()}: {message}\n")

    def banner(self):
        print(Fore.CYAN + "=" * 45)
        print(Fore.GREEN + "   🚀 WELCOME TO DAILY PRACTICE 🚀")
        print(Fore.CYAN + "=" * 45 + Style.RESET_ALL)

    def show_today(self):
        today = datetime.now().strftime("%A, %d-%m-%Y %H:%M:%S")
        message = f"Hôm nay là: {today}\n{self.greeting()}"
        print(Fore.YELLOW + message + Style.RESET_ALL)
        self.log_message(message)

    def show_quote(self):
        print(Fore.MAGENTA + "Chọn chủ đề quote: coding / life / motivation / all")
        choice = input("👉 Nhập lựa chọn: ").strip().lower()
        q = self.random_quote(choice if choice != "all" else None)
        print(Fore.MAGENTA + f"\n💡 Quote of the day: \"{q}\"" + Style.RESET_ALL)
        self.log_message(f"Quote shown: {q}")

    def run(self):
        while True:
            self.banner()
            print("1. Xem ngày & lời chào")
            print("2. Xem quote random")
            print("3. Thoát")
            choice = input("\n👉 Nhập lựa chọn: ")

            if choice == "1":
                self.show_today()
            elif choice == "2":
                self.show_quote()
            elif choice == "3":
                print(Fore.CYAN + "Tạm biệt! Hẹn gặp lại ngày mai 👋")
                break
            else:
                print(Fore.RED + "❌ Lựa chọn không hợp lệ!")

            input(Fore.BLUE + "\nNhấn Enter để tiếp tục...")  # Dừng trước khi lặp lại
            os.system("cls" if os.name == "nt" else "clear")  # Xóa màn hình


if __name__ == "__main__":
    app = HelloCreator()
    app.run()           