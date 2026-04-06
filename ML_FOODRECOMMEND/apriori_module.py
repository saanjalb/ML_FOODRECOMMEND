# -*- coding: utf-8 -*-
"""
Created on Thu Oct  2 23:53:51 2025

@author: Patil
"""

# apriori_module.py
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

class AprioriRecommender:
    def __init__(self, filepath, min_support=0.02, lift_threshold=0.1):
        self.min_support = min_support
        self.lift_threshold = lift_threshold

        df = pd.read_csv(filepath)
        if 'Items' not in df.columns:
            raise ValueError("CSV must have a column named 'Items'")

        transactions = df['Items'].apply(lambda x: [i.strip() for i in str(x).replace(';', ',').split(',') if i.strip()]).tolist()

        te = TransactionEncoder()
        te_ary = te.fit(transactions).transform(transactions)
        df_bool = pd.DataFrame(te_ary, columns=te.columns_)

        self.freq_itemsets = apriori(df_bool, min_support=self.min_support, use_colnames=True)
        self.rules = association_rules(self.freq_itemsets, metric="lift", min_threshold=self.lift_threshold)

    def recommend_items(self, last_item):
        if self.rules.empty or not last_item:
            return []

        recommended_scores = {}
        for _, row in self.rules.iterrows():
            antecedents = row['antecedents']   # frozenset
            consequents = row['consequents']   # frozenset
            if last_item in antecedents:
                for rec_item in consequents:
                    if rec_item != last_item:
                        recommended_scores[rec_item] = recommended_scores.get(rec_item, 0) + row['lift']

        recommended = [k for k, v in sorted(recommended_scores.items(), key=lambda x: x[1], reverse=True)]
        return recommended
