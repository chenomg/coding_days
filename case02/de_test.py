def dec(func):
    print('starting now...')

    def start():
        func()
        print('over now...')

    return start


@dec
def process():
    print('processing now...')


process()
