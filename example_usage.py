from client import LZWCoder

def main():
    text = "BABAABAAA_GENPARK_BABAABAAA"
    comp = LZWCoder.compress(text)
    decomp = LZWCoder.decompress(comp)
    print("Original Length:", len(text))
    print("Compressed Token Count:", len(comp))
    print("Tokens:", comp)
    print("Verified Decompress:", decomp == text)

if __name__ == "__main__":
    main()
