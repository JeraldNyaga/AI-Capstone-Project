import string
def is_pangram(st):
    seen = set(string.ascii_lowercase)
    for x in st.lower():
        if x not in string.ascii_letters:
            print(x)
            st = st.replace(x, "")
    
    return seen == set(st.lower())

# print(is_pangram("The quick brown fox jumps over the lazy; dog."))