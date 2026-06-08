import heapq

def top_k_heap(items, k):
    return heapq.nlargest(k, items, key=lambda x: x[0])