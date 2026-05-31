from itertools import product
import hashlib

def find_correct_case(word, target_hash):
    combinations = product(*[(c.lower(), c.upper()) for c in word])

    for combo in combinations:
        text = ''.join(combo)

        md5_hash = hashlib.md5(text.encode()).hexdigest()

        print(f"Checking: {text} -> {md5_hash}")

        if md5_hash == target_hash:
            print("\nMATCH FOUND!")
            print(f"Correct word: {text}")
            print(f"MD5: {md5_hash}")
            return

    print("\nNo match found.")


word = input("Enter base word: ")
target_hash = input("Enter target MD5 hash: ").strip()

find_correct_case(word, target_hash)