import hashlib
import time

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = self.hash_password(password)
        self.age = age
    
    def hash_password(self, password):
        return int(hashlib.sha256(password.encode()).hexdigest(), 16)
    
    def __eq__(self, other):
        return self.nickname == other.nickname and self.password == other.password
    
    def __str__(self):
        return self.nickname

class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title

    def __eq__(self, other):
        return self.title == other.title

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        hashed_password = int(hashlib.sha256(password.encode()).hexdigest(), 16)
        for user in self.users:
            if user.nickname == nickname and user.password == hashed_password:
                self.current_user = user
                print(f"Пользователь {nickname} вошел в систему")
                return
        print("Неверные логин или пароль")
    
    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user
        print(f"Пользователь {nickname} зарегистрирован и вошел в систему")

    def log_out(self):
        if self.current_user:
            print(f"Пользователь {self.current_user.nickname} вышел из системы")
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            if video not in self.videos:
                self.videos.append(video)
                print(f"Видео {video.title} добавлено")
            else:
                print(f"Видео {video.title} уже существует")

    def get_videos(self, search_word):
        search_word_lower = search_word.lower()
        result = [video.title for video in self.videos if search_word_lower in video.title.lower()]
        return result

    def watch_video(self, title):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        
        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return
                
                print(f"Начинается просмотр видео: {video.title}")
                for second in range(video.time_now + 1, video.duration + 1):
                    print(second, end=' ', flush=True)
                    time.sleep(1)
                video.time_now = 0
                print("Конец видео")
                return
        
        print(f"Видео с названием {title} не найдено")

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 10)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

ur.add(v1, v2)

print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

ur.watch_video('Лучший язык программирования 2024 года!')
