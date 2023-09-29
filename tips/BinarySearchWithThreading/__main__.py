from time import perf_counter as pc
import threading


def search_in_seq_ordinary(sequence, value):
    try:
        index = sequence.index(value)
        print("found")
    except ValueError:
        index = None

    return index

class BinarySearch:
    def __init__(self, sequence, value):
        self.sequence = sequence
        self.value = value
        self._split_sequence = self.split_sequence()
        self._threads = []

    def split_sequence(self):
        half_seq_len = len(self.sequence) // 2
        seq1 = self.sequence[:half_seq_len]
        seq2 = self.sequence[half_seq_len:]

        self._split_sequence = (seq1, seq2)

    def split_split_sequence(self) -> None:
        temp_seq = []
        for sequence in self._split_sequence:
            sub_sequence_len = len(sequence) // 2
            temp_seq.append(sequence[:sub_sequence_len])
            temp_seq.append(sequence[sub_sequence_len:])

        self._split_sequence = tuple(temp_seq)

    def search_in_seq(self, sequence):
        try:
            index = sequence.index(self.value)
            print("found")
        except ValueError:
            index = None

        return index

    def add_thread(self, sequence):
        thread = threading.Thread(target=self.search_in_seq, args=(sequence,))
        self._threads.append(thread)

    def start_search(self):
        self.split_sequence()
        # print("n1")
        # self.split_split_sequence()
        # print("n2")
        # self.split_split_sequence()
        # print("n3")
        # self.split_split_sequence()
        # print("n4")
        # self.split_split_sequence()
        # print("n5")
        # self.split_split_sequence()
        # self.split_split_sequence()

        for sub_sequence in self._split_sequence:
            self.add_thread(sub_sequence)

        print(self._threads)
        for thread in self._threads:
            thread.start()

        # for thread in self._threads:
        #     thread.join()


value = 10**7
seq = [*range(0, 10**8)]

start_time = pc()
search_in_seq_ordinary(seq, value)
end_time = pc() - start_time
print("ordinary took: ", end_time)

start_time = pc()
BinarySearch(seq, value).start_search()
end_time = pc() - start_time
print("Binary took: ", end_time)
