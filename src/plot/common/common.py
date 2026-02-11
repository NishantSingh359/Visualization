def chart_format_number(value, pos):
    if value >= 1000000000:
        return f"{value/1000000000:.1f}B"
    elif value >= 1000000:
        return f"{value/1000000:.1f}M"
    elif value >= 1000:
        return f"{value/1000:.0f}K"
    else:
        return f"{value}"
