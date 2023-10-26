import sys

from EucsContext import EucsContext
from Euc import euc
import numpy as np


def save_data_nns(data, no_of_dimensions, no_of_nns):
    index_filename = f"Generated/data_indices_nns_{no_of_dimensions}_{len(data)}_{no_of_nns}.csv"
    nns_filename = f"Generated/data_dists_nns_{no_of_dimensions}_{len(data)}_{no_of_nns}.csv"
    gen_nns(data, data, index_filename, nns_filename, no_of_nns)


def save_query_nns(queries, data, no_of_dimensions, no_of_nns):
    index_filename = f"Generated/query_indices_nns_{no_of_dimensions}_{len(data)}_{len(queries)}_{no_of_nns}.csv"
    nns_filename = f"Generated/query_dists_nns_{no_of_dimensions}_{len(data)}_{len(queries)}_{no_of_nns}.csv"
    gen_nns(queries, data, index_filename, nns_filename, no_of_nns)


def gen_nns(queries, dataset, index_filename, nns_filename, no_of_nns):
    index_file = open(index_filename, 'a')
    nns_file = open(nns_filename, 'a')
    for query in queries:
        dist_q_all_data = euc(query, dataset)
        indices_sorted = np.argsort(dist_q_all_data)
        np.savetxt(index_file, indices_sorted[0:no_of_nns], delimiter=',', newline=' ', fmt='%d')
        index_file.write('\n')
        np.savetxt(nns_file, dist_q_all_data[indices_sorted][0:no_of_nns], delimiter=',', newline=' ', fmt='%1.4e')
        nns_file.write('\n')
    index_file.close()
    nns_file.close()


def main():
    print("Running main")
    no_of_dimensions = 20
    distribution = 'gauss'
    data_size = 100_000
    no_of_queries = 1_000
    no_of_nns = 100
    no_of_ref_points = 0
    no_of_witnesses = 0
    ec = EucsContext(no_of_dimensions, distribution)
    ec.set_sizes(data_size, no_of_queries, no_of_ref_points, no_of_witnesses)
    data = ec.get_data()
    queries = ec.get_queries()
    np.savetxt(f"Generated/euc_data_{no_of_dimensions}_{data_size}.csv", data, delimiter=",")
    np.savetxt(f"Generated/euc_queries_{no_of_dimensions}_{data_size}.csv", queries, delimiter=",")
    save_data_nns(data, no_of_dimensions, no_of_nns)
    save_query_nns(queries, data, no_of_dimensions, no_of_nns)
    print("Finished")


if __name__ == '__main__':
    main()
