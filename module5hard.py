import time

class User:
    def __init__(self, nickname, password, age):
        self.nickname = str(nickname)
        self.password = int(password)
        self.age = int(age)

    def __hash__(self):
        return hash(self.password)

    def __str__(self):
        return f'{self.nickname}'

class Video:
    def __init__(self, title, duration, adult_mode = False):
        self.title = str(title)
        self.duration = int(duration)
        self.adult_mode = bool(adult_mode)
        self.time_now = 0

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def __str__(self):
        return f'{self.users}'

    def add(self, *videos):
        for video_new in videos:
            if video_new.title not in [video.title for video in self.videos]: #списковая сборка для проверки названия
              self.videos.append(video_new)

    def get_videos(self, word):
        list_title = []
        for video in self.videos:
            if word.upper() in video.title.upper():
                list_title.append(video.title)
        return list_title

    def register(self, nickname: str, password: int, age: int):
        for user in self.users:
            if nickname == user.nickname:
                return print(f'Пользователь {nickname} уже существует.')
        password = hash(password)
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user

    def log_in(self, nickname: str, password: int):
        password = hash(password)
        for user in self.users:
            if nickname == user.nickname and password == user.password:
                self.current_user = user
                return
        print("Ошибка: Неверный никнейм или пароль.")

    def log_out(self):
        self.current_user = None

    def watch_video(self, video_name):
        if self.current_user:
            for video in self.videos:
                if video.title == video_name:
                    if video.adult_mode == True and self.current_user.age < 18:
                        print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    else:
                        while video.time_now < video.duration:
                            time.sleep(1)
                            video.time_now += 1
                            print(video.time_now, end=' ')
                        video.time_now = 0
                        print('Конец видео')
        else:
            print("Войдите в аккаунт, чтобы смотреть видео")

# Код для проверки:
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2025 года!')

# Вывод в консоль:
#
# ['Лучший язык программирования 2024 года']
# ['Лучший язык программирования 2024 года', 'Для чего девушкам парень программист?']
# Войдите в аккаунт, чтобы смотреть видео
# Вам нет 18 лет, пожалуйста покиньте страницу
# 1 2 3 4 5 6 7 8 9 10 Конец видео
# Пользователь vasya_pupkin уже существует
# urban_pythonist