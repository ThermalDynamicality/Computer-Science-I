import tools
import insertion_sort


def optimal_location(_pos_list):
    _sorted_list = insertion_sort.insertion_sort(_pos_list)

    _sorted_list_length = len(_sorted_list)
    if _sorted_list_length % 2:  # Odd length case
        return _sorted_list[_sorted_list_length // 2]
    else:                        # Even length case
        _index = _sorted_list_length // 2
        return 0.5 * (_sorted_list[_index] + _sorted_list[_index - 1])


# Main function
def main() -> None:

    # Takes file name input from user
    _file_name = input("Enter data file: ")
    #_file_name = "test.txt"

    # Calculates doing math stuffz
    _pos_list = tools.read_file(_file_name)
    _optimal_loc = optimal_location(_pos_list)
    _total_distances = tools.sum_distances(_pos_list, _optimal_loc)

    # Prints results
    print(f"Optimum new store location:         {_optimal_loc}")
    print(f"Sum of distances to the new store:  {_total_distances}")


# Main guard
if __name__ == "__main__":
    main()
