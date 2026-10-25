s=input("Enter string 1:")
t=input("Enter String 2:")
#def anagram(s,t):
#    sorted_s= sorted(s)
#    sorted_t= sorted(t)
#
#    if sorted_s==sorted_t:
#        print("text is anagram")
#    else:
#        print("Not anagram")

def anagram(s,t):
    freq={}
    if len(s)!=len(t):
        return False

    for ch in s:
        freq[ch]=freq.get(ch,0)+1
    for ch in t:
        if ch not in freq:
            return False
    return True  
        
print(anagram(s,t))


