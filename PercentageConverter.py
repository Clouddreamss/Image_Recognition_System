def rescale_percentage(original_percentage):
    """
    将原始百分比按照10%为100%的新标准重新计算。

    :param original_percentage: float, 原始的百分比值 (例如10表示10%)
    :return: float, 新的百分比值
    """
    new_percentage = (original_percentage / 10) * 100
    return new_percentage

# 示例使用
# original_percentages = [10, 5, 1, 0.5, 20]
#
# for original in original_percentages:
#     new_percentage = rescale_percentage(original)
#     print(f"原始百分比: {original}% -> 新百分比: {new_percentage}%")