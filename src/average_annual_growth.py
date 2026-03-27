def calculation_average_annual_growth(start_value: float | int, end_value: float | int, years: int) -> float:
    """Рассчитывает и возвращает среднегодовой рост некой величины в процентах за период (years)"""
    return round(((end_value / start_value) ** (1 / (years - 1)) - 1) * 100, 2)
