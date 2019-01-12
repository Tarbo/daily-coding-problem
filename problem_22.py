"""
@author: Okwudili Ezeme
@date: 11-01-2019
This problem was asked by Microsoft.

Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list. If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].
"""


def reconstruct_sentence(dictionary, string):
    import re
    dict_list = []
    sentence_list = []
    for _, value in dictionary.items():
        dict_list.append(value)
    len_list = len(dict_list)
    while len_list != 0:
        for index, item in enumerate(dict_list):
            if re.match(item, string) is not None:
                sentence_list.append(item)
                string = string.replace(item, '', 1)
                _ = dict_list.pop(index)
                len_list -= 1
            elif re.search(item, string) == None:
                string = string.replace(item, '', 1)
                _ = dict_list.pop(index)
                len_list -= 1
    return sentence_list


# test the function
if __name__ == "__main__":
    string = "bedbathandbeyond"  # this test really killed my time
    dictionary = {1: 'bed', 2: 'bath', 3: 'bedbath', 4: 'and', 5: 'beyond'}
    print(
        f'>>> The reconstructed sentence is: {reconstruct_sentence(dictionary,string)} <<<')
