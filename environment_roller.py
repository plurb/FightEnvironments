import random as rng


def fetch_env():
    with open("environments.txt") as f:
        envs = f.readlines()
        if envs:
            env = rng.choice(envs).replace('\n', '')
        return env

if __name__ == '__main__':
    for i in range(10):
        print(fetch_env())
