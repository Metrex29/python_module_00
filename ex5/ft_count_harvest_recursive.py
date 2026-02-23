def ft_count_harvest_recursive():
    limit = int(input("Days until harvest: "))

    def recursive(days, limit):
        if (days > limit):
            print("Harvest time!")
            return
        print("Day", days)
        recursive(days + 1, limit)
    recursive(1, limit)
