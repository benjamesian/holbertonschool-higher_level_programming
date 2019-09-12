#!/home/benjames/Python-3.4.10/python
if __name__ == "__main__":
    so = dir('hidden_4.pyc')
    s = sorted(filter(lambda x: x[:2] != "__", so))
    for el in s:
        print(el)
