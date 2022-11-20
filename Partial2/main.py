def parser():
    import sys
    import os
    if len(sys.argv) <= 1 :
        raise Exception('[ERROR] nr paramatrii insuficiente')
    else:
        print(sys.argv)

try:
    parser()
except Exception as e:
    print(e)
    # sys.exit(1)