import argparse
import pickle
from train import ModelText
from train import TextGenRNN


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default='model.pkl', help="Путь к модели")
    parser.add_argument("--length", help="длина генерируемого текста")
    parser.add_argument("--prefix", nargs='?', help="начало текста")
    args = parser.parse_args()
    # if args.model is None:
    #     model = ModelText
    # else:
    model = pickle.load(open(args.model, 'rb'))
    lenn = None
    if args.length is not None:
        lenn = int(args.length)
    print(model.generate(init_str=args.prefix, predict_len=lenn))


if __name__ == '__main__':
    main()
