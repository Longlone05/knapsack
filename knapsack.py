# Tạo một bảng lưu trữ giá trị tối đa cho từng trọng lượng từ 0 đến 23
# Lần lượt xét từng món hàng, cập nhật giá trị tối đa nếu chọn món hàng đó.
# Kết quả nằm tại bảng tương ứng với trọng lượng 23.
items = {
    "A": {"giá trị": 250, "trọng lượng": 6},
    "B": {"giá trị": 900, "trọng lượng": 5},
    "C": {"giá trị": 700, "trọng lượng": 7},
    "D": {"giá trị": 650, "trọng lượng": 9},
    "E": {"giá trị": 1000, "trọng lượng": 9},
    "F": {"giá trị": 850, "trọng lượng": 2},
    "G": {"giá trị": 550, "trọng lượng": 4},
    "H": {"giá trị": 1250, "trọng lượng": 8},
    "I": {"giá trị": 750, "trọng lượng": 6},
    "J": {"giá trị": 450, "trọng lượng": 3},
}
def knapsack(items, max_weight):
    # Tạo bảng dp 
    dp = [0] * (max_weight + 1)
    n = len(items)
    
    # Tạo danh sách lựa chọn
    selected = [set() for _ in range(max_weight + 1)]

    # Duyệt qua từng món hàng
    for key, item in items.items():
        value = item["giá trị"]
        weight = item["trọng lượng"]
        
        # Cập nhật bảng dp từ cuối lên trên
        for w in range(max_weight, weight - 1, -1):
            if dp[w - weight] + value > dp[w]:
                dp[w] = dp[w - weight] + value
                selected[w] = selected[w - weight].copy()
                selected[w].add(key)

    return dp[max_weight], selected[max_weight]

max_weight = 23
result, selected_items = knapsack(items, max_weight)
print(f"Tổng giá trị tối đa cho trọng lượng {max_weight} là: {result}")
print(f"Các món hàng được chọn: {selected_items}")