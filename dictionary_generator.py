import argparse
import pandas as pd

def create_dictionary(target, alphabet):
    length_of_gen = len([char for char in target if char == "*"])
    length_of_alpha = len(alphabet)
    result = []
    for g in range(0, length_of_gen):
        line = list([''.join([x*(length_of_alpha**(length_of_gen-(g+1))) for x in alphabet])*(length_of_alpha**g)][0])
        result.append(line)
    dictionary = [f"{target.replace('*', '')}{''.join(obj)}" for obj in list(zip(*result))]
    return dictionary

def main():
    parser = argparse.ArgumentParser(description="Create password dictionary")
    parser.add_argument('-T', '--target', type=str, help="Target you are trying to crack. E.g.: --target \"passw****\"")
    parser.add_argument('-A', '--alphabet', type=str, help="OPTIONS: 'alpha', 'numeric', 'special', 'alnum', 'alnumspec'")
    parser.add_argument('-O', '--output', type=str, help="Path to output results")
    args = parser.parse_args()
    if not args.target and not args.alphabet:
        raise Exception("Failed to provide correct arguments!")
    if args.alphabet == 'alpha':
        args.alphabet = [char for char in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ']
    elif args.alphabet == 'numeric':
        args.alphabet = [char for char in '0123456789']
    elif args.alphabet == 'special':
        args.alphabet = [char for char in '!"£$%^&*()_+-=[]{};:\'@#~,<.>/?\\|']
    elif args.alphabet == 'alnum':
        args.alphabet = [char for char in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
    elif args.alphabet == 'alnumspec':
        args.alphabet = [char for char in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"£$%^&*()_+-=[]{};:\'@#~,<.>/?\\|']
    dictionary = create_dictionary(args.target, args.alphabet)
    if ".xlsx" in args.output.lower():
        df = pd.DataFrame(dictionary, columns=['Dictionary'])
        df.to_excel(args.output)
    elif ".txt" in args.output.lower():
        with open(args.output, "w") as file:
            for d in dictionary:
                file.write(d)
                file.write("\n")
            file.close()

if __name__ == "__main__":
    main()
