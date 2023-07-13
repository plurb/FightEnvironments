import random as rng


def generate_location():
    with open("environments.txt") as f:
        envs = f.readlines()
        if envs:
            env = rng.choice(envs).replace('\n', '')
        return env

if __name__ == '__main__':
    print(generate_location())
