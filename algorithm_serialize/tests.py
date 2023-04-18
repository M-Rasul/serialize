tests = [
    {
        "input": [1, 2, 3, 7, 8, 9],
        "output": "1-3-7-9",
        "compression_ratio": 0.5
    },
    {
        "input": [1, 2, 3, 4, 5, 7, 8, 10, 11, 12],
        "output": "1-5-7-8-10-12",
        "compression_ratio": 0.45
    },
    {
        "input": [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
        "output": "10-100",
        "compression_ratio": 0.1
    },
    {
        "input": [1] * 1000,
        "output": "1-1",
        "compression_ratio": 0.999
    }
]