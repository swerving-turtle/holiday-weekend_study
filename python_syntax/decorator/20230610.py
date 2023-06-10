import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(args[0], args[1])
        end = time.time()
        print(f"함수 {func.__name__}의 실행 시간은 {end - start}초 입니다.")

    return wrapper


@timer
def self_introduce(name, age):
    print(f"안녕하세요! 저는 {name}입니다.")
    print(f"나이는 {age}살 입니다.")
    print("잘 부탁드립니다.")
