from EucsContext import EucsContext
from Euc import euc
import numpy as np


def save_nns(data, queries, no_of_dimensions, no_of_nns):
    index_filename = f"Generated/indices_nns_{no_of_dimensions}_{len(data)}_{no_of_nns}.csv"
    nns_filename = f"Generated/nns_{no_of_dimensions}_{len(data)}_{no_of_nns}.csv"
    for datum in data:
        dist_q_all_data = euc(datum, data)
        indices_sorted = np.argsort( dist_q_all_data )
        index_file = open(index_filename, 'a')
        nns_file =  open(nns_filename, 'a')
        np.savetxt(index_file, indices_sorted[0:no_of_nns], delimiter=',', newline=' ', fmt='%d')
        np.savetxt(nns_file, dist_q_all_data[ indices_sorted ][0:no_of_nns], delimiter=',', newline=' ', fmt='%1.4e')
        index_file.write('\n')
        index_file.close()
        nns_file.write('\n')
        nns_file.close()

def main():
    print("Running main")
    no_of_dimensions = 20
    distribution = 'gauss'
    data_size = 100_000
    no_of_queries = 1_000
    no_of_nns = 100
    no_of_ref_points  = 0
    no_of_witnesses = 0
    ec = EucsContext(no_of_dimensions, distribution)
    ec.set_sizes(data_size, no_of_queries, no_of_ref_points, no_of_witnesses)
    data = ec.get_data()
    queries = ec.get_queries()
    np.savetxt(f"Generated/euc_data_{no_of_dimensions}_{data_size}.csv", data, delimiter=",")
    np.savetxt(f"Generated/euc_queries_{no_of_dimensions}_{data_size}.csv", queries, delimiter=",")
    save_nns(data,queries,no_of_dimensions,no_of_nns)
    print("Finished")




if __name__ == '__main__':
    main()
