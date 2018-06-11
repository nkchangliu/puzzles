def rectangle(A, B, C, D, E, F, G, H):
    area = (C - A) * (D - B) + (G - E) * (H - F)
    left = max(A, E)
    right = min(C, G)
    top = min(D, H)
    bottom = max(B, F)
    if left <= right and bottom <= top:
        return area - (left - right) * (bottom - top)
    return area

