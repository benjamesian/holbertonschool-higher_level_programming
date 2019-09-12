#!/home/benjames/Python-3.4.10/python
if __name__ == "__main__":
    s = dir('hidden_4.pyc')
    for el in s:
        if el[:2] == "__":
            continue
        print(el)
