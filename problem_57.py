"""
@author: Okwudili Ezeme
@date: 2/15/2019
This problem was asked by Amazon.

Given a string s and an integer k, break up the string into multiple 
texts such that each text has a length of k or less. 
You must break it up so that words don't break across lines. 
If there's no way to break the text up, then return null.

You can assume that there are no spaces at the ends of the string 
and that there is exactly one space between each word.

For example, given the string "the quick brown fox jumps over the lazy dog" and k = 10,
you should return: ["the quick", "brown fox", "jumps over", "the lazy", "dog"]. 
No string in the list has a length of more than 10.
"""
def split_string(string,sub_length):   
    words = string.split()
    new_string = []
    sub_string = ''
    while words:
        word = words.pop(0)
        sub_string=sub_string.strip() # remove trailing white spaces
        if len(sub_string+' '+ word)>sub_length:   
            new_string.append(sub_string)
            sub_string = ''
            words.insert(0,word)            
        else:
            sub_string = sub_string+' '+word
        if len(sub_string)!= 0 and len(words)==0:
            sub_string=sub_string.strip()
            new_string.append(sub_string)
    return new_string
if __name__ == "__main__":
    string = "the quick brown fox jumps over the lazy dog"
    sub_length = 10
    strings = split_string(string,sub_length) 
    print(strings)   
