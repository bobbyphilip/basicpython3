def approximate_size(size, kib=True):
    '''
     file size to human readable form
     Arguments
     size -- file size in bytes
     kib  -- if True use multiples of 1024

     Returns: string

    '''
    if size < 0:
        raise ValueError('number must be >0')

    factor = 1024 if kib else 1000
    for suffix in SUFFIXES[factor]:
        if size < factor:
            return '{0:.1f} {1}'.format(size, suffix)
        size /= factor

    return '{0:.1f} {1}'.format(size, SUFFIXES[factor][-1])


SUFFIXES = {1000: ['B','KB', 'MB', 'GB', 'TB', 'PB'],
        1024: ['B', 'KiB', 'MiB', 'GiB', 'TiB', 'PiB']}

if __name__ == '__main__':
    print(approximate_size(10000, False))
    print(approximate_size(10000000000000000000000))

