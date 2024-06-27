import os
import pandas as pd
from collections import Counter

def get_most_common_words(folder_path, mc):
    
    mc = int(mc)
    
    word_counts = Counter()
    word_order = []
    
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                words = file.read().split(", ")
                for word in words:
                    if word not in word_order:
                        word_order.append(word)
                word_counts.update(words)
    
    common_words_df = pd.DataFrame(word_counts.most_common(mc), columns=['Word', 'Frequency'])
    common_words_dict = dict(word_counts.most_common(mc))
    
    chronological_list = sorted(common_words_dict.keys(), key=lambda word: common_words_dict[word], reverse=True)
    # print("Common words: ", "\n", common_words_df, "\n", "Common words Dictionary: ", "\n", common_words_dict, "\n", "Common words List: ", "\n", chronological_list, "\n")
    
    # return common_words_df, common_words_dict, chronological_list
    return chronological_list

# df, word_dict, word_list = get_most_common_words(folder_loc)